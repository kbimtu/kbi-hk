#!/usr/bin/env python3
"""Remove duplicated gallery layout CSS now in kbi-hk.css."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GALLERY = ROOT / "event gallery"

GALLERY_STYLE = re.compile(
    r"\n  <style>\s*\.gallery-page-hero\s*\{.*?</style>",
    re.DOTALL,
)


def fix_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    new = GALLERY_STYLE.sub("", text)
    new = new.replace("</head><body>", "</head>\n<body>")
    if new == text:
        return False
    path.write_text(new, encoding="utf-8")
    print(path.name)
    return True


def main() -> None:
    for path in sorted(GALLERY.glob("event-gallery-*.html")):
        fix_file(path)


if __name__ == "__main__":
    main()
