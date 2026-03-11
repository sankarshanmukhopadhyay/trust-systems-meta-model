---
owner: maintainers
last_reviewed: 2026-03-11
applicable_version: v0.8.0
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
- `docs/getting-started-implementer-guide.md`
- documents under `docs/crosswalks/`
- documents under `docs/conformance/`
- documents under `docs/patterns/`

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

## Status field

Documents that map adjacent concepts onto TSMM without introducing new core primitives, or whose promotion to core is deliberately deferred, should carry:

- `status: experimental`
- `status_note`: a brief explanation of what experimental means for that document and a reference to the relevant framing document

The `experimental` status is a governance signal, not a quality signal. It means: the intellectual mapping has been done carefully, the framing rationale is documented, and promotion to core is deferred pending implementation experience. Experimental documents are production-quality and suitable for implementer use.

A document carrying `status: experimental` should always reference its framing document in `status_note`. Documents without a `status` field are considered stable.
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


## v0.5.0 note

The v0.5.0 release expands the documentation surface. New model, conformance, evaluation, security, and pattern documents should remain aligned with the core model, schema, examples, and release notes.

## v0.7.0 note

The v0.7.0 release added the evidence artifact model. The new conceptual document, extension schema, and example instance are Tier 1 artifacts and should be kept aligned with any future changes to the core Evidence abstraction, the assurance extension, and the Assured profile requirements.

## v0.8.0 note

The v0.8.0 release introduces the dynamic authorization framing document, crosswalk, and pattern. The framing document (`docs/model/dynamic-authorization-framing.md`) is a stable Tier 1 position statement and should be updated if the model's position on dynamic authorization changes. The crosswalk and pattern carry `status: experimental` and should be reviewed whenever the core Policy, Trust Decision, or Effect abstractions are modified, or when implementation experience warrants promotion consideration.
