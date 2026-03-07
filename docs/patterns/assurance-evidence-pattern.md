---
owner: maintainers
last_reviewed: 2026-03-07
applicable_version: v0.5.0
tier: 1
---

# Assurance Evidence Pattern

## Pattern summary

A system packages evidence so that assessments and trust decisions can be traced to concrete supporting material.

## TSMM mapping

- Requirement: expected control or posture condition
- Control: safeguard linked to threat
- Evidence: logs, reports, signed attestations, review records
- Assessment: structured evaluation of requirement satisfaction
- Trust decision: acceptance, warning, review, or denial
- Effect: reliance, downgrade, remediation, or escalation

## Sequence

```text
Requirement -> control implementation -> evidence capture -> assessment -> trust decision -> operational effect and review trail
```
