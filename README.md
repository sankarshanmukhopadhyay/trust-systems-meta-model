---
owner: maintainers
last_reviewed: 2026-03-29
applicable_version: v0.14.0
tier: 0
---

# Trust Systems Meta Model (TSMM)

[![Release](https://img.shields.io/badge/release-v0.14.0-blue)](releases/v0.14.0.md)
[![License: CC BY-SA 4.0](https://img.shields.io/badge/license-CC--BY--SA%204.0-lightgrey.svg)](LICENSE)
[![Docs](https://img.shields.io/badge/docs-GitHub%20Pages-brightgreen)](index.md)
[![Validate Schemas and Examples](https://github.com/sankarshanmukhopadhyay/trust-systems-meta-model/actions/workflows/validate.yml/badge.svg)](https://github.com/sankarshanmukhopadhyay/trust-systems-meta-model/actions/workflows/validate.yml)
[![Deploy GitHub Pages](https://github.com/sankarshanmukhopadhyay/trust-systems-meta-model/actions/workflows/pages.yml/badge.svg)](https://github.com/sankarshanmukhopadhyay/trust-systems-meta-model/actions/workflows/pages.yml)

**Version:** v0.14.0  
**Status:** Draft reference model with canonical primitive catalog  
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

On the current main branch, Workstream 1 of the meta-model hardening plan is now implemented. TSMM has a canonical primitive catalog at `schemas/tsmm.schema.json`, with a worked example at `examples/tsmm-meta-model-instance.json`. That addition separates the meta-model contract from the instance-layer schemas used to validate concrete trust-system examples.

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
- Canonical meta-model schema: `docs/model/tsmm-meta-model-schema.md`
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
- Interaction task: `docs/model/interaction-task.md`
- Content provenance policy: `docs/model/content-provenance-policy.md`
- Observability mode: `docs/model/observability-mode.md`
- A2A crosswalk: `docs/crosswalks/a2a-crosswalk.md`
- A2A binding: `docs/bindings/a2a-binding.md`
- OASF binding: `docs/bindings/oasf-binding.md`
- OASF crosswalk: `docs/crosswalks/oasf-crosswalk.md`

## Ecosystem positioning

TSMM sits above protocol and schema repositories. It should be read as the conceptual layer that explains **what kinds of trust objects exist, how they relate, and how trust decisions are formed**. Adjacent repositories then operationalize those abstractions:

- **trust-infrastructure-schemas** implements the canonical trust artifact layer, also described as the Open Trust Artifact Model (OTAM)
- **TRQP** and related bindings use those artifacts in discovery, query, and publication flows
- **DCAS** applies them in assessment, evidence, and assurance workflows
- domain baselines such as **ANAB** specialize them for bounded contexts
- **OASF** can act as a publication and extension surface so TSMM-described subjects become assurance-addressable in agent ecosystems

That separation matters because it keeps TSMM from collapsing into a schema dump wearing a philosophy hat.

## Design principles

### 1. Minimal but useful
TSMM aims to define the smallest practical abstraction layer that remains operationally meaningful. Workstream 1 makes that abstraction layer machine-addressable rather than leaving it as prose alone.

### 2. Effect-centered
The core question is not merely *who are you?* but *should this action, artifact, or signal produce an effect right now under bounded authority and policy?*

### 3. Policy-aware
Trust decisions are always evaluated in context. TSMM assumes that evaluation without policy is theater wearing a tie.

### 4. Evidence-backed
Claims, controls, and trust posture must be substantiated. TSMM treats evidence, assessment, and verification as first-class concepts.

### 5. Profile-aware but profile-agnostic
Many real systems implement trust through profiles, requirements, and assessment methods. TSMM models those structures without forcing one domain-specific profile on everyone.

## Current main-branch increment

The current non-release increment completes **Workstream 1 — Meta-Model Core Formalization**.

It adds:

- `schemas/tsmm.schema.json` — canonical schema for the TSMM primitive catalog
- `examples/tsmm-meta-model-instance.json` — worked example of the primitive catalog
- `docs/model/tsmm-meta-model-schema.md` — documentation for the canonical schema and required fields
- validation and coverage checks updated to include the new schema/example pair
- refreshed `schemas/tsmm-core.schema.json` description so the instance-layer schema is clearly distinguished from the canonical meta-model schema

This is intentionally a main-branch documentation-and-schema increment. It does not cut a new release.

## What changed in v0.14.0

v0.14.0 completes the Agent Interaction Extension and delivers the A2A binding. Three deferred abstractions land, the A2A crosswalk and machine-readable binding are published, and a full A2A-aligned worked example is added. No core model changes.

It adds:

- `docs/model/interaction-task.md` — durable stateful work unit with governance-significant status transitions
- `docs/model/content-provenance-policy.md` — governance obligations for payload content by modality
- `docs/model/observability-mode.md` — governance coverage constraints from delivery model
- `examples/agent-interaction-a2a-binding-instance.json` — full worked example exercising all 10 abstractions
- `docs/crosswalks/a2a-crosswalk.md` — A2A protocol concept-level alignment
- `docs/bindings/a2a-binding.md` — A2A binding prose
- `bindings/a2a/tsmm-a2a-binding.json` — machine-readable A2A binding
- Three new terms added to `docs/glossary.md`
- Conformance checklist extended with AI-15 through AI-21
- `docs/bindings/index.md` updated with A2A entry

## Repo contents

```text
trust-systems-meta-model/
├── .github/
│   └── workflows/
│       ├── pages.yml
│       └── validate.yml
├── bindings/
│   ├── a2a/
│   │   └── tsmm-a2a-binding.json
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
│   │   ├── a2a-binding.md
│   │   ├── dcas-binding.md
│   │   ├── index.md
│   │   ├── openid-federation-binding.md
│   │   ├── trqp-binding.md
│   │   └── vtc-binding.md
│   ├── conformance/
│   │   ├── tsmm-conformance-checklist.md
│   │   ├── tsmm-profile-agentic.md
│   │   ├── tsmm-profile-assured.md
│   │   ├── tsmm-profile-minimal.md
│   │   └── tsmm-profile-operational.md
│   ├── crosswalks/
│   │   ├── a2a-crosswalk.md
│   │   ├── agent-taxonomy-ssa-crosswalk.md
│   │   ├── dcas-crosswalk.md
│   │   ├── erc-8004-csp-crosswalk.md
│   │   ├── openid-federation-crosswalk.md
│   │   ├── trqp-tspp-crosswalk.md
│   │   ├── trust-reference-assurance-architecture-crosswalk.md
│   │   └── xacml-abac-crosswalk.md
│   ├── evaluation/
│   │   └── effect-evaluation-model.md
│   ├── extensions/
│   │   ├── agentic-ai-extension.md
│   │   ├── assurance-extension.md
│   │   ├── index.md
│   │   └── verifiable-trust-communities-extension.md
│   ├── model/
│   │   ├── agent-role-classification.md
│   │   ├── agentic-authz-analysis.md
│   │   ├── attention-governance.md
│   │   ├── authorization-checkpoint.md
│   │   ├── content-provenance-policy.md
│   │   ├── dynamic-authorization-framing.md
│   │   ├── evidence-artifact.md
│   │   ├── extension-contract.md
│   │   ├── interaction-context.md
│   │   ├── interaction-task.md
│   │   ├── observability-mode.md
│   │   ├── opacity-boundary.md
│   │   ├── peer-trust-relation.md
│   │   ├── service-descriptor.md
│   │   ├── skill-contract.md
│   │   ├── tsmm-entities.md
│   │   ├── tsmm-meta-model-schema.md
│   │   ├── tsmm-graph-model.md
│   │   ├── tsmm-lifecycle.md
│   │   └── tsmm-relationships.md
│   ├── patterns/
│   │   ├── assurance-evidence-pattern.md
│   │   ├── credential-verification-pattern.md
│   │   ├── delegated-agent-pattern.md
│   │   ├── dynamic-authz-pattern.md
│   │   ├── multi-agent-coordination-pattern.md
│   │   └── trust-registry-pattern.md
│   ├── registry/
│   │   └── tsmm-registry-format.md
│   ├── security/
│   │   └── trust-system-threat-model.md
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
│   ├── tsmm-meta-model-instance.json
│   ├── profiles/
│   │   ├── agent-governance-network.json
│   │   ├── agent-trust-network.json
│   │   ├── dpi-trust-layer.json
│   │   ├── ssi-ecosystem.json
│   │   └── trust-registry-federation.json
│   ├── registries/
│   │   └── tsmm-registry-example.json
│   ├── agent-interaction-a2a-binding-instance.json
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
│   ├── v0.3.0.md
│   ├── v0.4.0.md
│   ├── v0.5.0.md
│   ├── v0.6.0.md
│   ├── v0.7.0.md
│   ├── v0.8.0.md
│   ├── v0.9.0.md
│   ├── v0.10.0.md
│   ├── v0.11.0.md
│   ├── v0.12.0.md
│   ├── v0.13.0.md
│   └── v0.14.0.md
├── schemas/
│   ├── tsmm.schema.json
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
- `releases/v0.14.0.md`
