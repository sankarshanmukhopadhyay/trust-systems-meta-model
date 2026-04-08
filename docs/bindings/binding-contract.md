---
owner: maintainers
last_reviewed: 2026-04-08
applicable_version: v0.16.0
tier: 1
---

# TSMM Binding Contract Model

A TSMM binding is more than a list of loose correspondences. It is a bounded translation surface between TSMM and another ecosystem. The binding contract makes that boundary explicit so implementers can tell what the mapping preserves, where it becomes approximate, and what should not be inferred from the mapping alone.

## Contract fields

Every binding now includes a `bindingContract` object with the following elements:

- `sourceModel`: fixed to `TSMM`
- `targetSystem`: the external ecosystem being aligned
- `bindingVersion`: version of the translation contract
- `guarantees`: what the binding can preserve with confidence
- `limitations`: what remains ecosystem-specific or only partially captured
- `behavioralExpectations`: runtime or process expectations that the mapping assumes
- `constraintSetRef`: path to the accompanying constraint set

## Why the constraint set exists

A binding is useful only if readers know what *not* to conclude from it. Each `constraints.json` file records:

- assumptions that make the mapping meaningful
- prohibited inferences that the binding does not justify
- required artifacts that must travel with the binding
- comparison notes and validation hints for implementers

## Current catalog

The current main-branch catalog includes contract-backed bindings for:

- TRQP
- OpenID Federation
- DCAS
- Verifiable Trust Communities

These bindings are intentionally semantic. They make systems comparable without pretending to replace each ecosystem's protocol rules, processing logic, or governance text.
