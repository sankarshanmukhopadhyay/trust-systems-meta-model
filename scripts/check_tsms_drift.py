#!/usr/bin/env python3
import argparse, datetime, json, pathlib, re, sys, urllib.error, urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
SHA_RE = re.compile(r"^[0-9a-f]{40}$")


def load_json(path):
    return json.loads(pathlib.Path(path).read_text())


def classify(baseline, current):
    if current.get("remoteEvidenceStatus") != "available":
        return "INDETERMINATE", ["authoritative remote state unavailable or unverifiable"]
    if current.get("id") != baseline.get("id") or current.get("repository") != baseline.get("repository"):
        return "UNSUPPORTED", ["component identity or repository is outside baseline contract"]
    if current.get("role") != baseline.get("role"):
        return "REVIEW_REQUIRED", ["authority role changed"]
    commit = str(current.get("commit", ""))
    if not SHA_RE.fullmatch(commit):
        return "UNSUPPORTED", ["current commit is not an immutable SHA"]
    if current.get("version") != baseline.get("version"):
        return "REVIEW_REQUIRED", ["component version changed"]
    if commit != baseline.get("commit"):
        return "REVIEW_REQUIRED", ["same-version commit drift detected"]
    return "UNCHANGED", []


def fetch_github_state(component, timeout=10):
    repo = component["repository"]
    request = urllib.request.Request(
        f"https://api.github.com/repos/{repo}/commits/main",
        headers={"Accept": "application/vnd.github+json", "User-Agent": "tsms-drift-check"},
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            payload = json.load(response)
        commit = payload.get("sha")
        return {
            "id": component["id"],
            "repository": repo,
            "version": component["version"],
            "commit": commit,
            "role": component["role"],
            "remoteEvidenceStatus": "available" if SHA_RE.fullmatch(str(commit or "")) else "unavailable",
        }
    except (OSError, urllib.error.URLError, json.JSONDecodeError) as exc:
        return {
            "id": component["id"], "repository": repo, "version": component["version"],
            "commit": None, "role": component["role"], "remoteEvidenceStatus": "unavailable",
            "error": type(exc).__name__,
        }


def main():
    parser = argparse.ArgumentParser(description="Compare TSMS authoritative state with an accepted immutable baseline receipt.")
    parser.add_argument("--receipt", default=str(ROOT / "model/tsms-baseline-receipt.json"))
    parser.add_argument("--current-state", help="Fixture/current-state JSON. If omitted, GitHub main commit state is queried.")
    parser.add_argument("--output", default=str(ROOT / "artifacts/validation/tsms-drift.json"))
    args = parser.parse_args()

    receipt = load_json(args.receipt)
    baselines = {c["id"]: c for c in receipt.get("components", [])}
    if args.current_state:
        supplied = load_json(args.current_state)
        current_states = supplied.get("components", supplied if isinstance(supplied, list) else [])
    else:
        current_states = [fetch_github_state(c) for c in receipt.get("components", [])]

    current_by_id = {c.get("id"): c for c in current_states}
    results = []
    for cid, baseline in baselines.items():
        current = current_by_id.get(cid)
        if current is None:
            current = {"id": cid, "repository": baseline["repository"], "remoteEvidenceStatus": "unavailable"}
        disposition, reasons = classify(baseline, current)
        results.append({
            "component": cid, "repository": baseline["repository"],
            "baselineVersion": baseline["version"], "baselineCommit": baseline["commit"], "baselineRole": baseline["role"],
            "currentVersion": current.get("version"), "currentCommit": current.get("commit"), "currentRole": current.get("role"),
            "remoteEvidenceStatus": current.get("remoteEvidenceStatus"), "disposition": disposition, "reasons": reasons,
        })

    known = set(baselines)
    for current in current_states:
        if current.get("id") not in known:
            results.append({"component": current.get("id"), "repository": current.get("repository"), "disposition": "UNSUPPORTED", "reasons": ["unknown component"]})

    precedence = {"UNCHANGED": 0, "REVIEW_REQUIRED": 1, "UNSUPPORTED": 2, "INDETERMINATE": 3}
    overall = max((r["disposition"] for r in results), key=lambda x: precedence[x], default="INDETERMINATE")
    output = {
        "profile": "tsms-remote-drift", "baselineReceipt": receipt.get("receiptId"), "overallDisposition": overall,
        "results": results, "executedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "assuranceRule": "Only evidenced exact state is UNCHANGED; unavailable evidence never becomes PASS."
    }
    out_path = pathlib.Path(args.output); out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(output, indent=2) + "\n")
    print(f"TSMS drift disposition: {overall}")
    return 0 if overall == "UNCHANGED" else 2


if __name__ == "__main__":
    sys.exit(main())
