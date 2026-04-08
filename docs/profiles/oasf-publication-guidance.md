---
owner: maintainers
last_reviewed: 2026-04-08
applicable_version: v0.16.0
tier: 1
---

# OASF Publication Guidance for TSMM Profiles

## Purpose

This guide explains how to publish a TSMM-described system through an OASF-facing surface without losing the trust semantics that matter for assurance, review, or downstream operational decisions.

The goal is not to restate all TSMM content inside OASF. The goal is to publish enough machine-readable information so the following can still be recovered later:

- who is accountable for the published subject
- what kind of trust-relevant system or component is being described
- which control baseline, policy bundle, or assurance profile applies
- where evidence and evaluation artifacts can be found
- how status change, revocation, suspension, or expiry should be interpreted

## Publication design principles

### 1. Preserve accountable authority
Every published profile should make the accountable operator or publisher explicit. A consumer should not have to guess who stands behind the described agent, service, or evaluation surface.

### 2. Publish references, not flattened prose
Where possible, publish stable references to profiles, controls, evidence bundles, and evaluations rather than restating them informally in free text.

### 3. Keep effect semantics visible
If the published profile is meant to support trust-relevant decisions, include enough structure to show what kind of downstream effect is being enabled, constrained, warned on, or denied.

### 4. Surface lifecycle state
If revocation, expiry, suspension, or review state matters, the publication should expose how those lifecycle states are represented and where authoritative updates are expected.

## Minimum publication fields

A TSMM-aware OASF publication should make the following visible either directly or through dereferenceable references:

| Publication concern | Expected publication content |
| --- | --- |
| Subject identity | Stable identifier for the described system, agent, or service |
| Publisher accountability | Operator or publisher reference |
| Trust profile | Applicable policy bundle, baseline, or assurance profile |
| Evidence references | URIs or identifiers for evidence bundles and referred evaluations |
| Assessment linkage | Structured pointer to current or latest evaluation output |
| Lifecycle semantics | Revocation, suspension, expiry, and review handling |
| Extension semantics | Any ecosystem-specific module or extension contract |

## Recommended publication flow

1. Model the system in TSMM using the graph layer.
2. Bind the system to the relevant ecosystem semantics.
3. Validate the graph, examples, bindings, and test vectors.
4. Publish an OASF-facing record that points to the stable TSMM-aligned control, evidence, and evaluation references.
5. Ensure that lifecycle updates can be surfaced without changing the semantic meaning of the published subject.

## Evidence and evaluation pattern

A good publication pattern keeps evidence and evaluation separable:

- **Evidence** remains the replayable substrate.
- **Evaluation** states what conclusion was reached from that evidence.
- **Publication** exposes references to both so downstream consumers can decide how much they trust the conclusion.

That separation matters for contestability and audit. It avoids turning a publication surface into an opaque badge.

## Worked example

See `examples/profiles/oasf-publication-profile.json` for a simple graph-oriented profile showing how an OASF-facing publication pattern can preserve publisher identity, policy linkage, evidence references, and assessment traceability.

## Related material

- [TSMM to OASF Binding](../bindings/oasf-binding.md)
- [TSMM ↔ OASF Crosswalk](../crosswalks/oasf-crosswalk.md)
- [TSMM Operational Profile](../conformance/tsmm-profile-operational.md)
- [Validation and testability](../conformance/validation-and-testability.md)
