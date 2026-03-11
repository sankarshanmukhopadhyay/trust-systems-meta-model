---
owner: maintainers
last_reviewed: 2026-03-11
applicable_version: v0.8.0
tier: 1
---

# TSMM Extensions

TSMM uses a layered strategy:

- **Core** for cross-domain invariants
- **Extensions** for recurring domain specializations
- **Profiles and crosswalks** for concrete implementation mappings

This keeps the core stable while allowing real-world application families to add concepts that are operationally important but not universal.

## Available extensions

- [Agentic AI Extension](agentic-ai-extension.md)
- [Multi-Agent Coordination Extension](../patterns/multi-agent-coordination-pattern.md) — schema: `schemas/tsmm-multi-agent-extension.schema.json`
- [Verifiable Trust Communities Extension](verifiable-trust-communities-extension.md)
- [Assurance Extension](assurance-extension.md)
- [Evidence Artifact Extension](../model/evidence-artifact.md) — schema: `schemas/tsmm-evidence-artifact-extension.schema.json`
- [Dynamic Authorization Pattern](../patterns/dynamic-authz-pattern.md) *(experimental)* — see also: [Dynamic Authorization Framing](../model/dynamic-authorization-framing.md), [XACML / ABAC Crosswalk](../crosswalks/xacml-abac-crosswalk.md)

## Promotion rule

A concept should move from an extension into the TSMM core only when repeated implementation experience shows that it is:

1. cross-domain rather than domain-bound
2. structurally necessary to explain trust decisions
3. stable enough to avoid semantic churn
4. useful even outside the originating extension
