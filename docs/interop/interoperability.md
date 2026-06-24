---
owner: maintainers
last_reviewed: 2026-05-05
applicable_version: v0.21.0
tier: 1
---

# TSMM Interoperability Layer

## Purpose

TSMM now treats interoperability as something that can be described explicitly at three levels:

- structural
- semantic
- behavioral

## Why this matters

Two systems can share a similar vocabulary and still fail to interoperate. One may align structurally while diverging behaviorally. Another may preserve semantics while requiring translation at the artifact layer. By separating these modes, TSMM can compare ecosystems without pretending all forms of compatibility are equal.

## Machine-readable artifact

- Matrix: `interop/interoperability-matrix.yaml`
- Schema: `schemas/tsmm-interoperability.schema.json`

## Included comparisons

- TSMM and TRQP
- TSMM and OpenID Federation
- TSMM and KERI

## Practical use

This layer is meant to support binding review, portability planning, and architecture decisions about where translation is shallow and where it is expensive.
