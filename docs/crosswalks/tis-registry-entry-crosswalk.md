---
owner: maintainers
last_reviewed: 2026-05-05
applicable_version: v0.20.0
tier: 1
---

# TIS Registry Entry Crosswalk

TSMM models registries as governance surfaces. TIS defines a registry entry as an executable publication unit.

## Alignment rule

A TIS registry entry MAY publish a trust fact modeled by TSMM, but publication does not itself create runtime authority. Runtime reliance still requires authority, evidence, policy, revocation, assurance, and effect evaluation.

## Minimum references

A TSMM-aligned TIS registry entry SHOULD reference:

- declaration artifact;
- assurance level;
- controls checked;
- evidence bundle;
- evaluation envelope;
- decision receipt, where a relying-party decision exists;
- authority boundary.

See `examples/cross-repo/tsmm-registry-to-tis-entry.example.json`.
