---
owner: maintainers
last_reviewed: 2026-05-05
applicable_version: 0.23.0
tier: 1
---

# HAVID Crosswalk

This crosswalk records how HAVID should be interpreted in TSMM so composite identifier assurance can be compared without overstating what the current specification proves.

## Structural crosswalk

| HAVID concept | TSMM interpretation | Downstream consequence |
|---|---|---|
| Composite HAVID | Composite `Credential` informing reliance | Treat as a structured trust artifact, not as a single flattened identifier claim |
| Identifier class taxonomy | `Subject`-bound identifier surfaces | Preserve per-class assurance contribution and native trust semantics |
| Cross-endorsement | `VerificationProcess` | Require bi-directional, currently resolvable linkage before relying on composition |
| Assurance composition | `AssuranceProfile` | Keep verifier interpretation policy-aware rather than universalized |
| Validation state | `Assessment` | Surface full, degraded, and invalid outcomes as explicit verifier results |
| Lifecycle coordination | `Policy` plus lifecycle expectations | Make renewal, update, and synchronized maintenance operationally visible |
| Revocation / expiry / deactivation | `Effect` | Downgrade or deny reliance when linked state breaks |

## TSMM reading

TSMM treats HAVID as a **composite identifier-assurance pattern**.

That means the model should preserve four things together:

- which identifier classes participate
- what each class contributes natively
- what lifecycle duties keep the composite trustworthy
- what verifier-visible effects follow when linked state changes

## Guardrails

The same three guardrails should travel with every downstream use of HAVID:

1. **Composite identity is not delegated authority.**
2. **Cross-endorsement is not assurance transfer.**
3. **Validation is not governance completeness.**

## Practical consequence for downstream work

A HAVID-aware downstream profile should preserve at least these fields:

- identifier classes in scope
- cross-endorsement status
- integrity conditions for each identifier class
- current lifecycle state
- revocation / expiry status
- verifier assessment outcome
- policy notes on degraded acceptance

That keeps the binding useful for comparison while preventing semantic inflation.
