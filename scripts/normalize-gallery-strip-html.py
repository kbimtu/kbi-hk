#!/usr/bin/env python3
"""Tidy photo-strip markup after arrow removal."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GALLERY = ROOT / "event gallery"

WRAP_OPEN = re.compile(
    r'(<div class="photo-strip-wrap">)\s*(<div class="photo-strip-scroll")',
    re.IGNORECASE,
)

WRAP_CLOSE = re.compile(
    r'(</div>\s*</div>)\s*(</div>\s*\n\s*</div>\s*\n\s*</div>\s*\n\s*</section>)',
    re.MULTILINE,
)

ARIA = re.compile(
    r'<button type="button" class="photo-strip-item"(?! aria-label)',
)


def fix_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    original = text
    text = WRAP_OPEN.sub(
        r'\1\n              \2',
        text,
    )
    text = WRAP_CLOSE.sub(
        r'\1\n            \2',
        text,
    )
    text = ARIA.sub(
        '<button type="button" class="photo-strip-item" aria-label="View larger image"',
        text,
    )
    if text == original:
        return False
    path.write_text(text, encoding="utf-8")
    print(path.name)
    return True


def main() -> None:
    for path in sorted(GALLERY.glob("event-gallery-*.html")):
        fix_file(path)


if __name__ == "__main__":
    main()
