---
owner: maintainers
last_reviewed: 2026-05-05
applicable_version: 0.24.0
tier: 0
title: TSMM Binding&#58; TRQP
permalink: /bindings/trqp-binding.html
parent: Bindings
grand_parent: Documentation
---

# TSMM Binding: TRQP

This binding aligns TSMM with the TRQP operational stack so that the trust registry, trusted service provider publication logic, conformance evidence, and relying-party consumption flow can be expressed through one shared semantic frame. TSMM contributes the abstract model; trust-infrastructure-schemas contributes the canonical machine-readable trust artifact formats that TRQP-adjacent systems can publish or consume.

## Primary mappings

- **TRQP Trust Registry** -> `TrustRegistry`
- **Trust Framework Authority** -> `GovernanceAuthority`
- **Trusted Service Provider** -> `Issuer` in the general case, or `Agent` when the service is autonomous
- **Conformance evidence** -> `EvidenceBundle`
- **Assurance profile** -> `AssuranceProfile`
- **Downstream consumer** -> `RelyingParty`

## Why this matters

The TRQP family already carries the ingredients TSMM cares about: policy, publication, evidence, assurance, and operational consequences. The binding makes those elements portable across tooling. In plain English, it stops each repo from having to reinvent its own semantic wheel with fresh paint and a new naming argument.

## Related artifacts

- `bindings/trqp/tsmm-trqp-binding.json`
- `docs/crosswalks/trqp-tspp-crosswalk.md`
- `docs/patterns/trust-registry-pattern.md`
- `trust-infrastructure-schemas` for concrete artifact schemas aligned to this binding

## Contract and constraints

This binding now includes an explicit contract section in `bindings/trqp/tsmm-trqp-binding.json` and a paired constraint set at `bindings/trqp/constraints.json`. Together they record what the mapping preserves, where it becomes approximate, and what should not be inferred without the target ecosystem's own rules.
