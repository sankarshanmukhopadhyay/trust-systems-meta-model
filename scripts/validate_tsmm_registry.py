#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "tsmm-registry.schema.json"
DEFAULT_TARGETS = [ROOT / "examples" / "registries" / "tsmm-registry-example.json"]


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def build_registry() -> Registry:
    schema = load_json(SCHEMA_PATH)
    registry = Registry()
    registry = registry.with_resource(schema["$id"], Resource.from_contents(schema))
    registry = registry.with_resource(SCHEMA_PATH.resolve().as_uri(), Resource.from_contents(schema))
    return registry


def validate_registry(path: Path) -> None:
    schema = load_json(SCHEMA_PATH)
    instance = load_json(path)
    validator = Draft202012Validator(schema, registry=build_registry())
    errors = sorted(validator.iter_errors(instance), key=lambda e: list(e.path))
    if errors:
        print(f"FAILED schema validation: {path.relative_to(ROOT)}")
        for error in errors:
            loc = ".".join(str(p) for p in error.path) or "<root>"
            print(f"  - {loc}: {error.message}")
        raise SystemExit(1)

    seen: set[str] = set()
    for entry in instance["entries"]:
        if entry["id"] in seen:
            raise SystemExit(f"FAILED semantic validation: duplicate entry id {entry['id']} in {path.relative_to(ROOT)}")
        seen.add(entry["id"])
        target = (ROOT / entry["location"]).resolve()
        if not target.exists():
            raise SystemExit(
                f"FAILED semantic validation: {path.relative_to(ROOT)} references missing artifact {entry['location']}"
            )

    print(f"OK: {path.relative_to(ROOT)}")


def main(argv: list[str]) -> None:
    targets = [Path(arg).resolve() for arg in argv] if argv else DEFAULT_TARGETS
    for target in targets:
        validate_registry(target)
    print("All TSMM registry validations passed.")


if __name__ == "__main__":
    main(sys.argv[1:])
