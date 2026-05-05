---
owner: maintainers
last_reviewed: 2026-05-05
applicable_version: v0.19.0
tier: 0
---


# Capability Negotiation Pattern

## Intent

Use this pattern when a requester must determine whether a discovered capability can be invoked under policy.

## Pattern

1. Read the advertised capability or skill.
2. Filter by requester visibility and policy scope.
3. Negotiate input modes, output modes, and extensions.
4. Resolve required-extension failures.
5. Bind the accepted capability to an authorization decision.
6. Emit negotiation evidence.

## Assurance note

Capability negotiation is not final authorization. It is an admissibility and compatibility gate that must be joined with policy, authority, and evidence before execution.

## Implementation artifacts

- `docs/model/capability-negotiation.md`
- `schemas/tsmm-capability-negotiation.schema.json`
- `examples/capability-negotiation-instance.json`
