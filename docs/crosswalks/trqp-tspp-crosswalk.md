---
owner: maintainers
last_reviewed: 2026-03-14
applicable_version: v0.10.0
tier: 1
---

# TSMM Crosswalk: TRQP-TSPP

## Purpose

This document maps the **TRQP Security & Privacy Baseline (TSPP)** to the Trust Systems Meta Model (TSMM).

## Center of gravity

Within TSMM terms, TRQP-TSPP is primarily about:

- operator posture
- trust-registry or authoritative-directory query behavior
- profile-bound controls and requirements
- evidence-backed conformance and assurance readiness

Its center of gravity is therefore **operator-side trust infrastructure assurance**.

## Crosswalk table

| TSMM concept | TRQP-TSPP instantiation |
|---|---|
| **Governance Context** | TRQP ecosystem and Assurance Hub aligned operating context |
| **Profile** | security and privacy baseline for TRQP deployments |
| **Requirement** | profile requirements and stable control IDs |
| **Entity** | trust registry operator, directory service, relying client, bridge participant |
| **Role** | operator, query provider, verifier, client |
| **Authority** | authority to expose a query interface and publish trust-relevant metadata within governance constraints |
| **Artifact** | OpenAPI contract, metadata declaration, signed response envelope, bridge fixture, conformance report |
| **Claim** | service freshness, context constraints, signed response support, assurance posture, bridge equivalence |
| **Policy** | profile-required fields and headers, freshness semantics, context allowlisting, deployment guidance |
| **Control** | anti-enumeration expectations, rate-limiting evidence, authentication support, signed-envelope requirements, safe bridge behavior |
| **Threat** | enumeration, correlation, spoofed responses, unsafe exposure, bridge inconsistency |
| **Evidence** | evidence bundles, traceability material, JSON conformance results, deployment artifacts, test outputs |
| **Assessment** | posture evaluation against profile requirements and evidence expectations |
| **Verification** | pytest-based harness validation, schema checks, metadata checks, optional bridge-equivalence testing |
| **Level Framework** | assurance-level-parameterized expectations, with AL semantics sourced externally rather than redefined locally |
| **Trust Decision** | deployment passes or fails profile expectations at a required posture |
| **Effect** | relying systems may consume registry output with confidence appropriate to the validated posture |
| **Lifecycle Event** | registration, metadata update, signed-response enablement, bridge change, reassessment, remediation closure |

## Practical takeaway

Projects that are not implementing TRQP directly can still reuse the TSPP pattern through TSMM by adopting the following generic structure:

- declare machine-readable posture
- bind claims to explicit policy and profile requirements
- define controls against modeled threats
- require evidence for implemented safeguards
- assess and verify conformance with repeatable tooling
- tie validated posture to real downstream effects
