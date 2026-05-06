---
owner: maintainers
last_reviewed: 2026-05-05
applicable_version: v0.20.0
tier: 2
---

# GTR GRID/DIA Crosswalk

This crosswalk maps the Global Trust Registry, Global Registrar Information Directory, and Digital Identity Anchor vocabulary into TSMM primitives. It is designed to support implementation planning, governance review, assurance design, and future conformance testing.

## Executive summary

GTR is best modeled as a layered trust system:

1. **Governance layer**: defines participation, eligibility, standards, operating rules, and dispute paths.
2. **Authority layer**: identifies which registrars are legally authoritative for which registers and jurisdictions.
3. **Discovery layer**: publishes GRID records so verifiers can find registrar metadata, keys, endpoints, and status.
4. **Credential layer**: allows Authoritative Registrars to issue Digital Identity Anchors.
5. **Verification layer**: allows relying parties to evaluate GRID and DIA evidence.
6. **Effect layer**: admits, blocks, downgrades, warns, or routes business actions for review.

TSMM gives this stack a consistent grammar: entity, role, authority, policy, evidence, lifecycle state, verification, trust decision, and effect.

## Concept crosswalk

| GTR / GRID / DIA concept | TSMM primitive | Binding strength | Governance meaning | Technical implication |
| --- | --- | --- | --- | --- |
| Global Trust Registry | TrustDomain | Approximate | Ecosystem boundary for cross-border registrar discovery and verification | System model root and profile context |
| Global Registrar Information Directory | TrustRegistry | Approximate | Directory of authoritative registrar trust material | Curated registry with freshness, integrity, and lifecycle controls |
| GRID Board / administering body | GovernanceAuthority | Approximate | Defines eligibility, technical standards, and participation rules | Policy source and approval authority |
| Technical Operator | RegistryService | Approximate | Operates infrastructure under delegated mandate | Harvester, release manager, publication service, monitoring service |
| GRID Harvester | RegistryService | Approximate | Collects and validates registrar metadata | Schema validation, signature validation, release inclusion checks |
| UN Member State or competent authority | GovernanceAuthority | Composite | Provides or confirms national authority basis | Evidence source for registrar mandate and scope |
| Authoritative Registrar | Issuer | Composite | Legally responsible body for a register | Credential issuer and metadata publisher within scope |
| Authoritative Register | TrustRegistry | Approximate | Source register with legal effect under domestic law | External authoritative source, not copied into GRID by default |
| Register Scheme | Policy | Composite | Bounded identifier scheme or register type | Scope constraint for authority and credential claims |
| GRID Participant | Issuer / RegistryService | Composite | Admitted participant with obligations | Participant record with lifecycle state and assurance maturity |
| GRID Record | EvidenceBundle | Composite | Versioned registrar discovery record | Metadata, keys, endpoints, status, history, and release reference |
| Registrar DID / Issuer DID | EvidenceBundle | Composite | Verification material associated with registrar authority | DID document, key material, method reference, rotation state |
| Public key | EvidenceBundle | Approximate | Cryptographic evidence for metadata or DIA signatures | Key identifier, status, expiry, compromise flag, rotation path |
| Digital Identity Anchor | Credential | Approximate | Registrar-issued trust wrapper around legal identity assertions | Verifiable credential with issuer, subject, claims, DID binding, status |
| Registered Entity | Subject | Approximate | Entity represented by legal registration claims | Credential subject and DID controller |
| Verifier | Verifier | Approximate | Actor performing technical verification | Signature, status, scope, and freshness checks |
| Relying party | RelyingParty | Approximate | Actor deciding whether to act on verification result | Applies acceptance policy and records decision receipt |
| Eligibility criteria | Policy | Approximate | Rules for admission and continued participation | Validation requirements for registrar admission and updates |
| Lifecycle status | Assessment | Approximate | Active, suspended, withdrawn, revoked, expired, or archived state | Status check required before reliance |
| DIA verification result | TrustDecision | Approximate | Outcome of evidence and policy evaluation | Allow, deny, warn, downgrade, or review |
| Business action | Effect | Approximate | Consequence of relying on the decision | Onboarding, payment, shipment, compliance acceptance, or escalation |

## Authority and delegation model

The key TSMM point is that authority must be **bounded**.

A registrar may be authoritative for one jurisdiction, one register type, and one class of claims. It should not be treated as globally authoritative for all claims merely because it appears in GRID.

Minimum authority attributes:

| Attribute | Required meaning |
| --- | --- |
| Authority source | Legal instrument, official designation, or governance approval reference |
| Authority holder | Registrar or competent public authority |
| Scope | Register type, jurisdiction, identifier scheme, claim class |
| Permitted actions | Publish metadata, maintain register, issue DIA, provide status |
| Lifecycle state | Proposed, active, suspended, withdrawn, revoked, archived |
| Evidence reference | Document, signed submission, official URL, or release artifact |
| Revocation semantics | Effect of withdrawal, key compromise, or loss of mandate |

## Discovery governance model

GRID discovery should be modeled as a governed metadata flow:

```text
Registrar mandate evidence
  -> registrar admission decision
  -> GRID record publication
  -> metadata harvesting and validation
  -> GRID release
  -> verifier discovery
  -> DIA verification decision
  -> relying-party effect
```

Each step should produce evidence.

## DIA verification model

A verifier should not reduce DIA verification to signature validity. A TSMM-compatible DIA verification should check:

1. DIA signature validity.
2. Issuer discovery through GRID.
3. Registrar lifecycle state.
4. Registrar scope for the claim type.
5. Issuer key state and rotation status.
6. Credential expiry and revocation state.
7. GRID record freshness.
8. Relying-party policy for the intended effect.
9. Evidence availability for audit.

## Decision receipt model

A decision receipt should capture:

- subject reference,
- requesting actor,
- authority basis,
- policy references,
- evidence references,
- boundary crossed,
- decision outcome,
- effect admission,
- revocation state checked,
- assurance level,
- review path.

See `examples/gtr/gtr-dia-verification-decision-receipt.json`.

## Lifecycle and revocation model

A GTR lifecycle model should cover both registrar state and downstream reliance behavior.

| Trigger | State change | Relying-party consequence |
| --- | --- | --- |
| Registrar approved | Proposed to active | GRID entry can be used for discovery |
| Signed metadata accepted | Active to active with new evidence | Verifiers use new release and key material |
| Metadata stale | Active to suspended or review | New decisions warn or route to review |
| Key compromise | Active to suspended | New DIA verification should deny or review |
| Authority withdrawn | Active to revoked | New reliance should be blocked |
| Participant withdrawal | Active to withdrawn or revoked | GRID removes active discoverability |
| Credential expiry | Active credential to expired | DIA should not admit new effect |
| Revocation notice | Active credential to revoked | New reliance should be denied |

## Testing implications

A future GTR conformance profile can test:

- registrar admission records include authority evidence and scope,
- GRID records include lifecycle state and verification material,
- metadata publication has integrity evidence,
- stale or unverifiable records produce defined failure behavior,
- DIA verification checks issuer authority and not only credential signature,
- decision receipts are produced for relying-party effects,
- suspension and revocation change downstream decision outcomes,
- archived releases remain available for evidence reconstruction.

## Prohibited shortcuts

The following are explicitly out of scope for the TSMM interpretation:

- treating GRID recognition as general certification,
- treating signature validation as sufficient reliance,
- treating the GRID operator as controller of national register data,
- assuming a DIA changes the legal status of the subject,
- allowing cached discovery material to admit high-impact effects without freshness checks.
