#!/usr/bin/env python3
"""Remove prev/next scroll arrow buttons from event gallery photo strips."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GALLERY = ROOT / "event gallery"

STRIP_BTN = re.compile(
    r'\s*<button\s+type="button"\s+class="photo-strip-btn\s+photo-strip-btn--(?:prev|next)"'
    r'[^>]*>.*?</button>\s*',
    re.DOTALL | re.IGNORECASE,
)


def fix_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    new = STRIP_BTN.sub("\n", text)
    if new == text:
        return False
    path.write_text(new, encoding="utf-8")
    count = len(STRIP_BTN.findall(text))
    print(f"{path.name}: removed {count} arrow button(s)")
    return True


def main() -> None:
    for path in sorted(GALLERY.glob("event-gallery-*.html")):
        fix_file(path)


if __name__ == "__main__":
    main()
