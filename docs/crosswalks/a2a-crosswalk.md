---
owner: maintainers
last_reviewed: 2026-05-05
applicable_version: v0.22.0
tier: 0
---


# A2A Crosswalk

This crosswalk records how A2A-class concepts generalize into TSMM. The purpose is governance interoperability: make agent interaction patterns comparable, testable, and auditable across ecosystems.

## Core crosswalk

| A2A concept | TSMM concept | Governance interpretation |
| --- | --- | --- |
| Agent Card | Service Descriptor | Capability disclosure artifact whose visibility and integrity can be governed |
| Authenticated extended Agent Card | Discovery Governance + Service Descriptor | Conditional descriptor disclosure after authentication/authorization |
| Skill | Skill Contract | Advertised capability with modes, examples, tags, and authorization expectations |
| Extension URI | Extension Contract | Versioned optional or required behavior negotiated before use |
| Required extension | Capability Negotiation | Missing required extension creates denial or review condition |
| Task | Interaction Task | Trackable unit of work with governance-relevant state |
| `input-required` | Authorization Checkpoint or interaction checkpoint | Missing fact or input boundary requiring evidence |
| `auth-required` | Authorization Checkpoint | Authority boundary requiring scoped credential or approval |
| Message | Interaction communication | Communication object; not automatically audit evidence |
| Artifact | Evidence Artifact / output artifact | Output bound to task, provenance, and evidence obligations |
| Streaming | Observability Mode | Higher replay and audit considerations |
| Push notification | Observability Mode | Out-of-band event delivery requiring subscriber and delivery evidence |
| Opaque agent internals | Opacity Boundary | Hidden tools/state/memory require compensating controls |

## v0.19.0 generalized additions

TSMM v0.19.0 adds three A2A-derived but protocol-neutral surfaces:

1. **Discovery Governance** for descriptor source, access, freshness, integrity, trust basis, and failure behavior.
2. **Capability Negotiation** for modes, required extensions, policy scope, negotiation outcome, and evidence references.
3. **Task Evidence Lifecycle** for state-transition evidence and auditability.

## Boundary rule

A2A defines interaction mechanics. TSMM defines governance semantics. A system can be protocol-correct and still be governance-incomplete if it cannot evidence descriptor integrity, capability authorization, task transition accountability, or relying-party impact.
