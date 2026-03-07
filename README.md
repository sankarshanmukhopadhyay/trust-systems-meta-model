---
owner: maintainers
last_reviewed: 2026-03-07
applicable_version: v0.3.0
tier: 0
---

# Trust Systems Meta Model (TSMM)

**Version:** v0.3.0  
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

This repository is structured to publish cleanly with **GitHub Pages**.

- Docs home: `docs/index.md`
- Recommended Pages source: **Deploy from a branch** → `/docs` folder
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

- Conceptual entry point: `docs/index.md`
- Core abstractions: `docs/core-model.md`
- Relationship graph: `docs/relationship-model.md`
- Runtime legitimacy logic: `docs/effect-centered-trust-decision-model.md`
- Glossary: `docs/glossary.md`
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

## Scope status

### First release scope audit

The original first-release scope included:

1. core concepts
2. relationship model
3. effect-centered trust decision model
4. two crosswalks
5. one simple JSON schema
6. two worked examples

**Status:** complete since v0.2.0.

## What changed in v0.3.0

v0.3.0 hardens the repo after cross-checking it against TRQP-TSPP, ERC-8004-CSP, DCAS, and the repository freshness checklist.

It adds:

- GitHub Pages readiness
- explicit documentation governance and freshness metadata
- a terminology glossary
- a DCAS crosswalk
- refinement of the core model to include **governance context**, **profile**, **requirement**, and **assessment**
- an expanded machine-readable schema and refreshed examples
- security reporting guidance

## Repo contents

```text
trust-systems-meta-model/
├── README.md
├── LICENSE
├── SECURITY.md
├── CONTRIBUTING.md
├── _config.yml
├── docs/
│   ├── index.md
│   ├── core-model.md
│   ├── relationship-model.md
│   ├── effect-centered-trust-decision-model.md
│   ├── glossary.md
│   ├── documentation-governance.md
│   └── crosswalks/
│       ├── trqp-tspp-crosswalk.md
│       ├── erc-8004-csp-crosswalk.md
│       └── dcas-crosswalk.md
├── schemas/
│   └── tsmm-core.schema.json
└── examples/
    ├── minimal-trust-registry-instance.json
    ├── consumer-policy-instance.json
    └── delegated-agent-instance.json
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
