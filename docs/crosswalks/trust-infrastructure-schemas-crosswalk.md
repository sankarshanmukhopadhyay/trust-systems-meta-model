---
owner: maintainers
last_reviewed: 2026-05-05
applicable_version: 0.23.0
tier: 1
title: Trust Infrastructure Schemas Crosswalk
permalink: /crosswalks/trust-infrastructure-schemas-crosswalk.html
parent: Crosswalks
grand_parent: Documentation
---

# Trust Infrastructure Schemas Crosswalk

This crosswalk defines how TSMM concepts map to Trust Infrastructure Schemas artifacts. The mapping is intentionally asymmetric: TSMM concepts may have broader semantic scope than the TIS artifact that implements them.

| TSMM concept | TIS artifact | Mapping strength | Alignment note |
| --- | --- | --- | --- |
| GovernanceAuthority | `governance/authority-boundary.schema.json` | Strong | TIS constrains artifact-level reliance on a TSMM authority node, edge, or delegation chain. |
| EvidenceArtifact | `common/artifact-reference.schema.json` | Strong | TIS references the artifact; TSMM explains why it matters. |
| EvidenceBundle | `evidence/evidence-bundle-manifest.schema.json` | Strong | TIS packages evidence artifacts for replay and audit. |
| Assessment | `oasf/oasf-evaluation-envelope.schema.json` | Moderate | TIS captures verifier output and assurance result. |
| TrustDecision | `decision/decision-receipt.schema.json` | Strong | TIS records the executable decision evidence. |
| TrustRegistry | `registry/registry-entry.schema.json` | Moderate | TIS publishes discoverable state; TSMM models registry authority and role. |
| AssuranceProfile | `assurance/assurance.schema.json` | Moderate | TIS AL1-AL4 express assurance rigor; TSMM profiles express modeling posture. |
| Policy | `odrl/odrl-policy-reference.schema.json` or decision policy reference | Moderate | Policy references bind rules into the decision trail. |
| Effect | `decision.result.allowed_actions`, `decision.result.prohibited_actions`, `decision.result.conditions` | Strong | TIS captures operational consequence of the decision. |

## Non-equivalence rules

1. A registry entry is not an authority grant.
2. An assurance level is not an agentic capability.
3. A schema-valid artifact is not sufficient evidence of legitimate control.
4. A decision receipt is not only a log; it is a structured governance record.

## Machine-readable binding

See `bindings/tis/tsmm-tis-binding.json` and `bindings/tis/constraints.json`.
