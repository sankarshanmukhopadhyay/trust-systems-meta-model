---
owner: maintainers
last_reviewed: 2026-04-08
applicable_version: v0.16.0
tier: 1
---

# TSMM Maturity Model

TSMM can model systems that are incomplete, emerging, or experimental. Inclusion in TSMM means a system is structurally analyzable within the meta-model. It does **not** by itself imply production readiness, normative endorsement, or cross-ecosystem maturity.

This maturity model is the repo-wide taxonomy for bindings, crosswalks, and other comparison surfaces that need a governance signal.

## Maturity states

| Status | Meaning | Typical use |
| --- | --- | --- |
| `experimental` | Modeled for analysis, comparison, and early testing | Early-stage or still-evolving ecosystems that are worth comparing without overstating maturity |
| `candidate` | Structurally coherent and ready for broader ecosystem review | Comparison surfaces likely to stabilize soon but not yet treated as fully settled |
| `supported` | Stable enough for normal TSMM comparison use | Published and maintained comparison surfaces suitable for routine use |
| `deprecated` | Retained for reference, not recommended for new work | Historical or superseded surfaces kept to preserve traceability |

## Stability states

| Stability | Meaning |
| --- | --- |
| `draft` | Early or provisional documentation and machine-readable mapping |
| `review` | Ready for wider review but still open to material change |
| `stable` | Expected to change only in bounded and traceable ways |
| `sunset` | Being retained for continuity while active use winds down |

## Production recommendation values

| Value | Meaning |
| --- | --- |
| `not-yet` | Do not treat inclusion as a production-readiness signal |
| `conditional` | Use only with explicit caveats and composition requirements |
| `yes` | Normal comparison use is fine within the stated scope |
| `no-new-adoption` | Keep for reference, but do not expand new usage |

## How to apply this taxonomy

- Put machine-readable maturity fields on bindings where practical.
- Surface the same status in README, docs indexes, and human-readable binding notes.
- Keep `modeled` separate from `recommended`.
- Use explicit limitation language whenever a surface is strong in one dimension but thin in another.

## AIS-1 now

AIS-1 is currently treated as **experimental** in TSMM. That means it is useful to model and compare as a bonded identity and accountability substrate, but TSMM is not claiming that AIS-1 is already a mature or complete trust-stack profile.
