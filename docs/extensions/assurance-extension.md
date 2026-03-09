---
owner: maintainers
last_reviewed: 2026-03-09
applicable_version: v0.6.0
tier: 1
---

# TSMM Assurance Extension

## 1. Purpose

This extension adapts TSMM to **assurance-oriented trust systems**.

Some trust systems do not merely evaluate whether a claim can be accepted. They also need to show **how confidence was produced**, **which control objectives were tested**, **what evidence artifacts were generated**, and **how an assurance result can be independently reviewed**.

That is the terrain of assurance architecture.

The core TSMM model already includes **controls**, **threats**, **evidence**, **assessment**, **verification**, **profiles**, and **trust decisions**. This extension adds a more operational structure for systems that must organize those concepts into repeatable assurance workflows.

## 2. Why this is an extension

Assurance-heavy workflows are important across many trust ecosystems, but the full machinery of control catalogs, trust tasks, validation records, evidence bundles, and assurance decisions is not required by every trust system implementation.

These concepts therefore belong in an extension unless repeated cross-domain use proves they should migrate into the TSMM core.

## 3. Extension abstractions

### 3.1 Assurance Activity
An **Assurance Activity** is a structured evaluation step performed to test or substantiate trust posture.

Examples include independent validation, control testing, evidence review, profile conformance review, and periodic reassessment.

### 3.2 Trust Task
A **Trust Task** is an operational activity whose execution has assurance significance.

Examples include DID resolution, credential verification, registry validation, endpoint verification, authority delegation evaluation, and trust-list state checking.

### 3.3 Control Family
A **Control Family** groups related control objectives under a common assurance theme.

Examples include identifier integrity, credential authenticity, registry integrity, endpoint binding, delegation governance, transport integrity, and audit traceability.

### 3.4 Control Objective
A **Control Objective** is a requirement derived from one or more threats that describes a condition that must hold in order to mitigate risk.

### 3.5 Evidence Artifact
An **Evidence Artifact** is a machine-readable or human-readable output that substantiates the execution or outcome of assurance work.

Examples include validation records, signed reports, logs, checklists, snapshots, trace bundles, and remediation closure records.

### 3.6 Evidence Bundle
An **Evidence Bundle** is a grouped set of evidence artifacts assembled to support a claim, profile assessment, or assurance review.

### 3.7 Validation Record
A **Validation Record** documents the execution and outcome of a defined assurance activity or trust task.

### 3.8 Assurance Decision
An **Assurance Decision** expresses whether the evaluated subject satisfies the relevant profile, control objectives, or assurance threshold.

Examples include pass, fail, qualified pass, conditional pass, expired, suspended, and remediation required.

### 3.9 Assurance Method
An **Assurance Method** defines how assurance activities are executed and how outcomes are interpreted.

Examples include conformance harnesses, independent audit methodology, structured evidence review, and profile-based validation procedures.

## 4. Relationship to TSMM core

- A **Trust Task** is an operational specialization that can trigger **Verification**, **Assessment**, and **Evidence** generation.
- A **Control Family** organizes TSMM **Controls** into reusable assurance structures.
- A **Control Objective** refines TSMM **Requirements** and binds them more directly to a risk or threat context.
- An **Evidence Artifact** is a structured specialization of TSMM **Artifact** and **Evidence**.
- A **Validation Record** becomes evidence supporting later **Assessment**, **Verification**, and review.
- An **Assurance Decision** is a specialization of TSMM **Trust Decision** focused on assurance posture or profile satisfaction.
- An **Assurance Method** constrains how evidence is generated and how assurance outcomes are determined.

## 5. Design guidance

### 5.1 Keep threat-to-control traceability explicit
Assurance without threat traceability quickly becomes procedural theater.

### 5.2 Treat trust tasks as auditable units
Operational trust tasks should be identifiable, reviewable, and linked to validation records.

### 5.3 Separate raw evidence from assurance judgment
An evidence artifact documents what happened. An assurance decision interprets whether that is sufficient.

### 5.4 Bundle evidence for replayable review
Independent reviewers should be able to inspect evidence bundles without needing private folklore or oral tradition to decode them.

### 5.5 Bind assurance to profiles and time
Assurance posture is not eternal. Methods, evidence freshness, review cadence, and expiry should be explicit.

## 6. Example assurance workflow

1. Threat model identifies a trust-relevant risk.
2. Control family and control objectives are selected.
3. A trust task is executed or observed.
4. Validation records and evidence artifacts are generated.
5. Evidence artifacts are grouped into an evidence bundle.
6. Assurance method evaluates the bundle against profile requirements.
7. Assurance decision records the resulting posture and any remediation obligations.

## 7. Mapping note

This extension aligns closely with assurance-oriented architecture work such as:

- layered assurance architectures
- control catalogs
- evidence artifact models
- trust task taxonomies
- structured assurance workflows

It is intended as a modular home for those concepts inside TSMM without narrowing the TSMM core into an assurance-only framework.

## 8. Non-goals

This extension does not prescribe one certification regime, one audit framework, or one control taxonomy. It provides a portable structure for **assurance-oriented trust workflows grounded in controls, evidence, and review**.
