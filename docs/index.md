---
owner: maintainers
last_reviewed: 2026-03-07
applicable_version: v0.4.0
tier: 0
---

# Trust Systems Meta Model

Welcome to the documentation site for **Trust Systems Meta Model (TSMM)**.

TSMM is a portable reference model for designing, comparing, and implementing trust systems. It helps teams reason about how entities, roles, authority, policies, profiles, controls, evidence, assessment, verification, trust decisions, and effects fit together.

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

## Crosswalks

- [TRQP-TSPP Crosswalk](crosswalks/trqp-tspp-crosswalk.md)
- [ERC-8004-CSP Crosswalk](crosswalks/erc-8004-csp-crosswalk.md)
- [DCAS Crosswalk](crosswalks/dcas-crosswalk.md)

## Operational docs

- [Documentation governance](documentation-governance.md)
- [Freshness audit](freshness-audit.md)
- [Glossary](glossary.md)

## Model thesis

TSMM is effect-centered. The core governance question is not merely whether an identity exists. The question is whether a bounded authority, evaluated under policy and evidence, should be allowed to produce a specific effect.
