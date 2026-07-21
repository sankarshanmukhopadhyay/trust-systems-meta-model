---
owner: maintainers
last_reviewed: 2026-05-05
applicable_version: 0.23.0
tier: 1
title: Trust Registry Pattern
permalink: /patterns/trust-registry-pattern.html
parent: Patterns
grand_parent: Documentation
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
