---
owner: maintainers
last_reviewed: 2026-05-05
applicable_version: v0.20.0
tier: 1
---

# Decision Receipt

A **Decision Receipt** is the auditable evidence object emitted when a TSMM trust decision admits, blocks, restricts, warns, downgrades, suspends, or routes an effect for review.

The receipt is not merely a log entry. It is a governance artifact. It records which authority was relied on, which policy was applied, which evidence was inspected, which revocation state was checked, which trust boundary was crossed, and what effect was admitted or denied.

## Why this exists

Runtime governance becomes difficult to audit when the decision trail is distributed across logs, policy engines, registries, tool calls, and human review notes. TSMM v0.19.0 introduces a compact receipt object so that runtime decisions can produce machine-verifiable evidence.

A receipt makes the following claims explicit:

- the decision had an identifiable subject
- the requesting actor was known
- the asserted authority had a status
- policies were applied
- evidence was used
- revocation state was checked
- an operational effect was admitted or blocked
- a review path exists

## Machine-readable artifact

Schema:

```text
schemas/tsmm-decision-receipt.schema.json
```

Example:

```text
examples/decision-receipt-runtime-example.json
```

Validation vectors:

```text
validation/test_vectors/valid/decision-receipt-valid.json
validation/test_vectors/invalid/decision-receipt-missing-policy.json
```

## Required fields

| Field | Purpose |
|---|---|
| `decisionId` | Stable identifier for the decision event. |
| `timestamp` | Time at which the decision was made or recorded. |
| `subjectRef` | Effect, artifact, claim, actor, or request being decided. |
| `requestingActorRef` | Actor or agent requesting the effect. |
| `authorityBasis` | Authority source, scope, and state. |
| `policyRefs` | Policy references used during evaluation. |
| `evidenceRefs` | Evidence references used during evaluation. |
| `boundaryRef` | Trust boundary implicated by the decision. |
| `decision` | Decision outcome and reason. |
| `effect` | Effect reference and admission state. |
| `revocationStateChecked` | Status and source of revocation check. |
| `assuranceLevel` | Conformance/assurance level asserted for the decision. |
| `reviewPath` | Where the decision can be challenged, reviewed, or escalated. |

## Receipt outcomes

The schema supports these decision outcomes:

- `allow`
- `deny`
- `warn`
- `review`
- `downgrade`
- `suspend`

The schema supports these effect admissions:

- `permitted`
- `blocked`
- `queued-for-review`
- `restricted`

## Implementation guidance

A conforming implementation should produce receipts for all high-risk runtime effects and for every denied or suspended delegated effect. Receipts should be retained according to the governing assurance profile. Receipts should be linkable to policy, evidence, authority status, and any runtime governance envelope used for pre-effect evaluation.

For agentic systems, a decision receipt is the minimum viable artifact for post-event accountability. Without it, the system may enforce a decision but cannot demonstrate why that enforcement was legitimate.
