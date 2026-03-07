---
owner: maintainers
last_reviewed: 2026-03-07
applicable_version: v0.5.0
tier: 1
---

# Trust Registry Pattern

## Pattern summary

A registry operator publishes metadata or trust assertions that relying parties consume under policy.

## TSMM mapping

- Actor: registry operator, relying party
- Authority: publish registry metadata
- Artifact: metadata document or signed response
- Policy: reliance policy
- Evidence: conformance report or validation log
- Effect: show, suppress, gate, or route a result

## Sequence

```text
Registry operator -> publishes signed metadata -> relying party verifies -> policy evaluates -> trust decision -> bounded reliance effect
```
