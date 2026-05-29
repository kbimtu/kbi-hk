#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BAD = (
    "Two upcoming events in 2026: ETO Eastern Conference (9–11 Oct, CDNIS) and "
    "Two upcoming events in 2026: ETO Eastern Conference (9–11 Oct, CDNIS) and "
    "Emerging-Technology SkillSprint (ETS)."
)
GOOD = (
    "Two upcoming events in 2026: ETO Eastern Conference (9–11 Oct, CDNIS) and "
    "Emerging-Technology SkillSprint (ETS)."
)

import re

CONNECT_DUP = re.compile(
    r'(<a href="(?:\.\./programme/)?socratic\.html" class="nav-mobile-sub">Socratic Circles</a>\s*'
    r'<a href="(?:\.\./programme/)?gatherings\.html" class="nav-mobile-sub">KBI Community Gatherings</a>)\s*\n\s*\1',
)

for html in ROOT.rglob("*.html"):
    text = html.read_text(encoding="utf-8")
    orig = text
    text = text.replace(BAD, GOOD)
    text = text.replace(BAD + "  ", GOOD + "  ")
    prev = None
    while prev != text:
        prev = text
        text = CONNECT_DUP.sub(r"\1", text)
    if text != orig:
        html.write_text(text, encoding="utf-8")
        print(html.relative_to(ROOT))
