---
owner: maintainers
last_reviewed: 2026-03-07
applicable_version: v0.4.0
tier: 1
---

# TSMM Trust System Threat Model

## 1. Purpose

This document defines a reusable threat and failure taxonomy for TSMM-based systems.

## 2. Threat classes

| Category | Description | Example |
|---|---|---|
| Authority misuse | Authority is over-broad, stale, abused, or exercised outside scope | over-delegation by an agent |
| Policy bypass | Required checks are skipped or routing logic is evaded | direct invocation of a privileged path |
| Artifact forgery | Artifacts or metadata are altered or spoofed | fake registry response |
| Evidence suppression | Audit records or validation outputs are hidden or missing | deleted verification log |
| Registry poisoning | Trust lists or registries are manipulated | malicious inclusion or stale metadata injection |
| Misleading signal presentation | Weak evidence is displayed as strong confidence | badge theater |
| Lifecycle drift | Revoked or expired objects continue to influence decisions | zombie credential |
| Assessment theater | Assessment exists on paper but does not govern effects | checkbox assurance |

## 3. Mapping guidance

Threats should be mapped where possible to:

- controls that mitigate them
- policy rules that govern their handling
- lifecycle triggers such as suspension or revocation
- evidence required to demonstrate safe posture

## 4. Cross-framework alignment

This taxonomy can be cross-mapped to NIST RMF, OWASP threat and control thinking, and Trust over IP ecosystem threat modeling.
