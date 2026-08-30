#!/usr/bin/env python3
import datetime
import hashlib
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
RELEASE_ID = "tsms-stack-2026.1"
CODENAME = "Cashew-Nut"


def load(path):
    return json.loads((ROOT / path).read_text())


def sha256(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def main():
    wire_path = pathlib.Path("artifacts/e2e/TSMS-WIRE-001/wire-transaction-receipt.json")
    wire_tests_path = pathlib.Path("artifacts/e2e/TSMS-WIRE-001/pressure-tests.json")
    e2e_path = pathlib.Path("artifacts/e2e/TSMS-E2E-001/evidence-bundle.json")
    renewal_path = pathlib.Path("artifacts/e2e/TSMS-RENEWAL-001/transaction-evidence.json")
    drift_tests_path = pathlib.Path("artifacts/validation/tsms-drift-tests.json")
    baseline_path = pathlib.Path("model/tsms-baseline-receipt.json")

    required = [wire_path, wire_tests_path, e2e_path, renewal_path, drift_tests_path, baseline_path]
    for path in required:
        require((ROOT / path).exists(), f"required release evidence missing: {path}")

    wire = load(wire_path)
    wire_tests = load(wire_tests_path)
    e2e = load(e2e_path)
    renewal = load(renewal_path)
    drift_tests = load(drift_tests_path)
    baseline = load(baseline_path)

    require(wire.get("status") == "PASS", "wire transaction did not PASS")
    require(wire.get("decision") == "PERMIT", "wire transaction did not PERMIT")
    require(wire_tests.get("status") == "pass", "wire pressure tests did not pass")
    require(drift_tests.get("status") == "pass", "drift pressure tests did not pass")
    require(renewal.get("finalCompatibilityDisposition") == "RESTORED", "renewal transaction did not restore compatibility")
    require(wire.get("baselineReceipt") == baseline.get("receiptId"), "wire receipt is not bound to active accepted baseline")

    evidence = []
    for path in [wire_path, wire_tests_path, e2e_path, renewal_path, drift_tests_path, baseline_path]:
        evidence.append({"path": str(path), "sha256": sha256(path)})

    out = {
        "releaseId": RELEASE_ID,
        "codename": CODENAME,
        "status": "release-candidate-evidence-complete",
        "governingIssue": "https://github.com/sankarshanmukhopadhyay/trust-systems-meta-model/issues/19",
        "activeBaselineReceipt": baseline.get("receiptId"),
        "components": wire.get("componentEvidence", []),
        "wireTransaction": {
            "transactionId": wire.get("transactionId"),
            "status": wire.get("status"),
            "decision": wire.get("decision"),
            "executedAt": wire.get("executedAt"),
        },
        "assurance": {
            "wirePressureTests": wire_tests.get("status"),
            "driftPressureTests": drift_tests.get("status"),
            "renewalCompatibilityDisposition": renewal.get("finalCompatibilityDisposition"),
            "canonicalE2ECase": e2e.get("caseId") or e2e.get("profile"),
        },
        "evidence": evidence,
        "humanReleaseAcceptance": {
            "accepted": False,
            "actor": None,
            "acceptedAt": None,
            "scope": None,
            "rule": "CI evidence establishes release candidacy only; publication requires explicit human acceptance."
        },
        "authorityBoundary": "The stack release coordinates evidence only. TSMM retains semantic authority, TIS retains portable contract authority, and TGA retains executable governance authority.",
        "nonClaims": [
            "Green CI alone is not assurance acceptance.",
            "This release does not transfer authority among component repositories.",
            "The controlled renewal fixture is non-production unless a separately reviewed successor receipt exists."
        ],
        "generatedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    }

    out_path = ROOT / "artifacts/release/tsms-stack-2026.1.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, indent=2) + "\n")
    print(f"TSMS release candidate evidence: PASS / {RELEASE_ID} — {CODENAME}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"TSMS release candidate evidence: FAIL ({exc})")
        sys.exit(1)
