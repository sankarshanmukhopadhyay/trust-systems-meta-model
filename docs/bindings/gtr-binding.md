---
owner: maintainers
last_reviewed: 2026-05-05
applicable_version: v0.20.0
tier: 2
---

# GTR GRID/DIA Binding

The GTR GRID/DIA binding shows how TSMM can model the Global Trust Registry initiative as an effect-centered trust system. The binding is intentionally practical: it translates the GTR vocabulary of Authoritative Registrars, GRID records, Digital Identity Anchors, legal mandates, public keys, lifecycle status, and verification results into TSMM primitives that can be documented, validated, audited, and eventually tested.

This binding does **not** claim that TSMM certifies a GTR implementation. It provides a portable modeling surface for architects, governance engineers, implementers, assurance teams, and relying parties.

## Binding artifacts

| Artifact | Purpose |
| --- | --- |
| `bindings/gtr/tsmm-gtr-binding.json` | Machine-readable TSMM binding declaration |
| `bindings/gtr/constraints.json` | Assumptions, prohibited inferences, and required artifacts |
| `docs/crosswalks/gtr-grid-dia-crosswalk.md` | Human-readable GTR to TSMM crosswalk |
| `examples/systems/gtr-grid-dia-system.json` | System graph for GRID/DIA trust flow |
| `examples/gtr/gtr-authority-graph-example.json` | Authority and delegation graph |
| `examples/gtr/gtr-dia-verification-decision-receipt.json` | DIA verification decision receipt |
| `examples/gtr/gtr-registrar-lifecycle-event.json` | Registrar lifecycle and revocation model |

## Core interpretation

TSMM models GTR as a **discovery, verification, and reliance system**, not merely as a directory.

GRID makes registrar trust material discoverable. DIA gives Authoritative Registrars a credential mechanism for issuing digital identity anchors. TSMM describes the governance logic that decides whether discovered and verified material is sufficient for a relying-party effect.

The effect-centered question is:

> Is this registrar, credential, key, endpoint, or status assertion authoritative enough, current enough, and evidenced enough to allow this specific operational effect?

## Primary TSMM mappings

| GTR concept | TSMM primitive | Modeling rationale |
| --- | --- | --- |
| Global Trust Registry initiative | TrustDomain | Overall institutional and technical trust domain |
| GRID | TrustRegistry | Curated discovery surface for registrar metadata and trust material |
| GRID Board or administering UN body | GovernanceAuthority | Defines eligibility, policy, standards, and approval pathways |
| Technical Operator / Harvester | RegistryService | Operates harvesting, validation, publication, and release services |
| Authoritative Registrar | Issuer | Issues DIA only within a bounded legal mandate and register scope |
| Registered Entity / DIA holder | Subject | Entity represented by registrar-issued claims and DID binding |
| Digital Identity Anchor | Credential | Credential artifact that carries legal identity assertions and DID binding |
| Registrar mandate and eligibility rules | Policy | Scope, participation, and reliance constraints |
| GRID record and verification material | EvidenceBundle | Evidence supporting authority, key control, lifecycle, and freshness |
| Verifier / relying party | RelyingParty | Consumes evidence to make a trust decision |
| Verification result | TrustDecision | Outcome of applying policy to credential and discovery evidence |
| Onboarding, warning, rejection, review | Effect | Operational consequence admitted or blocked by the decision |

## Non-technical value

For policy and governance audiences, the binding makes GTR easier to explain and defend:

- It preserves **sovereign authority** by modeling GRID as discovery metadata rather than ownership of national register data.
- It clarifies **institutional responsibility** by separating governance authority, legal registrar authority, technical operation, credential issuance, verification, and reliance.
- It improves **auditability** by requiring evidence references for authority, signature checks, lifecycle state, revocation state, and relying-party decisions.
- It supports **inclusive maturity** by allowing baseline listing, signed harvested metadata, and DIA issuance to be modeled as different capability levels.
- It avoids overclaiming by treating GRID recognition as a discovery and transparency signal, not as general certification or endorsement.

## Technical model

A conformant GTR TSMM model should include:

1. **Authority graph**
   - authority source
   - registrar mandate
   - register scope
   - delegation to technical operators or publication services
   - revocation semantics

2. **Discovery governance**
   - GRID record source
   - metadata integrity requirement
   - public key and DID material
   - freshness policy
   - failure behavior for stale, missing, or unverifiable material

3. **DIA verification decision receipt**
   - DIA subject
   - registrar issuer
   - GRID entry version
   - policy references
   - evidence references
   - revocation state
   - decision outcome
   - admitted or blocked effect

4. **Lifecycle and revocation model**
   - registrar admission
   - active participation
   - signed metadata publication
   - key rotation
   - suspension
   - withdrawal
   - revocation
   - archival evidence

## Assurance implications

A GTR implementation modeled with TSMM should be able to produce the following evidence:

| Control question | Evidence expected |
| --- | --- |
| Is the registrar legally authoritative? | Legal mandate or official designation reference |
| Is the GRID entry current? | GRID release version, timestamp, freshness metadata |
| Is the metadata authentic? | Signature, key identifier, signed commit, or equivalent integrity evidence |
| Is the registrar in scope? | Jurisdiction and register-type scope declaration |
| Is the DIA issuer authorized? | GRID record, issuer key state, and registrar lifecycle status |
| Is the credential still usable? | Expiry, status, and revocation checks |
| What did the verifier decide? | Decision receipt with policy, evidence, outcome, and effect |
| What happens after suspension or withdrawal? | Lifecycle event and downstream reliance behavior |

## Adoption posture

This binding is marked **experimental** because it is a modeling and assurance scaffold for a developing ecosystem. It is suitable for:

- architectural analysis,
- GTR and GRID policy review,
- trust flow documentation,
- assurance profile design,
- decision-receipt prototyping,
- implementation planning,
- crosswalks with trust registry and credential-verification systems.

It should not be used as a final conformance profile until GTR-specific rules, schemas, status semantics, and operating procedures are bound to testable validation artifacts.
