#!/usr/bin/env python3
"""Remove stale mobile nav blocks and fix collaborations/sisters links."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

STALE_MOBILE = re.compile(
    r'\s*<div class="nav-mobile-section-label">Competitions</div>.*?'
    r'(?=\s*<div class="nav-mobile-section-label">Navigate)',
    re.DOTALL,
)

# Old Flagship-only block after Programmes label (some pages)
STALE_FLAGSHIP = re.compile(
    r'\s*<div class="nav-mobile-section-label">Programmes</div>\s*'
    r'<a href="[^"]*eto[^"]*"[^>]*>.*?</a>\s*'
    r'(?:<div class="nav-mobile-section-label">Competitions</div>.*?)?'
    r'(?=\s*<div class="nav-mobile-section-label">(?:Navigate|Compete))',
    re.DOTALL,
)

DUP_NAV_ITEMS = re.compile(
    r'\s*<a href="[^"]*membership\.html" class="nav-mobile-link">Membership</a>\n?'
    r'\s*<a href="[^"]*community\.html" class="nav-mobile-link">Community</a>\n?',
)


def fix_collab_links(text: str) -> str:
    text = re.sub(
        r'href="([^"]*)collaborations\.html([^"]*)"',
        lambda m: f'href="{m.group(1)}projects.html{m.group(2)}"',
        text,
    )
    text = re.sub(
        r'href="([^"]*)sisters\.html([^"]*)"',
        lambda m: f'href="{m.group(1)}about/about-who-we-are.html{m.group(2)}"',
        text,
    )
    return text


def main() -> None:
    n = 0
    for html in ROOT.rglob("*.html"):
        if "scripts" in html.parts:
            continue
        text = html.read_text(encoding="utf-8")
        orig = text
        text = STALE_MOBILE.sub("\n    ", text)
        text = STALE_FLAGSHIP.sub("\n    ", text)
        text = DUP_NAV_ITEMS.sub("\n", text)
        text = fix_collab_links(text)
        if text != orig:
            html.write_text(text, encoding="utf-8")
            n += 1
            print(html.relative_to(ROOT))
    print(f"Cleaned {n} files")


if __name__ == "__main__":
    main()
