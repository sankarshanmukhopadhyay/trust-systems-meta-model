---
title: Trust Systems Modelling Stack (TSMS)
permalink: /tsms.html
parent: Documentation
nav_order: 3
---

# Trust Systems Modelling Stack (TSMS)

TSMS is the coordinated modelling and executable-governance stack formed by three independently governed repositories:

| Layer | Repository | Role | Owns |
| --- | --- | --- | --- |
| Define | `trust-systems-meta-model` (TSMM) | canonical semantic model | concepts, semantic relationships, graph/meta-model, semantic conformance |
| Represent | `trust-infrastructure-schemas` (TIS) | portable contract layer | portable schemas, identifiers, evidence contracts, schema validation |
| Instantiate | `trust-graph-artifacts` (TGA) | executable governance and implementation layer | compositions, worked artifacts, implementation guidance, negative tests |

The stack is intended to make the path from **meaning → portable representation → executable instantiation → evidence** explicit and testable.

## Authority rule

TSMS is a coordination architecture, not a transfer of authority between repositories.

- TSMM does not own TIS wire/schema contracts or TGA implementation compositions.
- TIS does not redefine TSMM semantics.
- TGA does not redefine TSMM semantics or TIS portable contracts.
- A downstream requirement that exposes a semantic or contract gap must be raised at the layer that owns that authority.

Normative dependency flows downward:

```text
TSMM semantics
    ↓
TIS portable contracts
    ↓
TGA executable artifacts
    ↓
validation / evidence / assurance consumers
```

Feedback may flow upward through issues and proposals, but implementation need does not itself create semantic or schema authority.

## Current compatibility baseline

The initial TSMS programme starts from the already-declared repository relationships:

- TSMM: `v0.24.0`
- TIS: `v0.14.1`
- TGA: `v0.12.1`

This is a **candidate compatibility baseline**, not yet a blanket conformance claim. Machine-readable details are published in `model/tsms-stack.json`. Compatibility must be established by executable checks before a future TSMS baseline is described as validated.

## Consumption paths

### I want to understand or model a trust system

Start with **TSMM**. Define entities, authority, delegation, policy, evidence, lifecycle state, trust decisions and effects using canonical semantics.

### I need portable machine-readable artifacts

Start with **TIS**. Select the portable contract representing the TSMM-governed meaning you need to exchange or validate.

### I want a worked executable governance pattern

Start with **TGA**. Use an artifact or composition that declares its TSMM semantic dependencies and TIS portable-contract dependencies.

### I need to assure or pressure-test a claim

Consume the model/artifact evidence from TSMS in an assurance or interoperability system. TSMS does not itself turn repository validation into external certification.

## Golden-path target

The programme will publish at least one complete worked example with this trace:

```text
TSMM concept identifiers
→ TIS portable contracts
→ TGA executable artifact
→ validation command
→ machine-readable evidence
```

A consumer must be able to reproduce the path without inferring hidden version assumptions.

## Machine-readable contract

`model/tsms-stack.json` records:

- stack identity and status;
- participating repositories and roles;
- authority boundaries;
- candidate compatible versions;
- normative dependency direction;
- required conformance properties;
- governance rule for unknown compatibility.

Future validation will fail safely when required stack compatibility is unknown, unsupported or contradictory.

## Programme governance

The coordinating issue is:

- [TSMM #5 — Establish TSMS as a consumable, machine-verifiable product surface](https://github.com/sankarshanmukhopadhyay/trust-systems-meta-model/issues/5)

Repository workstreams:

- [TIS #7 — Portable contract layer and cross-repo compatibility](https://github.com/sankarshanmukhopadhyay/trust-infrastructure-schemas/issues/7)
- [TGA #16 — Stack-qualified executable artifacts](https://github.com/sankarshanmukhopadhyay/trust-graph-artifacts/issues/16)

Implementation follows visible-judgment discipline: proposition, authority/scope, alternatives, acceptance criteria, pressure tests, evidence, residual uncertainty, and human merge/release decision must remain inspectable.
