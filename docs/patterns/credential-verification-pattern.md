---
owner: maintainers
last_reviewed: 2026-03-14
applicable_version: v0.9.0
tier: 1
---

# Credential Verification Pattern

## Pattern summary

A verifier checks a credential, claims, and status information before relying on the result.

## TSMM mapping

- Actor: issuer, holder, verifier
- Artifact: credential and status metadata
- Claim: identity, qualification, entitlement, or status proposition
- Verification: signature, schema, status, and issuer checks
- Policy: acceptance or downgrade logic
- Effect: permit, deny, or route a downstream action

## Sequence

```text
Holder presents credential -> verifier checks artifact and status -> policy evaluates -> trust decision -> downstream access or warning effect
```
