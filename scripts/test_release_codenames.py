import importlib.util
import tempfile
import unittest
from pathlib import Path

SPEC = importlib.util.spec_from_file_location("release_codenames", Path(__file__).with_name("release_codenames.py"))
mod = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(mod)

class ReleaseCodenamePolicyTests(unittest.TestCase):
    def policy(self):
        return {"schemaVersion": 1, "minimumPoolSize": 3, "source": {"url": "https://example.test/source"}, "selection": {"allowReuseAfterExhaustion": False}}

    def test_valid_policy(self):
        self.assertTrue(mod.validate(["A", "B", "C"], self.policy(), {"schemaVersion": 1, "releases": []}))

    def test_duplicate_pool_rejected(self):
        with self.assertRaises(mod.PolicyError):
            mod.validate(["A", "a", "B"], self.policy(), {"schemaVersion": 1, "releases": []})

    def test_history_name_must_be_in_pool(self):
        with self.assertRaises(mod.PolicyError):
            mod.validate(["A", "B", "C"], self.policy(), {"schemaVersion": 1, "releases": [{"version": "v1", "codename": "Z", "status": "published"}]})

    def test_existing_version_is_idempotent(self):
        history = {"schemaVersion": 1, "releases": [{"version": "v1", "codename": "A", "status": "published"}]}
        self.assertEqual(("A", True), mod.select("v1", seed="x", pool=["A", "B", "C"], policy=self.policy(), history=history))

    def test_unused_name_preferred(self):
        history = {"schemaVersion": 1, "releases": [{"version": "v1", "codename": "A", "status": "published"}]}
        chosen, existing = mod.select("v2", seed="fixed", pool=["A", "B", "C"], policy=self.policy(), history=history)
        self.assertFalse(existing)
        self.assertIn(chosen, {"B", "C"})

    def test_exhaustion_fails(self):
        history = {"schemaVersion": 1, "releases": [
            {"version": "v1", "codename": "A", "status": "published"},
            {"version": "v2", "codename": "B", "status": "published"},
            {"version": "v3", "codename": "C", "status": "published"}]}
        with self.assertRaises(mod.PolicyError):
            mod.select("v4", seed="fixed", pool=["A", "B", "C"], policy=self.policy(), history=history)

    def test_persist_refuses_rename(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "history.json"
            path.write_text('{"schemaVersion":1,"releases":[{"version":"v1","codename":"A","status":"candidate"}]}')
            with self.assertRaises(mod.PolicyError):
                mod.persist("v1", "B", path)

if __name__ == "__main__":
    unittest.main()
