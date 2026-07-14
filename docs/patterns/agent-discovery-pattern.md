---
owner: maintainers
last_reviewed: 2026-05-05
applicable_version: v0.22.0
tier: 0
---


# Agent Discovery Pattern

## Intent

Use this pattern when an implementation needs to discover an agent, service, registry, or governed endpoint and make the discovery decision auditable.

## Problem

Agent ecosystems often treat discovery as a simple metadata lookup. That is insufficient for enterprise use. Discovery creates the first relying-party assumption about who a service is, what it claims to do, what authority it may have, and whether its descriptor can be trusted.

## Pattern

1. Fetch or receive the descriptor.
2. Identify the discovery mode and source.
3. Verify descriptor integrity where required.
4. Evaluate access and freshness policy.
5. Record discovery evidence.
6. Deny, warn, review, or proceed based on failure behavior.

## Implementation artifacts

- `docs/model/discovery-governance.md`
- `schemas/tsmm-discovery-governance.schema.json`
- `examples/agent-discovery-governance-instance.json`
