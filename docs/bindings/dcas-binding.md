---
owner: maintainers
last_reviewed: 2026-05-05
applicable_version: 0.24.0
tier: 1
title: TSMM to DCAS Binding
permalink: /bindings/dcas-binding.html
parent: Bindings
grand_parent: Documentation
---

# TSMM to DCAS Binding

## Purpose

This binding makes the long-standing DCAS crosswalk machine-readable. It packages the most important semantic alignments between TSMM and DTG Conformance & Assurance System (DCAS) so they can be published, indexed, validated, and compared alongside other ecosystem bindings.

## Why it exists

DCAS is one of the most frequently referenced assurance-oriented frameworks in the TSMM documentation set. Leaving it as prose-only after the introduction of the v0.10.0 binding pattern would have left the catalog materially incomplete.

## Binding summary

The binding maps the assurance-heavy surfaces of DCAS into TSMM:

- DCAS control objectives align most closely to TSMM policy and requirement surfaces
- DCAS evidence bundles align directly to TSMM EvidenceBundle
- DCAS assessments align directly to TSMM Assessment
- DCAS assurance profiles align directly to TSMM AssuranceProfile
- downstream assessors and relying evaluators align approximately to TSMM Verifier

## Artifact

- `bindings/dcas/tsmm-dcas-binding.json`

## Notes

This binding is semantic rather than normative. It improves interoperability and publication consistency without attempting to rewrite DCAS language or governance intent.

## Contract and constraints

This binding now includes an explicit contract section in `bindings/dcas/tsmm-dcas-binding.json` and a paired constraint set at `bindings/dcas/constraints.json`. Together they record what the mapping preserves, where it becomes approximate, and what should not be inferred without the target ecosystem's own rules.
