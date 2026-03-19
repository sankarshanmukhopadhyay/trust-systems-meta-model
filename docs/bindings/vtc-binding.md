---
owner: maintainers
last_reviewed: 2026-03-19
applicable_version: v0.11.0
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
