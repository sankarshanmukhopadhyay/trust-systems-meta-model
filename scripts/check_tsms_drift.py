#!/usr/bin/env python3
import argparse, datetime, hashlib, json, pathlib, re, sys, urllib.error, urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
SHA_RE = re.compile(r"^[0-9a-f]{40}$")
DECLARATIONS = {
    "tsmm": {"versionPath": "VERSION", "declarationPath": "model/tsms-stack.json", "versionField": None, "rolePath": ["candidateBaseline", "components"], "roleKey": "tsmm"},
    "tis": {"versionPath": "VERSION", "declarationPath": "model/tsms-compatibility.json", "versionField": "repositoryVersion", "rolePath": ["role"]},
    "tga": {"versionPath": "VERSION", "declarationPath": "examples/tsms/golden-path.json", "versionField": "tgaVersion", "roleLiteral": "executable-governance-and-implementation-layer"},
}


def load_json(path):
    return json.loads(pathlib.Path(path).read_text())


def canonical_digest(value):
    canonical = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(canonical).hexdigest()


def extract_role(component_id, declaration):
    cfg = DECLARATIONS.get(component_id)
    if not cfg:
        raise KeyError(component_id)
    if cfg.get("roleLiteral"):
        return cfg["roleLiteral"]
    if component_id == "tsmm":
        for item in declaration.get("candidateBaseline", {}).get("components", []):
            if item.get("id") == "tsmm":
                return item.get("role")
        return None
    value = declaration
    for key in cfg.get("rolePath", []):
        value = value.get(key) if isinstance(value, dict) else None
    return value


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
    if current.get("baselineDeclarationDigest") and current.get("declarationDigest") != current.get("baselineDeclarationDigest"):
        return "REVIEW_REQUIRED", ["same-version authoritative declaration drift detected"]
    if commit != baseline.get("commit"):
        return "REVIEW_REQUIRED", ["same-version commit drift detected"]
    return "UNCHANGED", []


def github_text(repo, ref, path, timeout=10):
    url = f"https://raw.githubusercontent.com/{repo}/{ref}/{path}"
    req = urllib.request.Request(url, headers={"User-Agent": "tsms-drift-check"})
    with urllib.request.urlopen(req, timeout=timeout) as response:
        return response.read().decode("utf-8")


def github_commit(repo, timeout=10):
    req = urllib.request.Request(f"https://api.github.com/repos/{repo}/commits/main", headers={"Accept": "application/vnd.github+json", "User-Agent": "tsms-drift-check"})
    with urllib.request.urlopen(req, timeout=timeout) as response:
        return json.load(response).get("sha")


def fetch_github_state(component, timeout=10):
    cid, repo = component["id"], component["repository"]
    cfg = DECLARATIONS.get(cid)
    if not cfg:
        return {"id": cid, "repository": repo, "remoteEvidenceStatus": "unsupported"}
    try:
        commit = github_commit(repo, timeout)
        current_version = github_text(repo, "main", cfg["versionPath"], timeout).strip()
        current_decl = json.loads(github_text(repo, "main", cfg["declarationPath"], timeout))
        baseline_version = github_text(repo, component["commit"], cfg["versionPath"], timeout).strip()
        baseline_decl = json.loads(github_text(repo, component["commit"], cfg["declarationPath"], timeout))
        if not SHA_RE.fullmatch(str(commit or "")) or baseline_version != component["version"]:
            raise ValueError("pinned baseline evidence does not match receipt")
        declared_version = current_decl.get(cfg["versionField"]) if cfg.get("versionField") else current_version
        if declared_version and declared_version != current_version:
            raise ValueError("VERSION and authoritative declaration disagree")
        return {
            "id": cid, "repository": repo, "version": current_version, "commit": commit,
            "role": extract_role(cid, current_decl), "remoteEvidenceStatus": "available",
            "declarationPath": cfg["declarationPath"], "declarationDigest": canonical_digest(current_decl),
            "baselineDeclarationDigest": canonical_digest(baseline_decl), "baselineVersionObserved": baseline_version,
        }
    except (OSError, urllib.error.URLError, json.JSONDecodeError, UnicodeDecodeError, ValueError, KeyError) as exc:
        return {"id": cid, "repository": repo, "version": None, "commit": None, "role": None, "remoteEvidenceStatus": "unavailable", "error": type(exc).__name__}


def main():
    parser = argparse.ArgumentParser(description="Compare independently attested TSMS authoritative state with an accepted immutable baseline receipt.")
    parser.add_argument("--receipt", default=str(ROOT / "model/tsms-baseline-receipt.json"))
    parser.add_argument("--current-state", help="Fixture/current-state JSON. If omitted, authoritative GitHub state is queried.")
    parser.add_argument("--output", default=str(ROOT / "artifacts/validation/tsms-drift.json"))
    args = parser.parse_args()
    receipt = load_json(args.receipt); baselines = {c["id"]: c for c in receipt.get("components", [])}
    if args.current_state:
        supplied = load_json(args.current_state); current_states = supplied.get("components", supplied if isinstance(supplied, list) else [])
    else:
        current_states = [fetch_github_state(c) for c in receipt.get("components", [])]
    current_by_id = {c.get("id"): c for c in current_states}; results = []
    for cid, baseline in baselines.items():
        current = current_by_id.get(cid) or {"id": cid, "repository": baseline["repository"], "remoteEvidenceStatus": "unavailable"}
        disposition, reasons = classify(baseline, current)
        results.append({"component": cid, "repository": baseline["repository"], "baselineVersion": baseline["version"], "baselineCommit": baseline["commit"], "baselineRole": baseline["role"], "currentVersion": current.get("version"), "currentCommit": current.get("commit"), "currentRole": current.get("role"), "declarationPath": current.get("declarationPath"), "baselineDeclarationDigest": current.get("baselineDeclarationDigest"), "currentDeclarationDigest": current.get("declarationDigest"), "remoteEvidenceStatus": current.get("remoteEvidenceStatus"), "disposition": disposition, "reasons": reasons})
    known = set(baselines)
    for current in current_states:
        if current.get("id") not in known:
            results.append({"component": current.get("id"), "repository": current.get("repository"), "disposition": "UNSUPPORTED", "reasons": ["unknown component"]})
    precedence = {"UNCHANGED": 0, "REVIEW_REQUIRED": 1, "UNSUPPORTED": 2, "INDETERMINATE": 3}
    overall = max((r["disposition"] for r in results), key=lambda x: precedence[x], default="INDETERMINATE")
    output = {"profile": "tsms-authoritative-remote-drift", "baselineReceipt": receipt.get("receiptId"), "overallDisposition": overall, "results": results, "executedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(), "assuranceRule": "Only independently evidenced exact state is UNCHANGED; unavailable evidence never becomes PASS."}
    out_path = pathlib.Path(args.output); out_path.parent.mkdir(parents=True, exist_ok=True); out_path.write_text(json.dumps(output, indent=2) + "\n")
    print(f"TSMS drift disposition: {overall}"); return 0 if overall == "UNCHANGED" else 2


if __name__ == "__main__":
    sys.exit(main())
