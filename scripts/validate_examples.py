#!/usr/bin/env python3
import json
from pathlib import Path
from jsonschema import Draft202012Validator, RefResolver

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas"
EXAMPLES = ROOT / "examples"

PAIRS = [
    ("minimal-trust-registry-instance.json", "tsmm-core.schema.json"),
    ("consumer-policy-instance.json", "tsmm-core.schema.json"),
    ("delegated-agent-instance.json", "tsmm-core.schema.json"),
    ("agentic-ai-extension-instance.json", "tsmm-agentic-extension.schema.json"),
    ("verifiable-trust-community-instance.json", "tsmm-vtc-extension.schema.json"),
]

def load_json(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)

def build_store():
    store = {}
    for schema_path in SCHEMAS.glob("*.json"):
        schema = load_json(schema_path)
        store[schema_path.resolve().as_uri()] = schema
        schema_id = schema.get("$id")
        if schema_id:
            store[schema_id] = schema
    return store

STORE = build_store()

def validate(example_name: str, schema_name: str) -> None:
    schema_path = SCHEMAS / schema_name
    example_path = EXAMPLES / example_name
    schema = load_json(schema_path)
    instance = load_json(example_path)
    base_uri = schema.get("$id", schema_path.resolve().as_uri())
    resolver = RefResolver(base_uri=base_uri, referrer=schema, store=STORE)
    validator = Draft202012Validator(schema, resolver=resolver)
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
