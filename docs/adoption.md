---
title: Adoption
permalink: /adoption.html
parent: Documentation
---
# Adoption

Choose the adoption path that matches the authority surface you need.

## Adopt the complete Trust Systems Modelling Stack

If you are using TSMM together with Trust Infrastructure Schemas (TIS) and Trust Graph Artifacts (TGA), start with the [TSMS Adopter Guide](tsms-adopter-guide.md). It provides the released-stack baseline, the canonical `TSMS-WIRE-001` transaction, validation commands, evidence surfaces, drift dispositions, extension rules, and non-claims.

Then read the [Trust Systems Modelling Stack architecture](tsms.md) for the coordination model and authority boundaries.

## Adopt TSMM only

1. Install the repository dependencies documented in the README.
2. Run `make validate` from the repository root.
3. Review `artifacts/validation/latest.json` for the executed checks and limitations.
4. Use `docs/architecture.md` to identify the correct artifact family.
5. Use `docs/interoperability.md` before asserting compatibility with another repository.

## First TSMS wire result

For the accepted TSMS baseline, run:

```bash
python3 scripts/test_tsms_wire.py
python3 scripts/run_tsms_wire.py
```

The deterministic pressure-test suite must pass. A successful live canonical transaction reports `TSMS-WIRE-001: PASS / PERMIT` and produces a machine-readable receipt under `artifacts/e2e/TSMS-WIRE-001/`.

The live runner resolves the exact accepted TSMM, TIS and TGA commits. Unavailable authoritative state must not be converted into compatibility.

## Implementation contract

Every adoption path must identify inputs, authority assumptions, expected outputs, evidence produced, failure conditions, and non-claims. Validation fails closed when required authority or relationship metadata is absent.

## Cross-repository walkthrough

The shared delegated-authority assurance flow is documented in `docs/delegated-authority-assurance-flow.md`. The executable stack-qualified flow and adopter repository pattern are documented in `docs/tsms-adopter-guide.md`.
