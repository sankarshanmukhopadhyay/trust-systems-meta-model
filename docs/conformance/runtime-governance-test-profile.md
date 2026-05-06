---
owner: maintainers
last_reviewed: 2026-05-05
applicable_version: v0.20.0
tier: 1
---

# Runtime Governance Test Profile

The **Runtime Governance Test Profile** defines the minimum testable obligations for TSMM implementations that make or model pre-effect trust decisions.

It applies when a system evaluates an attempted operational effect by an actor, agent, service, tool, registry client, or delegated automation.

## Required test surfaces

| Test surface | Required evidence |
|---|---|
| Actor identity | Actor or agent reference is present. |
| Effect definition | Requested effect has action, class, and target. |
| Trust boundary | Boundary crossing is identified. |
| Authority basis | Authority reference, source, scope, and state are present. |
| Policy binding | At least one policy reference is attached. |
| Evidence binding | At least one evidence reference is attached. |
| Revocation freshness | Status source, status value, check time, and freshness window are present. |
| Decision outcome | Outcome and effect admission are recorded. |
| Receipt emission | Receipt expectation is declared, and receipt schema is referenced where required. |

## Positive tests

A valid runtime governance envelope should pass when:

- authority status is active
- policy references are present
- evidence references are present
- revocation state is fresh
- the requested effect is within scope
- a decision receipt is required for high-risk effects

Reference vector:

```text
validation/test_vectors/valid/runtime-governance-envelope-valid.json
```

## Negative tests

An implementation should fail or reject an envelope when:

- policy references are missing
- authority status is revoked, suspended, expired, stale, or unavailable
- revocation freshness exceeds the permitted window
- the requested effect is outside authority scope
- a high-risk effect has no receipt expectation

Reference vector:

```text
validation/test_vectors/invalid/runtime-governance-envelope-missing-policy.json
```

## Assurance mapping

| TSMM profile | Runtime obligation |
|---|---|
| Minimal | Identify actor, effect, and boundary. |
| Operational | Bind authority, policy, and evidence. |
| Assured | Emit decision receipts and retain review path. |
| Agentic | Validate delegation chain, revocation freshness, and effect scope before execution. |

## Evidence produced

A conforming implementation should produce at least one of the following artifacts:

- validated runtime governance envelope
- decision receipt
- failed validation output for invalid envelope
- audit trail linking envelope, policy, evidence, authority, and effect
