---
owner: maintainers
last_reviewed: 2026-05-05
applicable_version: 0.24.0
tier: 2
title: TSMM ↔ OASF Crosswalk
permalink: /crosswalks/oasf-crosswalk.html
parent: Crosswalks
grand_parent: Documentation
---

# TSMM ↔ OASF Crosswalk

## Why this crosswalk exists

OASF is becoming a useful publication layer for agent descriptions, extensions, and evaluation artifacts. TSMM is not trying to duplicate that work. The value here is to clarify **which OASF objects can act as transport surfaces for TSMM-relevant trust semantics**.

Without this crosswalk, an assurance system can ingest an OASF record but still lack clarity on what the record means in trust terms. With this crosswalk, OASF becomes a practical carrier for assurance-addressable trust metadata.

## Crosswalk table

| OASF object / surface | Closest TSMM abstraction | Assurance significance |
| --- | --- | --- |
| `record` | `ServiceDescriptor` | Entry point for describing the subject under evaluation. |
| `publisher` | `Operator` | Indicates who is accountable for the publication surface. |
| `a2a_data` | `InteractionContext` | Captures protocol-facing interaction metadata relevant to trust decisions. |
| `evaluation_report` | `Assessment` | Carries structured evaluation output that can be reviewed or reused. |
| `referred_evaluation` | `EvidenceArtifact` | Lets an assessment cite external evidence rather than flattening it into prose. |
| module / extension attachment | `ExtensionContract` | Attaches bounded ecosystem-specific semantics such as ANAB control publication requirements. |

## Publication-oriented interpretation

Use the crosswalk together with [OASF publication guidance](../profiles/oasf-publication-guidance.md) when the objective is not just comparison but discoverable publication. In that mode, the crosswalk helps ensure that published records still expose operator accountability, policy or profile references, evidence pointers, and status semantics.

## Practical use across this repo set

### TSMM
TSMM uses the crosswalk to identify which OASF surfaces can be treated as trust-relevant model carriers.

### ANAB
ANAB uses the crosswalk to publish naming, operator-binding, and evidence expectations through an OASF-aware profile rather than inventing a separate discovery envelope.

### DCAS
DCAS uses the crosswalk to consume OASF-described subjects and produce evaluation outputs that remain traceable to TSMM entities and ANAB controls.

## Strategic point

The important move is not “put all trust semantics into OASF.” That would be the wrong architectural instinct. The important move is to make OASF publications **referenceable by assurance systems that need stable meaning, traceable controls, and replayable evidence**.
