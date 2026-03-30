#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas"

PAIRS = [
    ("model/authority-graph.yaml", "tsmm-authority-graph.schema.json"),
    ("model/delegation-patterns.yaml", "tsmm-delegation-patterns.schema.json"),
    ("model/lifecycle/trust-object-lifecycle.yaml", "tsmm-lifecycle.schema.json"),
    ("extensions/assurance/assurance-properties.yaml", "tsmm-assurance-properties.schema.json"),
    ("interop/interoperability-matrix.yaml", "tsmm-interoperability.schema.json"),
]


def load_data(path: Path):
    with path.open("r", encoding="utf-8") as f:
        if path.suffix in {".yaml", ".yml"}:
            return yaml.safe_load(f)
        return json.load(f)


def build_registry() -> Registry:
    registry = Registry()
    for schema_path in SCHEMAS.glob("*.json"):
        schema = load_data(schema_path)
        uri = schema.get("$id", schema_path.resolve().as_uri())
        registry = registry.with_resource(uri, Resource.from_contents(schema))
        registry = registry.with_resource(schema_path.resolve().as_uri(), Resource.from_contents(schema))
    return registry


REGISTRY = build_registry()


def validate(data_path: str, schema_name: str) -> None:
    schema_path = SCHEMAS / schema_name
    instance_path = ROOT / data_path
    schema = load_data(schema_path)
    instance = load_data(instance_path)
    validator = Draft202012Validator(schema, registry=REGISTRY)
    errors = sorted(validator.iter_errors(instance), key=lambda e: list(e.path))
    if errors:
        print(f"FAILED: {data_path} against {schema_name}")
        for error in errors:
            loc = ".".join(str(p) for p in error.path) or "<root>"
            print(f"  - {loc}: {error.message}")
        raise SystemExit(1)
    print(f"OK: {data_path} against {schema_name}")


if __name__ == "__main__":
    for data_path, schema_name in PAIRS:
        validate(data_path, schema_name)
    print("All YAML model validations passed.")
