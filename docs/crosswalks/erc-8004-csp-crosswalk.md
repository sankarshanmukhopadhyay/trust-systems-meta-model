# TSMM Crosswalk: ERC-8004-CSP

## Purpose

This document maps the **ERC-8004 Consumer Security Profile (CSP)** to the Trust Systems Meta Model (TSMM).

The goal is to show how ERC-8004-CSP expresses a consumer-side trust evaluation system that fits the TSMM abstractions.

ERC-8004-CSP publicly presents itself as a consumer-side security profile for wallets, agent directories, marketplaces, explorers, and indexers, with a human-readable profile, policy schema, conformance checklist, test cases, threat model, architecture guidance, and L0-L4 conformance levels.

## Center of gravity

Within TSMM terms, ERC-8004-CSP is primarily about:

- consumer-side signal interpretation
- safe metadata fetching and validation
- integrity and context checks
- conformance-guided handling of trust cues
- preventing misleading trust presentation or badge theater

Its center of gravity is therefore **consumer-side trust signal evaluation**.

## Crosswalk table

| TSMM concept | ERC-8004-CSP instantiation |
|---|---|
| **Entity** | wallet, explorer, marketplace, indexer, agent directory, user-facing client |
| **Role** | consumer, validator, presenter, scorer |
| **Authority** | authority to interpret, weight, surface, suppress, or gate ERC-8004 trust signals according to local policy |
| **Artifact** | fetched metadata, trust signals, policy file, conformance checklist, test case suite |
| **Claim** | integrity of fetched data, meaning of a reputation signal, validator scope, finality status, transfer or control state |
| **Policy** | example-policy.json and related local acceptance rules governing trust signal handling |
| **Control** | safe-fetch sandbox, hash verification, transfer/control-change UX, scoring and weighting logic, validator policy checks |
| **Threat** | badge theater, unsafe fetching, Sybil-amplified reputation distortion, misleading validation, stale or weak finality assumptions |
| **Evidence** | validation logs, checklist outputs, test execution results, policy configuration |
| **Verification** | integrity checking, safe-fetch enforcement, validator and finality evaluation, conformance testing |
| **Level Framework** | L0-L4 conformance levels from demo parsing to economically secured consumption |
| **Trust Decision** | show, suppress, downgrade, warn, or require stronger validation before presenting trust cues |
| **Effect** | end users and systems receive or are denied specific trust signals, warnings, or action affordances |
| **Lifecycle Event** | metadata refresh, ownership transfer, validator change, policy update, signal expiry, reassessment |

## Interpretation notes

### 1. CSP is not just about parsing
The repo frames L0 as basic parsing and builds upward through safe fetch, integrity checks, Sybil-aware handling, validation meaning, and stronger economic security expectations.

That maps neatly into TSMM as a **Level Framework** linked to increasingly strong **Verification**, **Control**, and **Effect** discipline.

### 2. Consumer policy is the decisive layer
In TSMM terms, ERC-8004-CSP demonstrates that trust signals should not be consumed raw. They should be evaluated under local policy.

That is one of the most reusable lessons in the whole stack.

### 3. CSP is effect-centered by design
The practical consequence is not merely whether a signal exists. The consequence is whether a user interface, wallet, or marketplace should:

- show the signal
- suppress the signal
- contextualize the signal
- warn about the signal
- or block an action that depends on the signal

That makes ERC-8004-CSP a particularly clean example of TSMM's effect-centered thesis.

### 4. CSP should not be confused with operator assurance
Unlike TSPP, which is centered on operator posture and trust-registry query infrastructure, ERC-8004-CSP is centered on the consumer side.

The difference matters. One system is about publishing authoritative trust-relevant material. The other is about consuming trust-relevant material safely.

## Compact model view

```text
Consumer Entity -> Role -> Authority to interpret signals
        |
        v
Fetched Artifacts / Signals -> Claims -> Policy Evaluation -> Trust Decision
        |                          ^             ^               |
        v                          |             |               v
   Threat Model  <---- Controls ---+---- Verification ----> User-facing Effect
        ^
        +--------------------------- Evidence -------------------+
```

## Practical takeaway

Projects that are not implementing ERC-8004 directly can still reuse the CSP pattern through TSMM by adopting the following generic structure:

- treat trust signals as claims, not truth
- require local policy for interpretation
- define consumer-side controls against fetch, integrity, and presentation risks
- use conformance levels to stage maturity
- tie evaluation outcomes to real presentation or action effects

That is the portable design pattern hiding in the repo.
