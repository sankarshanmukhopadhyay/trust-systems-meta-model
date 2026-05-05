---
owner: maintainers
last_reviewed: 2026-05-05
applicable_version: v0.19.0
tier: 1
---

# TSMM Delegation Patterns

## Purpose

This document defines a small catalog of delegation patterns so different trust systems can be compared without treating every delegation flow as bespoke folklore.

## Included patterns

- direct authority
- delegated authority
- federated authority
- conditional authority

## Why it matters

Delegation is where many trust systems become ambiguous. The important question is not only whether a delegation exists. It is whether the delegation has a clear origin, bounded scope, a verification expectation, and a revocation path.

## Machine-readable artifact

- Catalog: `model/delegation-patterns.yaml`
- Schema: `schemas/tsmm-delegation-patterns.schema.json`

## Practical use

The catalog is designed to support comparison work, profile design, and binding review. It is not a protocol. It is a way to make authority transfer legible enough to test.
