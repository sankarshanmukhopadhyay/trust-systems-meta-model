---
owner: maintainers
last_reviewed: 2026-05-05
applicable_version: v0.22.0
tier: 1
---

# Trust Infrastructure Schemas Alignment

TSMM and Trust Infrastructure Schemas (TIS) are now aligned as a two-layer executable-governance stack. The purpose of this document is to prevent semantic drift by making ownership boundaries explicit.

## Canonical layering

| Layer | Repository | Primary responsibility | Output |
| --- | --- | --- | --- |
| Semantic model | `trust-systems-meta-model` | Define portable concepts for entities, authority, delegation, policy, evidence, lifecycle state, verification, trust decisions, operational effects, and runtime governance. | Graphs, bindings, profiles, crosswalks, model examples. |
| Executable artifact contracts | `trust-infrastructure-schemas` | Define machine-validatable artifact shapes for authority boundaries, evidence bundles, evaluation envelopes, decision receipts, registry entries, assurance, controls, and artifact references. | JSON Schemas, examples, validation coverage, artifact taxonomy. |

## Operating rule

Model meaning in TSMM. Package and validate evidence in TIS. Preserve enough references that an auditor can move from a TIS artifact back to the TSMM concept, node, edge, or decision it implements.

## Scope and authority

TSMM owns the abstract meaning of authority. TIS owns the artifact contract for bounded reliance on authority. This distinction matters because authority exists as a governance relationship before it becomes an artifact claim.

A TIS authority boundary is therefore not a replacement for a TSMM authority graph. It is an artifact-level projection of a bounded portion of that graph.

## Enforcement and revocation

Both repositories apply the same rule: discovery is not authorization. Registry publication may make a trust fact discoverable, but runtime authority must still be checked against policy, evidence, scope, revocation state, and requested effect.

## Evidence and auditability

The aligned stack SHOULD produce the following evidence trail for runtime reliance:

```text
TSMM authority graph -> TIS authority boundary -> TIS evidence bundle -> TIS evaluation envelope -> TIS decision receipt -> TIS registry entry
```

The decision receipt is the audit pivot. It binds the policy, authority basis, evidence considered, revocation posture, decision result, operational effect, and review path.

## Adoption guidance

Implementers SHOULD begin with the cross-repo walkthrough in `docs/examples/tis-executable-artifact-walkthrough.md` and the machine-readable binding in `bindings/tis/tsmm-tis-binding.json`.
