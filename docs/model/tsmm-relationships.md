---
owner: maintainers
last_reviewed: 2026-03-14
applicable_version: v0.9.0
tier: 1
---

# TSMM Relationship Specification

## 1. Purpose

This document specifies the high-value TSMM relationships in a more formal way than `docs/relationship-model.md`.

## 2. Normative relationships

| Source | Relationship | Target | Cardinality guidance |
|---|---|---|---|
| Actor | holds | Role | one-to-many |
| Role | carries | Authority | zero-to-many |
| Authority | bounded by | Policy | many-to-one or many-to-many |
| Authority | permits or constrains | Effect | many-to-many |
| Actor | creates, controls, or relies on | Artifact | many-to-many |
| Artifact | contains | Claim | zero-to-many |
| Governance Context | shapes | Policy | one-to-many |
| Governance Context | shapes | Profile | one-to-many |
| Profile | bundles | Requirement | one-to-many |
| Profile | expects | Control | zero-to-many |
| Control | mitigates | Threat | many-to-many |
| Evidence | supports | Claim, Control, Requirement, Assessment, or Verification | many-to-many |
| Assessment | evaluates | Requirement or Profile | many-to-many |
| Verification | checks | Artifact, Claim, Control, or state | many-to-many |
| Policy | evaluates | Claim, Assessment, Verification, and context state | many-to-many |
| Policy | produces | Trust Decision | one-to-many |
| Trust Decision | permits, denies, degrades, or routes | Effect | one-to-many |
| Lifecycle Event | changes state of | Authority, Artifact, Claim, Profile, or Decision | many-to-one |

## 3. Compact view

```text
Actor -> Role -> Authority -> Effect
  |                  |           ^
  v                  v           |
Artifact -> Claim -> Policy -> Trust Decision
  ^                  ^
  |                  |
Evidence -> Assessment and Verification
  ^
  |
Control -> Threat

Governance Context -> Policy and Profile -> Requirement
Lifecycle Event -> changes Authority, Artifact, Claim, Profile, or Decision state
```

## 4. Dependency rules

### 4.1 Authority should be bounded

Authority should include scope and should normally carry time bounds, conditions, obligations, or revocation semantics.

### 4.2 Effects should be explicit

Every trust decision should point to at least one effect. Otherwise the evaluation has no operational landing zone.

### 4.3 Policy should be contextual

Policy should be understood within governance context and, where relevant, within a profile. Policy without context is usually a compliance costume.

### 4.4 Evidence should be attached to evaluation

Evidence should support claims, controls, requirements, assessments, or verifications. Floating evidence without evaluation linkage is archival soup.
