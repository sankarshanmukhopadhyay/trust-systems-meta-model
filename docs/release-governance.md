# TSMS release codename governance

TSMS stack releases use a repository-local codename pool derived from the Simple English Wikipedia **List of Indian state fruits**. The external page is provenance, not a runtime dependency.

## Authority

The stack release ID/tag is authoritative. The codename is human-readable release metadata. This mechanism coordinates TSMS release presentation only and does not transfer TSMM semantic authority, TIS portable-contract authority, or TGA executable-governance authority.

## Machine-readable state

- `config/release-codenames.txt` — reviewed eligible names.
- `config/release-codename-policy.json` — provenance and selection rules.
- `config/release-codename-history.json` — immutable binding of release IDs to codenames, with `candidate` or `published` state.
- `scripts/release_codenames.py` — validator/selector/persistence helper.

## Lifecycle

```text
capability boundary
  ↓
release candidate ID
  ↓
select unused name from pinned pool
  ↓
persist candidate binding in repository history
  ↓
review + executable assurance evidence
  ↓
explicit human acceptance of ID + codename + evidence
  ↓
Actions revalidates policy and release gates
  ↓
publish tag/GitHub Release
  ↓
mark/retain published binding
```

Use `python3 scripts/release_codenames.py validate` to validate the pool/policy/history. To propose a future candidate, run `python3 scripts/release_codenames.py select --version <release-id> --write` on a branch and review the resulting history change through a PR before release acceptance.

## Invariants

1. Wikipedia is never fetched during release publication.
2. Pool entries are unique case-insensitively and source-attributed.
3. An unused codename is selected while unused names remain.
4. Reuse is forbidden unless policy is explicitly changed through review.
5. A release ID already bound to a codename is idempotent; it cannot silently acquire a different name.
6. Selection is persisted before human release acceptance.
7. Green CI alone does not authorize publication.

`tsms-stack-2026.1 — Cashew-Nut` is retained as historical published state.
