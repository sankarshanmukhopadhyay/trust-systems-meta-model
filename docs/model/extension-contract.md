---
owner: maintainers
last_reviewed: 2026-05-05
applicable_version: v0.21.0
tier: 1
---

# ExtensionContract

## Concept definition

An **ExtensionContract** is a protocol-neutral abstraction for negotiated extension
compatibility. It captures the extension URI, version, requiredness, negotiated status,
and failure handling for a single extension within an interaction.

The abstraction generalizes across any extension-carrying protocol: A2A's extension
mechanism, MCP's capability extensions, OpenID Federation extension URIs, and any
protocol where two parties must agree on optional or required capabilities before an
interaction can proceed at a defined capability level.

## Trust significance

Extension negotiation is a governance surface that is frequently treated as a transport
or compatibility detail. TSMM models it as trust-significant for one primary reason:
**silent downgrade**.

When a required extension cannot be negotiated, the interaction proceeds at a reduced
capability level. If that reduction is not recorded, the governance record reflects a
capability that was not actually available. This creates an audit gap: the record shows
that an interaction occurred under certain conditions, but the conditions that actually
governed the interaction were different.

ExtensionContract makes the negotiation record explicit and auditable:

- Was the extension required or optional?
- What was the negotiated outcome?
- If the extension was reduced or rejected, how was that handled?
- Why did the negotiation reach its outcome?

A `degraded` status (capability reduction without full rejection) is particularly
important to record. It signals that the interaction proceeded but at a reduced
governance coverage level.

## Relationship to existing TSMM abstractions

| TSMM abstraction | Relationship |
|---|---|
| `InteractionContext` | ExtensionContracts are established at session open and are part of the session's governance envelope |
| `TrustDecision` | Extension availability affects what a trust decision can evaluate. A trust decision that assumed a required extension was available, when it was actually degraded, has an unrecorded dependency. |
| `Evidence` | The `resolutionRecord` in an ExtensionContract is evidence of the negotiation outcome |
| `LifecycleEvent` | Extension rejection or degradation may trigger a lifecycle event in the interaction |

## Key properties

| Property | Required | Description |
|---|---|---|
| `id` | Yes | Unique identifier |
| `extensionUri` | Yes | Versioned URI identifying the extension |
| `version` | Yes | Extension version |
| `requiredness` | Yes | `required` or `optional` |
| `negotiatedStatus` | Yes | `accepted`, `degraded`, `rejected`, or `not-attempted` |
| `failureHandling` | Yes | `abort`, `warn`, or `continue` |
| `resolutionRecord` | No | Record of why the negotiation reached its current status |

## Negotiated status semantics

| Status | Meaning |
|---|---|
| `accepted` | Both parties support the extension at the requested version |
| `degraded` | One or both parties support a reduced form of the extension (different version, partial capability) |
| `rejected` | One or both parties do not support the extension |
| `not-attempted` | Negotiation was not initiated for this extension in this session |

## Design notes

**Required extensions with `failed` negotiation must abort or be explicitly recorded.**
If an extension is marked `required` and negotiation fails, the `failureHandling`
property must be set to `abort` unless there is a governance-justified reason to
continue. Continuing a required-extension interaction under a `rejected` or `degraded`
status with `failureHandling: continue` should produce an explicit governance record.

**URI versioning.** Extension URIs should carry version information so that the
negotiation record is unambiguous about which version was negotiated, accepted, or
rejected.

## Related artifacts

- Schema: `schemas/tsmm-agent-interaction-extension.schema.json`
- Example: `examples/agent-interaction-extension-instance.json`
- A2A binding: `docs/bindings/a2a-binding.md` *(v0.14.0)*
- Extension index: `docs/extensions/index.md`
