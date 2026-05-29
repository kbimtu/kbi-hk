#!/usr/bin/env python3
"""Move photo-strip inside gallery-event-header-body; remove premature closing divs."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GALLERY = ROOT / "event gallery"

# Premature header-body + header closes immediately before the strip.
BEFORE_STRIP = re.compile(
    r"\n          </div>\s*\n        </div>\s*\n(\s*<div class=\"photo-strip-wrap\">)",
    re.MULTILINE,
)

# Normalize messy strip-wrap closing indent.
STRIP_WRAP_CLOSE = re.compile(
    r"\n\s{20,}</div>\s*\n(\s*</div>\s*\n\s*</div>\s*\n\s*</section>)",
    re.MULTILINE,
)


def fix_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if "photo-strip-wrap" not in text:
        return False

    original = text
    text = re.sub(
        r"\n\s+<div class=\"photo-strip-wrap\">",
        "\n            <div class=\"photo-strip-wrap\">",
        text,
    )
    text, n_before = BEFORE_STRIP.subn(r"\n            \1", text)

    def _close_strip(m: re.Match[str]) -> str:
        return "\n            </div>\n" + m.group(1)

    text, n_close = STRIP_WRAP_CLOSE.subn(_close_strip, text)

    if text == original:
        return False
    path.write_text(text, encoding="utf-8")
    print(f"{path.name}: moved {n_before} strip(s), normalized {n_close} closing(s)")
    return True


def main() -> None:
    for path in sorted(GALLERY.glob("event-gallery-*.html")):
        fix_file(path)


if __name__ == "__main__":
    main()
