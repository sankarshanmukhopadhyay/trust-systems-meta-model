---
owner: maintainers
last_reviewed: 2026-05-05
applicable_version: v0.22.0
tier: 1
---


# TSMM Roadmap

This roadmap is directional. It is not a delivery schedule. TSMM evolves through additive, testable model surfaces that can be adopted independently and promoted based on evidence.

## Current release line

**v0.21.0 — Executable Binding Assurance and Catalog Completeness** is the current release line. It makes the published binding and graph catalog an enforceable assurance surface through:

- complete machine-readable binding contracts
- binding maturity and publication-status alignment
- catalog-wide binding and graph validation
- reproducible local validation dependencies

The v0.19.0 agent-interaction release added candidate governance surfaces for:

- discovery governance
- descriptor integrity and freshness
- authenticated extended descriptor disclosure
- capability and extension negotiation
- task state evidence lifecycle
- A2A-class binding refresh
- validation and documentation staleness hardening

## Candidate near-term increments

1. **Descriptor signing and registry publication profile**
   - Define a stronger descriptor-integrity publication profile.
   - Add examples for signed descriptor bundles and registry-mediated descriptor attestations.

2. **Human review and redress hooks**
   - Bind task lifecycle transitions to review, challenge, appeal, or rollback events.
   - Extend decision receipts with contestability metadata where appropriate.

3. **Cross-protocol agent registry comparison**
   - Compare A2A-class discovery with OpenID Federation, TRQP registry discovery, and enterprise catalog patterns.
   - Add portability notes for registry-mediated agent ecosystems.

4. **Evidence bundle packaging**
   - Define a lightweight packaging model for discovery, negotiation, runtime decision, and task lifecycle evidence.
   - Align with downstream assurance and conformance suites where available.

## Experimental surfaces

- Agent role taxonomy
- Attention governance
- ODRL policy expression alignment
- AIS-1 and bonded agent identity concepts
- HAVID high-assurance identifier binding
- Agent Governance Toolkit crosswalk

## Promotion criteria

A TSMM surface should move toward stable status only when it has:

- documentation
- JSON/YAML schema where applicable
- at least one valid example
- at least one invalid conformance vector where applicable
- validation coverage
- binding or crosswalk notes when derived from an external ecosystem
- freshness metadata aligned to the current release

## Out of scope

TSMM does not define an agent wire protocol, a wallet protocol, a registry API, a credential format, or an implementation runtime. It defines the governance semantics and model surfaces needed to compare, bind, and assure those systems.
