---
owner: maintainers
last_reviewed: 2026-08-20
applicable_version: 0.24.0
tier: 1
title: Repository and Semantic Authority
---
# Repository and Semantic Authority

TSMM treats repository boundaries as governance boundaries. A repository can depend on another repository's semantics without acquiring authority to redefine them.

## Authority invariants

- TSMM owns canonical TSMM semantics and stable TSMM semantic identifiers.
- Trust Infrastructure Schemas (TIS) owns portable schema identifiers, serialization, and validation contracts.
- The portfolio repository owns portfolio classification and relationship declarations.
- A binding, implementation, test suite, or assurance result does not transfer normative authority unless governance explicitly delegates it.

These invariants allow cross-repository composition without collapsing semantic, serialization, and classification authority into one control surface.
