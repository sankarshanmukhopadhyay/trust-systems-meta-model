---
owner: maintainers
last_reviewed: 2026-05-05
applicable_version: v0.21.0
tier: 1
---

# Implementation Paths

TSMM can be adopted incrementally. This guide helps implementers choose the smallest useful path instead of trying to absorb the entire repository at once.

## I want to model a trust registry

Start with:

- `docs/patterns/trust-registry-pattern.md`
- `docs/registry/tsmm-registry-format.md`
- `examples/registries/tsmm-registry-example.json`
- `examples/systems/trqp-registry-system.json`

Validation:

```bash
python scripts/validate_tsmm_registry.py
python scripts/validate_examples.py
```

## I want to model agent-to-tool governance

Start with:

- `docs/model/runtime-governance-envelope.md`
- `docs/model/decision-receipt.md`
- `docs/patterns/pre-effect-governance-pattern.md`
- `examples/runtime-governance-boundary-instance.json`
- `examples/decision-receipt-runtime-example.json`

Validation:

```bash
python scripts/validate_examples.py
python scripts/validate_test_vectors.py
```

## I want to compare two trust systems

Start with:

- `docs/getting-started/model-bind-validate-compare.md`
- `docs/interop/interoperability.md`
- `interop/interoperability-matrix.yaml`
- `docs/crosswalks/`

Validation:

```bash
python scripts/validate_bindings.py
python scripts/validate_yaml_models.py
```

## I want to produce assurance evidence

Start with:

- `docs/extensions/assurance-extension.md`
- `docs/model/evidence-artifact.md`
- `docs/patterns/assurance-evidence-pattern.md`
- `docs/model/decision-receipt.md`

Output:

- evidence artifact
- assessment result
- verification result
- decision receipt
- conformance profile assertion

## I want to publish a TSMM-compatible profile

Start with:

- `docs/profiles/oasf-publication-guidance.md`
- `docs/bindings/binding-contract.md`
- `docs/conformance/tsmm-conformance-checklist.md`
- `validation/conformance/tsmm-validation-profile.json`

Output:

- profile document
- machine-readable binding or schema
- example instance
- validation test vector
- release note
