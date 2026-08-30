#!/usr/bin/env python3
import argparse, datetime, json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]


def load(path):
    return json.loads(pathlib.Path(path).read_text())


def classify_drift(baseline_component, drift):
    if drift.get("remoteEvidenceStatus") != "available":
        return "INDETERMINATE", "authoritative remote state unavailable"
    if drift.get("role") != baseline_component.get("role"):
        return "REVIEW_REQUIRED", "authority role changed"
    if drift.get("version") != baseline_component.get("version"):
        return "REVIEW_REQUIRED", "component version changed"
    if drift.get("commit") != baseline_component.get("commit"):
        return "REVIEW_REQUIRED", "same-version commit drift detected"
    return "UNCHANGED", "no material drift detected"


def evaluate(receipt, tx):
    components = {c["id"]: c for c in receipt.get("components", [])}
    drift = tx["drift"]
    baseline = components.get(drift.get("component"))
    transitions = []

    def record(stage, disposition, reason):
        transitions.append({"stage": stage, "disposition": disposition, "reason": reason})

    if tx.get("production") is not False or tx.get("renewalReceipt", {}).get("production") is not False:
        record("fixture-guardrail", "DENIED", "controlled transaction must not assert production receipt state")
        return transitions, "DENIED"
    record("fixture-guardrail", "PASS", "fixture explicitly non-production")

    if tx.get("baselineReceipt") != receipt.get("receiptId"):
        record("baseline-binding", "DENIED", "transaction fixture is not bound to the accepted baseline receipt")
        return transitions, "DENIED"
    record("baseline-binding", "PASS", "transaction fixture bound to accepted baseline receipt")

    start = tx.get("startingE2E", {})
    if start.get("caseId") != "TSMS-E2E-001" or start.get("result") != "PASS":
        record("starting-e2e", "DENIED", "accepted starting state must pass TSMS-E2E-001 before drift is introduced")
        return transitions, "DENIED"
    record("starting-e2e", "PASS", "accepted starting state passed TSMS-E2E-001")

    if baseline is None:
        record("baseline-resolution", "DENIED", "drift component is not in accepted baseline")
        return transitions, "DENIED"
    record("baseline-resolution", "PASS", "drift component resolved in accepted baseline")

    drift_disposition, reason = classify_drift(baseline, drift)
    record("drift-detection", drift_disposition, reason)
    if drift_disposition == "INDETERMINATE":
        record("compatibility", "DENIED", "indeterminate evidence cannot preserve or renew compatibility")
        record("renewal", "DENIED", "renewal blocked until authoritative evidence is available")
        return transitions, "DENIED"
    if drift_disposition != "REVIEW_REQUIRED":
        record("compatibility", "DENIED", "transaction fixture must exercise material drift")
        return transitions, "DENIED"

    record("compatibility", "WITHDRAWN", "accepted prior state cannot be inherited after material drift")

    evidence = tx.get("freshEvidence", {})
    if evidence.get("owningLayer") != drift.get("component") or evidence.get("validationConclusion") != "success" or not evidence.get("references"):
        record("fresh-owning-layer-evidence", "DENIED", "fresh successful owning-layer evidence is required")
        return transitions, "DENIED"
    record("fresh-owning-layer-evidence", "PASS", "fresh successful owning-layer evidence supplied")

    acceptance = tx.get("humanAcceptance", {})
    if acceptance.get("accepted") is not True or not acceptance.get("actor") or not acceptance.get("scope"):
        record("human-acceptance", "DENIED", "explicit scoped human acceptance is required")
        return transitions, "DENIED"
    record("human-acceptance", "PASS", "explicit scoped human acceptance recorded")

    renewed = tx.get("renewalReceipt", {})
    if renewed.get("predecessor") != receipt.get("receiptId") or renewed.get("activeInFixture") is not True:
        record("renewal-lineage", "DENIED", "renewal predecessor and active fixture state must resolve to the accepted baseline")
        return transitions, "DENIED"
    record("renewal-lineage", "PASS", "fixture renewal lineage is valid")

    post = tx.get("postRenewalE2E", {})
    if post.get("caseId") != "TSMS-E2E-001" or post.get("result") != "PASS":
        record("post-renewal-e2e", "DENIED", "TSMS-E2E-001 must pass against renewed fixture state")
        return transitions, "DENIED"
    record("post-renewal-e2e", "PASS", "TSMS-E2E-001 passed against renewed fixture state")
    record("compatibility-restoration", "RESTORED", "all renewal preconditions satisfied in controlled fixture")
    return transitions, "RESTORED"


def main():
    parser = argparse.ArgumentParser(description="Execute the controlled TSMS drift-to-renewal assurance transaction.")
    parser.add_argument("--receipt", default=str(ROOT / "model/tsms-baseline-receipt.json"))
    parser.add_argument("--transaction", default=str(ROOT / "validation/tsms/renewal/controlled-transaction.json"))
    parser.add_argument("--output", default=str(ROOT / "artifacts/e2e/TSMS-RENEWAL-001/transaction-evidence.json"))
    args = parser.parse_args()

    receipt = load(args.receipt)
    tx = load(args.transaction)
    transitions, final = evaluate(receipt, tx)
    evidence = {
        "profile": "tsms-drift-to-renewal-transaction",
        "caseId": "TSMS-RENEWAL-001",
        "fixtureId": tx.get("fixtureId"),
        "production": False,
        "baselineReceipt": receipt.get("receiptId"),
        "renewalReceipt": tx.get("renewalReceipt", {}).get("receiptId"),
        "executedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "transitions": transitions,
        "finalCompatibilityDisposition": final,
        "assuranceRule": "Compatibility withdrawn by material drift is restored only after fresh owning-layer evidence, explicit human acceptance, valid lineage, and successful post-renewal E2E validation."
    }
    out = pathlib.Path(args.output); out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(evidence, indent=2) + "\n")
    print(f"TSMS renewal transaction: {final}")
    return 0 if final == "RESTORED" else 2


if __name__ == "__main__":
    sys.exit(main())
