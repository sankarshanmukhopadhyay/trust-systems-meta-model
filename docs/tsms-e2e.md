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
python3 scripts/run_tsms_renewal_transaction.py
python3 scripts/test_tsms_renewal_transaction.py
```

The E2E harness emits evidence under `artifacts/e2e/TSMS-E2E-001/`. The renewal transaction emits `artifacts/e2e/TSMS-RENEWAL-001/transaction-evidence.json`.

## Drift-to-renewal transaction

`TSMS-RENEWAL-001` demonstrates the compatibility lifecycle using a deliberately non-production fixture:

```text
accepted baseline
  ↓
starting TSMS-E2E-001 PASS
  ↓
controlled material drift
  ↓
REVIEW_REQUIRED
  ↓
compatibility WITHDRAWN
  ↓
fresh successful owning-layer evidence
  ↓
explicit scoped human acceptance
  ↓
valid fixture renewal lineage
  ↓
post-renewal TSMS-E2E-001 PASS
  ↓
compatibility RESTORED
```

A separate pressure test removes authoritative remote evidence and requires:

```text
remote evidence unavailable
  ↓
INDETERMINATE
  ↓
compatibility DENIED
  ↓
renewal DENIED
```

## Pressure tests

The transaction must reject restoration when any critical precondition is falsified independently, including baseline mismatch, failed starting E2E state, unavailable remote evidence, missing or wrong owning-layer evidence, failed layer validation, absent human acceptance, invalid lineage, inactive renewed fixture state, failed post-renewal E2E state, attempted production receipt use, or absence of material drift.

## Authority boundary

TSMM coordinates the transaction but does not acquire TIS contract authority or TGA executable-governance authority. Fresh evidence must come from the layer that owns the changed state. The controlled fixture demonstrates orchestration semantics; it is not an owning-layer validation substitute.

## Production receipt guardrail

The renewal fixture and its renewed receipt are explicitly marked `production: false`. They MUST NOT be interpreted as an accepted TSMS baseline or used to supersede `model/tsms-baseline-receipt.json`.

A production successor receipt may be created only when real cross-repository state has changed, fresh owning-layer validation evidence exists, and explicit human acceptance records that reviewed state. Historical accepted receipts remain immutable.

## Assurance boundary

A green workflow is not itself evidence that current branch heads remain TSMS-compatible. Compatibility belongs to an evidenced immutable state. Material drift withdraws inherited compatibility; missing authoritative state is `INDETERMINATE`; compatibility is restored only through the governed renewal transaction.

## Remaining limitation

Remote drift detection currently independently obtains remote commits but still derives some declaration information, including version and authority role, from baseline state. Independent remote declaration and digest attestation remains a subsequent TSMS assurance slice.

## Non-claims

Repository conformance is not external certification. The transaction proves fail-safe orchestration and renewal gating with a controlled deterministic fixture; it does not manufacture a production successor receipt or claim stronger remote-state evidence than the repositories currently produce.
