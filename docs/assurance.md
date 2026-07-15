---
title: Assurance
---
# Assurance

Repository validation demonstrates that published artifacts conform to the repository's declared schemas, structural rules, documentation controls, and authority boundaries. It does not establish legal validity, production security, factual truth of supplied evidence, or independent certification.

## Evidence produced

Run `make validate`. The command executes the repository-owned validation suite and writes `artifacts/validation/latest.json` with the checks executed, pass/fail state, repository version, and limitations.

## Assurance boundaries

- **Structural assurance:** schemas, examples, references, and required metadata validate.
- **Governance assurance:** repository authority, lifecycle, and relationship declarations are complete and non-conflicting.
- **Documentation assurance:** active documentation identifies current posture and resolves internal references.
- **Non-claims:** validation is not external certification and does not prove the truth of operational claims.
