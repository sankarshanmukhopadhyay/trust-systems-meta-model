---
owner: maintainers
last_reviewed: 2026-05-05
applicable_version: 0.23.0
tier: 1
---

# AuthorizationCheckpoint

## Concept definition

An **AuthorizationCheckpoint** is a first-class trust event representing a runtime
authorization challenge that interrupts or pauses an interaction pending resolution.
It models the case where the inputs required for policy evaluation are absent or
insufficient, and the interaction must be suspended until they are supplied.

An AuthorizationCheckpoint is structurally distinct from normal policy evaluation.
Policy evaluation produces a trust decision given available inputs. An
AuthorizationCheckpoint signals that available inputs are insufficient to produce any
trust decision — and that the interaction cannot proceed until the gap is resolved.

## Trust significance

In A2A-class agent systems, interactions may pause mid-task in states such as
`input-required` or `auth-required`. These are not merely transport states — they are
**governance checkpoints**. Whether an interaction is allowed to resume, under what
conditions, and with what new evidence, are trust decisions.

Four trigger conditions are modeled:

| Trigger | Meaning |
|---|---|
| `policy-gap` | Policy cannot be evaluated because required attributes are missing |
| `auth-required` | An authentication credential is missing, expired, or invalid |
| `input-required` | Required data input is absent and cannot be inferred |
| `scope-exceeded` | The requested action falls outside the scope of delegated authority or the active SkillContract |

`scope-exceeded` is the most governance-significant trigger. It indicates that the
interaction has reached an authority boundary — the executing agent does not hold
sufficient delegation or the SkillContract does not cover the requested action. This
cannot be resolved by supplying a credential; it requires principal escalation or scope
reduction.

## Relationship to existing TSMM abstractions

| TSMM abstraction | Relationship |
|---|---|
| `LifecycleEvent` | AuthorizationCheckpoint is a specialized lifecycle event: a state change in the interaction that has governance consequences and requires a resolution path |
| `TrustDecision` | An AuthorizationCheckpoint precedes and blocks a trust decision. Resolution of the checkpoint provides the missing inputs that allow evaluation to proceed. |
| `Evidence` | `requiredEvidenceRefs` identifies the evidence that would satisfy the checkpoint. Supplying that evidence is a resolution path. |
| `InteractionContext` | Every AuthorizationCheckpoint references the active InteractionContext. The resolution record becomes part of that session's governance state. |
| `Authority` | `scope-exceeded` checkpoints indicate that the current authority set does not cover the requested action. Resolution requires authority escalation. |

## Key properties

| Property | Required | Description |
|---|---|---|
| `id` | Yes | Unique identifier |
| `triggerCondition` | Yes | `policy-gap`, `auth-required`, `input-required`, or `scope-exceeded` |
| `interactionContextRef` | Yes | The session within which this checkpoint was raised |
| `taskRef` | No | The specific task or work unit that triggered the checkpoint |
| `requiredEvidenceRefs` | No | Evidence that would satisfy this checkpoint |
| `resolutionPaths` | No | Ordered candidate resolution approaches |
| `status` | Yes | `pending`, `resolved`, `failed`, or `timed-out` |
| `resolvedAt` | No | Timestamp of resolution |

## Design notes

**Resolution is not automatic.** An AuthorizationCheckpoint is a governance record. The
implementation is responsible for resolution logic; TSMM models the checkpoint as a
structured trust event with explicit status tracking, not as an executable workflow.

**Failed and timed-out checkpoints are governance-significant.** A checkpoint that
reaches `failed` or `timed-out` status without resolution means the interaction
proceeded with an unresolved authorization gap — or was correctly terminated. Both
outcomes should be traceable in the governance record.

**Agent-to-agent delegation.** The `scope-exceeded` trigger is especially important in
delegated-agent interactions where a sub-agent encounters an authority boundary it
cannot resolve autonomously. The resolution path in that case typically involves
escalation to the delegating principal, which is itself a trust decision event.

## Related artifacts

- Schema: `schemas/tsmm-agent-interaction-extension.schema.json`
- Example: `examples/agent-interaction-extension-instance.json`
- A2A binding: `docs/bindings/a2a-binding.md` *(v0.14.0)*
- Agentic AI extension: `docs/extensions/agentic-ai-extension.md`
- Extension index: `docs/extensions/index.md`
