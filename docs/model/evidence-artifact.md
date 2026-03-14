---
owner: maintainers
last_reviewed: 2026-03-14
applicable_version: v0.10.0
tier: 1
---

# TSMM Evidence Artifact Model

## 1. Purpose

This document defines the **EvidenceArtifact** concept for TSMM.

An EvidenceArtifact is a structured, typed output that an operational system, authorized actor, or assessment process produces in order to demonstrate that a rule was checked, a behavior occurred, or a condition holds.

The central question the concept answers is:

> How does a trust system prove behavior, not just define rules?

Most governance frameworks stop at rules. Stronger systems model:

1. rules exist
2. behavior happened
3. evidence proves it

EvidenceArtifacts occupy the third position. They are instances of the core TSMM **Evidence** abstraction, carrying enough structure to be machine-processable, policy-linked, and assessor-consumable.

## 2. Relationship to the TSMM core

EvidenceArtifact is not a new top-level core abstraction. It is a typed specialization of the existing **Evidence** entity defined in `docs/model/tsmm-entities.md`.

The core model already establishes:

- **Evidence** — material used to substantiate a claim, control, requirement, or assessment outcome
- **Evidence** supports **Assessment** and **Verification**
- **Evidence** is produced by or linked to **Actors** and **Artifacts**

EvidenceArtifact makes the production context, artifact type, and traceability fields explicit so that implementations can validate, route, and consume them consistently.

## 3. Artifact types

| Type | Description | Typical producer | TSMM core mapping |
|---|---|---|---|
| `reconciliation` | State reconciled against expected conditions. Proves the system checked itself. | Operational system | Evidence → supports → Requirement, Control |
| `drift` | Deviation between observed state and expected policy conditions. Triggers review or remediation. | Operational system | Evidence → supports → Assessment, Verification |
| `attestation` | Signed declaration by an authorized actor asserting that a condition, claim, or state holds at a point in time. | Authorized actor | Evidence → supports → Claim, Assessment |
| `conformance` | Output of a structured test or assessment run demonstrating profile requirement satisfaction. | Assessment process | Evidence → supports → Requirement, Profile |

These types are not exhaustive. Implementations may define additional types using the same structural conventions. The four types above represent the most common operational patterns observed across trust registry, verifiable credential, and agentic system contexts.

## 4. Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `id` | `idString` | Yes | Unique identifier following the `^[A-Za-z0-9._:-]+$` pattern |
| `artifactType` | `string` (enum) | Yes | One of: `reconciliation`, `drift`, `attestation`, `conformance` |
| `producedBy` | `idString → Actor` | Yes | Reference to the entity that generated this artifact |
| `timestamp` | ISO 8601 datetime string | Yes | Moment of artifact production |
| `evidenceHash` | `string` | No | Integrity anchor. Supports tamper detection and chain-of-custody claims |
| `verificationMethod` | `string` | No | How this artifact should be verified. Examples: `schema-validation`, `signature-check`, `human-review` |
| `relatedPolicy` | `idString → Policy` | No | Policy whose evaluation this artifact supports or was produced under |
| `relatedAction` | `idString → Action` | No | Action (agentic extension concept) this artifact traces. Present when produced in an agentic execution context |
| `supportsRefs` | `array[idString]` | No | References to the Claims, Controls, Requirements, Assessments, or Verifications this artifact substantiates |

## 5. Relationships

```text
Actor → produces → EvidenceArtifact
EvidenceArtifact → proves → PolicyCompliance
EvidenceArtifact → references → Action        (agentic context)
EvidenceArtifact → references → Policy
EvidenceArtifact → supports → Assessment
Assessment → produces → Trust Decision
```

These relationships follow the cardinality and dependency conventions in `docs/model/tsmm-relationships.md`.

## 6. Lifecycle

EvidenceArtifacts participate in the TSMM lifecycle model defined in `docs/model/tsmm-lifecycle.md`.

| Stage | Behavior for EvidenceArtifact |
|---|---|
| Issuance | Artifact is produced and enters valid circulation |
| Activation | Artifact becomes consumable by an assessment or verifier |
| Archival | Artifact is retained for audit, remediation, or chain-of-custody purposes |
| Revocation | Artifact is marked invalid. Assessments that relied on it should be re-evaluated |

EvidenceArtifacts do not typically undergo Suspension or Delegation. Remediation of the underlying condition produces a new artifact rather than mutating the original.

## 7. Profile expectations

| Profile | EvidenceArtifact status |
|---|---|
| Minimal | Not required |
| Operational | Not required, but drift and reconciliation artifacts are strongly recommended for live systems |
| Assured | Required. At least one evidence artifact linked to an assessment or verification |

This follows the pattern in `docs/conformance/tsmm-profile-assured.md`, which requires an evidence package linked to requirements, controls, or claims.

## 8. Relationship to the assurance extension

The assurance extension (`docs/extensions/assurance-extension.md`, schema: `schemas/tsmm-assurance-extension.schema.json`) already defines a narrower `evidenceArtifact` object used in assurance workflow contexts. That definition captures `artifactType`, `generatedByRef`, `timestamp`, and `result` for use within an assurance activity chain.

The EvidenceArtifact model defined here is the broader, cross-domain concept. It is not a replacement for the assurance extension object but an upstream definition that the assurance extension's object is consistent with. Implementations using the assurance extension satisfy the EvidenceArtifact model when they populate the shared fields.

## 9. Promotion rationale

This concept is a candidate for eventual promotion into the TSMM core under the promotion rule defined in `docs/extensions/index.md`. The current case:

1. **Cross-domain** — reconciliation, drift, attestation, and conformance evidence appear across trust registry, credential, and agentic system contexts
2. **Structurally necessary** — without typed evidence artifacts, the pathway from behavior to trust decision is underdocumented
3. **Stable** — the four types and property set are drawn from observed operational patterns and are unlikely to change in structure
4. **Broadly useful** — any TSMM-aligned system that produces outputs for downstream governance consumption needs this concept

The promotion decision is deferred until at least one operational implementation demonstrates the model in practice.
