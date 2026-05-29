#!/usr/bin/env python3
"""Update site navigation to Compete / Certify / Collab / Connect structure."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

ANNOUNCEMENT_ETS = (
    "Two upcoming events in 2026: ETO Eastern Conference (9–11 Oct, CDNIS) "
    "and Emerging-Technology SkillSprint (ETS). "
)


def link_paths(file_path: Path) -> dict[str, str]:
    rel = file_path.parent.relative_to(ROOT)
    depth = len(rel.parts)
    base = "../" * depth if depth else ""

    if rel.parts == ("programme",):
        return {
            "eto": "../upcoming events/eto2026.html",
            "ets": "../upcoming events/ets2026.html",
            "i2ol": "i2ol.html",
            "etti": "etti.html",
            "abc5": "abc5.html",
            "skillsprint": "skillsprint.html",
            "isfretic": "isfretic.html",
            "projects": "projects.html",
            "working": "working-research-groups.html",
            "programmes": "programmes.html",
            "community": "membership.html",
            "socratic": "socratic.html",
            "gatherings": "gatherings.html",
            "sponsors": "sponsors.html",
            "membership": "membership.html",
        }
    if rel.parts == ("upcoming events",):
        return {
            "eto": "eto2026.html",
            "ets": "ets2026.html",
            "i2ol": "../programme/i2ol.html",
            "etti": "../programme/etti.html",
            "abc5": "../programme/abc5.html",
            "skillsprint": "../programme/skillsprint.html",
            "isfretic": "../programme/isfretic.html",
            "projects": "../programme/projects.html",
            "working": "../programme/working-research-groups.html",
            "programmes": "../programme/programmes.html",
            "community": "../programme/membership.html",
            "socratic": "../programme/socratic.html",
            "gatherings": "../programme/gatherings.html",
            "sponsors": "../programme/sponsors.html",
            "membership": "../programme/membership.html",
        }

    return {
        "eto": f"{base}upcoming events/eto2026.html",
        "ets": f"{base}upcoming events/ets2026.html",
        "i2ol": f"{base}programme/i2ol.html",
        "etti": f"{base}programme/etti.html",
        "abc5": f"{base}programme/abc5.html",
        "skillsprint": f"{base}programme/skillsprint.html",
        "isfretic": f"{base}programme/isfretic.html",
        "projects": f"{base}programme/projects.html",
        "working": f"{base}programme/working-research-groups.html",
        "programmes": f"{base}programme/programmes.html",
        "community": f"{base}programme/membership.html",
        "socratic": f"{base}programme/socratic.html",
        "gatherings": f"{base}programme/gatherings.html",
        "sponsors": f"{base}programme/sponsors.html",
        "membership": f"{base}programme/membership.html",
    }


def build_nav(file_path: Path) -> tuple[str, str, str, str]:
    u = link_paths(file_path)

    dd = f'''          <div class="nav-dropdown" id="dd-prog" role="menu">
            <div class="nav-dropdown-label">Compete</div>
            <a href="{u['eto']}" role="menuitem">Emerging Technologies Olympiad (ETO)</a>
            <a href="{u['i2ol']}" role="menuitem">I&sup2;OL Scheme</a>
            <div class="nav-dropdown-divider"></div>
            <div class="nav-dropdown-label">Certify</div>
            <a href="{u['etti']}" role="menuitem">Emerging Tech Training &amp; Internship (ETTI) Program</a>
            <a href="{u['skillsprint']}" role="menuitem">SkillSprint</a>
            <a href="{u['abc5']}" role="menuitem">AI, Blockchain, Cybersecurity (ABC5) Program</a>
            <a href="{u['isfretic']}" role="menuitem">International Standards Framework of Reference for Emerging Technologies Innovation and Competency (ISFRETIC)</a>
            <div class="nav-dropdown-divider"></div>
            <div class="nav-dropdown-label">Collab</div>
            <a href="{u['projects']}" role="menuitem">Project Support</a>
            <a href="{u['working']}" role="menuitem">Working &amp; Research Groups</a>
            <div class="nav-dropdown-divider"></div>
            <div class="nav-dropdown-label">Connect</div>
            <a href="{u['socratic']}" role="menuitem">Socratic Circles</a>
            <a href="{u['gatherings']}" role="menuitem">KBI Community Gatherings</a>
          </div>'''

    mob = f'''    <div class="nav-mobile-section-label">Compete</div>
    <a href="{u['eto']}" class="nav-mobile-link">Emerging Technologies Olympiad (ETO)</a>
    <a href="{u['i2ol']}" class="nav-mobile-sub">I&sup2;OL Scheme</a>
    <div class="nav-mobile-section-label">Certify</div>
    <a href="{u['etti']}" class="nav-mobile-sub">ETTI Program</a>
    <a href="{u['skillsprint']}" class="nav-mobile-sub">SkillSprint</a>
    <a href="{u['abc5']}" class="nav-mobile-sub">ABC5 Program</a>
    <a href="{u['isfretic']}" class="nav-mobile-sub">ISFRETIC</a>
    <div class="nav-mobile-section-label">Collab</div>
    <a href="{u['projects']}" class="nav-mobile-sub">Project Support</a>
    <a href="{u['working']}" class="nav-mobile-sub">Working &amp; Research Groups</a>
    <div class="nav-mobile-section-label">Connect</div>
    <a href="{u['socratic']}" class="nav-mobile-sub">Socratic Circles</a>
    <a href="{u['gatherings']}" class="nav-mobile-sub">KBI Community Gatherings</a>'''

    cta = f'''      <div class="nav-ctas">
        <a href="{u['sponsors']}" class="btn btn-outline-prussian btn--sm">Partner With Us</a>
        <a href="{u['membership']}" class="btn btn-yellow btn--sm">Join Us</a>
      </div>'''

    mob_cta = f'''    <div class="nav-mobile-ctas">
      <a href="{u['sponsors']}" class="btn btn-outline-white">Partner With Us</a>
      <a href="{u['membership']}" class="btn btn-yellow">Join Us</a>
    </div>'''

    return dd, mob, cta, mob_cta


DD_RE = re.compile(
    r'<div class="nav-dropdown" id="dd-prog" role="menu">.*?</div>\s*(?=\s*</li>)',
    re.DOTALL,
)

MOB_CERT_RE = re.compile(
    r'<div class="nav-mobile-section-label">Certify</div>.*?'
    r'(?=\s*<div class="nav-mobile-section-label">Collab</div>)',
    re.DOTALL,
)

CTA_RE = re.compile(r'<div class="nav-ctas">\s*.*?</div>', re.DOTALL)
MOB_CTA_RE = re.compile(r'<div class="nav-mobile-ctas">\s*.*?</div>', re.DOTALL)
COMMUNITY_NAV_RE = re.compile(
    r'\s*<li class="hide-md"><a href="[^"]*membership\.html">Community</a></li>',
)
SISTERS_FOOTER_RE = re.compile(
    r'\s*<li><a href="[^"]*sisters\.html">Sibling Organisations</a></li>\n?',
)
COLLAB_FOOTER_RE = re.compile(
    r'\s*<li><a href="[^"]*collaborations\.html">Collaborations</a></li>\n?',
)
CONNECT_MOB_RE = re.compile(
    r'<div class="nav-mobile-section-label">Connect</div>.*?'
    r'(?=\s*(?:<div class="nav-mobile-section-label">(?:Competitions|Navigate)</div>|\s*<a href="[^"]*socratic\.html))',
    re.DOTALL,
)
ANNOUNCEMENT_FINTECH_RE = re.compile(
    r"the launch of FinTech SkillSprint[^.<]*\.?",
    re.IGNORECASE,
)
ANNOUNCEMENT_DUP_RE = re.compile(
    r"Two upcoming events in 2026: ETO Eastern Conference \(9–11 Oct, CDNIS\) and Two upcoming events in 2026: ETO Eastern Conference \(9–11 Oct, CDNIS\) and Emerging-Technology SkillSprint \(ETS\)\.?\s*",
)
ANNOUNCEMENT_GOOD = (
    "Two upcoming events in 2026: ETO Eastern Conference (9–11 Oct, CDNIS) "
    "and Emerging-Technology SkillSprint (ETS). "
)
COMMUNITY_HASH_NAV_RE = re.compile(
    r'href="([^"]*socratic\.html)#(socratic|gatherings)"',
)


def patch_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    orig = text
    u = link_paths(path)
    dd, mob, cta, mob_cta = build_nav(path)

    if DD_RE.search(text):
        text = DD_RE.sub(dd, text, count=1)
    if MOB_CERT_RE.search(text):
        cert_mob = (
            f'    <div class="nav-mobile-section-label">Certify</div>\n'
            f'    <a href="{u["etti"]}" class="nav-mobile-sub">ETTI Program</a>\n'
            f'    <a href="{u["skillsprint"]}" class="nav-mobile-sub">SkillSprint</a>\n'
            f'    <a href="{u["abc5"]}" class="nav-mobile-sub">ABC5 Program</a>\n'
            f'    <a href="{u["isfretic"]}" class="nav-mobile-sub">ISFRETIC</a>\n'
            "    "
        )
        text = MOB_CERT_RE.sub(cert_mob, text, count=1)
    if CONNECT_MOB_RE.search(text):
        connect_block = (
            f'    <div class="nav-mobile-section-label">Connect</div>\n'
            f'    <a href="{u["socratic"]}" class="nav-mobile-sub">Socratic Circles</a>\n'
            f'    <a href="{u["gatherings"]}" class="nav-mobile-sub">KBI Community Gatherings</a>\n'
        )
        text = CONNECT_MOB_RE.sub(connect_block, text, count=1)
    if CTA_RE.search(text):
        text = CTA_RE.sub(cta, text, count=1)
    if MOB_CTA_RE.search(text):
        text = MOB_CTA_RE.sub(mob_cta, text, count=1)

    def _fix_connect_hash(m: re.Match[str]) -> str:
        anchor = m.group(2)
        key = anchor
        return f'href="{u[key]}"'

    text = COMMUNITY_HASH_NAV_RE.sub(_fix_connect_hash, text)
    text = ANNOUNCEMENT_DUP_RE.sub(ANNOUNCEMENT_GOOD, text)
    text = ANNOUNCEMENT_FINTECH_RE.sub(ANNOUNCEMENT_ETS.rstrip("."), text)
    text = text.replace(
        "launch of FinTech SkillSprint — plus",
        "Emerging-Technology SkillSprint (ETS) — plus",
    )
    text = text.replace(
        "and the launch of FinTech SkillSprint.",
        "and Emerging-Technology SkillSprint (ETS).",
    )
    text = COMMUNITY_NAV_RE.sub("", text)
    text = re.sub(
        r'\s*<a href="[^"]*sisters\.html" class="nav-mobile-link">Sibling Organisations</a>\n?',
        "\n",
        text,
    )
    text = SISTERS_FOOTER_RE.sub("", text)
    text = COLLAB_FOOTER_RE.sub("", text)
    text = re.sub(r'\s*<div class="lang-switcher"[^>]*>.*?</div>\s*', "\n", text, flags=re.DOTALL)
    text = re.sub(r'\s*<div class="nav-mobile-lang"[^>]*>.*?</div>\s*', "\n", text, flags=re.DOTALL)

    if text != orig:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def main() -> None:
    updated = []
    for html in sorted(ROOT.rglob("*.html")):
        if patch_file(html):
            updated.append(html.relative_to(ROOT))
    print(f"Updated {len(updated)} files")


if __name__ == "__main__":
    main()
