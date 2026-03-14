---
owner: maintainers
last_reviewed: 2026-03-14
applicable_version: v0.9.0
tier: 1
---

# TSMM Entity Catalog

## 1. Purpose

This document defines the core TSMM entities in a more normative form than the conceptual overview in `docs/core-model.md`.

The objective is portability. Different ecosystems can name things differently, but if they share these structural invariants they can still map to a common trust grammar.

## 2. Core entities

| Entity | Description | Mandatory fields |
|---|---|---|
| Actor | A person, organization, software agent, or system component capable of participating in a trust-relevant flow | `id`, `type` |
| Role | The context-specific capacity in which an actor operates | `id`, `type` |
| Authority | A bounded right, mandate, permission, or recognized competence attached to a role | `id`, `scope` |
| Artifact | A structured object that carries trust-relevant information | `id`, `type` |
| Claim | A proposition asserted by or about an actor, artifact, system, or state | `id`, `statement` |
| Policy | A ruleset governing acceptance, denial, routing, downgrade, or escalation | `id`, `name`, `decisionMode` |
| Requirement | A normative condition that should be satisfied | `id`, `statement` |
| Control | A safeguard that reduces risk or constrains unsafe behavior | `id`, `type` |
| Threat | A modeled harm, abuse case, or failure mode relevant to trust posture | `id`, `type` |
| Evidence | Material used to substantiate a claim, requirement, control, or assessment outcome | `id`, `type` |
| Assessment | A structured evaluation activity over requirements, controls, or profiles | `id`, `method`, `result` |
| Verification | A checking operation that evaluates whether a target condition holds | `id`, `method`, `result` |
| Trust Decision | The evaluated outcome produced under policy and context | `id`, `outcome`, `policyRef`, `effectRefs` |
| Effect | The operational consequence permitted, denied, degraded, routed, or recorded | `id`, `class`, `action`, `status` |
| Lifecycle Event | A state change affecting trust posture or trust-relevant validity | `id`, `type`, `targetRef` |

## 3. Modeling rules

### 3.1 Actor and role

An actor does not carry raw, universal permission. It participates through one or more roles.

### 3.2 Role and authority

A role should only be treated as operationally meaningful when the role carries bounded authority. Unbounded authority is governance confetti.

### 3.3 Artifact and claim

Artifacts may contain one or more claims. Claims should not be treated as self-proving merely because they are well dressed in JSON.

### 3.4 Policy and effect

A policy exists to govern whether an evaluation can produce an effect. If there is no defined effect, the system is documenting trust rather than operating it.

### 3.5 Evidence and assessment

Evidence supports assessment and verification. Evidence may also support claims, controls, or requirements directly.

## 4. Minimal implementation expectation

A TSMM implementation should include at least the following objects:

- one actor with one role and bounded authority
- one policy
- one trust decision
- one effect

That is the smallest useful skeleton that still behaves like a trust system rather than a decorative ontology.
