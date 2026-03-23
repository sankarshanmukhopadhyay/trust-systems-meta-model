---
owner: maintainers
last_reviewed: 2026-03-23
applicable_version: v0.13.0
tier: 1
---

# InteractionContext

## Concept definition

An **InteractionContext** is a session or conversation scope that groups tasks,
messages, and trust decisions into a shared governance envelope. It models the
accumulated governance state across a sequence of agent interactions — specifically:
what authority remains in force, what evidence has already been established, and
under what conditions re-authorization is required.

InteractionContext extends `ExecutionContext` to the session level. Where
`ExecutionContext` captures the operational parameters of a single action or event,
`InteractionContext` captures the governance history and forward-carrying state across
an entire multi-turn exchange.

## Trust significance

Trust decisions in multi-step agent workflows are not independent. What was established,
authorized, or denied in turn 1 constrains what can be assumed in turn 3. Without an
explicit model of session-level governance state, implementations must either:

- Re-verify everything on every turn (expensive, often infeasible for long sessions), or
- Silently inherit context with no governance record (creates accountability gaps)

InteractionContext makes the third option explicit: selected authority and evidence
objects carry forward with a documented scope and re-authorization policy. This means:

- `inheritedAuthorityRefs` — authorities established earlier in the session that remain
  in force without re-verification
- `inheritedEvidenceRefs` — evidence objects from earlier turns that carry forward
- `reAuthorizationPolicy` — the conditions under which inherited authority is
  insufficient and a new trust decision must be produced

The `reAuthorizationPolicy` is especially important. It encodes the governance boundary
between inherited trust and fresh evaluation, preventing unbounded session inheritance
from eroding the trust decision chain.

## Relationship to existing TSMM abstractions

| TSMM abstraction | Relationship |
|---|---|
| `ExecutionContext` | InteractionContext is the session-level complement. ExecutionContext is per-event; InteractionContext is per-session. They coexist — each action within a session still carries its own ExecutionContext. |
| `Authority` | `inheritedAuthorityRefs` reference authority objects from the core model that remain active within this session |
| `Evidence` | `inheritedEvidenceRefs` reference evidence objects already established in this session |
| `TrustDecision` | Trust decisions produced within a session should reference the active InteractionContext so the governance envelope for the session is traceable |
| `AuthorizationCheckpoint` | When inherited authority proves insufficient for a requested action, an AuthorizationCheckpoint is raised referencing this context |

## Key properties

| Property | Required | Description |
|---|---|---|
| `id` | Yes | Unique identifier |
| `initiatorRef` | Yes | The entity that opened this interaction context |
| `participantRefs` | Yes | All entities participating in this session |
| `inheritedAuthorityRefs` | No | Authorities from this session that remain in force |
| `inheritedEvidenceRefs` | No | Evidence from earlier in the session that carries forward |
| `reAuthorizationPolicy` | No | Conditions under which re-authorization is required despite inherited authority |
| `createdAt` | Yes | Session open timestamp |
| `expiresAt` | No | Session expiry |
| `terminationReason` | No | Recorded when the context is closed |

## Design notes

**Not a conversation store.** InteractionContext is not a message log or task history.
It is a governance artifact: a record of what trust state persists across turns and
under what conditions it can be relied upon. Message content, task artifacts, and
execution traces are managed by the implementation layer.

**Expiry is governance-significant.** A session with an `expiresAt` value must treat
that expiry as a governance boundary, not just a timeout. After expiry, inherited
authority and evidence cannot be used without re-verification.

**Multi-party sessions.** `participantRefs` may include more than two parties. In
multi-agent coordination scenarios, a single InteractionContext may span a chain of
delegating and sub-delegating agents, each contributing authority and evidence into
the shared governance envelope.

## Related artifacts

- Schema: `schemas/tsmm-agent-interaction-extension.schema.json`
- Example: `examples/agent-interaction-extension-instance.json`
- A2A binding: `docs/bindings/a2a-binding.md` *(v0.14.0)*
- Extension index: `docs/extensions/index.md`
