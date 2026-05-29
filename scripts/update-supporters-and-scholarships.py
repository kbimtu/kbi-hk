#!/usr/bin/env python3
"""Wire supporter marquees to images/logo/ and remove scholarships page."""
from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
LOGO_DIR = ROOT / "images" / "logo"
SKIP_EXT = {".ai"}  # not displayable in browsers

MARQUEE_RE = re.compile(
    r'<div class="logo-marquee-wrap[^"]*"[^>]*aria-label="Our supporters[^"]*">.*?</div>\s*</div>\s*</div>',
    re.DOTALL,
)

INDEX_MARQUEE_RE = re.compile(
    r'<!-- SPONSOR LOGO MARQUEE.*?<div class="logo-marquee-wrap logo-marquee-wrap--dark[^"]*"[^>]*>.*?</div>\s*</div>\s*</div>',
    re.DOTALL,
)

SCHOLARSHIPS_MOBILE = re.compile(
    r'\s*<a href="[^"]*scholarships\.html" class="nav-mobile-link">Scholarships</a>\n?',
)
SCHOLARSHIPS_FOOTER = re.compile(
    r'\s*<li><a href="[^"]*scholarships\.html">Scholarships</a></li>\n?',
)
SCHOLARSHIPS_INLINE = re.compile(
    r'<a href="[^"]*scholarships\.html"[^>]*>[^<]*</a>',
)


def logo_files() -> list[Path]:
    files = []
    for p in sorted(LOGO_DIR.iterdir()):
        if p.is_file() and p.suffix.lower() not in SKIP_EXT:
            files.append(p)
    return files


def alt_text(filename: str) -> str:
    base = Path(filename).stem
    return base.replace("_", " ").replace("  ", " ").strip()


def pill(img_path: str, alt: str, hidden: bool = False) -> str:
    aria = ' aria-hidden="true"' if hidden else ""
    return (
        f'            <div class="logo-marquee-pill"{aria}>'
        f'<img src="{img_path}" alt="{alt}"></div>\n'
    )


def build_marquee(prefix: str, wrap_class: str) -> str:
    """prefix e.g. images/logo/ or ../images/logo/"""
    files = logo_files()
    pills = []
    for f in files:
        # URL-encode path segments for safety
        rel = prefix + quote(f.name)
        pills.append(pill(rel, alt_text(f.name)))
    for f in files:
        rel = prefix + quote(f.name)
        pills.append(pill(rel, alt_text(f.name), hidden=True))

    track = "".join(pills)
    return f'''      <div class="logo-marquee-wrap {wrap_class} reveal reveal-delay-2" aria-label="Our supporters">
        <div class="logo-marquee">
          <div class="logo-marquee-track">
{track}          </div>
        </div>
      </div>'''


def patch_marquees() -> None:
    impact = ROOT / "about" / "about-impact.html"
    t = impact.read_text(encoding="utf-8")
    t = MARQUEE_RE.sub(build_marquee("../images/logo/", "logo-marquee-wrap--light"), t, count=1)
    t = t.replace(
        "<!-- OUR SUPPORTERS (mist) — add logo images under ../images/partners/ -->",
        "<!-- OUR SUPPORTERS (mist) -->",
    )
    impact.write_text(t, encoding="utf-8")
    print("Updated about-impact.html")

    index = ROOT / "index.html"
    t = index.read_text(encoding="utf-8")
    block = build_marquee("images/logo/", "logo-marquee-wrap--dark")
    t = INDEX_MARQUEE_RE.sub(
        "<!-- SPONSOR LOGO MARQUEE -->\n      " + block,
        t,
        count=1,
    )
    index.write_text(t, encoding="utf-8")
    print("Updated index.html")


def remove_scholarships() -> None:
    redirect = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="refresh" content="0; url=membership.html">
  <link rel="canonical" href="membership.html">
  <title>Redirecting…</title>
  <script>location.replace('membership.html');</script>
</head>
<body>
  <p><a href="membership.html">Membership — KBI Hong Kong</a></p>
</body>
</html>
"""
    (ROOT / "programme" / "scholarships.html").write_text(redirect, encoding="utf-8")

    n = 0
    for html in ROOT.rglob("*.html"):
        if "scripts" in html.parts or html.name == "scholarships.html":
            continue
        text = html.read_text(encoding="utf-8")
        orig = text
        text = SCHOLARSHIPS_MOBILE.sub("\n", text)
        text = SCHOLARSHIPS_FOOTER.sub("\n", text)
        # projects page bursary link
        text = text.replace(
            'href="scholarships.html" style="color:var(--prussian);font-weight:600;">scholarships page',
            'href="contact.html" style="color:var(--prussian);font-weight:600;">contact us',
        )
        text = text.replace(
            'href="../programme/scholarships.html" style="color:var(--prussian);font-weight:600;">scholarships page',
            'href="../contact.html" style="color:var(--prussian);font-weight:600;">contact us',
        )
        if text != orig:
            html.write_text(text, encoding="utf-8")
            n += 1
    print(f"Removed scholarships links from {n} files")


def main() -> None:
    print(f"Found {len(logo_files())} logos in images/logo/")
    patch_marquees()
    remove_scholarships()


if __name__ == "__main__":
    main()
