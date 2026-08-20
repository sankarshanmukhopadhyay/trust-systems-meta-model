---
owner: maintainers
last_reviewed: 2026-05-05
applicable_version: 0.24.0
tier: 1
title: TrustBoundary
permalink: /model/trust-boundary.html
parent: Model
grand_parent: Documentation
---

# TrustBoundary

## Concept definition

A **TrustBoundary** is the modeled edge across which an actor, agent, service, registry, tool, or control plane accepts input, authority, or execution requests from another party under bounded conditions.

TSMM already models entities, roles, authority, policy, evidence, trust decisions, and effects. TrustBoundary adds a more explicit answer to a practical governance question: **where does a request cross from one accountable execution context into another?**

This matters because many failures in agentic and trust systems do not begin with a malformed credential. They begin when a system accepts a request across a boundary without proving:

- who is acting
- what authority is being relied upon
- what policy applies at this edge
- what evidence or status freshness is required
- what effect is allowed if the request passes

## Why model it explicitly

A trust system can have valid credentials and still make unsafe decisions if runtime boundaries are not described clearly. The same named agent may participate in multiple boundaries with different control expectations:

- **human → agent** for instruction intake and step-up approval
- **agent → agent** for delegated sub-tasks and bounded authority transfer
- **agent → tool** for side-effecting actions against infrastructure or data stores
- **agent → control plane** for policy updates, state synchronization, or execution override
- **agent → knowledge source** for retrieval into a decision path

TrustBoundary is therefore a modeling aid for distinguishing **identity**, **authority**, and **execution admission**.

## Relationship to existing TSMM abstractions

| TSMM abstraction | Relationship |
|---|---|
| `Entity` | A boundary connects accountable entities or services operating under distinct control conditions |
| `Authority` | A boundary constrains which authority can traverse the edge |
| `Policy` | The boundary names the policy surface evaluated before execution |
| `Evidence` | Boundary crossing may require evidence such as identity proof, revocation status, or task scope |
| `TrustDecision` | A boundary crossing either results in a trust decision or an interrupt such as checkpoint, deny, downgrade, or review |
| `Effect` | The boundary determines what downstream effect can occur if admission succeeds |
| `LifecycleEvent` | Suspension, revocation, replay, rollback, or kill-switch activation can be boundary-governed events |

## Suggested properties

TrustBoundary is introduced here as an **experimental supporting abstraction** rather than a required core-schema primitive. Implementers may model it using existing TSMM objects until a stable schema surface is needed.

Suggested descriptive properties:

| Property | Description |
|---|---|
| `id` | Stable boundary identifier |
| `sourceRef` | Originating entity, service, or role |
| `targetRef` | Receiving entity, service, or role |
| `boundaryType` | `human-agent`, `agent-agent`, `agent-tool`, `agent-control-plane`, `agent-knowledge`, or ecosystem-defined equivalent |
| `policyRefs` | Policies evaluated at this edge |
| `requiredEvidenceRefs` | Evidence or status material needed before effect |
| `allowedEffectClasses` | Effect classes permitted across the boundary |
| `failureMode` | Expected fail behavior such as deny, review, suspend, or degrade |
| `statusFreshnessRequirement` | Freshness expectation for revocation or runtime state |

## Design notes

### Boundary-first analysis improves assurance

When a repo or implementation starts with boundaries, the resulting control model becomes easier to test. Instead of asking “is the agent trusted?”, the evaluator asks “what is trusted **at this edge**, under what policy, and for what effect?”

### Boundary modeling is not a replacement for isolation

TSMM models the governance meaning of a boundary. It does not claim OS-level separation or sandboxing by itself. That distinction is also explicit in the Microsoft Agent Governance Toolkit architecture notes, which describe deterministic application-layer interception and recommend composing with container or VM isolation for defense in depth. See `docs/crosswalks/agent-governance-toolkit-crosswalk.md` for the upstream reference context.

## Related artifacts

- [Pre-effect Governance Pattern](../patterns/pre-effect-governance-pattern.md)
- [AuthorizationCheckpoint](authorization-checkpoint.md)
- [Delegation patterns](delegation-patterns.md)
- [Agent Governance Toolkit crosswalk](../crosswalks/agent-governance-toolkit-crosswalk.md)
