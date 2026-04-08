---
owner: maintainers
last_reviewed: 2026-04-08
applicable_version: v0.16.0
tier: 1
---

# Validation and Testability

TSMM should be testable as a model, not only readable as documentation. The current validation layer is intentionally lightweight, but it is designed to catch structural drift before it turns into interpretive drift.

## Validation surfaces

The repository now validates six surfaces:

1. core and extension examples against their schemas
2. schema coverage so examples exercise modeled properties
3. ecosystem bindings against the binding schema
4. binding constraint sets against the constraint-set schema
5. representative valid and invalid test vectors
6. YAML-based authority, delegation, lifecycle, assurance, and interoperability artifacts

## Validation tree

- `validation/schemas/tsmm-binding-constraints.schema.json`
- `validation/test_vectors/valid/`
- `validation/test_vectors/invalid/`
- `validation/conformance/tsmm-validation-profile.json`

## Validation scripts

- `python scripts/validate_examples.py`
- `python scripts/check_schema_coverage.py`
- `python scripts/validate_bindings.py`
- `python scripts/validate_test_vectors.py`
- `python scripts/check_docs.py`
- `python scripts/validate_yaml_models.py`

## Design intent

This layer does not claim external certification. It does something more immediate and more useful for an evolving reference model: it verifies that the catalog, examples, bindings, and documentation still fit together coherently after each increment on the main branch.
