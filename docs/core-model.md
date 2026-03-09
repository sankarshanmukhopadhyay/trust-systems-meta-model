---
owner: maintainers
last_reviewed: 2026-03-09
applicable_version: v0.6.0
tier: 1
---

# TSMM Core Model

## 1. Purpose

The Trust Systems Meta Model (TSMM) provides an abstract model for how trust systems are structured and how they make operational decisions.

The model is built around a practical question:

> Under what bounded authority, policy, evidence, assessment, and verification conditions should a system allow a trust-relevant effect to occur?

TSMM is therefore not primarily identity-centered. It is **effect-centered**.

## 2. Core modeling thesis

A trust system is not only a mechanism for storing identifiers or publishing metadata.
A trust system is a mechanism for:

1. representing participants and artifacts
2. expressing claims, requirements, and constraints
3. applying policy, profiles, and controls
4. accounting for governance context and threats
5. gathering evidence
6. assessing and verifying posture or validity
7. producing a trust decision
8. permitting, denying, degrading, or routing an effect

That chain is the operational heart of TSMM.

## 3. Primary abstractions

### 3.1 Entity
An **Entity** is any actor, component, or participant that can exist within a trust system.

### 3.2 Role
A **Role** is a context-specific capacity in which an entity acts.

### 3.3 Authority
**Authority** is a bounded right, permission, mandate, or recognized competence attached to a role.

Typical attributes include:
- scope
- source
- time bounds
- conditions
- obligations
- delegation status
- revocation conditions

### 3.4 Artifact
An **Artifact** is any structured object that carries trust-relevant information.

### 3.5 Claim
A **Claim** is a proposition asserted by or about an entity, artifact, system, or state.

A claim is not automatically true. It is a statement subject to evaluation.

### 3.6 Policy
A **Policy** is a set of evaluation rules that governs interpretation, acceptance, rejection, downgrade, routing, or escalation.

### 3.7 Control
A **Control** is a safeguard that reduces a defined risk or constrains an unsafe condition.

### 3.8 Threat
A **Threat** is a modeled harm, abuse case, or failure mode that matters for trust posture or trust decisions.

### 3.9 Evidence
**Evidence** is the material used to support a claim, demonstrate a control, substantiate a requirement outcome, or support an assessment result.

### 3.10 Verification
**Verification** is a checking process that evaluates whether some expected condition holds.

### 3.11 Level Framework
A **Level Framework** is a tiered structure used to express maturity, assurance, conformance, or rigor.

### 3.12 Trust Decision
A **Trust Decision** is the evaluated outcome produced under policy and context.

### 3.13 Effect
An **Effect** is the operational consequence the system permits, denies, downgrades, routes, or records after a trust decision.

### 3.14 Lifecycle Event
A **Lifecycle Event** is a change relevant to trust posture or trust state.

## 4. Supporting abstractions added in v0.3.0

These abstractions were made explicit after reviewing how TRQP-TSPP, ERC-8004-CSP, and DCAS package requirements, profiles, and evaluation methods.

### 4.1 Governance Context
A **Governance Context** captures the institutional, legal, contractual, or ecosystem environment within which trust decisions operate.

Examples:
- a sovereign trust registry program
- a marketplace rulebook
- an assurance hub operating model
- a sector-specific governance framework

### 4.2 Profile
A **Profile** is a packaged set of requirements, controls, policy expectations, or assessment expectations defined for a particular implementation class.

Examples:
- a security and privacy baseline
- a consumer trust-signal profile
- a domain assurance baseline

### 4.3 Requirement
A **Requirement** is a normative or expected condition that a system, process, artifact, or participant should satisfy.

### 4.4 Assessment
An **Assessment** is a structured activity that evaluates whether requirements, controls, profiles, or claims are satisfied.

Assessment is broader than verification. Verification may be one checking operation. Assessment is often the orchestrated review process that uses verification outputs, evidence, and method guidance.

## 5. Why these additions matter

Without governance context, profile, requirement, and assessment, a meta-model struggles to describe how real repos actually operate.

Those concepts are visible across:

- **TRQP-TSPP**, where a profile binds controls, requirements, evidence expectations, and verification
- **ERC-8004-CSP**, where consumer policy and conformance levels shape signal handling
- **DCAS**, where profiles, control objectives, evidence structures, and verifier workflows are central

TSMM now models those ideas directly while keeping the abstraction layer lean enough to travel.
