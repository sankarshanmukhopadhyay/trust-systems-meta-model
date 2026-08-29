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

The three versions now form the first **validated repository baseline** for TSMS, pinned to exact reviewed commits in `model/tsms-baseline-receipt.json`. This is deliberately narrower than a floating or blanket conformance claim: the receipt covers the pinned commits and recorded CI evidence only. Future branch heads or same-version changes require a new review and receipt.

## Consumption paths

### I want to understand or model a trust system

Start with **TSMM**. Define entities, authority, delegation, policy, evidence, lifecycle state, trust decisions and effects using canonical semantics.

### I need portable machine-readable artifacts

Start with **TIS**. Select the portable contract representing the TSMM-governed meaning you need to exchange or validate.

### I want a worked executable governance pattern

Start with **TGA**. Use an artifact or composition that declares its TSMM semantic dependencies and TIS portable-contract dependencies.

### I need to assure or pressure-test a claim

Consume the model/artifact evidence from TSMS in an assurance or interoperability system. TSMS does not itself turn repository validation into external certification.

## Golden path

The first complete stack-qualified example is published by TGA and follows this trace:

```text
TSMM concept identifiers
→ TIS portable contracts
→ TGA executable artifact
→ validation command
→ machine-readable evidence
```

A consumer can inspect the TGA golden-path artifact, its positive/negative fixtures, and machine-readable evidence without inferring hidden version assumptions.

## Machine-readable contract

`model/tsms-stack.json` records:

- stack identity and status;
- participating repositories and roles;
- authority boundaries;
- candidate compatible versions;
- normative dependency direction;
- required conformance properties;
- governance rule for unknown compatibility.

`model/tsms-baseline-receipt.json` pins the first reviewed baseline to exact commits and CI evidence. `scripts/validate_tsms_baseline.py` rejects version drift, floating commit references, and failed validation evidence. Unknown or future versions remain unsupported until a new receipt is issued.

## Programme governance

The coordinating issue is:

- [TSMM #5 — Establish TSMS as a consumable, machine-verifiable product surface](https://github.com/sankarshanmukhopadhyay/trust-systems-meta-model/issues/5)

Repository workstreams:

- [TIS #7 — Portable contract layer and cross-repo compatibility](https://github.com/sankarshanmukhopadhyay/trust-infrastructure-schemas/issues/7)
- [TGA #16 — Stack-qualified executable artifacts](https://github.com/sankarshanmukhopadhyay/trust-graph-artifacts/issues/16)

Implementation follows visible-judgment discipline: proposition, authority/scope, alternatives, acceptance criteria, pressure tests, evidence, residual uncertainty, and human merge/release decision must remain inspectable.


## First validated baseline receipt

The reviewed baseline is pinned as:

| Layer | Version | Merge commit |
| --- | --- | --- |
| TSMM | `v0.24.0` | `2867010121e8a61971184d8fe7d3306b985e5884` |
| TIS | `v0.14.1` | `d25539932181e6d883f5bec261daaf011f740059` |
| TGA | `v0.12.1` | `f0bdc309a691a7be8dca3b48fed8ac1555219bec` |

Run:

```bash
python scripts/validate_tsms_baseline.py
```

The check writes `artifacts/validation/tsms-baseline.json` and exercises negative fixtures for version mismatch, unpinned commits, and failed validation evidence.

This receipt proves consistency of the reviewed, pinned baseline. It is **not** continuous remote-drift monitoring and is not external certification.
