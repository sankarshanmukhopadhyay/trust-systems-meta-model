---
owner: maintainers
last_reviewed: 2026-03-07
applicable_version: v0.4.0
tier: 1
---

# TSMM Lifecycle Model

## 1. Purpose

This document defines how TSMM treats lifecycle state, because trust systems do not live in a magical present tense.

## 2. Lifecycle stages

| Stage | Description |
|---|---|
| Issuance or onboarding | Authority, artifact, or profile enters valid circulation |
| Delegation | Authority is granted or propagated within defined bounds |
| Activation | A previously staged object becomes usable |
| Suspension | Temporary restriction is applied pending review or remediation |
| Revocation | Validity is withdrawn |
| Expiry | Validity ends due to time bounds |
| Remediation | Defects are corrected and posture is re-evaluated |
| Archival | Object is retained for record, audit, or evidence purposes |

## 3. Lifecycle targets

Lifecycle events may apply to:

- authorities
- artifacts
- claims
- profiles
- requirements
- trust decisions

## 4. Governance implications

### 4.1 Delegation

Delegation should not be treated as permanent inheritance. It should remain bounded by scope, purpose, policy, and revocation conditions.

### 4.2 Suspension and review

Suspension is useful when a system has reason to doubt current posture but lacks enough information for permanent revocation.

### 4.3 Revocation and downstream effect

Revocation should change what effects the system allows. A revoked authority that still produces live effects is a zombie credential problem.

### 4.4 Remediation

Remediation should be modeled explicitly because many trust failures are corrected rather than terminal.

## 5. Example lifecycle sequence

```text
Issue artifact -> delegate authority -> verify state -> allow effect
        |                |
        |                v
        |            suspend authority
        v                |
   detect defect -> remediate -> reassess -> restore bounded effect
```
