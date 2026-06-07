#!/usr/bin/env python3
"""Convert event gallery photo-card blocks to horizontal photo-strip layout."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GALLERY = ROOT / "event gallery"

STRIP_HINT = (
    '<span class="photo-strip-item-hint" aria-hidden="true">'
    '<svg viewBox="0 0 24 24" aria-hidden="true">'
    '<path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7" fill="none" stroke="currentColor" '
    'stroke-width="2" stroke-linecap="round"/></svg></span>'
)

PHOTO_CARD_RE = re.compile(
    r'<div class="photo-card(?:\s+photo-card--wide)?"\s+onclick="openLightbox\(this\)"\s*'
    r'(?:data-caption="([^"]*)"\s*)?>'
    r'\s*<img\s+[^>]*?src="([^"]+)"[^>]*?alt="([^"]*)"[^>]*>'
    r'(?:\s*<div class="photo-card-overlay">(?:</div>)?)?'
    r'\s*<div class="photo-card-icon">.*?</div>\s*</div>',
    re.DOTALL,
)


def build_strip(matches: list[re.Match[str]]) -> str:
    items = []
    for m in matches:
        caption, src, alt = m.group(1) or m.group(3), m.group(2), m.group(3)
        cap = caption.replace('"', "&quot;")
        items.append(
            f'''          <button type="button" class="photo-strip-item" data-caption="{cap}" aria-label="View larger image">
            <img src="{src}" alt="{alt}" loading="lazy" decoding="async">
            {STRIP_HINT}
          </button>'''
        )
    body = "\n".join(items)
    return f'''            <div class="photo-strip-wrap">
              <div class="photo-strip-scroll" tabindex="0" role="region" aria-label="Event photos — scroll horizontally">
                <div class="photo-strip-track">
{body}
                </div>
              </div>
            </div>'''


def replace_runs(text: str) -> str:
    out: list[str] = []
    pos = 0
    while pos < len(text):
        m = PHOTO_CARD_RE.search(text, pos)
        if not m:
            out.append(text[pos:])
            break
        out.append(text[pos : m.start()])
        cards: list[re.Match[str]] = []
        cursor = m.start()
        while True:
            m2 = PHOTO_CARD_RE.match(text, cursor)
            if not m2:
                break
            cards.append(m2)
            cursor = m2.end()
            gap = re.match(r"\s*", text[cursor:])
            if gap:
                cursor += gap.end()
        out.append(build_strip(cards))
        pos = cursor
    return "".join(out)


def migrate_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if "class=\"photo-card" not in text:
        return False
    new = replace_runs(text)
    if new != text:
        path.write_text(new, encoding="utf-8")
        return True
    return False


def main() -> None:
    for html in sorted(GALLERY.glob("event-gallery-*.html")):
        if migrate_file(html):
            print(html.name)


if __name__ == "__main__":
    main()
