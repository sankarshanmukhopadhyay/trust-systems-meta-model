---
owner: maintainers
last_reviewed: 2026-08-28
applicable_version: 0.24.0
tier: 1
title: TSMM Roadmap
permalink: /roadmap.html
parent: Documentation
---

# TSMM Roadmap

TSMM evolves through additive, testable semantic surfaces. Coordinated portfolio releases may consume TSMM semantics, but they do not require TSMM changes or version bumps unless a genuine semantic gap exists.

## Current release line

**v0.24.0 — Executable Cross-Repository Semantic Governance** is the current semantic baseline for the TRQP Stack and related portfolio projections.

## September 2026 conditional work: assurance validity under change

**Coordinating issue:** https://github.com/sankarshanmukhopadhyay/trqp-assurance-hub/issues/39  
**TSMM assessment issue:** https://github.com/sankarshanmukhopadhyay/trust-systems-meta-model/issues/3

TRQP Stack 2026.2 targets assurance validity under change. TSMM's role is assessment-first: determine whether existing canonical semantics already support the required lifecycle without creating duplicate vocabulary.

### Question

> Are existing TSMM semantics sufficient to represent assurance validity under change, material/non-material impact, reassessment, authority drift, freshness, and supersession?

### Evaluate

- change event and changed-relationship semantics;
- evidence validity/freshness;
- authority drift and compatibility;
- current versus historical assurance state;
- reassessment obligation;
- supersession/lineage;
- unknown-impact/fail-safe semantics.

### Allowed outcomes

1. **Existing semantics sufficient:** document bindings/projections and retain `v0.24.0` in Stack 2026.2.
2. **Bounded clarification required:** make the smallest additive, validated change.
3. **New canonical semantics required:** define the minimum new surface with identifiers, examples, invalid vectors, validation, and downstream projection evidence before considering a release.

### Acceptance evidence

- explicit semantic sufficiency/gap decision;
- no duplicate concept introduced when an existing semantic identifier suffices;
- projection and validation coverage for any new semantics;
- preserved TSMM/TIS/Hub authority boundaries;
- explicit version decision with rationale;
- residual semantic uncertainty recorded for the Stack release decision.

## Stack 2026.2 version policy

The default is **retain TSMM v0.24.0**. A new TSMM version is justified only by actual semantic change, not coordinated-release symmetry.

## Continuing near-term increments

Descriptor integrity/publication, human review and redress hooks, cross-protocol registry comparison, and evidence-bundle packaging remain valid TSMM backlog. They are not Stack 2026.2 blockers unless the semantic sufficiency assessment demonstrates a direct dependency.

## Promotion criteria

A TSMM surface moves toward stable status only with documentation, schema where applicable, valid and invalid examples, validation coverage, binding/crosswalk notes where relevant, and freshness metadata aligned to the current release.
