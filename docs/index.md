---
owner: maintainers
last_reviewed: 2026-03-14
applicable_version: v0.10.0
tier: 0
---

# Trust Systems Meta Model

Welcome to the documentation site for **Trust Systems Meta Model (TSMM)**.

TSMM is a portable reference model for designing, comparing, and implementing trust systems. It gives architects, standards authors, assurance teams, and protocol designers a common grammar for reasoning about roles, authority, policies, profiles, controls, evidence, assessment, verification, trust decisions, and operational effects.

## What you get here

- a compact **core model** for trust systems
- an **effect-centered evaluation model** for runtime legitimacy
- **conformance profiles** that help structure implementation maturity
- reusable **reference patterns** for recurring trust-system designs
- modular **extensions** for application domains such as Agentic AI, Verifiable Trust Communities, and assurance-oriented architectures
- practical **crosswalks** to related repositories and implementations
- a machine-readable **graph model** for executable trust topology design

## Read this first

1. [Repository overview](../README.md)
2. [Core model](core-model.md)
3. [Entity model](model/tsmm-entities.md)
4. [Relationship model](model/tsmm-relationships.md)
5. [Lifecycle model](model/tsmm-lifecycle.md)
6. [Graph model](model/tsmm-graph-model.md)
7. [Effect evaluation model](evaluation/effect-evaluation-model.md)
8. [Threat model](security/trust-system-threat-model.md)

## Conformance profiles

- [TSMM Minimal Profile](conformance/tsmm-profile-minimal.md)
- [TSMM Operational Profile](conformance/tsmm-profile-operational.md)
- [TSMM Assured Profile](conformance/tsmm-profile-assured.md)

## Reference patterns

- [Trust Registry Pattern](patterns/trust-registry-pattern.md)
- [Delegated Agent Pattern](patterns/delegated-agent-pattern.md)
- [Credential Verification Pattern](patterns/credential-verification-pattern.md)
- [Assurance Evidence Pattern](patterns/assurance-evidence-pattern.md)
- [Multi-Agent Coordination Pattern](patterns/multi-agent-coordination-pattern.md)

## Extensions

- [Extensions overview](extensions/index.md)
- [Agentic AI Extension](extensions/agentic-ai-extension.md)
- [Verifiable Trust Communities Extension](extensions/verifiable-trust-communities-extension.md)
- [Assurance Extension](extensions/assurance-extension.md)

## Crosswalks

- [TRQP-TSPP Crosswalk](crosswalks/trqp-tspp-crosswalk.md)
- [ERC-8004-CSP Crosswalk](crosswalks/erc-8004-csp-crosswalk.md)
- [DCAS Crosswalk](crosswalks/dcas-crosswalk.md)
- [TRAA Crosswalk](crosswalks/trust-reference-assurance-architecture-crosswalk.md)
- [OpenID Federation Crosswalk](crosswalks/openid-federation-crosswalk.md)

## Ecosystem bindings

- [Bindings overview](bindings/index.md)
- [TRQP binding](bindings/trqp-binding.md)
- [OpenID Federation binding](bindings/openid-federation-binding.md)
- `bindings/trqp/tsmm-trqp-binding.json`
- `bindings/openid-federation/tsmm-openid-federation-binding.json`

## Executable graph layer

- [TSMM Graph Model](model/tsmm-graph-model.md)
- `schemas/tsmm-graph.schema.json`
- `examples/tsmm-ecosystem-example.json`
- `examples/profiles/ssi-ecosystem.json`
- `examples/profiles/agent-trust-network.json`
- `examples/profiles/agent-governance-network.json`
- `examples/profiles/trust-registry-federation.json`
- `examples/profiles/dpi-trust-layer.json`

## Registry publication

- [TSMM Registry Format](registry/tsmm-registry-format.md)
- `schemas/tsmm-registry.schema.json`
- `examples/registries/tsmm-registry-example.json`

## Operational docs

- [Documentation governance](documentation-governance.md)
- [Freshness audit](freshness-audit.md)
- [Glossary](glossary.md)
- [Getting Started: Implementer Guide](getting-started-implementer-guide.md)

## Model thesis

TSMM is effect-centered. The core governance question is not merely whether an identity exists. The question is whether a bounded authority, evaluated under policy and evidence, should be allowed to produce a specific effect.

## Release snapshot

This documentation set is aligned to **v0.10.0** and is intended to remain usable both on GitHub and through GitHub Pages. Validation coverage now includes the executable TSMM graph layer, the registry format, and ecosystem publication artifacts so the reference model does not quietly drift into decorative theory.
