---
owner: maintainers
last_reviewed: 2026-05-05
applicable_version: v0.19.0
tier: 1
---

# TSMM Canonical Meta-Model Schema

## 1. Purpose

This document defines the machine-readable canonical schema for the TSMM primitive catalog.

TSMM already had concrete instance schemas such as `schemas/tsmm-core.schema.json` and the extension schemas. Those are useful for validating worked examples. They do not, by themselves, formalize the meta-model as a portable object that other systems can parse, compare, and bind against. The canonical primitive catalog closes that gap.

The new canonical schema lives at `schemas/tsmm.schema.json`.

## 2. What this schema does

The canonical schema expresses TSMM itself as a structured object. It defines the first-class primitives that any implementation, binding, or extension can map against:

- Actor
- Authority
- Credential
- Policy
- TrustRelationship
- Delegation
- VerificationProcess

Each primitive definition is machine-addressable. It has:

- a stable `identifier`
- a canonical `kind`
- a description
- a list of `requiredFields`
- typed `fieldDefinitions`
- a `tsmmCoreMapping` that shows how the primitive maps into the current instance schema

That separation matters. The primitive catalog is the meta-model layer. `schemas/tsmm-core.schema.json` remains the concrete instance layer.

## 3. Canonical required fields

The canonical primitive catalog introduces four field names that make the primitive layer computable across implementations:

| Canonical field | Meaning |
|---|---|
| `identifier` | Stable machine-readable handle for the primitive |
| `authority_source` | Origin of authority, mandate, or delegation |
| `validation_method` | Method used to check whether the primitive can be relied on |
| `revocation_mechanism` | How validity can be suspended, revoked, or expired |

Not every primitive uses all four. The schema requires them where they are structurally necessary.

- `Authority` must define `authority_source`
- `Credential` must define `revocation_mechanism`
- `Delegation` must define `authority_source` and `revocation_mechanism`
- `VerificationProcess` must define `validation_method`

## 4. Why this matters

This change makes TSMM resemble a meta-model more robustly for three reasons.

First, the abstractions are now explicit enough to be validated independently of any one example trust system.

Second, the primitive catalog can now act as a contract surface for future binding work. A binding can say not only which TSMM concept it targets, but which required fields it can or cannot satisfy.

Third, the repo now distinguishes between **the model of the model** and **instances of the model**. That is a healthier architecture than asking one instance schema to do both jobs at once.

## 5. Companion artifacts

- Canonical schema: `schemas/tsmm.schema.json`
- Worked example: `examples/tsmm-meta-model-instance.json`
- Instance-layer schema: `schemas/tsmm-core.schema.json`
- Validation script: `scripts/validate_examples.py`
- Schema coverage script: `scripts/check_schema_coverage.py`

## 6. Design note

The canonical schema does not replace the existing TSMM instance schemas. It sits above them.

That is intentional. A meta-model should define the primitive contract first. Concrete instance schemas, bindings, and extensions can then refine those primitives for operational use without collapsing the abstraction layer into a single implementation shape.
