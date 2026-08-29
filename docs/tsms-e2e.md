---
title: TSMS End-to-End Conformance
permalink: /tsms-e2e.html
parent: Documentation
nav_order: 5
---

# TSMS end-to-end conformance

The TSMS end-to-end harness tests the stack as one executable governance path rather than treating TSMM, TIS, and TGA as three unrelated green repositories.

## Governing proposition

A delegated action is admissible only when canonical TSMM semantics, TIS portable contracts, TGA executable governance, authority, scope, evidence, and current relationship state all permit the requested effect.

## Canonical case

`TSMS-E2E-001 — Delegated Authority Decision` binds:

- TSMM concepts for authority, delegation, scope, evidence bundle, trust decision, and effect;
- TIS authority-boundary, evidence-bundle-manifest, and decision-receipt contracts;
- TGA artifact `urn:tga:tsms:golden-path:delegated-authority-decision`;
- the active TSMS baseline receipt and baseline-lineage registry.

## Run

```bash
python3 scripts/run_tsms_e2e.py
python3 scripts/test_tsms_e2e.py
```

The first command emits `artifacts/e2e/TSMS-E2E-001/evidence-bundle.json`. The second emits `artifacts/e2e/TSMS-E2E-001/pressure-tests.json`.

## Current pressure tests

The suite proves the accepted baseline passes and rejects missing stack layers, active-receipt mismatch, missing portable-contract declarations, missing executable-governance binding, and an incorrect PERMIT expectation.

The delegated-authority execution matrix separately proves rejection when authority is missing, delegation is no longer current, scope does not permit the effect, or required evidence is incomplete.

## Assurance boundary

A green workflow is not itself evidence that the current branch heads remain TSMS-compatible. The E2E harness is bound to the accepted receipt. Remote drift detection and receipt renewal remain explicit governance transitions.

## Follow-on lifecycle test

The next slice will deliberately move an owning layer away from the accepted receipt, require `REVIEW_REQUIRED` or `INDETERMINATE`, collect fresh cross-layer evidence, and exercise a new immutable receipt with human acceptance. Only that renewal may restore compatibility.

## Non-claims

This harness does not constitute external certification. This first slice deterministically verifies the pinned cross-layer contract and decision semantics; independent retrieval of remote TIS/TGA state and the full drift-to-renewal transaction are separate executable stages under the TSMS programme.
