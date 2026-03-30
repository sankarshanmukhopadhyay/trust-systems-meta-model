---
owner: maintainers
last_reviewed: 2026-03-30
applicable_version: v0.14.0
tier: 1
---

# AIS-1 Crosswalk

This crosswalk records how AIS-1 should be interpreted across the current trust-stack repositories so the same bonded-identity substrate does not acquire different meanings in different places.

## Structural crosswalk

| AIS-1 concept | TSMM interpretation | Downstream consequence |
|---|---|---|
| Agent Card | Agent | Publish as a durable software-agent subject with identifiable sponsor-backed status |
| Sponsor Card | GovernanceAuthority | Preserve accountable operator or sponsor context for relying parties |
| Bond | Trust-relevant status, assessment input, lifecycle state | Never interpret as a complete delegation object |
| `did:ais1` | Agent identifier | Reuse as the canonical identifier in schema profiles and conformance notes |
| Tier | AssuranceProfile | Keep as a verifier input, not a blanket proof of safe operation |
| Suspension / Revocation | Effect / lifecycle state | Trigger downgrade or denial of reliance where policy requires it |

## Cross-repo reading

### TSMM

TSMM treats AIS-1 as a trust-system component that contributes **identity, accountability, and lifecycle-visible trust state**.

### trust-infrastructure-schemas

The schema layer should capture AIS-1 as a profile with reusable fields for:

- agent identifier
- sponsor identity
- issuer or trust anchor
- bond status
- tier claim
- evidence references
- status timestamps

### agent-name-assurance-baseline

ANAB should not treat AIS-1 verification as a complete answer to agent trust. The practical interpretation is narrower:

- AIS-1 can improve confidence that a named agent maps to a sponsor-backed identity surface
- AIS-1 alone is not enough for high-risk actions that require delegation proof, bounded authority, or policy-specific acceptance criteria
- relying parties should separate identity assurance from authority assurance

## Guardrails

The same three guardrails should travel with every downstream use of AIS-1:

1. **Bond is not delegation.**
2. **Tier is not full assurance.**
3. **Verification is not provenance.**

These guardrails exist to keep the portfolio consistent as AIS-1 is normalized into model, schema, and relying-party interpretation surfaces.
