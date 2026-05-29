#!/usr/bin/env python3
"""Remove broken duplicate announcement bar markup."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

BROKEN = re.compile(
    r"(?:<!--\s*ANNOUNCEMENT BAR\s*-->\s*)?"
    r'<div class="announcement-bar" id="announcementBar">\s*'
    r'<div class="announcement-bar-inner">\s*'
    r'<p class="announcement-bar-text">.*?</p>\s*'
    r"</div>\s*<!--\s*ANNOUNCEMENT BAR\s*-->\s*"
    r'<div class="announcement-bar" id="announcementBar">\s*'
    r"(<div class=\"announcement-bar-inner\">\s*"
    r'<p class="announcement-bar-text">.*?</p>\s*'
    r"</div>\s*"
    r'<button class="announcement-close"[^>]*>.*?</button>\s*'
    r"</div>)",
    re.DOTALL | re.IGNORECASE,
)

STANDARD = (
    "  <!-- ANNOUNCEMENT BAR -->\n"
    "  <div class=\"announcement-bar\" id=\"announcementBar\">\n"
    "    {inner}\n"
    "    {button}\n"
    "  </div>"
)


def fix_text(text: str) -> tuple[str, int]:
    count = 0

    def repl(m: re.Match[str]) -> str:
        nonlocal count
        count += 1
        block = m.group(1)
        inner_m = re.search(
            r'(<div class="announcement-bar-inner">.*?</div>)',
            block,
            re.DOTALL,
        )
        btn_m = re.search(
            r'(<button class="announcement-close"[^>]*>.*?</button>)',
            block,
            re.DOTALL,
        )
        inner = inner_m.group(1) if inner_m else ""
        button = btn_m.group(1) if btn_m else ""
        return STANDARD.format(inner=inner, button=button)

    return BROKEN.sub(repl, text), count


def main() -> None:
    for path in sorted(ROOT.rglob("*.html")):
        if "node_modules" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        if text.count('id="announcementBar"') < 2:
            continue
        new, n = fix_text(text)
        if n:
            path.write_text(new, encoding="utf-8")
            print(f"{path.relative_to(ROOT)}: fixed {n}")


if __name__ == "__main__":
    main()
