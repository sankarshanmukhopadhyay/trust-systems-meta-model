---
owner: maintainers
last_reviewed: 2026-09-03
applicable_version: 0.24.0
tier: 2
title: Security Policy
---

# Security Policy

TSMM is a documentation-first reference model repository and does not operate a production service. Security relevance still matters because canonical semantics, examples, schemas, and guidance can influence deployed systems.

## Supported versions

Security-relevant corrections are supported for the current `v0.24.x` line. Older releases remain available for reproducibility and semantic-history review but should not be assumed to receive fixes unless a release note explicitly states otherwise.

A security correction does not silently rewrite the meaning of an already published release. If the correction changes canonical semantics or invalidates downstream assumptions, the release/judgment trail must record the compatibility and reassessment consequence.

## Reporting

If you find a security-sensitive issue in this repository, use GitHub private vulnerability reporting when available, or contact the repository maintainer privately using the contact route on the maintainer's GitHub profile. Do not open a public issue containing exploit details.

Include the affected TSMM version/concept or artifact, impact, safe reproduction or counterexample, and proposed containment where known.

## What counts as security-relevant here

Examples include:

- semantics or guidance that could cause unsafe trust decisions;
- incorrect statements about authority, delegation, revocation, verification, or evidence handling;
- examples that normalize insecure defaults;
- schema/validation behavior that contradicts the canonical model; and
- broken or misleading links to security-critical documentation.

## Authority and disclosure handling

TSMM owns canonical trust-system semantics. It does not own downstream schema serialization, implementation policy, runtime decisions, or independent certification. Security reports must be resolved at the authority layer that owns the affected proposition rather than silently transferring authority into TSMM.

Maintainers should:

1. confirm receipt;
2. classify the affected semantic/artifact authority and compatibility impact;
3. patch the affected model/docs/schema/tests as appropriate;
4. run the canonical validation gate;
5. publish release notes for material corrections; and
6. record any downstream reassessment or supersession requirement.
