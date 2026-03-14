---
owner: maintainers
last_reviewed: 2026-03-14
applicable_version: v0.9.0
tier: 1
status: experimental
status_note: >
  This document maps an adjacent runtime evaluation concept onto TSMM abstractions.
  It does not introduce new core primitives. Dynamic authorization concepts are
  deliberately held at extension scope pending implementation experience. See
  docs/model/dynamic-authorization-framing.md before reading this document.
---

# TSMM Crosswalk: XACML 3.0 and ABAC

## Purpose

This document maps **XACML 3.0** and **Attribute-Based Access Control (ABAC)** concepts to the Trust Systems Meta Model (TSMM).

XACML 3.0 (eXtensible Access Control Markup Language) is the OASIS standard for policy-based access control. It defines the PAP/PDP/PEP/PIP architecture, a policy language, and a request/response protocol that is widely implemented in enterprise, government, and cloud authorization systems.

ABAC is the access control paradigm in which authorization decisions are made by evaluating attributes of the subject, action, resource, and environment against a policy. XACML is ABAC's most fully specified expression. NGAC (Next Generation Access Control), defined in NIST SP 800-178, is an alternative formal model with stronger composition properties.

## Center of gravity

Within TSMM terms, XACML and ABAC are primarily about:

- separating policy administration, decision, and enforcement into distinct architectural components
- evaluating fine-grained, context-sensitive authorization requests at runtime
- producing structured decisions with obligations and advice attached
- externalizing policy from application logic to enable independent governance and auditability

Their center of gravity is **runtime request evaluation under externalized, attribute-sensitive policy**.

Read `docs/model/dynamic-authorization-framing.md` for TSMM's position on how this center of gravity relates to TSMM's effect-centered framing before using this crosswalk.

## Crosswalk table

| TSMM concept | XACML / ABAC instantiation |
|---|---|
| **Governance Context** | The organizational, regulatory, or ecosystem context within which policies are authored and administered; the PAP's operating environment |
| **Profile** | A named policy set grouping related policies for a domain, application, or assurance level |
| **Requirement** | A policy rule or condition that must be satisfied for a permit decision to be produced |
| **Entity** | Subject: the principal making the authorization request, identified by subject attributes |
| **Role** | Subject attribute expressing role or group membership; evaluated by the PDP as an attribute value |
| **Authority** | The grant that makes a subject's attributes sufficient to satisfy a policy rule; expressed as policy conditions rather than as a separate object in XACML |
| **Artifact** | Resource: the target object, dataset, endpoint, or action being requested, identified by resource attributes |
| **Claim** | An attribute asserted about a subject, resource, or environment; claims are the atomic inputs to PDP evaluation |
| **Policy** | XACML Policy or PolicySet; the evaluation function the PDP applies to a request |
| **Control** | An obligation or advice attached to a permit decision; a policy condition that constrains what the PEP must do after enforcement |
| **Threat** | An attack or misuse pattern that the policy is designed to prevent; modeled in ABAC threat analysis and NGAC composition proofs |
| **Evidence** | Attribute values retrieved by the PIP; audit logs produced by the PEP; decision records retained for compliance |
| **Assessment** | Policy analysis: verification that a policy set is consistent, complete, and produces correct decisions for representative requests |
| **Verification** | PDP evaluation: the computation that takes a request and produces a permit/deny/indeterminate/notApplicable decision |
| **Level Framework** | Assurance levels expressed as attribute constraints in policy rules; e.g., require `assuranceLevel >= AL2` |
| **Trust Decision** | The PDP decision: permit, deny, indeterminate, or notApplicable |
| **Effect** | The permitted or denied operation; obligations that the PEP must fulfill; advice the PEP may act on |
| **Lifecycle Event** | Attribute change events: credential expiry, role revocation, policy update, environment state change |

## PAP / PDP / PEP / PIP mapped to TSMM

```text
PAP (Policy Administration Point)
  → Where TSMM Policy, Profile, and Requirement objects are defined,
    versioned, and governed.
  → Corresponds to the governance layer: Governance Context shapes what
    policies are permissible.

PDP (Policy Decision Point)
  → The evaluation step within TSMM Trust Decision production.
  → Receives a request (subject + action + resource + environment),
    retrieves attribute data via PIP, evaluates Policy, and returns
    a structured decision.

PEP (Policy Enforcement Point)
  → The system component that acts on a Trust Decision to permit or
    block an Effect.
  → Also responsible for fulfilling obligations attached to the decision.

PIP (Policy Information Point)
  → The retrieval of Evidence, Artifact state, and Lifecycle Event data
    to inform PDP evaluation.
  → Corresponds to the evidence and verification layer in TSMM.
```

## Request and response as TSMM flows

An XACML authorization request is a structured input to PDP evaluation containing:

- `Subject` attributes — maps to TSMM `Entity` + `Role` + `Authority` scope
- `Action` attributes — maps to the requested operation that would produce a TSMM `Effect`
- `Resource` attributes — maps to TSMM `Artifact` or the target of an agentic `Action`
- `Environment` attributes — maps to TSMM `Execution Context` (agentic extension) and lifecycle state

An XACML authorization response contains:

- `Decision` (Permit / Deny / Indeterminate / NotApplicable) — maps to TSMM `Trust Decision` outcome
- `Obligations` — conditions the PEP must fulfill; maps to obligations in TSMM `Authority` or conditions on `Effect`
- `Advice` — information the PEP may use; maps to non-mandatory guidance in the effect or decision context

## Obligations as TSMM conditions

XACML obligations are conditions attached to a decision that the PEP is required to fulfill. If the PEP cannot fulfill an obligation, it must treat the decision as deny.

Within TSMM, obligations map onto:

- conditions in `Authority` objects (the acting role must satisfy these conditions for the authority to be valid)
- action requirements attached to `Effect` objects (the system must do this in addition to permitting the effect)
- requirements in a `Profile` that apply at enforcement time rather than at assessment time

Obligations are not decorative. A permit decision with an unfulfilled obligation is a governance failure, not a partial success.

## NGAC note

NIST SP 800-178's Next Generation Access Control model introduces formal composition properties that XACML's policy combination algorithms do not guarantee. NGAC reasons about policy correctness through graph-based access relationships rather than rule evaluation order. Within TSMM terms, NGAC's policy graph maps to a formal expression of the `Authority → Effect` relationship set, with provable properties about what subjects can and cannot reach under a given policy configuration.

NGAC is not widely implemented but is worth noting for implementations in regulated contexts where policy correctness proofs are required.

## Practical takeaway

Implementations that use OPA, Cedar, XACML, or similar policy engines alongside TSMM should:

- Keep the PAP's governance context (TSMM `Policy`, `Profile`, `Governance Context`) separate from the PDP's evaluation runtime
- Not reduce TSMM `Effect` to a permit flag — preserve class, action, and status distinctions alongside any XACML decision
- Treat PIP attribute retrieval as a TSMM evidence and lifecycle state lookup, not as raw data fetching outside the governance model
- Map obligations to existing TSMM Authority conditions or Effect action requirements rather than treating them as out-of-band enforcement logic
- Read `docs/patterns/dynamic-authz-pattern.md` for the sequence that puts these mappings into practice
