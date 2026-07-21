#!/usr/bin/env python3
"""Fail the Pages build when the generated site is incomplete or internally unsafe."""
from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "_site"
SOURCE_MD = [
    p for p in ROOT.rglob("*.md")
    if not any(part in {".git", "vendor", "node_modules", "_site"} for part in p.parts)
    and p.name != "README.md"
]
HREF_RE = re.compile(r'href=["\']([^"\']+)["\']', re.I)
errors: list[str] = []

if not (SITE / "index.html").is_file():
    errors.append("Missing _site/index.html")

html_files = list(SITE.rglob("*.html"))
if len(html_files) < len(SOURCE_MD):
    errors.append(
        f"Generated only {len(html_files)} HTML files for {len(SOURCE_MD)} publishable Markdown sources"
    )

if not (SITE / "assets/js/mermaid-init.js").is_file():
    errors.append("Missing generated Mermaid bootstrap asset")

for page in html_files:
    text = page.read_text(encoding="utf-8", errors="replace")
    for href in HREF_RE.findall(text):
        parsed = urlsplit(href)
        if parsed.scheme or href.startswith(("#", "mailto:", "tel:", "javascript:")):
            continue
        path = unquote(parsed.path)
        if not path:
            continue
        if path.startswith("/trust-systems-meta-model/"):
            path = path.removeprefix("/trust-systems-meta-model/")
            target = SITE / path
        elif path.startswith("/"):
            continue
        else:
            target = page.parent / path
        candidates = [target]
        if target.suffix == "":
            candidates.extend([target.with_suffix(".html"), target / "index.html"])
        if target.suffix == ".md":
            candidates.append(target.with_suffix(".html"))
        if not any(c.resolve().exists() for c in candidates):
            errors.append(f"Broken generated link in {page.relative_to(SITE)} -> {href}")

if errors:
    for error in sorted(set(errors)):
        print(error)
    raise SystemExit(1)

print(
    f"Verified {len(html_files)} generated HTML pages, internal links, root landing page, and Mermaid asset."
)
