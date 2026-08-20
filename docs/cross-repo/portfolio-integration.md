---
owner: maintainers
last_reviewed: 2026-08-20
applicable_version: 0.24.0
tier: 1
title: Portfolio Integration Contract
permalink: /cross-repo/portfolio-integration.html
parent: Cross-Repository Alignment
grand_parent: Documentation
---
# Portfolio Integration Contract

The portfolio relationship model acts as the governed topology for repository relationships. TSMM contributes canonical meaning; TIS contributes portable machine contracts; the portfolio repository decides which relationships actually exist.

This separation prevents authority loops. Local repository relationship contracts are assertions used for drift detection, not competing sources of portfolio truth.

## Evidence

`make validate` checks semantic identifiers, the TIS projection, repository relationship structure, and release-version consistency, and emits `artifacts/validation/latest.json`.
