#!/usr/bin/env python3
import copy, importlib.util, json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("renewal", ROOT / "scripts/run_tsms_renewal_transaction.py")
renewal = importlib.util.module_from_spec(spec); spec.loader.exec_module(renewal)
receipt = json.loads((ROOT / "model/tsms-baseline-receipt.json").read_text())
base = json.loads((ROOT / "validation/tsms/renewal/controlled-transaction.json").read_text())


def expect(name, mutate, expected_final="DENIED", required_stage=None, required_disposition=None):
    tx = copy.deepcopy(base); mutate(tx)
    transitions, final = renewal.evaluate(receipt, tx)
    if final != expected_final:
        raise AssertionError(f"{name}: expected final {expected_final}, got {final}: {transitions}")
    if required_stage and not any(t["stage"] == required_stage and (required_disposition is None or t["disposition"] == required_disposition) for t in transitions):
        raise AssertionError(f"{name}: missing {required_stage}/{required_disposition}: {transitions}")
    print(f"PASS {name}")


transitions, final = renewal.evaluate(receipt, copy.deepcopy(base))
assert final == "RESTORED", transitions
print("PASS controlled renewal restores compatibility")

expect("baseline receipt mismatch", lambda x: x.update(baselineReceipt="urn:tsms:baseline:wrong"), required_stage="baseline-binding")
expect("starting E2E failure", lambda x: x["startingE2E"].update(result="FAIL"), required_stage="starting-e2e")
expect("remote evidence unavailable", lambda x: x["drift"].update(remoteEvidenceStatus="unavailable"), required_stage="drift-detection", required_disposition="INDETERMINATE")
expect("fresh evidence absent", lambda x: x["freshEvidence"].update(references=[]), required_stage="fresh-owning-layer-evidence")
expect("wrong owning layer", lambda x: x["freshEvidence"].update(owningLayer="tga"), required_stage="fresh-owning-layer-evidence")
expect("failed layer validation", lambda x: x["freshEvidence"].update(validationConclusion="failure"), required_stage="fresh-owning-layer-evidence")
expect("human acceptance absent", lambda x: x["humanAcceptance"].update(accepted=False), required_stage="human-acceptance")
expect("invalid predecessor", lambda x: x["renewalReceipt"].update(predecessor="urn:tsms:baseline:wrong"), required_stage="renewal-lineage")
expect("renewed receipt inactive", lambda x: x["renewalReceipt"].update(activeInFixture=False), required_stage="renewal-lineage")
expect("post-renewal E2E failure", lambda x: x["postRenewalE2E"].update(result="FAIL"), required_stage="post-renewal-e2e")
expect("production receipt guardrail", lambda x: x["renewalReceipt"].update(production=True), required_stage="fixture-guardrail")
expect("no material drift", lambda x: x["drift"].update(commit=next(c["commit"] for c in receipt["components"] if c["id"] == x["drift"]["component"])), required_stage="compatibility")

print("TSMS renewal transaction pressure tests passed")
sys.exit(0)
