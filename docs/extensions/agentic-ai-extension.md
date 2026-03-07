---
owner: maintainers
last_reviewed: 2026-03-07
applicable_version: v0.5.0
tier: 1
---

# TSMM Agentic AI Extension

## 1. Purpose

This extension adapts TSMM to **agentic AI systems** without expanding the TSMM core in ways that would make it domain-heavy.

Agentic systems introduce runtime questions that are sharper than simple identity or artifact validation. The central question becomes:

> Should this agent, under this delegation, with these capabilities and in this execution context, be allowed to attempt this action and produce this effect?

## 2. Why this is an extension

Agent planners, toolchains, approval states, and multi-agent coordination are operationally important for agentic systems, but they are not universal across all trust systems. They therefore belong in an extension unless repeated cross-domain use proves otherwise.

## 3. Extension abstractions

### 3.1 Agent
An **Agent** is an entity that can plan, select, or execute bounded actions, typically on behalf of a principal, operator, or workflow.

### 3.2 Action
An **Action** is an intended or attempted operation. It is distinct from an **Effect**, which is the realized consequence after evaluation and execution.

### 3.3 Delegation
A **Delegation** is an explicit grant that binds a delegator, a delegate, a scope of authority, obligations, and revocation conditions.

### 3.4 Capability
A **Capability** describes the class of operations an agent is allowed to perform.

### 3.5 Resource
A **Resource** is the object, dataset, system, or endpoint that an action touches.

### 3.6 Execution Context
An **Execution Context** captures runtime conditions relevant to evaluation. Examples include session state, user presence, environment, data sensitivity, transaction value, and approval state.

### 3.7 Oversight Mode
An **Oversight Mode** expresses whether an action path is autonomous, pre-approved, approval-gated, sampled for review, fully manual, or subject to emergency override.

### 3.8 Trace Record
A **Trace Record** captures provenance for a multi-step agent action path: input trigger, tool calls, evidence gathered, policy checks, approvals, outputs, and resulting effects.

### 3.9 Risk Tier
A **Risk Tier** classifies workflow severity so that stronger controls can be required for rights-affecting or high-impact automation.

## 4. Relationship to TSMM core

- An **Agent** is a specialized TSMM **Entity**.
- A **Delegation** specializes bounded **Authority** and links it to an acting agent.
- A **Capability** constrains which **Action** types can be attempted.
- An **Execution Context** informs **Policy**, **Assessment**, **Verification**, and the resulting **Trust Decision**.
- A **Trace Record** becomes structured **Evidence** for later audit, review, and remediation.
- A **Risk Tier** informs profile and policy selection.

## 5. Design guidance

### 5.1 Separate action from effect
An agent may propose or attempt an action that never produces an effect. Governance should evaluate both the attempted action and the realized effect.

### 5.2 Make delegation explicit
Do not infer agent authority from identity alone. Delegation must be bounded, reviewable, and revocable.

### 5.3 Bind capability to risk tier
A low-risk informational agent should not silently drift into rights-affecting action simply because it can call another tool.

### 5.4 Preserve execution trace
Without traceability, agent governance degrades into post-hoc guesswork with better branding.

## 6. Example evaluation flow

1. Principal grants delegation to an agent.
2. Agent requests an action against a resource.
3. Policy evaluates delegation, capability, execution context, and risk tier.
4. Oversight mode determines whether approval is required.
5. Trust decision permits, denies, downgrades, or routes the action.
6. If executed, the resulting effect and trace record are stored as evidence.

## 7. Non-goals

This extension does not define model architecture, prompting methods, benchmark methodology, or ML safety claims in general. It focuses on **bounded delegated action under policy, evidence, and review**.
