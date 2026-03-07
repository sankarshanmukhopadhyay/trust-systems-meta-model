# TSMM Crosswalk: TRQP-TSPP

## Purpose

This document maps the **TRQP Security & Privacy Baseline (TSPP)** to the Trust Systems Meta Model (TSMM).

The goal is not to restate TSPP. The goal is to show how TSPP can be understood as an instantiation of the TSMM core abstractions.

TRQP-TSPP publicly presents itself as a practical, implementer-ready security and privacy profile for TRQP, including OpenAPI contracts, JSON Schemas, a conformance harness, threat modeling, deployment guidance, evidence expectations, and assurance-level-parameterized requirements.

## Center of gravity

Within TSMM terms, TRQP-TSPP is primarily about:

- operator posture
- trust-registry or authoritative-directory query behavior
- profile-bound controls
- evidence-backed conformance and assurance readiness

Its center of gravity is therefore **operator-side trust infrastructure assurance**.

## Crosswalk table

| TSMM concept | TRQP-TSPP instantiation |
|---|---|
| **Entity** | trust registry operator, directory service, relying client, bridge participant |
| **Role** | operator, query provider, verifier, client |
| **Authority** | authority to expose a query interface and publish trust-relevant metadata within governance constraints |
| **Artifact** | OpenAPI contract, metadata declaration, signed response envelope, bridge fixture, conformance report |
| **Claim** | service freshness, context constraints, signed response support, assurance posture, bridge equivalence |
| **Policy** | profile-required fields and headers, freshness semantics, context allowlisting, deployment guidance |
| **Control** | anti-enumeration expectations, rate-limiting evidence, authentication support, signed-envelope requirements, safe bridge behavior |
| **Threat** | enumeration, correlation, spoofed responses, unsafe exposure, bridge inconsistency |
| **Evidence** | evidence bundles, traceability material, JSON conformance results, deployment artifacts, test outputs |
| **Verification** | pytest-based harness validation, schema checks, metadata checks, optional bridge-equivalence testing |
| **Level Framework** | assurance-level-parameterized expectations, with AL semantics sourced externally rather than redefined locally |
| **Trust Decision** | deployment passes or fails profile expectations at a required posture |
| **Effect** | relying systems may consume registry output with confidence appropriate to the validated posture |
| **Lifecycle Event** | registration, metadata update, signed-response enablement, bridge change, reassessment, remediation closure |

## Interpretation notes

### 1. TSPP makes policy concrete
TSPP is not merely descriptive. It turns governance expectations into testable implementation conditions.

Within TSMM, this means TSPP sits strongly across the **Policy**, **Control**, **Verification**, and **Evidence** layers.

### 2. TSPP separates level semantics from level use
The repository states that it does not define Assurance Level semantics locally and instead depends on canonical AL definitions elsewhere.

That is actually a clean TSMM move. It means the repo **uses** a level framework without pretending to own all level meaning.

### 3. TSPP is effect-relevant, not merely metadata-relevant
Although TSPP deals with query interfaces, schemas, and response posture, the real operational consequence is downstream reliance.

Under TSMM, the important effect is:

- whether relying systems should trust the query output
- with what level of confidence
- and under what constrained use posture

### 4. TSPP is an operator-side profile, not a universal trust theory
This crosswalk helps avoid overreach. TSPP is a specialization of TSMM, not TSMM itself.

## Compact model view

```text
Operator Entity -> Role -> Authority to publish/query posture
        |
        v
 Metadata / Response Artifacts -> Claims -> Verification Harness
        |                                |
        v                                v
   Controls + Threat Model          Trust Decision
        |                                |
        +---------- Evidence ------------+
                                         |
                                         v
                             Downstream relying effect
```

## Practical takeaway

Projects that are not implementing TRQP directly can still reuse the TSPP pattern through TSMM by adopting the following generic structure:

- declare machine-readable posture
- bind claims to explicit policy
- define controls against modeled threats
- require evidence for implemented safeguards
- verify conformance with repeatable tooling
- tie validated posture to real downstream effects

That is the portable pattern hiding underneath the repo.
