#!/usr/bin/env python3
import argparse
import json
import random
import secrets
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POOL_PATH = ROOT / "config" / "release-codenames.txt"
POLICY_PATH = ROOT / "config" / "release-codename-policy.json"
HISTORY_PATH = ROOT / "config" / "release-codename-history.json"

class PolicyError(ValueError):
    pass

def load_pool(path=POOL_PATH):
    items = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        value = raw.strip()
        if value and not value.startswith("#"):
            items.append(value)
    return items

def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))

def validate(pool=None, policy=None, history=None):
    pool = load_pool() if pool is None else pool
    policy = load_json(POLICY_PATH) if policy is None else policy
    history = load_json(HISTORY_PATH) if history is None else history
    errors = []
    if policy.get("schemaVersion") != 1:
        errors.append("policy schemaVersion must be 1")
    if history.get("schemaVersion") != 1:
        errors.append("history schemaVersion must be 1")
    if len(pool) < int(policy.get("minimumPoolSize", 5)):
        errors.append("codename pool is smaller than minimumPoolSize")
    normalized = [x.casefold() for x in pool]
    if len(normalized) != len(set(normalized)):
        errors.append("codename pool contains duplicates (case-insensitive)")
    source = policy.get("source", {})
    if not str(source.get("url", "")).startswith("https://"):
        errors.append("policy source.url must be https")
    releases = history.get("releases", [])
    versions = [r.get("version") for r in releases]
    if len(versions) != len(set(versions)):
        errors.append("history contains duplicate versions")
    pool_lookup = {x.casefold(): x for x in pool}
    names = []
    for release in releases:
        codename = release.get("codename")
        names.append(codename)
        if not codename or codename.casefold() not in pool_lookup:
            errors.append(f"history codename is not in pinned pool: {codename!r}")
        if release.get("status") not in {"candidate", "published"}:
            errors.append(f"invalid history status for {release.get('version')}")
    allow_reuse = bool(policy.get("selection", {}).get("allowReuseAfterExhaustion", False))
    if not allow_reuse:
        normalized_names = [x.casefold() for x in names if isinstance(x, str)]
        if len(normalized_names) != len(set(normalized_names)):
            errors.append("history reuses a codename while policy forbids reuse")
    if errors:
        raise PolicyError("; ".join(errors))
    return True

def select(version, *, seed=None, pool=None, policy=None, history=None):
    pool = load_pool() if pool is None else pool
    policy = load_json(POLICY_PATH) if policy is None else policy
    history = load_json(HISTORY_PATH) if history is None else history
    validate(pool, policy, history)
    for release in history["releases"]:
        if release["version"] == version:
            return release["codename"], True
    used = {r["codename"].casefold() for r in history["releases"]}
    unused = [x for x in pool if x.casefold() not in used]
    allow_reuse = bool(policy["selection"].get("allowReuseAfterExhaustion", False))
    candidates = unused if unused else (pool if allow_reuse else [])
    if not candidates:
        raise PolicyError("codename pool exhausted and reuse is forbidden")
    chosen = secrets.choice(candidates) if seed is None else random.Random(seed).choice(candidates)
    return chosen, False

def persist(version, codename, history_path=HISTORY_PATH):
    history = load_json(history_path)
    existing = next((r for r in history["releases"] if r["version"] == version), None)
    if existing:
        if existing["codename"] != codename:
            raise PolicyError("existing version is already bound to a different codename")
        return False
    history["releases"].append({"version": version, "codename": codename, "status": "candidate"})
    history_path.write_text(json.dumps(history, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return True

def main():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("validate")
    choose = sub.add_parser("select")
    choose.add_argument("--version", required=True)
    choose.add_argument("--seed")
    choose.add_argument("--write", action="store_true")
    args = parser.parse_args()
    if args.command == "validate":
        validate()
        print("release codename policy: PASS")
        return
    codename, existing = select(args.version, seed=args.seed)
    if args.write:
        persist(args.version, codename)
        validate()
    print(json.dumps({"version": args.version, "codename": codename, "existing": existing}))

if __name__ == "__main__":
    main()
