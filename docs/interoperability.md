---
title: Interoperability
---
# Interoperability

The flagship stack separates semantic authority, portable contracts, and executable governance:

```text
TSMM semantic requirement
        ↓
TIS portable contract
        ↓
TGA governance pattern or implementation composition
        ↓
Validation evidence and assurance conclusion
```

## Required distinctions

- **Semantic alignment** means two artifacts express compatible concepts.
- **Schema compatibility** means an instance validates against an agreed contract.
- **Behavioral interoperability** requires compatible runtime expectations, not only matching fields.
- **Conformance** is evaluated against a declared profile.
- **Certification** requires an authorized external process and is not produced by these repositories.

Cross-repository relationships are declared in `data/portfolio-relationships.json` and checked by `scripts/validate_portfolio_relationships.py`.
