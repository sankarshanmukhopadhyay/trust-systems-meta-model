---
owner: maintainers
last_reviewed: 2026-05-05
applicable_version: 0.23.0
tier: 1
title: Pre-effect Governance Pattern *(experimental)*
permalink: /patterns/pre-effect-governance-pattern.html
parent: Patterns
grand_parent: Documentation
---

# Pre-effect Governance Pattern *(experimental)*

## Purpose

This pattern describes how a trust system makes a decision **immediately before an effect is allowed to occur**.

The pattern is motivated by a practical execution insight reinforced by the Microsoft Agent Governance Toolkit: governance becomes operational only when an action request is intercepted and evaluated against policy before execution. The upstream toolkit frames this as deterministic application-layer interception where every agent action is evaluated against policy before execution. TSMM adopts that idea here as an **experimental pattern**, not as a core requirement, so that systems can model runtime governance without changing the stable core semantics.

## Pattern statement

A requested effect SHOULD be admitted only after the system can determine, at the relevant trust boundary:

1. which actor or agent is requesting the effect
2. what authority basis is being relied upon
3. what policy and profile apply
4. what evidence and freshness conditions are required
5. what trust decision is reached
6. what effect is produced, denied, downgraded, delayed, or sent for review

## Canonical sequence

**Request → boundary admission check → policy evaluation → evidence/status verification → trust decision → effect**

This pattern is useful where static publication alone is not enough:

- delegated agent actions
- tool invocation with side effects
- registry publication or status mutation
- step-up approval before high-risk operations
- runtime revocation or kill-switch handling

## Minimal TSMM mapping

| Pattern stage | TSMM object(s) |
|---|---|
| Request enters system | `Entity`, `InteractionContext`, optional `TrustBoundary` |
| Authority basis located | `Authority`, `Artifact`, `Claim` |
| Policy surface selected | `Policy`, `Profile`, `Requirement` |
| Evidence and freshness checked | `Evidence`, `Verification`, `Assessment` |
| Decision reached | `TrustDecision` |
| Consequence applied | `Effect`, `LifecycleEvent` |

## Common outcomes

- **allow** when authority, policy, and evidence all hold
- **deny** when the requested effect exceeds scope or violates policy
- **review** when evidence is insufficient but escalation is legitimate
- **degrade** when a weaker effect is allowed than originally requested
- **suspend** when the interaction must wait for a checkpoint or status refresh
- **terminate** when a kill switch, revocation, or safety condition invalidates the path

## Design implications

### A. Publication is not execution governance

Publishing identity, metadata, or policy does not by itself govern runtime effects. The effect remains unguided until a request is checked at execution time.

### B. Revocation matters at the decision point

A valid artifact at issuance time may be stale at action time. This pattern therefore treats freshness and revocation as **decision-time inputs**, not archival annotations.

### C. Decision trails should be reproducible

To support assurance, the system should be able to reproduce which authority, policy, evidence, and status inputs led to the effect. That does not require a specific implementation, but it strongly favors structured receipts or tamper-evident event trails.

## Recommended usage

Use this pattern when modeling:

- agent-to-tool execution
- agent-to-agent delegation
- checkpointed human approval
- registry state mutation
- runtime policy enforcement overlays

## Related artifacts

- [TrustBoundary](../model/trust-boundary.md)
- [Effect-centered trust decision model](../effect-centered-trust-decision-model.md)
- [Delegated Agent Pattern](delegated-agent-pattern.md)
- Example: `examples/runtime-governance-pre-effect-instance.json`
