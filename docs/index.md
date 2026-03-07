---
owner: maintainers
last_reviewed: 2026-03-07
applicable_version: v0.5.0
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

## Read this first

1. [Repository overview](../README.md)
2. [Core model](core-model.md)
3. [Entity model](model/tsmm-entities.md)
4. [Relationship model](model/tsmm-relationships.md)
5. [Lifecycle model](model/tsmm-lifecycle.md)
6. [Effect evaluation model](evaluation/effect-evaluation-model.md)
7. [Threat model](security/trust-system-threat-model.md)

## Conformance profiles

- [TSMM Minimal Profile](conformance/tsmm-profile-minimal.md)
- [TSMM Operational Profile](conformance/tsmm-profile-operational.md)
- [TSMM Assured Profile](conformance/tsmm-profile-assured.md)

## Reference patterns

- [Trust Registry Pattern](patterns/trust-registry-pattern.md)
- [Delegated Agent Pattern](patterns/delegated-agent-pattern.md)
- [Credential Verification Pattern](patterns/credential-verification-pattern.md)
- [Assurance Evidence Pattern](patterns/assurance-evidence-pattern.md)

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

## Operational docs

- [Documentation governance](documentation-governance.md)
- [Freshness audit](freshness-audit.md)
- [Glossary](glossary.md)

## Model thesis

TSMM is effect-centered. The core governance question is not merely whether an identity exists. The question is whether a bounded authority, evaluated under policy and evidence, should be allowed to produce a specific effect.

## Release snapshot

This documentation set is aligned to **v0.5.0** and is intended to remain usable both on GitHub and through GitHub Pages. Validation workflow coverage is included for schema and example integrity so the reference model does not quietly drift into decorative theory.
