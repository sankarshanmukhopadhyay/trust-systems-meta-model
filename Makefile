PYTHON ?= python3
.PHONY: validate
validate:
	$(PYTHON) scripts/validate_all.py

.PHONY: candidate-check
candidate-check:
	python scripts/validate_all.py
	python scripts/validate_mermaid.py
	python scripts/write_candidate_evidence.py
