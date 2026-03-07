---
owner: maintainers
last_reviewed: 2026-03-07
applicable_version: v0.3.0
tier: 2
---

# Documentation Governance

## Purpose

This document defines how TSMM documentation is structured, reviewed, and kept current.

## Inventory

### Tier 0
- `README.md`
- `docs/index.md`

### Tier 1
- `docs/core-model.md`
- `docs/relationship-model.md`
- `docs/effect-centered-trust-decision-model.md`
- `docs/glossary.md`
- documents under `docs/crosswalks/`

### Tier 2
- `CONTRIBUTING.md`
- `SECURITY.md`
- `docs/documentation-governance.md`

## Ownership

Unless otherwise noted in frontmatter, documentation owner is `maintainers`.

## Freshness rules

Every markdown document should include frontmatter with:

- `owner`
- `last_reviewed`
- `applicable_version`
- `tier`

## Review cadence

- Tier 0: every 30 days or at each release
- Tier 1: every 60 days or when model semantics change
- Tier 2: every 90 days or when process changes

## Release gate checks

Before release:

1. ensure internal links resolve
2. confirm version numbers are current
3. validate examples against the current schema
4. confirm new abstractions appear consistently in glossary, schema, and examples
5. confirm docs site entry points still reflect the actual repo structure
