---
owner: maintainers
last_reviewed: 2026-03-23
applicable_version: v0.13.0
tier: 0
---

# Trust Systems Meta Model (TSMM)

[![Release](https://img.shields.io/badge/release-v0.13.0-blue)](releases/v0.13.0.md)
[![License: CC BY-SA 4.0](https://img.shields.io/badge/license-CC--BY--SA%204.0-lightgrey.svg)](LICENSE)
[![Docs](https://img.shields.io/badge/docs-GitHub%20Pages-brightgreen)](index.md)
[![Validate Schemas and Examples](https://github.com/sankarshanmukhopadhyay/trust-systems-meta-model/actions/workflows/validate.yml/badge.svg)](https://github.com/sankarshanmukhopadhyay/trust-systems-meta-model/actions/workflows/validate.yml)
[![Deploy GitHub Pages](https://github.com/sankarshanmukhopadhyay/trust-systems-meta-model/actions/workflows/pages.yml/badge.svg)](https://github.com/sankarshanmukhopadhyay/trust-systems-meta-model/actions/workflows/pages.yml)

**Version:** v0.13.0  
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

Across repositories such as **trust-infrastructure-schemas**, **TRQP-TSPP**, **ERC-8004-CSP**, and **DTG Conformance & Assurance (DCAS)**, a recurring pattern is visible:

- machine-readable trust artifacts
- normative controls and requirements
- explicit threat models
- conformance or assurance levels
- evidence expectations
- profile-governed trust decisions
- operational consequences for acceptance, denial, downgrade, warning, or review

TSMM extracts those recurring invariants into an abstract model so that other projects can apply the theory without waiting for a repo-specific profile, harness, or implementation package. In the current stack, **trust-infrastructure-schemas** implements the canonical machine-readable trust artifact layer, while TSMM defines the abstract semantics and relationships those artifacts rely on. The model is the blueprint; the schema registry is the concrete wiring.

## Start here

- Pages landing page: `index.md`
- Documentation home: `docs/index.md`
- Core model: `docs/core-model.md`
- Entity model: `docs/model/tsmm-entities.md`
- Relationship model: `docs/model/tsmm-relationships.md`
- Lifecycle model: `docs/model/tsmm-lifecycle.md`
- Agent role classification: `docs/model/agent-role-classification.md`
- Attention governance model: `docs/model/attention-governance.md`
- Effect evaluation model: `docs/evaluation/effect-evaluation-model.md`
- Threat model: `docs/security/trust-system-threat-model.md`
- Implementer guide: `docs/getting-started-implementer-guide.md`
- Roadmap: `docs/roadmap.md`

**Agent Interaction Extension (v0.13.0):**
- Service descriptor: `docs/model/service-descriptor.md`
- Skill contract: `docs/model/skill-contract.md`
- Interaction context: `docs/model/interaction-context.md`
- Authorization checkpoint: `docs/model/authorization-checkpoint.md`
- Extension contract: `docs/model/extension-contract.md`
- Opacity boundary: `docs/model/opacity-boundary.md`
- Peer trust relation: `docs/model/peer-trust-relation.md`
- Schema: `schemas/tsmm-agent-interaction-extension.schema.json`
- Example: `examples/agent-interaction-extension-instance.json`

## Ecosystem positioning

TSMM sits above protocol and schema repositories. It should be read as the conceptual layer that explains **what kinds of trust objects exist, how they relate, and how trust decisions are formed**. Adjacent repositories then operationalize those abstractions:

- **trust-infrastructure-schemas** implements the canonical trust artifact layer, also described as the Open Trust Artifact Model (OTAM)
- **TRQP** and related bindings use those artifacts in discovery, query, and publication flows
- **DCAS** applies them in assessment, evidence, and assurance workflows
- domain baselines such as **ANAB** specialize them for bounded contexts

That separation matters because it keeps TSMM from collapsing into a schema dump wearing a philosophy hat.

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

## What changed in v0.13.0

v0.13.0 adds the Agent Interaction Extension — seven new trust-semantic abstractions for agent-to-agent interaction. The extension is aimed at A2A-class agent ecosystems and any protocol where agents discover, negotiate, and interact as peers without hierarchical authority relationships. No core model changes.

It adds:

- `schemas/tsmm-agent-interaction-extension.schema.json` — new extension schema with seven abstractions
- `examples/agent-interaction-extension-instance.json` — two-party procurement interaction worked example
- `docs/model/service-descriptor.md` — trust-relevant capability disclosure artifacts
- `docs/model/skill-contract.md` — operational envelope separating capability from authorization
- `docs/model/interaction-context.md` — session-level governance state across multi-turn interactions
- `docs/model/authorization-checkpoint.md` — runtime authorization pause as a first-class trust event
- `docs/model/extension-contract.md` — negotiated extension compatibility record
- `docs/model/opacity-boundary.md` — governance constraints from deliberate agent non-observability
- `docs/model/peer-trust-relation.md` — lateral peer trust distinct from hierarchical delegation
- Agent Interaction Extension checklist tier added to `docs/conformance/tsmm-conformance-checklist.md`
- Seven new terms added to `docs/glossary.md`
- `docs/extensions/index.md` updated with Agent Interaction Extension entry

## Repo contents

```text
trust-systems-meta-model/
├── .github/
│   └── workflows/
│       ├── pages.yml
│       └── validate.yml
├── bindings/
│   ├── dcas/
│   │   └── tsmm-dcas-binding.json
│   ├── openid-federation/
│   │   └── tsmm-openid-federation-binding.json
│   ├── trqp/
│   │   └── tsmm-trqp-binding.json
│   └── vtc/
│       └── tsmm-vtc-binding.json
├── docs/
│   ├── bindings/
│   ├── conformance/
│   ├── crosswalks/
│   ├── evaluation/
│   ├── extensions/
│   ├── model/
│   ├── patterns/
│   ├── registry/
│   ├── security/
│   ├── core-model.md
│   ├── documentation-governance.md
│   ├── effect-centered-trust-decision-model.md
│   ├── freshness-audit.md
│   ├── getting-started-implementer-guide.md
│   ├── glossary.md
│   ├── index.md
│   ├── relationship-model.md
│   └── roadmap.md
├── examples/
│   ├── profiles/
│   ├── registries/
│   ├── agent-interaction-extension-instance.json
│   ├── agentic-ai-extension-instance.json
│   ├── assurance-extension-instance.json
│   ├── consumer-policy-instance.json
│   ├── delegated-agent-instance.json
│   ├── evidence-artifact-instance.json
│   ├── minimal-trust-registry-instance.json
│   ├── multi-agent-coordination-instance.json
│   ├── tsmm-ecosystem-example.json
│   └── verifiable-trust-community-instance.json
├── releases/
│   ├── v0.10.0.md
│   ├── v0.11.0.md
│   └── v0.12.0.md
├── schemas/
│   ├── tsmm-agent-interaction-extension.schema.json
│   ├── tsmm-agentic-extension.schema.json
│   ├── tsmm-assurance-extension.schema.json
│   ├── tsmm-binding.schema.json
│   ├── tsmm-core.schema.json
│   ├── tsmm-evidence-artifact-extension.schema.json
│   ├── tsmm-graph.schema.json
│   ├── tsmm-multi-agent-extension.schema.json
│   ├── tsmm-registry.schema.json
│   └── tsmm-vtc-extension.schema.json
├── scripts/
│   ├── check_docs.py
│   ├── check_schema_coverage.py
│   ├── render_tsmm_graph.py
│   ├── validate_examples.py
│   ├── validate_tsmm_graph.py
│   └── validate_tsmm_registry.py
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── SECURITY.md
├── VERSION
├── _config.yml
└── index.md
```

## Validation

Run these checks from the repository root:

```bash
python3 scripts/validate_examples.py
python3 scripts/check_schema_coverage.py
python3 scripts/check_docs.py
python3 scripts/validate_tsmm_graph.py examples/tsmm-ecosystem-example.json
python3 scripts/validate_tsmm_registry.py examples/registries/tsmm-registry-example.json
```

## Release history

- `releases/v0.3.0.md`
- `releases/v0.4.0.md`
- `releases/v0.5.0.md`
- `releases/v0.6.0.md`
- `releases/v0.7.0.md`
- `releases/v0.8.0.md`
- `releases/v0.9.0.md`
- `releases/v0.10.0.md`
- `releases/v0.11.0.md`
- `releases/v0.12.0.md`
- `releases/v0.13.0.md`
