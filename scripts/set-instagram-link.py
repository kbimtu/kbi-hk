#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
URL = "https://www.instagram.com/kbi_hongkong/"

PATTERN = re.compile(r'href="#"([^>\n]*aria-label="Instagram"[^>]*)')

updated = 0
for html in ROOT.rglob("*.html"):
    text = html.read_text(encoding="utf-8")
    new_text = PATTERN.sub(lambda m: f'href="{URL}"{m.group(1)}', text)
    if new_text != text:
        html.write_text(new_text, encoding="utf-8")
        updated += 1

print(updated)
