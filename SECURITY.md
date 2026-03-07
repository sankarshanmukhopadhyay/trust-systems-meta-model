---
owner: maintainers
last_reviewed: 2026-03-07
applicable_version: v0.5.0
tier: 2
---

# Security Policy

TSMM is a documentation-first reference model repository and does not operate a production service. Security relevance still matters because examples, schemas, and guidance can influence deployed systems.

## Reporting

If you find a security-sensitive issue in this repository, please report it privately to the maintainers before opening a public issue.

## What counts as security-relevant here

Examples include:

- guidance that could cause unsafe trust decisions
- incorrect statements about delegation, verification, or evidence handling
- examples that normalize insecure defaults
- broken links to security-critical documentation

## Disclosure handling

The maintainers should:

1. confirm receipt
2. assess whether the issue affects model guidance, examples, or schema
3. patch the affected docs
4. publish release notes describing the documentation-impacting correction
