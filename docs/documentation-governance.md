---
owner: maintainers
last_reviewed: 2026-05-05
applicable_version: v0.19.0
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

## Repo-wide maturity taxonomy

TSMM uses a shared maturity taxonomy for bindings, crosswalks, and other comparison surfaces. See [TSMM maturity model](maturity-model.md).

- `experimental` → modeled for analysis, comparison, and early testing
- `candidate` → structurally coherent and ready for broader ecosystem review
- `supported` → stable enough for normal TSMM comparison use
- `deprecated` → retained for reference, not recommended for new work

This taxonomy separates **modeled** from **recommended**. Inclusion in TSMM means a system is structurally analyzable within the meta-model. It does not by itself imply production readiness, normative endorsement, or cross-ecosystem maturity.

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

## v0.13.0 note

The v0.13.0 release adds the Agent Interaction Extension. Seven new model documents are Tier 1 artifacts: `service-descriptor.md`, `skill-contract.md`, `interaction-context.md`, `authorization-checkpoint.md`, `extension-contract.md`, `opacity-boundary.md`, and `peer-trust-relation.md`. These should be kept aligned with the extension schema (`tsmm-agent-interaction-extension.schema.json`), the worked example (`agent-interaction-extension-instance.json`), the glossary (seven new terms), and the conformance checklist (Agent Interaction Extension tier). The A2A binding planned for v0.14.0 must align with all seven model documents and the schema; any changes to this extension before the binding is published must be reflected in the binding draft.

## v0.14.0 note

The v0.14.0 release completes the Agent Interaction Extension and adds the A2A binding. Three additional Tier 1 model documents are added: `interaction-task.md`, `content-provenance-policy.md`, `observability-mode.md`. The A2A binding JSON and binding/crosswalk prose documents are Tier 0 artifacts (released at each version). The A2A binding carries an implicit currency note — it reflects the A2A protocol as of March 2026 and should be reviewed if the A2A specification changes. The complete Agent Interaction Extension now comprises ten abstractions across two schema releases; any future changes to the extension schema must propagate to all ten model documents, both worked examples, the glossary, the conformance checklist (AI-1 through AI-21), and the A2A binding.

## v0.19.0 documentation governance obligations

The v0.19.0 release adds candidate governance surfaces for discovery, capability negotiation, and task evidence lifecycle. Documentation updates for these surfaces MUST include: schema link, example link, valid/invalid test-vector links, maturity status, and validation command coverage.

A documentation change that references A2A-class concepts SHOULD distinguish protocol mechanics from generalized TSMM semantics. TSMM documentation MUST NOT imply that use of A2A or any other protocol automatically creates authority, assurance, or runtime legitimacy.
