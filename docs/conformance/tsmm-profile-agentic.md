---
owner: maintainers
last_reviewed: 2026-05-05
applicable_version: v0.19.0
tier: 1
---

# TSMM Agentic Conformance Profile

## 1. Purpose

This profile defines the additional conformance expectations that apply when TSMM is used to govern agentic or delegated-action deployments. It is not a fourth maturity tier. It is a cross-cutting profile that may be applied alongside the Operational or Assured baseline.

## 2. Why this profile exists

The existing Minimal, Operational, and Assured profiles describe increasing rigor for general trust-system implementation. Agentic systems introduce a different problem shape. The primary risks are not only around identity, policy, or evidence. They are around delegated action, runtime context, oversight mode, and traceability of effects.

## 3. Profile scope

This profile applies where a system includes one or more of the following characteristics:

- software agents acting under delegated authority
- tool-using or workflow-executing agents
- multi-agent coordination with shared effect paths
- automated or semi-automated actions that may create rights-affecting or governance-relevant outcomes

## 4. Required controls

### 4.1 Delegation artifacts
Implementations SHALL define explicit delegation artifacts or records that bind delegator, delegate, scope, obligations, and revocation conditions.

### 4.2 Oversight mode declaration
Implementations SHALL declare the oversight mode for governed actions. Oversight mode SHOULD be recorded per action class or per workflow.

### 4.3 Risk-tier documentation
Implementations SHALL classify agentic actions by risk tier and SHALL document the rationale used to assign the tier.

### 4.4 Trace record structure
Implementations SHALL preserve structured trace records for governed actions, including action reference, context reference, applicable delegation, and resulting effect where one occurs.

### 4.5 Escalation and review
Implementations SHOULD define when an agentic action is denied, downgraded, routed for approval, or sampled for review.

### 4.6 Multi-agent coordination
Where multiple agents participate in a single effect chain, implementations SHALL document coordination boundaries and SHOULD define which agent is accountable for which action stage.

## 5. Relationship to baseline profiles

The Agentic Profile is additive. It does not replace Operational or Assured requirements. It constrains how those baselines apply in agentic contexts.

## 6. Evidence expectations

Suitable evidence may include delegation records, workflow approval policies, trace logs, risk-tier inventories, oversight procedures, remediation workflows, and coordination diagrams.
