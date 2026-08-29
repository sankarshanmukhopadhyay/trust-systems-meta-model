---
title: TSMS Remote Drift Detection
permalink: /tsms-drift.html
parent: Documentation
nav_order: 4
---

# TSMS remote drift detection

TSMS compatibility is a reviewed claim over immutable repository state. It is not inherited by a branch head merely because a component retains the same version label.

## Governing proposition

A previously accepted TSMS baseline remains evidence for its pinned commits. Any current authoritative state that differs from those commits requires new evidence before compatibility can be renewed.

## Dispositions

| Disposition | Meaning |
| --- | --- |
| `UNCHANGED` | Exact authoritative component state is evidenced as identical to the accepted receipt. |
| `REVIEW_REQUIRED` | Evidence is available and material state differs. Fresh validation and human acceptance are required. |
| `UNSUPPORTED` | The component or comparison state is outside the supported TSMS contract. |
| `INDETERMINATE` | Required remote evidence is unavailable or unverifiable. Compatibility is not inferred. |

The fail-safe rule is deliberate: **unavailable evidence never becomes `UNCHANGED` or PASS**.

## Executable invariants

- same version + same pinned commit → `UNCHANGED`;
- same version + different commit → `REVIEW_REQUIRED`;
- changed version → `REVIEW_REQUIRED` pending compatibility review;
- authority-role change → `REVIEW_REQUIRED`;
- unknown component or non-immutable commit state → `UNSUPPORTED`;
- unavailable remote state → `INDETERMINATE`.

## Commands

Run deterministic pressure tests without network access:

```bash
python3 scripts/test_tsms_drift.py
```

Compare the accepted receipt with current GitHub `main` commit state:

```bash
python3 scripts/check_tsms_drift.py
```

The latter is intentionally not a compatibility-renewal operation. A changed branch head produces `REVIEW_REQUIRED`; it does not mutate or supersede the accepted receipt.

For deterministic inspection of a supplied state:

```bash
python3 scripts/check_tsms_drift.py --current-state validation/tsms/drift/exact-baseline.json
```

## Evidence

The classifier writes `artifacts/validation/tsms-drift.json`. Pressure tests write `artifacts/validation/tsms-drift-tests.json`.

## Authority boundary

TSMM coordinates the cross-repository comparison because it carries the accepted TSMS baseline receipt. Drift detection does not transfer semantic authority from TSMM, contract authority from TIS, or executable-governance authority from TGA. A detected change must be reviewed by the layer that owns the changed authority surface.

## Non-claims

Drift detection is not external certification, does not continuously attest branch heads, and does not issue a new baseline receipt. Baseline renewal remains a separate human-accepted lifecycle step under issue #9.
