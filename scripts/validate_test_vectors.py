#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
from referencing import Registry, Resource
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
VALID = ROOT / 'validation' / 'test_vectors' / 'valid'
INVALID = ROOT / 'validation' / 'test_vectors' / 'invalid'
BINDING_SCHEMA = ROOT / 'schemas' / 'tsmm-binding.schema.json'
CONSTRAINT_SCHEMA = ROOT / 'validation' / 'schemas' / 'tsmm-binding-constraints.schema.json'
RUNTIME_SCHEMA = ROOT / 'schemas' / 'tsmm-runtime-governance.schema.json'
RECEIPT_SCHEMA = ROOT / 'schemas' / 'tsmm-decision-receipt.schema.json'
DISCOVERY_SCHEMA = ROOT / 'schemas' / 'tsmm-discovery-governance.schema.json'
CAPABILITY_SCHEMA = ROOT / 'schemas' / 'tsmm-capability-negotiation.schema.json'
TASK_LIFECYCLE_SCHEMA = ROOT / 'schemas' / 'tsmm-task-evidence-lifecycle.schema.json'

CASES = [
    (VALID / 'tsmm-binding-valid.json', BINDING_SCHEMA, True),
    (INVALID / 'tsmm-binding-invalid-missing-guarantees.json', BINDING_SCHEMA, False),
    (VALID / 'tsmm-binding-constraints-valid.json', CONSTRAINT_SCHEMA, True),
    (INVALID / 'tsmm-binding-constraints-invalid-empty-prohibited-inferences.json', CONSTRAINT_SCHEMA, False),
    (VALID / 'runtime-governance-envelope-valid.json', RUNTIME_SCHEMA, True),
    (INVALID / 'runtime-governance-envelope-missing-policy.json', RUNTIME_SCHEMA, False),
    (VALID / 'decision-receipt-valid.json', RECEIPT_SCHEMA, True),
    (INVALID / 'decision-receipt-missing-policy.json', RECEIPT_SCHEMA, False),
    (VALID / 'discovery-governance-valid.json', DISCOVERY_SCHEMA, True),
    (INVALID / 'discovery-governance-missing-integrity.json', DISCOVERY_SCHEMA, False),
    (VALID / 'capability-negotiation-valid.json', CAPABILITY_SCHEMA, True),
    (INVALID / 'capability-negotiation-required-extension-missing.json', CAPABILITY_SCHEMA, False),
    (VALID / 'task-evidence-lifecycle-valid.json', TASK_LIFECYCLE_SCHEMA, True),
    (INVALID / 'task-evidence-lifecycle-missing-receipt.json', TASK_LIFECYCLE_SCHEMA, False),
    (INVALID / 'task-evidence-lifecycle-invalid-transition.json', TASK_LIFECYCLE_SCHEMA, False),
]


def load_json(path: Path):
    with path.open('r', encoding='utf-8') as f:
        return json.load(f)


def build_registry() -> Registry:
    registry = Registry()
    for path in list((ROOT / 'schemas').glob('*.json')) + [CONSTRAINT_SCHEMA]:
        schema = load_json(path)
        if '$id' in schema:
            registry = registry.with_resource(schema['$id'], Resource.from_contents(schema))
        registry = registry.with_resource(path.resolve().as_uri(), Resource.from_contents(schema))
    return registry


REGISTRY = build_registry()


def run_case(instance_path: Path, schema_path: Path, should_pass: bool) -> None:
    instance = load_json(instance_path)
    schema = load_json(schema_path)
    validator = Draft202012Validator(schema, registry=REGISTRY)
    errors = list(validator.iter_errors(instance))
    passed = not errors
    if passed != should_pass:
        verdict = 'pass' if should_pass else 'fail'
        print(f'FAILED: {instance_path.relative_to(ROOT)} expected to {verdict} against {schema_path.relative_to(ROOT)}')
        for error in errors:
            loc = '.'.join(str(p) for p in error.path) or '<root>'
            print(f'  - {loc}: {error.message}')
        raise SystemExit(1)
    print(f"OK: {instance_path.relative_to(ROOT)}")


def main() -> None:
    for instance_path, schema_path, should_pass in CASES:
        run_case(instance_path, schema_path, should_pass)
    print('All validation test vectors behaved as expected.')


if __name__ == '__main__':
    main()
