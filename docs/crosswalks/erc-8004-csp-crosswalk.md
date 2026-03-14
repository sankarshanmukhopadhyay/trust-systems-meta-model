---
owner: maintainers
last_reviewed: 2026-03-14
applicable_version: v0.10.0
tier: 1
---

# TSMM Crosswalk: ERC-8004-CSP

## Purpose

This document maps the **ERC-8004 Consumer Security Profile (CSP)** to the Trust Systems Meta Model (TSMM).

## Center of gravity

Within TSMM terms, ERC-8004-CSP is primarily about:

- consumer-side signal interpretation
- safe metadata fetching and validation
- integrity and context checks
- profile-guided handling of trust cues
- preventing misleading trust presentation or badge theater

Its center of gravity is therefore **consumer-side trust signal evaluation**.

## Crosswalk table

| TSMM concept | ERC-8004-CSP instantiation |
|---|---|
| **Governance Context** | local wallet, marketplace, explorer, or directory operating context |
| **Profile** | consumer-side security profile for ERC-8004 signal handling |
| **Requirement** | conformance checklist items and level-specific expectations |
| **Entity** | wallet, explorer, marketplace, indexer, agent directory, user-facing client |
| **Role** | consumer, validator, presenter, scorer |
| **Authority** | authority to interpret, weight, surface, suppress, or gate ERC-8004 trust signals according to local policy |
| **Artifact** | fetched metadata, trust signals, policy file, conformance checklist, test case suite |
| **Claim** | integrity of fetched data, meaning of a reputation signal, validator scope, finality status, transfer or control state |
| **Policy** | local acceptance rules governing trust signal handling |
| **Control** | safe-fetch sandbox, hash verification, transfer/control-change UX, scoring and weighting logic, validator policy checks |
| **Threat** | badge theater, unsafe fetching, Sybil-amplified reputation distortion, misleading validation, stale or weak finality assumptions |
| **Evidence** | validation logs, checklist outputs, test execution results, policy configuration |
| **Assessment** | conformance-level evaluation against consumer-side requirements |
| **Verification** | integrity checking, safe-fetch enforcement, validator and finality evaluation, conformance testing |
| **Level Framework** | L0-L4 conformance levels from demo parsing to economically secured consumption |
| **Trust Decision** | show, suppress, downgrade, warn, or require stronger validation before presenting trust cues |
| **Effect** | end users and systems receive or are denied specific trust signals, warnings, or action affordances |
| **Lifecycle Event** | metadata refresh, ownership transfer, validator change, policy update, signal expiry, reassessment |

## Practical takeaway

Projects that are not implementing ERC-8004 directly can still reuse the CSP pattern through TSMM by adopting the following generic structure:

- treat trust signals as claims, not truth
- require local policy for interpretation
- package consumer expectations into a profile
- assess conformance levels against explicit requirements
- tie evaluation outcomes to real presentation or action effects
