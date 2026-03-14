---
owner: maintainers
last_reviewed: 2026-03-14
applicable_version: v0.10.0
tier: 0
---

# TSMM Binding: TRQP

This binding aligns TSMM with the TRQP operational stack so that the trust registry, trusted service provider publication logic, conformance evidence, and relying-party consumption flow can be expressed through one shared semantic frame.

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
