---
owner: maintainers
last_reviewed: 2026-03-09
applicable_version: v0.6.0
tier: 1
---

# TSMM Effect Evaluation Model

## 1. Purpose

This document formalizes the execution-time logic of TSMM trust decisions.

The key question is not just whether an actor is known. The key question is whether a specific effect should be allowed right now.

## 2. Canonical inputs

| Input | Description |
|---|---|
| Actor | The acting person, organization, or software agent |
| Role | The capacity in which the actor is acting |
| Authority | The bounded right or mandate being exercised |
| Artifact | The relevant trust-carrying object |
| Claim | The propositions under evaluation |
| Governance context | Institutional, contractual, legal, or ecosystem setting |
| Policy | Decision rules to apply |
| Profile and requirements | Applicable baseline or implementation class |
| Controls and threats | Relevant safeguards and failure modes |
| Evidence | Supporting material |
| Assessment | Structured evaluation outputs |
| Verification | Point checks over target conditions |
| Lifecycle state | Revoked, suspended, expired, active, remediated, or similar |

## 3. Canonical evaluation flow

```text
Input collection
    -> authority validation
    -> policy lookup
    -> lifecycle state check
    -> requirement and control evaluation
    -> evidence sufficiency check
    -> risk and threat threshold check
    -> decision outcome
    -> effect selection
    -> logging and review routing
```

## 4. Canonical outputs

| Output | Description |
|---|---|
| Trust decision | Accept, deny, warn, downgrade, quarantine, or review |
| Permitted or blocked effect | What the system actually does |
| Trace record | What evidence, verification, and policy produced the outcome |
| Escalation | Human review or exception handling where needed |

## 5. Design implication

This is the operational heart of TSMM. Governance shifts from identity verification to effect authorization.
