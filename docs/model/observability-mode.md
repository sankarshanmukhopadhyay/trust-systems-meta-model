---
owner: maintainers
last_reviewed: 2026-05-05
applicable_version: v0.20.0
tier: 1
---

# ObservabilityMode

## Concept definition

An **ObservabilityMode** models the governance observability properties of an
interaction delivery channel — what can be known about delivery, timing, and progress
given the channel's delivery model, and what compensating controls are structurally
required as a consequence.

ObservabilityMode is explicitly **not** a model of transport mechanics. TSMM does not
model HTTP methods, SSE framing, webhook retry logic, or polling intervals. It models
the governance implications: what level of auditability is achievable, what replay risk
exists, whether a human principal can be aware of in-progress state, and what controls
are required to compensate for governance gaps that a given delivery model introduces.

## Trust significance

The delivery model of an interaction channel directly constrains what a governance
system can observe, record, and audit. These constraints are structurally determined —
they cannot be engineered away at the application layer without the compensating
controls that ObservabilityMode identifies.

| Delivery model | Structural governance consequence |
|---|---|
| `synchronous` | Full request-response record available; replay risk minimal; real-time principal awareness possible |
| `streaming` | Partial observability — intermediate state visible but not complete; sequence gaps detectable only with explicit sequencing; clean completion vs. connection drop must be distinguished |
| `polling` | Metadata-only observability for in-progress state; state snapshots at poll intervals but no continuous record; replay/duplicate risk from concurrent polls |
| `push-callback` | Principal awareness is delayed and conditional on callback delivery; no in-progress visibility; replay risk from retries without idempotency keys |

The `userAwarenessModel` property is governance-significant beyond auditability. In
agent workflows involving human principals, the question of whether the principal can
observe what an agent is doing in real time — or only learns of it after completion or
not at all — is a control posture question. An agent operating under `opaque` user
awareness with `human-on-loop` control mode (from the agentic extension) creates a
specific governance risk profile that TSMM can now represent explicitly.

## Relationship to existing TSMM abstractions

| TSMM abstraction | Relationship |
|---|---|
| `ExecutionContext` | ExecutionContext carries `userPresence` (present / not-present). ObservabilityMode extends that with `userAwarenessModel`, which models not just whether a user is present but whether they can observe progress. |
| `Control` | `requiredCompensatingControls` identifies controls in the TSMM sense that must be applied to maintain governance adequacy given the delivery model's constraints. |
| `Evidence` | `auditabilityLevel` directly constrains what evidence is structurally collectable. An evidence requirement that assumes full auditability cannot be satisfied by a `metadata-only` channel. |
| `InteractionTask` | The delivery model used for a task affects what governance record exists for that task's execution. ObservabilityMode should be referenced when specifying the governance envelope for a task type. |
| `AttentionPolicy` | The agentic extension's `attentionPolicy` governs signal admission before reaching a principal. ObservabilityMode models whether the principal can see what is happening during execution — the downstream complement to attention governance. |

## Key properties

| Property | Required | Description |
|---|---|---|
| `id` | Yes | Unique identifier |
| `deliveryModel` | Yes | `synchronous`, `streaming`, `polling`, or `push-callback` |
| `auditabilityLevel` | Yes | `full`, `partial`, `metadata-only`, or `none` |
| `replayRisk` | Yes | `none`, `low`, `medium`, or `high` |
| `userAwarenessModel` | Yes | `real-time`, `delayed`, or `opaque` |
| `requiredCompensatingControls` | No | Controls required to maintain governance adequacy |

## Auditability level semantics

| Level | Meaning |
|---|---|
| `full` | Complete request and response record structurally available. Every exchange can be replayed or audited from the channel record alone. |
| `partial` | Progress or intermediate state is recordable but the record is not complete. Streaming channels with sequence numbers achieve partial auditability. |
| `metadata-only` | Only timing, routing, and status metadata is available. Content of exchanges is not structurally recoverable from the channel record. |
| `none` | No reliable audit trail is possible without external instrumentation. Fire-and-forget delivery with no acknowledgement falls here. |

## Design notes

**Compensating controls are governance obligations, not suggestions.** When
`requiredCompensatingControls` is non-empty, those controls must be implemented for
the governance record to be adequate. An implementation that deploys a `polling`
channel without idempotency keys has accepted a governance gap, not merely an
engineering tradeoff.

**`opaque` user awareness is a governance risk signal.** An agent operating with
`deliveryModel: push-callback` and `userAwarenessModel: opaque` means the principal
learns of outcomes only when the agent reports them, and only if the callback is
delivered. This should be reflected in the oversight mode and control mode declared
in the agentic extension.

## Related artifacts

- Schema: `schemas/tsmm-agent-interaction-extension.schema.json`
- Example: `examples/agent-interaction-a2a-binding-instance.json`
- A2A binding: `docs/bindings/a2a-binding.md`
- Attention governance: `docs/model/attention-governance.md`
- Agentic AI extension: `docs/extensions/agentic-ai-extension.md`
