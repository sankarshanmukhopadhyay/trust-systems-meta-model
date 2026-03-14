---
owner: maintainers
last_reviewed: 2026-03-14
applicable_version: v0.10.0
tier: 1
---

# TSMM Crosswalk: DTG Conformance & Assurance (DCAS)

## Purpose

This document maps **DTG Conformance & Assurance (DCAS)** to the Trust Systems Meta Model (TSMM).

## Center of gravity

Within TSMM terms, DCAS is primarily about:

- portable assurance artifacts
- risk-proportionate claims
- conformance profiles and assurance levels
- evidence organization
- repeatable verifier workflow and evaluation method

Its center of gravity is therefore **assessment-oriented trust system assurance**. In the current stack, TSMM supplies the abstract semantics, while trust-infrastructure-schemas provides the canonical machine-readable trust artifact layer that DCAS can consume, assess, and package as evidence.

## Crosswalk table

| TSMM concept | DCAS instantiation |
|---|---|
| **Governance Context** | DTG ecosystem operating model, verifier workflow, standards and policy context |
| **Profile** | conformance profiles and domain-specific adoption bundles |
| **Requirement** | control objectives, test suites, evidence expectations, assurance level obligations |
| **Entity** | issuer, verifier, assessor, maintainers, ecosystem participant |
| **Role** | issuer, verifier, reviewer, profile adopter |
| **Authority** | authority to declare posture, submit evidence, evaluate bundles, and issue assurance outcomes |
| **Artifact** | declarations, CSV exports, schemas, templates, coverage reports, risk mappings |
| **Claim** | explicit and reviewable conformance or assurance statements |
| **Policy** | methodology, review cycles, governance release guidance, profile rules |
| **Control** | control objectives and mapped safeguards |
| **Threat** | risks and failure modes surfaced through risk registers and ecosystem assumptions |
| **Evidence** | evidence catalog entries, linked artifacts, coverage outputs, validation results |
| **Assessment** | verifier workflow, repeatable evaluation method, coverage analysis |
| **Verification** | CSV and structure validation, coverage checks, method-specific validation tooling |
| **Level Framework** | assurance levels and profile-defined rigor |
| **Trust Decision** | whether submitted material satisfies the selected profile or assurance posture |
| **Effect** | acceptance, rejection, remediation, or escalation of trust claims |
| **Lifecycle Event** | reassessment, remediation closure, profile update, release update |

## Practical takeaway

DCAS shows why TSMM cannot stop at claims, controls, and verification alone. Real assurance systems need:

- profiles
- requirements
- assessment method
- evidence packaging
- governance context
- repeatable effect on acceptance, remediation, or review

That is why these abstractions were made explicit in TSMM v0.3.0.


## Layering note

DCAS should not be read as redefining the artifact layer locally. Canonical trust artifact schemas now live in `trust-infrastructure-schemas`; DCAS specializes those artifacts into verifier workflows, evidence handling, and assurance outcomes. TSMM remains the semantic frame that keeps the whole stack from turning into a very earnest pile of YAML.
