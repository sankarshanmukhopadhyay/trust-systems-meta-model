---
owner: maintainers
last_reviewed: 2026-05-05
applicable_version: v0.21.0
tier: 1
---

# InteractionTask

## Concept definition

An **InteractionTask** is a durable, stateful work unit with governance-significant
state transitions, artifact accumulation, and cancellation/continuation semantics. It
models a bounded piece of work in progress — what it is doing, what it has produced,
and how it was resolved or terminated.

InteractionTask is distinct from three existing TSMM abstractions it might superficially
resemble:

- **`ExecutionContext`** models the operational parameters of a single evaluation
  (environment, userPresence, approvalState, riskTier). It is flat and per-event. It
  has no history, no artifact accumulation, and no state machine.
- **`InteractionContext`** models session-level governance state across a multi-turn
  exchange — which authority carries forward, which evidence has been established, and
  when re-authorization is required. It is the governance envelope for a session, not
  a work unit.
- **`Action`** models a single act within a context. An InteractionTask may involve
  many actions; it is the container they execute within.

## Trust significance

The trust significance of InteractionTask is concentrated in its **state machine** and
the distinction between terminal and non-terminal states:

| Status | Terminal? | Governance significance |
|---|---|---|
| `submitted` | No | Task accepted; governance record opened |
| `working` | No | Execution in progress; trace record should be active |
| `input-required` | No | Paused awaiting input; AuthorizationCheckpoint may be active |
| `auth-required` | No | Paused at authority boundary; AuthorizationCheckpoint required |
| `completed` | Yes | Task resolved successfully; artifact record is final |
| `cancelled` | Yes | Task terminated before completion; `cancellationReason` required |
| `failed` | Yes | Task terminated due to error or unresolvable checkpoint |

The `auth-required` status is the most governance-significant. It signals that the task
has reached an authority boundary and cannot proceed without principal escalation, scope
reduction, or new evidence — all of which are trust decisions. The
`authorizationCheckpointRef` field links the suspended task to the checkpoint that
governs its resumption or termination.

A task that reaches `cancelled` or `failed` without a recorded `cancellationReason` is
a governance gap: there is no traceability from the open task record to the governance
event that closed it.

## Relationship to existing TSMM abstractions

| TSMM abstraction | Relationship |
|---|---|
| `ExecutionContext` | Per-evaluation operational parameters. An InteractionTask may reference many ExecutionContext objects across its lifetime — one per action taken within the task. |
| `InteractionContext` | Session envelope. Every InteractionTask references the InteractionContext it belongs to via `contextRef`. The session governance state (inherited authority, evidence, re-authorization policy) applies to all tasks within the context. |
| `AuthorizationCheckpoint` | When a task status is `auth-required` or `input-required`, an AuthorizationCheckpoint governs resolution. `authorizationCheckpointRef` is the link. Resolving the checkpoint allows the task to transition back to `working`; failing it terminates the task with `failed`. |
| `Artifact` | `artifactRefs` accumulates references to artifacts produced during task execution. These are the governance record of what the task produced. |
| `TraceRecord` | `historyRef` references a trace record capturing the task's execution history. |

## Key properties

| Property | Required | Description |
|---|---|---|
| `id` | Yes | Unique identifier |
| `contextRef` | Yes | InteractionContext this task belongs to |
| `initiatorRef` | Yes | Entity that initiated this task |
| `assigneeRef` | No | Entity currently executing the task |
| `status` | Yes | `submitted`, `working`, `input-required`, `auth-required`, `completed`, `cancelled`, or `failed` |
| `authorizationCheckpointRef` | No | Active AuthorizationCheckpoint when status is `auth-required` or `input-required` |
| `artifactRefs` | No | Artifacts produced during execution |
| `cancellationReason` | No | Required for governance traceability when status is `cancelled` |
| `historyRef` | No | Reference to trace record for this task |

## Design notes

**`auth-required` is not a delivery state.** It is a governance event. The task is
not merely waiting — it has hit an authority boundary. The resolution path is always a
trust decision: escalate, reduce scope, or terminate. Implementations that treat
`auth-required` as a transient retry condition misread the governance semantics.

**Terminal states are final.** A task with status `completed`, `cancelled`, or `failed`
must not be resumed or have its status changed. Resumption of a failed task is a new
task referencing the same context.

**Cancellation reason is governance-required.** A `cancelled` task without a
`cancellationReason` has an incomplete governance record. The reason may be brief but
must be present.

## Related artifacts

- Schema: `schemas/tsmm-agent-interaction-extension.schema.json`
- Example: `examples/agent-interaction-a2a-binding-instance.json`
- Authorization checkpoint: `docs/model/authorization-checkpoint.md`
- Interaction context: `docs/model/interaction-context.md`
- A2A binding: `docs/bindings/a2a-binding.md`
