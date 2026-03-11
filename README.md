---
owner: maintainers
last_reviewed: 2026-03-11
applicable_version: v0.8.0
tier: 0
---

# Trust Systems Meta Model (TSMM)

[![Release](https://img.shields.io/badge/release-v0.8.0-blue)](releases/v0.8.0.md)
[![License: CC BY-SA 4.0](https://img.shields.io/badge/license-CC--BY--SA%204.0-lightgrey.svg)](LICENSE)
[![Docs](https://img.shields.io/badge/docs-GitHub%20Pages-brightgreen)](index.md)
[![Validate Schemas and Examples](https://github.com/sankarshanmukhopadhyay/trust-systems-meta-model/actions/workflows/validate.yml/badge.svg)](https://github.com/sankarshanmukhopadhyay/trust-systems-meta-model/actions/workflows/validate.yml)
[![Deploy GitHub Pages](https://github.com/sankarshanmukhopadhyay/trust-systems-meta-model/actions/workflows/pages.yml/badge.svg)](https://github.com/sankarshanmukhopadhyay/trust-systems-meta-model/actions/workflows/pages.yml)

**Version:** v0.8.0  
**Status:** Draft reference model  
**License:** CC BY-SA 4.0

## Overview

Most trust systems are described through their visible parts: credentials, registries, wallets, agents, assurance schemes, governance frameworks, and verification flows. TSMM starts one layer deeper. It asks whether the underlying structure of a trust system can be described clearly enough to compare systems, study them, and improve them without beginning from a single protocol or implementation.

Trust Systems Meta Model (TSMM) is a portable abstract reference model for designing, comparing, and implementing trust systems. It provides a shared vocabulary for how trust-relevant systems connect:

- entities and roles
- authority and constraints
- artifacts and claims
- policy, profiles, and requirements
- controls, threats, and governance context
- evidence, assessment, and verification
- trust decisions and downstream effects
- lifecycle events and state changes

TSMM is intentionally **effect-centered**. The key question is not only who an actor is, but whether a bounded authority, under policy and evidence, should be allowed to produce a defined effect. That makes the model useful for examining where trust is asserted, where it is verified, what substantiates it, how policy shapes decisions, and what consequences follow from acceptance, denial, downgrade, warning, or review.

That framing makes TSMM usable across trust registries, verifiable credential ecosystems, delegated-agent systems, trust signal consumers, conformance suites, assurance frameworks, and modular domain extensions. In practice, TSMM is not meant to be a product or a protocol. It is a way to make trust systems more legible so they can be studied with more clarity and built with more rigor.

## Documentation site

This repository is structured to publish cleanly with **GitHub Pages via GitHub Actions**.

- Pages landing page: `index.md`
- Docs home: `docs/index.md`
- Extensions home: `docs/extensions/index.md`
- Workflow: `.github/workflows/pages.yml`
- Validation workflow: `.github/workflows/validate.yml`
- Validator script: `scripts/validate_examples.py`
- Jekyll config: `_config.yml`

## Why this repo exists

Across repositories such as **TRQP-TSPP**, **ERC-8004-CSP**, and **DTG Conformance & Assurance (DCAS)**, a recurring pattern is visible:

- machine-readable trust artifacts
- normative controls and requirements
- explicit threat models
- conformance or assurance levels
- evidence expectations
- profile-governed trust decisions
- operational consequences for acceptance, denial, downgrade, warning, or review

TSMM extracts those recurring invariants into an abstract model so that other projects can apply the theory without waiting for a repo-specific profile, harness, or implementation package.

## Start here

- Pages landing page: `index.md`
- Conceptual entry point: `docs/index.md`
- Core abstractions: `docs/core-model.md`
- Entity catalog: `docs/model/tsmm-entities.md`
- Relationship graph: `docs/model/tsmm-relationships.md`
- Lifecycle model: `docs/model/tsmm-lifecycle.md`
- Evidence artifact model: `docs/model/evidence-artifact.md`
- Dynamic authorization framing: `docs/model/dynamic-authorization-framing.md`
- Agentic AI and dynamic authorization analysis: `docs/model/agentic-authz-analysis.md`
- Runtime legitimacy logic: `docs/evaluation/effect-evaluation-model.md`
- Threat taxonomy: `docs/security/trust-system-threat-model.md`
- Glossary: `docs/glossary.md`
- Conformance profiles:
  - `docs/conformance/tsmm-profile-minimal.md`
  - `docs/conformance/tsmm-profile-operational.md`
  - `docs/conformance/tsmm-profile-assured.md`
  - `docs/conformance/tsmm-conformance-checklist.md`
- Reference patterns:
  - `docs/patterns/trust-registry-pattern.md`
  - `docs/patterns/delegated-agent-pattern.md`
  - `docs/patterns/credential-verification-pattern.md`
  - `docs/patterns/assurance-evidence-pattern.md`
  - `docs/patterns/multi-agent-coordination-pattern.md`
  - `docs/patterns/dynamic-authz-pattern.md` *(experimental)*
- Extensions:
  - `docs/extensions/index.md`
  - `docs/extensions/agentic-ai-extension.md`
  - `docs/extensions/verifiable-trust-communities-extension.md`
  - `docs/extensions/assurance-extension.md`
  - `docs/model/evidence-artifact.md` (Evidence Artifact Extension)
- Crosswalks:
  - `docs/crosswalks/trqp-tspp-crosswalk.md`
  - `docs/crosswalks/erc-8004-csp-crosswalk.md`
  - `docs/crosswalks/dcas-crosswalk.md`
  - `docs/crosswalks/trust-reference-assurance-architecture-crosswalk.md`
  - `docs/crosswalks/openid-federation-crosswalk.md`
  - `docs/crosswalks/xacml-abac-crosswalk.md` *(experimental)*
- Implementer guide: `docs/getting-started-implementer-guide.md`
- Documentation governance and freshness: `docs/documentation-governance.md`

## Design principles

### 1. Minimal but useful
TSMM aims to define the smallest practical abstraction layer that remains operationally meaningful.

### 2. Effect-centered
The core question is not merely *who are you?* but *should this action, artifact, or signal produce an effect right now under bounded authority and policy?*

### 3. Policy-aware
Trust decisions are always evaluated in context. TSMM assumes that evaluation without policy is theater wearing a tie.

### 4. Evidence-backed
Claims, controls, and trust posture must be substantiated. TSMM treats evidence, assessment, and verification as first-class concepts.

### 5. Profile-aware but profile-agnostic
Many real systems implement trust through profiles, requirements, and assessment methods. TSMM models those structures without forcing one domain-specific profile on everyone.

## What changed after v0.8.0

Following the v0.8.0 release, three documents were added or updated to address the emerging consensus that dynamic authorization is *the* governance pattern for agentic AI systems.

The analysis document concludes that dynamic authorization correctly describes the runtime evaluation layer but does not model the governance envelope that makes that layer trustworthy. Four elements present in TSMM's agentic extension are absent from dynamic authorization frameworks: delegation governance, oversight mode, risk-tier-driven profile selection, and trace records as structured Evidence. A system built on dynamic authorization alone has access control, not governance.

It adds and updates:

- `docs/model/agentic-authz-analysis.md` *(new)* — structural analysis of the relationship between dynamic authorization and TSMM's agentic governance model; introduces the governance envelope framing and implementer guidance for building the envelope before the PDP layer
- `docs/model/dynamic-authorization-framing.md` *(updated)* — adds an agentic context note to section 6 and extends implementer guidance in section 7 with a dedicated paragraph for agentic system builders
- `docs/conformance/tsmm-conformance-checklist.md` *(updated)* — adds a cross-reference to the analysis document in the Dynamic Authorization checklist preamble and adds DA-8, a new agentic-systems-only item requiring the governance envelope to be defined before the PDP layer is built

## What changed in v0.8.0

v0.8.0 introduces TSMM's treatment of dynamic authorization as a crosswalk and pattern release rather than a schema extension release. The decision to hold dynamic authorization at this scope — rather than introducing new core primitives — is deliberate and documented. No core abstractions were changed. No schemas were added or modified.

It adds:

- a framing document (`docs/model/dynamic-authorization-framing.md`) establishing TSMM's position: dynamic authorization is a runtime evaluation pattern that operates within the TSMM governance chain, not a replacement framing for it
- a crosswalk (`docs/crosswalks/xacml-abac-crosswalk.md`) mapping XACML 3.0, ABAC, and NGAC concepts to TSMM abstractions, covering the PAP/PDP/PEP/PIP architecture, request/response flow, and obligations as TSMM conditions
- a pattern document (`docs/patterns/dynamic-authz-pattern.md`) defining the TSMM-aligned sequence for a runtime authorization flow, the structural rules that must hold, and an example in a verifiable credential context
- a formal definition of the `status: experimental` frontmatter field in `docs/documentation-governance.md` — a governance signal that a concept is mapped carefully and core promotion is deliberately deferred, not a quality or stability signal

The crosswalk and pattern carry `status: experimental`. The framing document is stable.

## What changed in v0.7.0

v0.7.0 adds the Evidence Artifact model, formalizing how trust systems produce, structure, and consume operational evidence. It closes the conceptual gap between rule definition and behavioral proof — the third layer of trust systems that most governance frameworks leave implicit.

It adds:

- a conceptual document (`docs/model/evidence-artifact.md`) defining the EvidenceArtifact concept as a typed specialization of the core Evidence abstraction, with four types (reconciliation, drift, attestation, conformance), a property specification, lifecycle expectations, and profile mapping
- an extension schema (`schemas/tsmm-evidence-artifact-extension.schema.json`) with required fields and optional traceability fields including integrity anchors, verification method, policy reference, and action reference for agentic contexts
- a worked example instance demonstrating all four artifact types in a trust registry context

## What changed in v0.6.0

v0.6.0 adds implementer-readiness tooling and closes the gap between the conceptual model and practical adoption.

It adds:

- a conformance self-assessment checklist for Minimal, Operational, and Assured profiles, with extension checklists for Agentic AI, VTC, and Assurance
- an opinionated getting-started implementer guide with three entry points: trust registry operator, verifiable credential issuer/verifier, and agentic system builder
- a multi-agent coordination pattern covering chained delegation, sub-delegation governance, and oversight mode escalation
- a multi-agent coordination extension schema and worked example
- an OpenID Federation crosswalk
- a schema coverage validation script

## Repo contents

```text
trust-systems-meta-model/
├── .github/
│   └── workflows/
│       ├── pages.yml
│       └── validate.yml
├── README.md
├── LICENSE
├── SECURITY.md
├── CONTRIBUTING.md
├── VERSION
├── index.md
├── _config.yml
├── docs/
│   ├── index.md
│   ├── core-model.md
│   ├── relationship-model.md
│   ├── effect-centered-trust-decision-model.md
│   ├── glossary.md
│   ├── documentation-governance.md
│   ├── freshness-audit.md
│   ├── getting-started-implementer-guide.md
│   ├── model/
│   │   ├── tsmm-entities.md
│   │   ├── tsmm-relationships.md
│   │   ├── tsmm-lifecycle.md
│   │   ├── evidence-artifact.md
│   │   ├── dynamic-authorization-framing.md
│   │   └── agentic-authz-analysis.md
│   ├── extensions/
│   │   ├── index.md
│   │   ├── agentic-ai-extension.md
│   │   ├── verifiable-trust-communities-extension.md
│   │   └── assurance-extension.md
│   ├── conformance/
│   │   ├── tsmm-profile-minimal.md
│   │   ├── tsmm-profile-operational.md
│   │   ├── tsmm-profile-assured.md
│   │   └── tsmm-conformance-checklist.md
│   ├── evaluation/
│   │   └── effect-evaluation-model.md
│   ├── security/
│   │   └── trust-system-threat-model.md
│   ├── patterns/
│   │   ├── trust-registry-pattern.md
│   │   ├── delegated-agent-pattern.md
│   │   ├── credential-verification-pattern.md
│   │   ├── assurance-evidence-pattern.md
│   │   ├── multi-agent-coordination-pattern.md
│   │   └── dynamic-authz-pattern.md          ← experimental
│   └── crosswalks/
│       ├── trqp-tspp-crosswalk.md
│       ├── erc-8004-csp-crosswalk.md
│       ├── dcas-crosswalk.md
│       ├── trust-reference-assurance-architecture-crosswalk.md
│       ├── openid-federation-crosswalk.md
│       └── xacml-abac-crosswalk.md           ← experimental
├── schemas/
│   ├── tsmm-core.schema.json
│   ├── tsmm-agentic-extension.schema.json
│   ├── tsmm-vtc-extension.schema.json
│   ├── tsmm-assurance-extension.schema.json
│   ├── tsmm-multi-agent-extension.schema.json
│   └── tsmm-evidence-artifact-extension.schema.json
├── examples/
│   ├── minimal-trust-registry-instance.json
│   ├── consumer-policy-instance.json
│   ├── delegated-agent-instance.json
│   ├── agentic-ai-extension-instance.json
│   ├── verifiable-trust-community-instance.json
│   ├── assurance-extension-instance.json
│   ├── multi-agent-coordination-instance.json
│   └── evidence-artifact-instance.json
├── scripts/
│   ├── validate_examples.py
│   ├── check_docs.py
│   └── check_schema_coverage.py
└── releases/
    ├── v0.3.0.md
    ├── v0.4.0.md
    ├── v0.5.0.md
    ├── v0.6.0.md
    ├── v0.7.0.md
    └── v0.8.0.md
```

## What TSMM is not

TSMM does **not**:

- define the full semantics of every assurance model
- prescribe one universal trust policy
- collapse assurance, conformance, reputation, and authorization into one blob
- require one serialization format
- claim that every trust decision is binary
- replace domain-specific standards or implementation profiles

In plain terms: this repo is a bridge, not a cathedral.

## License

This repository is published under **Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)**.
