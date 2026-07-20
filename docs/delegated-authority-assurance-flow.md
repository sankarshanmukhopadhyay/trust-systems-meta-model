---
title: Delegated authority assurance flow
---
# Delegated authority assurance flow

This walkthrough demonstrates the portfolio control path without claiming production certification.

1. **TSMM** defines the originating principal, delegate, scope, attenuation, revocation, evidence, decision, and effect semantics.
2. **TIS** expresses authority, delegation lineage, evidence, and receipt data as portable machine-readable contracts.
3. **TGA** composes the governance pattern and evaluates positive and negative scenarios.
4. Repository validators produce traceable evidence records.

## Required scenarios

| Scenario | Expected result |
|---|---|
| Valid bounded delegation | Effect may be admitted and a decision receipt produced |
| Scope escalation | Evaluation fails closed |
| Revoked delegation | Effect is denied and the revocation basis is recorded |
| Broken lineage | Authority claim is rejected |

## Evidence

The evidence chain must identify the semantic requirement, schema contract, implementation pattern, validation result, and assurance limitation.

## Delegation lineage and revocation

```mermaid
flowchart TD
  P[Originating principal] -->|delegates bounded scope| A[Delegate A]
  A -->|attenuates scope| B[Delegate B]
  A -->|parallel branch| C[Delegate C]
  B --> E[Requested effect]
  C --> E
  R[Revocation event] -. invalidates lineage .-> A
  R -. propagates .-> B
  R -. propagates .-> C
  E --> V{Lineage, scope and freshness valid?}
  V -- yes --> OK[Effect admitted]
  V -- no --> NO[Denied and evidenced]
```
