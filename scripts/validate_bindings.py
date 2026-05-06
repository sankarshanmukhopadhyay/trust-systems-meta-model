#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
from referencing import Registry, Resource
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
BINDINGS = [
    ROOT / "bindings" / "trqp" / "tsmm-trqp-binding.json",
    ROOT / "bindings" / "openid-federation" / "tsmm-openid-federation-binding.json",
    ROOT / "bindings" / "dcas" / "tsmm-dcas-binding.json",
    ROOT / "bindings" / "vtc" / "tsmm-vtc-binding.json",
    ROOT / "bindings" / "ais1" / "tsmm-ais1-binding.json",
    ROOT / "bindings" / "havid" / "tsmm-havid-binding.json",
    ROOT / "bindings" / "gtr" / "tsmm-gtr-binding.json",
    ROOT / "bindings" / "tis" / "tsmm-tis-binding.json",
]
BINDING_SCHEMA = ROOT / "schemas" / "tsmm-binding.schema.json"
CONSTRAINT_SCHEMA = ROOT / "validation" / "schemas" / "tsmm-binding-constraints.schema.json"


def load_json(path: Path):
    with path.open('r', encoding='utf-8') as f:
        return json.load(f)


def build_registry() -> Registry:
    registry = Registry()
    for path in [BINDING_SCHEMA, CONSTRAINT_SCHEMA]:
        schema = load_json(path)
        if '$id' in schema:
            registry = registry.with_resource(schema['$id'], Resource.from_contents(schema))
        registry = registry.with_resource(path.resolve().as_uri(), Resource.from_contents(schema))
    return registry


REGISTRY = build_registry()


def validate_binding(path: Path) -> None:
    data = load_json(path)
    schema = load_json(BINDING_SCHEMA)
    validator = Draft202012Validator(schema, registry=REGISTRY)
    errors = sorted(validator.iter_errors(data), key=lambda e: list(e.path))
    if errors:
        print(f'FAILED binding schema validation: {path.relative_to(ROOT)}')
        for error in errors:
            loc = '.'.join(str(p) for p in error.path) or '<root>'
            print(f'  - {loc}: {error.message}')
        raise SystemExit(1)

    contract = data['bindingContract']
    if contract['targetSystem'] != data['targetEcosystem']:
        raise SystemExit(f"FAILED binding contract target mismatch: {path.relative_to(ROOT)}")

    constraint_path = ROOT / contract['constraintSetRef']
    if not constraint_path.exists():
        raise SystemExit(f"FAILED missing constraint set: {constraint_path.relative_to(ROOT)}")

    constraint_data = load_json(constraint_path)
    constraint_validator = Draft202012Validator(load_json(CONSTRAINT_SCHEMA), registry=REGISTRY)
    errors = sorted(constraint_validator.iter_errors(constraint_data), key=lambda e: list(e.path))
    if errors:
        print(f'FAILED constraint schema validation: {constraint_path.relative_to(ROOT)}')
        for error in errors:
            loc = '.'.join(str(p) for p in error.path) or '<root>'
            print(f'  - {loc}: {error.message}')
        raise SystemExit(1)

    if constraint_data['bindingId'] != data['bindingId']:
        raise SystemExit(f"FAILED constraint bindingId mismatch: {constraint_path.relative_to(ROOT)}")
    if constraint_data['targetEcosystem'] != data['targetEcosystem']:
        raise SystemExit(f"FAILED constraint targetEcosystem mismatch: {constraint_path.relative_to(ROOT)}")

    referenced_files = set(data.get('sources', [])) | set(constraint_data.get('requiredArtifacts', []))
    for ref in referenced_files:
        ref_path = ROOT / ref
        if not ref_path.exists():
            raise SystemExit(f"FAILED missing referenced artifact: {ref}")

    print(f"OK: {path.relative_to(ROOT)}")
    print(f"OK: {constraint_path.relative_to(ROOT)}")


def main() -> None:
    for path in BINDINGS:
        validate_binding(path)
    print('All binding validations passed.')


if __name__ == '__main__':
    main()
