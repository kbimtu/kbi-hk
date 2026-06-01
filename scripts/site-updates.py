#!/usr/bin/env python3
"""Hero gradients, competitions redirects, ETO naming, international olympiad links."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GRADIENT = "background:linear-gradient(160deg, var(--night) 0%, var(--prussian) 100%);"

HERO_IMG_RE = re.compile(
    r"(<div class=\"page-hero-bg\"[^>]*style=\"[^\"]*?)background-image:url\([^)]+\);([^\"]*\")",
    re.DOTALL,
)

COMP_REPLACEMENTS = [
    (re.compile(r'href="([^"]*)programme/competitions\.html#ibcol"'), r'href="https://2026.ibcol.org" target="_blank" rel="noopener"'),
    (re.compile(r'href="([^"]*)programme/competitions\.html#idsol"'), r'href="https://2026.idsol.org" target="_blank" rel="noopener"'),
    (re.compile(r'href="([^"]*)programme/competitions\.html#iqcol"'), r'href="https://2026.iqcol.org" target="_blank" rel="noopener"'),
    (re.compile(r'href="([^"]*)competitions\.html#ibcol"'), r'href="https://2026.ibcol.org" target="_blank" rel="noopener"'),
    (re.compile(r'href="([^"]*)competitions\.html#idsol"'), r'href="https://2026.idsol.org" target="_blank" rel="noopener"'),
    (re.compile(r'href="([^"]*)competitions\.html#iqcol"'), r'href="https://2026.iqcol.org" target="_blank" rel="noopener"'),
    (re.compile(r'href="([^"]*)programme/competitions\.html"'), r'href="\1programme/i2ol.html"'),
    (re.compile(r'href="([^"]*)competitions\.html"'), r'href="\1i2ol.html"'),
]

ETO_REPLACEMENTS = [
    ("ETO HK 2026", "ETO Eastern Conference 2026"),
    ("ETO Hong Kong 2026", "ETO Eastern Conference 2026"),
    ("ETO Hong Kong", "ETO Eastern Conference"),
    ("ETO HK", "ETO Eastern"),
    ("Eastern ETO @ Hong Kong", "ETO Eastern Conference"),
    ("Eastern ETO @ HK", "ETO Eastern Conference"),
    ("About ETO HK", "About ETO Eastern"),
]


def strip_hero_images(path: Path, text: str) -> str:
    if path.name == "index.html":
        return text
    return HERO_IMG_RE.sub(rf"\1{GRADIENT}\2", text)


def main() -> None:
    # competitions redirect
    comp = ROOT / "programme" / "competitions.html"
    comp.write_text(
        """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="refresh" content="0; url=i2ol.html">
  <link rel="canonical" href="i2ol.html">
  <title>Redirecting…</title>
  <script>location.replace('i2ol.html');</script>
</head>
<body>
  <p>Olympiad information has moved to the <a href="i2ol.html">I2OL Scheme</a> page, with links to the international competitions.</p>
</body>
</html>
""",
        encoding="utf-8",
    )

    for html in ROOT.rglob("*.html"):
        if "scripts" in html.parts or html == comp:
            continue
        text = html.read_text(encoding="utf-8")
        orig = text
        text = strip_hero_images(html, text)
        for pat, repl in COMP_REPLACEMENTS:
            text = pat.sub(repl, text)
        if html.name != "eto2026.html":
            for old, new in ETO_REPLACEMENTS:
                text = text.replace(old, new)
        if text != orig:
            html.write_text(text, encoding="utf-8")
            print(html.relative_to(ROOT))


if __name__ == "__main__":
    main()
