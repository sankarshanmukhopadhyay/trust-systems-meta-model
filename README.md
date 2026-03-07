---
owner: maintainers
last_reviewed: 2026-03-07
applicable_version: v0.4.0
tier: 0
---

# Trust Systems Meta Model (TSMM)

**Version:** v0.4.0  
**Status:** Draft reference model  
**License:** CC BY-SA 4.0

## Overview

Trust Systems Meta Model (TSMM) is a portable abstract reference model for designing, comparing, and implementing trust systems.

It provides a shared vocabulary for how trust-relevant systems connect:

- entities and roles
- authority and constraints
- artifacts and claims
- policy, profiles, and requirements
- controls, threats, and governance context
- evidence, assessment, and verification
- trust decisions and downstream effects
- lifecycle events and state changes

TSMM is intentionally **effect-centered**. It does not treat identity as the final unit of governance. Instead, it treats trust systems as mechanisms for deciding whether a bounded authority, under policy and evidence, should be allowed to produce a defined effect.

That framing makes TSMM usable across trust registries, verifiable credential ecosystems, delegated-agent systems, trust signal consumers, conformance suites, and assurance frameworks.

## Documentation site

This repository is structured to publish cleanly with **GitHub Pages via GitHub Actions**.

- Pages landing page: `index.md`
- Docs home: `docs/index.md`
- Workflow: `.github/workflows/pages.yml`
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
- Reference patterns:
  - `docs/patterns/trust-registry-pattern.md`
  - `docs/patterns/delegated-agent-pattern.md`
  - `docs/patterns/credential-verification-pattern.md`
  - `docs/patterns/assurance-evidence-pattern.md`
- Crosswalks:
  - `docs/crosswalks/trqp-tspp-crosswalk.md`
  - `docs/crosswalks/erc-8004-csp-crosswalk.md`
  - `docs/crosswalks/dcas-crosswalk.md`
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

## What changed in v0.4.0

v0.4.0 turns TSMM from a conceptual bundle into a more operational architecture toolkit.

It adds:

- a formal entity catalog with mandatory fields and modeling guidance
- a normative relationship specification with cardinality and dependency rules
- a lifecycle model covering issuance, delegation, suspension, revocation, expiry, remediation, and archival
- TSMM conformance profiles for Minimal, Operational, and Assured implementations
- a formal effect evaluation model for execution-time trust decisions
- a reusable threat and failure taxonomy for trust systems
- reference architecture patterns for trust registries, delegated agents, credential verification, and assurance evidence
- GitHub Pages deployment through GitHub Actions
- refreshed navigation for docs and release packaging

## Repo contents

```text
trust-systems-meta-model/
├── .github/
│   └── workflows/
│       └── pages.yml
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
│   ├── model/
│   │   ├── tsmm-entities.md
│   │   ├── tsmm-relationships.md
│   │   └── tsmm-lifecycle.md
│   ├── conformance/
│   │   ├── tsmm-profile-minimal.md
│   │   ├── tsmm-profile-operational.md
│   │   └── tsmm-profile-assured.md
│   ├── evaluation/
│   │   └── effect-evaluation-model.md
│   ├── security/
│   │   └── trust-system-threat-model.md
│   ├── patterns/
│   │   ├── trust-registry-pattern.md
│   │   ├── delegated-agent-pattern.md
│   │   ├── credential-verification-pattern.md
│   │   └── assurance-evidence-pattern.md
│   └── crosswalks/
│       ├── trqp-tspp-crosswalk.md
│       ├── erc-8004-csp-crosswalk.md
│       └── dcas-crosswalk.md
├── schemas/
│   └── tsmm-core.schema.json
├── examples/
│   ├── minimal-trust-registry-instance.json
│   ├── consumer-policy-instance.json
│   └── delegated-agent-instance.json
└── releases/
    ├── v0.3.0.md
    └── v0.4.0.md
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
