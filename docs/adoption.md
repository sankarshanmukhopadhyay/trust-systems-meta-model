---
title: Adoption
permalink: /adoption.html
parent: Documentation
---
# Adoption

If you are adopting TSMM together with Trust Infrastructure Schemas (TIS) or Trust Graph Artifacts (TGA), start with the [Trust Systems Modelling Stack (TSMS) guide](tsms.md). It explains authority boundaries, the candidate compatibility baseline, and the intended concept → contract → executable-artifact path.

## First valid result

1. Install the repository dependencies documented in the README.
2. Run `make validate` from the repository root.
3. Review `artifacts/validation/latest.json` for the executed checks and limitations.
4. Use `docs/architecture.md` to identify the correct artifact family.
5. Use `docs/interoperability.md` before asserting compatibility with another repository.

## Implementation contract

Every adoption path must identify inputs, authority assumptions, expected outputs, evidence produced, failure conditions, and non-claims. Validation fails closed when required authority or relationship metadata is absent.

## Cross-repository walkthrough

The shared delegated-authority assurance flow is documented in `docs/delegated-authority-assurance-flow.md`.
