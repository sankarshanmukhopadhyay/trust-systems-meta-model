---
owner: maintainers
last_reviewed: 2026-04-08
applicable_version: v0.16.0
tier: 0
---

# TSMM Binding: OpenID Federation

OpenID Federation is a rich test case for TSMM because it distributes trust through signed metadata, authority chains, and federation-managed publication semantics. That makes it an excellent ecosystem for semantic binding.

## Primary mappings

- **Federation operator** -> `GovernanceAuthority`
- **Federation authority** -> `TrustRegistry` in the publication and trust-anchor sense
- **OpenID Provider / Issuer** -> `Issuer`
- **Relying Party** -> `Verifier`
- **Entity statement** -> `Credential` in a composite sense because the artifact blends metadata, authority, and trust assertion

## Why this matters

TSMM can describe the governance topology that sits underneath federation artifacts. That lets implementers compare OpenID Federation-style ecosystems with trust registries, credential ecosystems, and agent networks without pretending they are identical. Similar is not identical; identical is rare; and pretending otherwise is how interoperability decks become fiction.

## Related artifacts

- `bindings/openid-federation/tsmm-openid-federation-binding.json`
- `docs/crosswalks/openid-federation-crosswalk.md`
- `docs/model/tsmm-graph-model.md`

## Contract and constraints

This binding now includes an explicit contract section in `bindings/openid-federation/tsmm-openid-federation-binding.json` and a paired constraint set at `bindings/openid-federation/constraints.json`. Together they record what the mapping preserves, where it becomes approximate, and what should not be inferred without the target ecosystem's own rules.
