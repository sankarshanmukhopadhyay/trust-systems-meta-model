---
owner: maintainers
last_reviewed: 2026-05-05
applicable_version: v0.21.0
tier: 1
---

# TSMM to Verifiable Trust Communities Binding

## Purpose

This binding packages the Verifiable Trust Communities extension into the same machine-readable binding shape used for external ecosystem mappings. That allows community-oriented TSMM deployments to publish VTC alignment as infrastructure rather than prose.

## Why it exists

The VTC extension has been one of the more developed TSMM specializations, but until now it was not represented in the binding catalog. v0.11.0 closes that gap.

## Binding summary

The binding maps the main VTC abstractions into TSMM:

- Verifiable Trust Community to TrustDomain
- Community Governance Authority to GovernanceAuthority
- Community Member Registry to TrustRegistry
- Membership Credential to Credential
- Community Relying Service to RelyingParty

## Artifact

- `bindings/vtc/tsmm-vtc-binding.json`

## Notes

The VTC binding is useful both for comparison across ecosystems and for publication through the TSMM registry format where extension-specific artifacts need first-class indexing.

## Contract and constraints

This binding now includes an explicit contract section in `bindings/vtc/tsmm-vtc-binding.json` and a paired constraint set at `bindings/vtc/constraints.json`. Together they record what the mapping preserves, where it becomes approximate, and what should not be inferred without the target ecosystem's own rules.
