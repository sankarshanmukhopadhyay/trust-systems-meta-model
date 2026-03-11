#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas"
EXAMPLES = ROOT / "examples"

PAIRS = [
    ("minimal-trust-registry-instance.json", "tsmm-core.schema.json"),
    ("consumer-policy-instance.json", "tsmm-core.schema.json"),
    ("delegated-agent-instance.json", "tsmm-core.schema.json"),
    ("agentic-ai-extension-instance.json", "tsmm-agentic-extension.schema.json"),
    ("verifiable-trust-community-instance.json", "tsmm-vtc-extension.schema.json"),
    ("assurance-extension-instance.json", "tsmm-assurance-extension.schema.json"),
    ("multi-agent-coordination-instance.json", "tsmm-multi-agent-extension.schema.json"),
    ("evidence-artifact-instance.json", "tsmm-evidence-artifact-extension.schema.json"),
]


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def build_registry() -> Registry:
    registry = Registry()
    for schema_path in SCHEMAS.glob("*.json"):
        schema = load_json(schema_path)
        uri = schema.get("$id", schema_path.resolve().as_uri())
        registry = registry.with_resource(uri, Resource.from_contents(schema))
        registry = registry.with_resource(schema_path.resolve().as_uri(), Resource.from_contents(schema))
    return registry


REGISTRY = build_registry()


def validate(example_name: str, schema_name: str) -> None:
    schema_path = SCHEMAS / schema_name
    example_path = EXAMPLES / example_name
    schema = load_json(schema_path)
    instance = load_json(example_path)
    validator = Draft202012Validator(schema, registry=REGISTRY)
    errors = sorted(validator.iter_errors(instance), key=lambda e: list(e.path))
    if errors:
        print(f"FAILED: {example_name} against {schema_name}")
        for error in errors:
            loc = ".".join(str(p) for p in error.path) or "<root>"
            print(f"  - {loc}: {error.message}")
        raise SystemExit(1)
    print(f"OK: {example_name} against {schema_name}")


def main() -> None:
    for example_name, schema_name in PAIRS:
        validate(example_name, schema_name)
    print("All schema/example validations passed.")


if __name__ == "__main__":
    main()
