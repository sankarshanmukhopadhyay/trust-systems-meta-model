---
owner: maintainers
last_reviewed: 2026-03-09
applicable_version: v0.6.0
tier: 1
---

# Delegated Agent Pattern

## Pattern summary

A human principal delegates bounded authority to a software agent, which attempts to produce an effect on a system.

## TSMM mapping

- Actor: principal, software agent
- Authority: delegated mandate with scope and conditions
- Artifact: delegation artifact
- Policy: delegated-action policy
- Evidence: audit log and verification output
- Effect: allow, block, downgrade, or route action

## Sequence

```text
Human principal -> delegates authority -> software agent acts -> policy evaluates scope and evidence -> trust decision -> system state change or block
```
