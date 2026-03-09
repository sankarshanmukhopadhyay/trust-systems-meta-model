---
owner: maintainers
last_reviewed: 2026-03-09
applicable_version: v0.6.0
tier: 1
---

# TSMM Relationship Model

## 1. Purpose

This document describes the conceptual relationships between TSMM abstractions.

## 2. Core relationship graph

The model assumes the following high-value relationships:

- **Entity holds Role**
- **Role carries Authority**
- **Authority permits or constrains Effect**
- **Entity creates, controls, or relies on Artifact**
- **Artifact contains Claim**
- **Governance Context shapes Policy and Profile**
- **Profile bundles Requirement and Control expectations**
- **Requirement is tested by Assessment and Verification**
- **Policy evaluates Claim, Artifact, Assessment, and Verification results**
- **Control mitigates Threat**
- **Evidence substantiates Claim, Control, Requirement, Assessment, or Verification**
- **Level Framework classifies expected rigor**
- **Trust Decision is produced from Policy, Context, and evaluation results**
- **Effect occurs or is blocked based on Trust Decision**
- **Lifecycle Event can change Authority, Artifact, Claim, Profile status, or Decision state**

## 3. Compact relationship view

```text
Governance Context -> Profile -> Requirements -> Assessment -> Trust Decision -> Effect
         |                |           |             ^               ^
         v                v           v             |               |
       Policy --------> Controls -> Threats         |               |
         ^                |                         |               |
         |                v                         |               |
Entity -> Role -> Authority                    Verification <---- Evidence
   |                                             ^
   v                                             |
Artifact -> Claims -----------------------------+
```

## 4. Interpretive guidance

### Entity, role, authority
Identity is not enough. The relationship that matters operationally is whether a role holds bounded authority relevant to the effect in question.

### Governance context, profile, requirement
Real-world systems rarely operate from a raw pile of controls. They operate from profiles and requirement sets shaped by governance context.

### Assessment and verification
Verification usually checks whether a thing is valid or conforms. Assessment is the broader structured evaluation that may combine many verification results, human review, and evidence analysis.

### Decision and effect
A trust system is operational only when evaluation outcomes are tied to real effects.
