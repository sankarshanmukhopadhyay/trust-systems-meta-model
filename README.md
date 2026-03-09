---
owner: maintainers
last_reviewed: 2026-03-09
applicable_version: v0.6.0
tier: 0
---

# Trust Systems Meta Model (TSMM)

[![Release](https://img.shields.io/badge/release-v0.6.0-blue)](releases/v0.6.0.md)
[![License: CC BY-SA 4.0](https://img.shields.io/badge/license-CC--BY--SA%204.0-lightgrey.svg)](LICENSE)
[![Docs](https://img.shields.io/badge/docs-GitHub%20Pages-brightgreen)](index.md)
[![Validate Schemas and Examples](https://github.com/sankarshanmukhopadhyay/trust-systems-meta-model/actions/workflows/validate.yml/badge.svg)](https://github.com/sankarshanmukhopadhyay/trust-systems-meta-model/actions/workflows/validate.yml)
[![Deploy GitHub Pages](https://github.com/sankarshanmukhopadhyay/trust-systems-meta-model/actions/workflows/pages.yml/badge.svg)](https://github.com/sankarshanmukhopadhyay/trust-systems-meta-model/actions/workflows/pages.yml)

**Version:** v0.6.0  
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
- Extensions:
  - `docs/extensions/index.md`
  - `docs/extensions/agentic-ai-extension.md`
  - `docs/extensions/verifiable-trust-communities-extension.md`
  - `docs/extensions/assurance-extension.md`
- Crosswalks:
  - `docs/crosswalks/trqp-tspp-crosswalk.md`
  - `docs/crosswalks/erc-8004-csp-crosswalk.md`
  - `docs/crosswalks/dcas-crosswalk.md`
  - `docs/crosswalks/trust-reference-assurance-architecture-crosswalk.md`
  - `docs/crosswalks/openid-federation-crosswalk.md`
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

## What changed in v0.6.0

v0.6.0 adds implementer-readiness tooling and closes the gap between the conceptual model and practical adoption.

It adds:

- a conformance self-assessment checklist for Minimal, Operational, and Assured profiles, with extension checklists for Agentic AI, VTC, and Assurance
- an opinionated getting-started implementer guide with three entry points: trust registry operator, verifiable credential issuer/verifier, and agentic system builder
- a multi-agent coordination pattern covering chained delegation, sub-delegation governance, and oversight mode escalation
- a multi-agent coordination extension schema with support for delegation chains, per-agent actions, effective oversight mode tracking, and coordination-level trace records
- a worked multi-agent coordination example instance
- an OpenID Federation crosswalk mapping federation concepts to TSMM abstractions
- a schema coverage validation script that checks whether example instances exercise all properties defined in their paired schemas

v0.5.0 extends TSMM with modular application-layer support while keeping the core model stable.

It adds:

- a formal entity catalog with mandatory fields and modeling guidance
- a normative relationship specification with cardinality and dependency rules
- a lifecycle model covering issuance, delegation, suspension, revocation, expiry, remediation, and archival
- TSMM conformance profiles for Minimal, Operational, and Assured implementations
- a formal effect evaluation model for execution-time trust decisions
- a reusable threat and failure taxonomy for trust systems
- reference architecture patterns for trust registries, delegated agents, credential verification, and assurance evidence
- GitHub Pages deployment through GitHub Actions
- extension architecture for Agentic AI, Verifiable Trust Communities, and assurance-oriented trust workflows
- extension schemas and worked examples
- refreshed navigation for docs and release packaging

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
│   │   └── tsmm-lifecycle.md
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
│   │   └── multi-agent-coordination-pattern.md
│   └── crosswalks/
│       ├── trqp-tspp-crosswalk.md
│       ├── erc-8004-csp-crosswalk.md
│       ├── dcas-crosswalk.md
│       ├── trust-reference-assurance-architecture-crosswalk.md
│       └── openid-federation-crosswalk.md
├── schemas/
│   ├── tsmm-core.schema.json
│   ├── tsmm-agentic-extension.schema.json
│   ├── tsmm-vtc-extension.schema.json
│   ├── tsmm-assurance-extension.schema.json
│   └── tsmm-multi-agent-extension.schema.json
├── examples/
│   ├── minimal-trust-registry-instance.json
│   ├── consumer-policy-instance.json
│   ├── delegated-agent-instance.json
│   ├── agentic-ai-extension-instance.json
│   ├── verifiable-trust-community-instance.json
│   ├── assurance-extension-instance.json
│   └── multi-agent-coordination-instance.json
├── scripts/
│   ├── validate_examples.py
│   ├── check_docs.py
│   └── check_schema_coverage.py
└── releases/
    ├── v0.3.0.md
    ├── v0.4.0.md
    ├── v0.5.0.md
    └── v0.6.0.md
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
