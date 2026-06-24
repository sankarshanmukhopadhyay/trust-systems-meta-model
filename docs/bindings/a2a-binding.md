---
owner: maintainers
last_reviewed: 2026-05-05
applicable_version: v0.21.0
tier: 0
---


# A2A Binding

This binding maps A2A-class protocol concepts into TSMM governance abstractions. It does not restate the A2A protocol. It identifies the trust-system semantics that TSMM can model, validate, and compare.

## Binding posture

| A2A pattern | TSMM abstraction | v0.19.0 treatment |
| --- | --- | --- |
| Public Agent Card | Service Descriptor | Public descriptor disclosure |
| Authenticated extended Agent Card | Service Descriptor + Discovery Governance | Conditional disclosure, integrity, access, freshness |
| Agent Skill | Skill Contract + Capability Negotiation | Capability is negotiated before execution |
| Extension declaration | Extension Contract + Capability Negotiation | URI, version, requiredness, opt-in, failure behavior |
| Task | Interaction Task + Task Evidence Lifecycle | State transitions produce evidence obligations |
| `auth-required` state | Authorization Checkpoint | Authority boundary requiring explicit evidence |
| Message/artifact separation | Content Provenance Policy + Evidence Artifact | Communication is not evidence unless captured and referenced |
| Streaming/async/push | Observability Mode | Delivery mode affects replay, auditability, and user awareness |
| Agent opacity | Opacity Boundary | Hidden internals require compensating evidence |

## Generalized TSMM artifacts

- `docs/model/discovery-governance.md`
- `docs/model/capability-negotiation.md`
- `docs/model/task-evidence-lifecycle.md`
- `schemas/tsmm-discovery-governance.schema.json`
- `schemas/tsmm-capability-negotiation.schema.json`
- `schemas/tsmm-task-evidence-lifecycle.schema.json`

## Binding requirements

An A2A-class implementation mapped into TSMM SHOULD produce evidence for:

1. descriptor discovery and freshness;
2. descriptor integrity or explicit integrity waiver;
3. authenticated extended descriptor access decision;
4. capability negotiation outcome;
5. required extension compatibility;
6. authorization checkpoint for privileged task continuation;
7. task completion artifact binding;
8. streaming or push observability obligations where applicable.

## Maturity status

This binding is **candidate** in v0.21.0. It is suitable for modeling, validation experiments, enterprise architecture review, and assurance design. Its machine-readable contract and constraint set prohibit treating descriptor discovery, protocol reachability, or task completion as a conformance claim against the A2A protocol or as standing authority to produce an effect.
