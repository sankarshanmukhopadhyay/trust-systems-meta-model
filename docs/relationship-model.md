# TSMM Relationship Model

## 1. Purpose

This document defines the primary relationships among TSMM concepts.

The core model names the pieces.  
The relationship model explains how the pieces constrain one another.

That distinction matters. A pile of concepts without relationship logic is not a model. It is a glossary cosplaying as architecture.

## 2. Canonical relationships

### 2.1 Entity holds Role
An **Entity** may hold one or more **Roles**.

Examples:
- an organization may act as an issuer and an operator
- a wallet may act as both consumer and presenter
- a software agent may act as a delegate under a bounded mandate

### 2.2 Role carries Authority
A **Role** carries one or more **Authority** objects.

Authority is never assumed from identity alone. It is attached through a contextual role.

### 2.3 Authority is bounded by constraints
An **Authority** is constrained by:
- scope
- time
- conditions
- obligations
- revocation status
- delegation rules

These constraints are not decorative metadata. They determine whether a downstream effect is legitimate.

### 2.4 Entity creates, controls, or references Artifact
An **Entity** may create, issue, publish, sign, host, maintain, consume, or reference an **Artifact**.

Artifacts are the transportable and inspectable carriers of trust-relevant data.

### 2.5 Artifact contains or points to Claim
An **Artifact** contains, encodes, or references one or more **Claims**.

The same artifact may carry multiple claims with different trust significance.

### 2.6 Policy governs interpretation
A **Policy** governs how **Claims**, **Artifacts**, **Authorities**, **Levels**, and **Verification** outputs are interpreted.

Policy is the context engine of the model.

### 2.7 Control mitigates Threat
A **Control** exists to reduce, detect, contain, or prevent a **Threat**.

A control without a mapped threat is often cargo-cult security wearing a hard hat.

### 2.8 Evidence substantiates Claim, Control, Verification, or Level assertion
**Evidence** may support:
- a claim made in an artifact
- the implementation of a control
- the result of a verification step
- the attainment of a level

Evidence is not restricted to audits. It includes any material that can ground an evaluation.

### 2.9 Verification evaluates trust-relevant material
**Verification** evaluates one or more of:
- artifact validity
- claim integrity
- control implementation
- policy conformance
- evidence sufficiency
- level alignment

Verification produces inputs to a trust decision.

### 2.10 Level Framework classifies rigor or posture
A **Level Framework** classifies implementation rigor, assurance expectation, maturity, or risk tier.

A level framework does not act on its own. It shapes policy thresholds and expected evidence.

### 2.11 Trust Decision is produced under policy
A **Trust Decision** is produced by applying **Policy** to the outputs of **Verification**, contextualized by authority, level, and constraints.

Trust decisions are not free-floating opinions. They are governed outcomes.

### 2.12 Effect is produced, blocked, degraded, or routed
An **Effect** is allowed, denied, downgraded, or routed based on the **Trust Decision**.

This is the operational end of the relationship chain.

### 2.13 Lifecycle Event changes state
A **Lifecycle Event** changes the state of one or more of:
- authority
- artifact
- claim
- policy
- control
- level
- trust decision context

Lifecycle is how the system remembers that the world moves.

## 3. Relationship graph

```text
Entity --holds--> Role --carries--> Authority --permits/constrains--> Effect
   |                              |
   |                              +--bounded by--> Policy / Conditions / Time
   |
   +--creates/controls/references--> Artifact --contains--> Claim
                                              |
                                              +--substantiated by--> Evidence

Control --mitigates--> Threat
Policy --governs--> Claim / Artifact / Verification / Decision
Evidence --supports--> Claim / Control / Verification / Level
Verification --evaluates--> Artifact / Claim / Control / Policy / Evidence / Level
Verification --produces--> Trust Decision
Trust Decision --allows/denies/routes--> Effect
Lifecycle Event --changes--> Authority / Artifact / Claim / Policy / Level / Decision Context
```

## 4. Cardinality guidance

TSMM is abstract, but some practical cardinality assumptions are useful.

- one **Entity** may hold many **Roles**
- one **Role** may carry many **Authority** objects
- one **Artifact** may carry many **Claims**
- one **Policy** may govern many evaluations
- one **Threat** may be mitigated by many **Controls**
- one **Trust Decision** may control one or more **Effects**
- one **Lifecycle Event** may change many objects

TSMM does not require every system to implement all these relationships explicitly, but the model assumes they exist conceptually.

## 5. Constraint guidance

The following guardrails are recommended for any implementation derived from TSMM.

### 5.1 No direct identity-to-effect shortcut
Implementations should avoid a direct shortcut from identity to effect.

The preferred route is:

**Entity -> Role -> Authority -> Policy and Verification -> Trust Decision -> Effect**

### 5.2 Claims should not imply truth without evaluation
Artifacts may carry claims, but claims should not be treated as truth merely because they are present.

### 5.3 Levels should not override policy
A high level should not bypass local policy. It should inform evaluation, not replace it.

### 5.4 Effects should remain contextual
The same validated artifact may produce different effects in different policy environments.

### 5.5 Lifecycle must be first-class
Revocation, expiry, suspension, reassessment, and remediation closure should be treated as normal events, not as edge-case cleanup.

## 6. Relationship patterns worth reusing

### 6.1 Operator assurance pattern
Used where a system publishes trust-relevant artifacts and needs to prove posture.

Pattern:
- entity acts as operator
- artifacts publish claims
- controls mitigate operator threats
- evidence and verification support posture
- trust decision permits downstream reliance

### 6.2 Consumer interpretation pattern
Used where a system consumes external trust signals.

Pattern:
- entity acts as consumer
- artifacts are fetched or presented
- policy controls interpretation
- controls mitigate fetch and presentation risks
- trust decision determines whether the signal should cause a user-facing effect

### 6.3 Delegated action pattern
Used where software acts on behalf of a principal.

Pattern:
- entity acts as delegate
- role carries bounded authority
- lifecycle and revocation become critical
- trust decision determines whether a delegated effect should occur

## 7. Implementation note

The JSON schema in `schemas/tsmm-core.schema.json` gives a minimal machine-readable representation of these relationships. It is intentionally small. Giant schemas are how useful abstractions die under paperwork.
