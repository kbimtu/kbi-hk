#!/usr/bin/env python3
"""Ensure every page nav uses the brand logo-icon.png image (not inline SVG)."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

NAV_SVG_MARK_RE = re.compile(
    r'<div class="nav-logo-mark">\s*<svg\b[^>]*>.*?</svg>\s*</div>',
    re.DOTALL | re.IGNORECASE,
)

NAV_IMG_MARK_RE = re.compile(
    r'<div class="nav-logo-mark">\s*<img\b[^>]*>\s*</div>',
    re.DOTALL | re.IGNORECASE,
)


def asset_base(file_path: Path) -> str:
    depth = len(file_path.parent.relative_to(ROOT).parts)
    return "../" * depth if depth else ""


def nav_logo_mark(base: str) -> str:
    return (
        f'<div class="nav-logo-mark"><img src="{base}assets/brand/logo-icon.png" '
        f'alt="" class="brand-mark-img" width="40" height="40"></div>'
    )


def patch_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    orig = text
    base = asset_base(path)

    if NAV_SVG_MARK_RE.search(text):
        text = NAV_SVG_MARK_RE.sub(nav_logo_mark(base), text, count=1)

    # Normalise any nav img with wrong path or missing dimensions
    if 'class="nav-logo"' in text and "logo-icon.png" not in text.split("</nav>", 1)[0]:
        if NAV_IMG_MARK_RE.search(text):
            text = NAV_IMG_MARK_RE.sub(nav_logo_mark(base), text, count=1)
        elif NAV_SVG_MARK_RE.search(text):
            text = NAV_SVG_MARK_RE.sub(nav_logo_mark(base), text, count=1)

    if text != orig:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def main() -> None:
    updated: list[Path] = []
    for html in sorted(ROOT.rglob("*.html")):
        if "scripts" in html.parts:
            continue
        if patch_file(html):
            updated.append(html.relative_to(ROOT))
    for p in updated:
        print(p)
    print(f"Updated {len(updated)} file(s).")


if __name__ == "__main__":
    main()
