---
owner: maintainers
last_reviewed: 2026-05-05
applicable_version: v0.19.0
tier: 0
---

# TSMM Binding: HAVID

This **experimental** binding explains how **High Assurance Verifiable Identifiers (HAVID)** can be interpreted through TSMM.

HAVID is not a full trust meta model. It is a compositional identifier architecture. It links multiple identifier classes through cross-endorsement so a verifier can discover, validate, and combine distinct assurance contributions without pretending that all identifiers mean the same thing.

That makes HAVID relevant to TSMM in a specific way. TSMM can model the identifier classes, the composed assurance signal, the lifecycle coordination duties, and the verifier-visible effect of revocation or expiry. TSMM should not treat HAVID as a substitute for delegation, runtime authorization, or ecosystem governance semantics.

## Primary mappings

- **HAVID composite identifier** → composite `Credential`
- **Identifier class taxonomy** → `Subject`-bound identifier surfaces interpreted through profile and policy
- **Cross-endorsement** → `VerificationProcess`
- **Assurance composition** → `AssuranceProfile`
- **Validation state** → `Assessment`
- **Lifecycle coordination** → `Policy`
- **Revocation / deactivation / expiry impact** → trust-relevant `Effect`

## The four integration surfaces that matter most

### 1. Identifier class

HAVID is strongest when different identifier classes remain analytically distinct. A DID, a DNS domain, an X.509 certificate, and an organizational identifier do not contribute the same kind of assurance. TSMM therefore treats HAVID as a composition surface rather than as a flattening surface.

### 2. Assurance level

HAVID does not create a universal assurance level that overrides native trust frameworks. It creates a verifier-side composition problem. TSMM models that as an `AssuranceProfile` informed by the identifier classes present, their integrity properties, and the verifier's policy context.

### 3. Lifecycle semantics

HAVID is lifecycle-sensitive by design. Renewal, update, synchronized rekeying, and cross-endorsement maintenance change whether the composite remains trustworthy. TSMM captures those duties as policy and lifecycle expectations rather than leaving them as operational footnotes.

### 4. Revocation model

The most important runtime property is that revocation, expiry, deactivation, or integrity failure on one linked identifier degrades or invalidates reliance on the composite HAVID. TSMM models that consequence as an `Effect` so verifier behavior remains explicit.

## Why the mapping is not 1:1

Three guardrails matter.

**Composite identity is not delegated authority.** A validated HAVID can improve confidence in who is being referenced. It does not prove what the subject may do.

**Cross-endorsement is not assurance transfer.** Identifier classes keep their native assurance properties. Cross-endorsement helps compose them. It does not merge them.

**Validation is not governance completeness.** HAVID gives a stronger identifier surface. It does not by itself define dispute handling, relying-party policy, or ecosystem accountability structures.

## How to use this binding

Use this binding when you need to compare HAVID with other trust systems, or when you need to normalize HAVID into graph-comparable trust artifacts without inflating what identifier composition proves.

Typical downstream uses include:

- modeling composite identifier assurance as a TSMM-comparable trust artifact
- making lifecycle coordination duties visible in profile and control design
- separating revocation impact from static identity claims
- preserving verifier-state reasoning without turning HAVID into a complete authorization system

## Related artifacts

- Machine-readable binding: `bindings/havid/tsmm-havid-binding.json`
- Constraint set: `bindings/havid/constraints.json`
- Crosswalk: `docs/crosswalks/havid-crosswalk.md`
