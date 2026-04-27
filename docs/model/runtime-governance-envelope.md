---
owner: maintainers
last_reviewed: 2026-04-27
applicable_version: v0.18.0
tier: 1
---

# Runtime Governance Envelope

The **Runtime Governance Envelope** is the TSMM structure used when a trust decision is made close to execution. It captures the information a system must evaluate before allowing a delegated actor, agent, tool, registry client, or automation to create an operational effect.

The envelope is deliberately pre-effect. It is not an after-the-fact log. It is the admission surface where authority, delegation, revocation freshness, policy, evidence, and trust-boundary crossing are checked before the system acts.

## Why this exists

Many trust systems can describe credentials, registries, policies, and roles. Fewer can show how those elements are evaluated at runtime when a concrete action is about to happen. TSMM v0.18.0 adds the envelope so that runtime governance can be modeled and tested as a first-class trust-system surface.

The envelope answers seven questions:

1. **Who is requesting the effect?**
2. **What effect is being requested?**
3. **Which trust boundary is being crossed?**
4. **What authority or delegation justifies the request?**
5. **Which policies and evidence are used?**
6. **Was revocation state checked recently enough?**
7. **Was the effect admitted, blocked, restricted, or queued for review?**

## Machine-readable artifact

Schema:

```text
schemas/tsmm-runtime-governance.schema.json
```

Example:

```text
examples/runtime-governance-boundary-instance.json
```

Validation vectors:

```text
validation/test_vectors/valid/runtime-governance-envelope-valid.json
validation/test_vectors/invalid/runtime-governance-envelope-missing-policy.json
```

## Required fields

| Field | Purpose |
|---|---|
| `envelopeId` | Stable identifier for the runtime governance evaluation. |
| `actor` | Actor, agent, service, or organization requesting the effect. |
| `requestedEffect` | Concrete effect that would occur if admitted. |
| `trustBoundary` | Boundary crossed by the attempted effect. |
| `authorityBasis` | Authority or delegation basis asserted for the action. |
| `policyRefs` | Policies applied to the decision. |
| `evidenceRefs` | Evidence used to support the decision. |
| `revocationCheck` | Freshness and status of revocation/state validation. |
| `decision` | Admission decision and rationale. |
| `receiptExpectation` | Whether a decision receipt must be emitted. |

## Governance semantics

A runtime envelope is valid only when the attempted effect is evaluated under a bounded authority claim and a policy reference. The model intentionally treats missing policy as a validation failure because authority without policy is not governance; it is merely capability.

Revocation freshness is part of the envelope because runtime trust is temporal. An authority that was valid yesterday may not be valid at the point of effect. Implementations should define freshness windows by domain risk, effect class, and assurance level.

## Conformance expectations

- **Minimal:** identify the actor, effect, and boundary.
- **Operational:** bind the envelope to policy and evidence.
- **Assured:** include revocation freshness and emit a decision receipt.
- **Agentic:** evaluate delegation chain, tool-effect scope, and revocation state before execution.

## Relationship to existing TSMM concepts

The envelope connects these model surfaces:

- `TrustBoundary`
- `AuthorityGraph`
- `DelegationPattern`
- `EvidenceArtifact`
- `TrustDecision`
- `EffectEvaluationModel`
- `Pre-effect Governance Pattern`
- `DecisionReceipt`

This makes the envelope an execution-facing composition layer rather than a replacement for the core model.
