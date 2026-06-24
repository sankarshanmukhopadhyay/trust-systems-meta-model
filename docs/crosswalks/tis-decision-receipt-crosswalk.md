---
owner: maintainers
last_reviewed: 2026-05-05
applicable_version: v0.21.0
tier: 1
---

# TIS Decision Receipt Crosswalk

TSMM models a trust decision as a policy-bound evaluation of authority, evidence, lifecycle state, and requested effect. TIS records that evaluation as a machine-validatable decision receipt.

| TSMM field | TIS field | Required preservation rule |
| --- | --- | --- |
| `decisionId` | `receipt_id` | MUST preserve decision identity. |
| `timestamp` | `timestamps.decided_at` | MUST preserve decision time. |
| `subjectRef` | `subject.subject_id` | MUST preserve evaluated subject. |
| `requestingActorRef` | evaluated artifact metadata, evidence, or extension context | SHOULD preserve actor context when the actor differs from the subject. |
| `authorityBasis` | `authority_boundary` | MUST preserve authority basis, scope, delegation, and revocation obligations. |
| `policyRefs[]` | `policy_reference` | MUST preserve applied policy. |
| `evidenceRefs[]` | `evaluated_artifacts[]` and `evidence[]` | MUST preserve evaluated evidence references. |
| `boundaryRef` | `authority_boundary` | MUST preserve artifact-level boundary. |
| `decision.outcome` | `decision_type` and `result.status` | MUST map outcome to both decision intent and validation result. |
| `effect` | `result.allowed_actions`, `result.prohibited_actions`, `result.conditions` | MUST preserve admitted and prohibited effects. |
| `revocationStateChecked` | `authority_boundary.revocation.status_check_required` and receipt timestamps | SHOULD record revocation check obligation and freshness. |
| `assuranceLevel` | `assurance.assurance_level` | SHOULD use TIS AL1-AL4 when making assurance rigor claims. |
| `reviewPath` | `result.conditions` | SHOULD preserve escalation path. |

## Outcome mapping

| TSMM outcome | TIS decision type | TIS result status |
| --- | --- | --- |
| allow | accept | passed |
| deny | reject | failed |
| warn | defer | deferred |
| review | escalate | escalated |
| downgrade | defer | deferred |
| suspend | suspend | suspended |

See `examples/cross-repo/tis-decision-receipt-mapping-example.json`.
