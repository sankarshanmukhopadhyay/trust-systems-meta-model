---
owner: maintainers
last_reviewed: 2026-05-05
applicable_version: v0.19.0
tier: 1
---

# TSMM Minimal Profile

## 1. Purpose

The Minimal Profile defines the smallest TSMM implementation that still counts as an operational trust system.

## 2. Required elements

| Requirement | Description |
|---|---|
| Core actor-role-authority chain | At least one actor, one role, and bounded authority |
| Policy | At least one policy governing a trust decision |
| Trust decision | At least one trust decision outcome |
| Effect | At least one effect linked from the trust decision |

## 3. Suitable use cases

- early design work
- conceptual mapping exercises
- low-risk informational flows
- architecture comparison work

## 4. Not yet expected

The Minimal Profile does not require formal assessment, explicit evidence packaging, or threat modeling. It is intentionally lean.

## v0.19.0 runtime governance obligation

This profile now recognizes the runtime assurance layer introduced in TSMM v0.19.0. Implementations that evaluate operational effects should use the Runtime Governance Envelope and Decision Receipt artifacts where applicable.

Minimum expectation by profile maturity:

- **Minimal:** identify actor, requested effect, and trust boundary.
- **Operational:** bind the decision to authority, policy, and evidence.
- **Assured:** emit a decision receipt with review path and revocation-state evidence.
- **Agentic:** evaluate delegation chain, revocation freshness, and effect scope before execution.

Reference: `docs/conformance/runtime-governance-test-profile.md`.
