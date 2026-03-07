# Trust Systems Meta Model (TSMM)

**Version:** v0.2.0  
**Status:** Draft reference model  
**License:** CC BY-SA 4.0

## Overview

Trust Systems Meta Model (TSMM) is a portable abstract reference model for designing, comparing, and implementing trust systems.

It provides a shared vocabulary for how trust-relevant systems connect:

- entities and roles
- authority and constraints
- artifacts and claims
- policy and controls
- threats and evidence
- verification and levels
- trust decisions and effects
- lifecycle events and state changes

TSMM is intentionally **effect-centered**. It does not treat identity as the final unit of governance. Instead, it treats trust systems as mechanisms for deciding whether a bounded authority, under policy and evidence, should be allowed to produce a defined effect.

That framing makes TSMM usable across trust registries, verifiable credential ecosystems, agent systems, trust signal consumers, conformance suites, and assurance frameworks.

## Why this repo exists

Across repositories such as **TRQP-TSPP** and **ERC-8004-CSP**, a recurring pattern is visible:

- machine-readable trust artifacts
- normative controls
- explicit threat models
- conformance or assurance levels
- evidence expectations
- policy-governed trust decisions
- operational consequences for acceptance, denial, downgrade, or warning

TSMM extracts those recurring invariants into an abstract model so that other projects can apply the theory without waiting for a repo-specific profile, harness, or implementation package.

## Design principles

### 1. Minimal but useful
TSMM aims to define the smallest practical abstraction layer that remains operationally meaningful.

### 2. Effect-centered
The core question is not merely *who are you?* but *should this action, artifact, or signal produce an effect right now under bounded authority and policy?*

### 3. Policy-aware
Trust decisions are always evaluated in context. TSMM assumes that evaluation without policy is theater wearing a tie.

### 4. Evidence-backed
Claims, controls, and trust posture must be substantiated. TSMM treats evidence and verification as first-class concepts.

### 5. Profile-agnostic
TSMM is not a replacement for protocol profiles, implementation guides, or assurance frameworks. It is a transfer layer and reference grammar.

## Scope status

### First release scope audit

The original first-release scope included:

1. core concepts
2. relationship model
3. effect-centered trust decision model
4. two crosswalks
5. one simple JSON schema
6. two worked examples

**Status in v0.2.0:** complete.

The first public seed, v0.1.0, covered the README, core model, and crosswalk tables. It did **not** yet ship the dedicated relationship model, standalone effect-centered trust decision model, schema, or worked examples. v0.2.0 closes that gap.

## Repo contents

```text
trust-systems-meta-model/
├── README.md
├── LICENSE
├── docs/
│   ├── core-model.md
│   ├── relationship-model.md
│   ├── effect-centered-trust-decision-model.md
│   └── crosswalks/
│       ├── trqp-tspp-crosswalk.md
│       └── erc-8004-csp-crosswalk.md
├── schemas/
│   └── tsmm-core.schema.json
└── examples/
    ├── minimal-trust-registry-instance.json
    ├── consumer-policy-instance.json
    └── delegated-agent-instance.json
```

## What is included in v0.2.0

### Documents
- `docs/core-model.md`
- `docs/relationship-model.md`
- `docs/effect-centered-trust-decision-model.md`
- crosswalks for TRQP-TSPP and ERC-8004-CSP

### Machine-readable baseline
- `schemas/tsmm-core.schema.json`

### Worked examples
- `examples/minimal-trust-registry-instance.json`
- `examples/consumer-policy-instance.json`

### Additional worked example
- `examples/delegated-agent-instance.json`

The delegated-agent example goes slightly beyond the original first-release scope because this is exactly the kind of thing meta-models should handle before they start congratulating themselves.

## What TSMM is not

TSMM does **not**:

- define the full semantics of every assurance model
- prescribe one universal trust policy
- collapse assurance, conformance, reputation, and authorization into one blob
- require one serialization format
- claim that every trust decision is binary
- replace domain-specific standards or implementation profiles

In plain terms: this repo is a bridge, not a cathedral.

## Core concepts at a glance

The current model includes these primary abstractions:

- **Entity**
- **Role**
- **Authority**
- **Artifact**
- **Claim**
- **Policy**
- **Control**
- **Threat**
- **Evidence**
- **Verification**
- **Level Framework**
- **Trust Decision**
- **Effect**
- **Lifecycle Event**

## Relationship skeleton

```text
Entity -> Role -> Authority -> Effect
   |        |        |
   |        |        v
   |        |     Constraints
   |        |
   v        v
Artifact -> Claim -> Verification -> Trust Decision -> Effect
   |           ^          ^                ^
   v           |          |                |
 Evidence ------          |                |
   ^                      |                |
   |                      |                |
Control <---- mitigates Threat ----> Policy / Level Framework
```

## Release notes

### v0.2.0
- added `relationship-model.md`
- added `effect-centered-trust-decision-model.md`
- added `schemas/tsmm-core.schema.json`
- added worked examples for trust registry, consumer policy, and delegated agent patterns
- cleaned the repo to be self-contained and offline-readable
- preserved the initial crosswalks and aligned them to the broader release scope

### v0.1.0
- initial seed
- README
- core model
- first crosswalk tables

## Source repositories informing the first crosswalks

The initial crosswalks are based on the public positioning and repository structure of:

- `sankarshanmukhopadhyay/TRQP-TSPP`
- `sankarshanmukhopadhyay/ERC-8004-CSP`

These source repositories may evolve over time. TSMM crosswalks should therefore be treated as explanatory mappings, not immutable claims about every future version of those repos.

## Roadmap after v0.2.0

Natural next steps:

1. add a concise terminology registry
2. add specialization-pattern documents
3. add more crosswalks, especially for assurance-hub and conformance-suite patterns
4. add formal relationship constraints and validation profiles
5. add diagrams in SVG or Mermaid for documentation sites

That is enough abstraction to be useful without becoming a taxonomy theme park.
