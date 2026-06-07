#!/usr/bin/env python3
"""Point former community.html links (now on socratic.html) to membership.html."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

PATTERNS: list[tuple[re.Pattern[str], str]] = [
    (
        re.compile(
            r'(<a href=")([^"]*?)socratic\.html(" class="nav-mobile-link">Community</a>)'
        ),
        r"\1\2membership.html\3",
    ),
    (
        re.compile(r'(<li><a href=")([^"]*?)socratic\.html(">Community Hub</a></li>)'),
        r"\1\2membership.html\3",
    ),
    (
        re.compile(
            r'(<a href=")([^"]*?)socratic\.html(" class="btn[^"]*">Join the Community</a>)'
        ),
        r"\1\2membership.html\3",
    ),
    (
        re.compile(r'(<li><a href=")([^"]*?)socratic\.html(">Community</a></li>)'),
        r"\1\2membership.html\3",
    ),
]


def patch_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    orig = text
    for pattern, repl in PATTERNS:
        text = pattern.sub(repl, text)
    if text != orig:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def main() -> None:
    updated = []
    for html in sorted(ROOT.rglob("*.html")):
        if patch_file(html):
            updated.append(html.relative_to(ROOT))
    print(f"Updated {len(updated)} files:")
    for p in updated:
        print(f"  {p}")


if __name__ == "__main__":
    main()
