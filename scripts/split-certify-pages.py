#!/usr/bin/env python3
"""Split ISFRETIC, ETTI, and ABC5 into separate programme pages; update nav links."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROG = ROOT / "programme"


def make_isfretic() -> None:
    text = (PROG / "certifications.html").read_text(encoding="utf-8")
    # Remove ETTI and ABC5 sections
    text = re.sub(
        r"\n  <!-- ETTI -->.*?<!-- SECTION 1: What ISFRETIC Is -->",
        "\n  <!-- SECTION 1: What ISFRETIC Is -->",
        text,
        count=1,
        flags=re.DOTALL,
    )
    text = text.replace(
        "<title>Certifications — KBI Hong Kong</title>",
        "<title>ISFRETIC — KBI Hong Kong</title>",
    )
    text = text.replace(
        '<span class="u-label u-label--light">Certification</span>',
        '<span class="u-label u-label--light">ISFRETIC</span>',
    )
    text = re.sub(
        r'  <div id="isfretic" tabindex="-1" aria-hidden="true" style="position:absolute;margin-top:-80px;"></div>\n',
        "",
        text,
    )
    (PROG / "isfretic.html").write_text(text, encoding="utf-8")


def prog_page(
    *,
    filename: str,
    title: str,
    meta: str,
    label: str,
    heading: str,
    lead: str,
    sections: list[tuple[str, str, str, str]],
) -> str:
    """sections: (id, heading, body_html, wrap_class white|mist)"""
    body_sections = ""
    for i, (sid, h, body, wrap) in enumerate(sections):
        cls = "section-wrap--white" if wrap == "white" else "section-wrap--mist"
        delay = f' reveal-delay-{i}' if i else ""
        body_sections += f'''
  <section class="section-wrap {cls}" id="{sid}" aria-labelledby="{sid}-heading">
    <div class="section-inner">
      <div class="label-row"><div class="u-rule" aria-hidden="true"></div><span class="u-label">Programme</span></div>
      <h2 class="section-heading reveal{delay}" id="{sid}-heading">{h}</h2>
      {body}
    </div>
  </section>
'''
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="icon" href="../assets/brand/favicon-32.png" type="image/png" sizes="32x32">
  <link rel="apple-touch-icon" href="../assets/brand/apple-touch-icon.png">
  <title>{title} — KBI Hong Kong</title>
  <meta name="description" content="{meta}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../kbi-hk.css">
</head>
<body>

  <div class="announcement-bar" id="announcementBar">
    <div class="announcement-bar-inner">
      <p><span class="ab-badge">New</span> Two upcoming events in 2026: ETO Eastern Conference (9–11 Oct, CDNIS) and the launch of FinTech SkillSprint. <a href="../upcoming events/events.html">View events &rarr;</a></p>
    </div>
    <button class="announcement-close" id="announcementClose" aria-label="Close announcement">&#x2715;</button>
  </div>

  <nav class="site-nav nav-light" id="siteNav" role="navigation" aria-label="Main navigation">
    <div class="nav-inner">
      <a href="../index.html" class="nav-logo" aria-label="KBI Hong Kong — home">
        <div class="nav-logo-mark"><img src="../assets/brand/logo-icon.png" alt="" class="brand-mark-img" width="40" height="40"></div>
        <div class="nav-wordmark"><span class="nav-wordmark-name">KBI Hong Kong</span><span class="nav-wordmark-sub">Königsberger Bridges Institute</span></div>
      </a>
      <ul class="nav-links" role="list">
        <li class="has-dropdown">
          <button class="nav-dropdown-trigger" aria-expanded="false" aria-controls="dd-about">About <svg viewBox="0 0 10 10" fill="none" aria-hidden="true"><path d="M2 3.5l3 3 3-3" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/></svg></button>
          <div class="nav-dropdown" id="dd-about" role="menu">
            <a href="../about/about-who-we-are.html" role="menuitem">Who We Are</a>
            <a href="../about/about-history.html" role="menuitem">Our History</a>
            <a href="../about/about-impact.html" role="menuitem">Our Impact</a>
            <a href="../about/about-team.html" role="menuitem">Our Team</a>
            <div class="nav-dropdown-divider"></div>
            <a href="../media.html" role="menuitem">Media &amp; Brand Kit</a>
          </div>
        </li>
        <li class="has-dropdown">
          <button class="nav-dropdown-trigger" aria-expanded="false" aria-controls="dd-prog">Programmes <svg viewBox="0 0 10 10" fill="none" aria-hidden="true"><path d="M2 3.5l3 3 3-3" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/></svg></button>
          <div class="nav-dropdown" id="dd-prog" role="menu">
            <div class="nav-dropdown-label">Compete</div>
            <a href="../upcoming events/eto2026.html" role="menuitem">Emerging Technologies Olympiad (ETO)</a>
            <a href="i2ol.html" role="menuitem">I&sup2;OL Scheme</a>
            <div class="nav-dropdown-divider"></div>
            <div class="nav-dropdown-label">Certify</div>
            <a href="etti.html" role="menuitem">Emerging Tech Training &amp; Internship (ETTI) Program</a>
            <a href="abc5.html" role="menuitem">AI, Blockchain, Cybersecurity (ABC5) Program</a>
            <a href="isfretic.html" role="menuitem">International Standards Framework of Reference for Emerging Technologies Innovation and Competency (ISFRETIC)</a>
            <div class="nav-dropdown-divider"></div>
            <div class="nav-dropdown-label">Collab</div>
            <a href="projects.html" role="menuitem">Project Support</a>
            <a href="working-research-groups.html" role="menuitem">Working &amp; Research Groups</a>
            <div class="nav-dropdown-divider"></div>
            <div class="nav-dropdown-label">Connect</div>
            <a href="community.html#socratic" role="menuitem">Socratic Circles</a>
            <a href="community.html#gatherings" role="menuitem">KBI Community Gatherings</a>
          </div></li>
        <li><a href="../upcoming events/events.html">Events</a></li>
        <li class="hide-md"><a href="../news/news.html">News</a></li>
        <li><a href="../contact.html">Contact</a></li>
      </ul>
      <div class="nav-ctas">
        <a href="sponsors.html#enquiry" class="btn btn-outline-prussian btn--sm">Partner With Us</a>
        <a href="membership.html" class="btn btn-yellow btn--sm">Join Us</a>
      </div>
      <button class="nav-hamburger" id="navHamburger" aria-label="Open navigation" aria-expanded="false" aria-controls="navMobile"><span></span><span></span><span></span></button>
    </div>
  </nav>

  <nav class="nav-mobile" id="navMobile" aria-label="Mobile navigation">
    <div class="nav-mobile-section-label">About</div>
    <a href="../about/about-who-we-are.html" class="nav-mobile-link">Who We Are</a>
    <a href="../about/about-history.html" class="nav-mobile-sub">Our History</a>
    <a href="../about/about-impact.html" class="nav-mobile-sub">Our Impact</a>
    <a href="../about/about-team.html" class="nav-mobile-sub">Our Team</a>
    <a href="../media.html" class="nav-mobile-sub">Media &amp; Brand Kit</a>
    <div class="nav-mobile-section-label">Compete</div>
    <a href="../upcoming events/eto2026.html" class="nav-mobile-link">ETO Eastern Conference (2026)</a>
    <a href="i2ol.html" class="nav-mobile-sub">I&sup2;OL Scheme</a>
    <div class="nav-mobile-section-label">Certify</div>
    <a href="etti.html" class="nav-mobile-sub">ETTI Program</a>
    <a href="abc5.html" class="nav-mobile-sub">ABC5 Program</a>
    <a href="isfretic.html" class="nav-mobile-sub">ISFRETIC</a>
    <div class="nav-mobile-section-label">Collab</div>
    <a href="projects.html" class="nav-mobile-sub">Project Support</a>
    <a href="working-research-groups.html" class="nav-mobile-sub">Working &amp; Research Groups</a>
    <div class="nav-mobile-section-label">Connect</div>
    <a href="community.html#socratic" class="nav-mobile-sub">Socratic Circles</a>
    <a href="community.html#gatherings" class="nav-mobile-sub">KBI Community Gatherings</a>
    <div class="nav-mobile-section-label">Navigate</div>
    <a href="../upcoming events/events.html" class="nav-mobile-link">Events</a>
    <a href="../news/news.html" class="nav-mobile-link">News &amp; Insights</a>
    <a href="../faq.html" class="nav-mobile-link">FAQ</a>
    <a href="../contact.html" class="nav-mobile-link">Contact</a>
    <div class="nav-mobile-ctas">
      <a href="sponsors.html#enquiry" class="btn btn-outline-white">Partner With Us</a>
      <a href="membership.html" class="btn btn-yellow">Join Us</a>
    </div>
  </nav>

  <header class="page-hero page-hero--night" aria-label="{title}">
    <div class="page-hero-bg" aria-hidden="true" style="position:absolute;inset:0;background:linear-gradient(160deg, var(--night) 0%, var(--prussian) 100%);"></div>
    <div class="page-hero-inner" style="position:relative;z-index:1;">
      <div class="label-row"><div class="u-rule u-rule--white" aria-hidden="true"></div><span class="u-label u-label--light">{label}</span></div>
      <h1 class="page-hero-heading">{heading}</h1>
      <p class="page-hero-sub" style="max-width:720px;">{lead}</p>
    </div>
  </header>
{body_sections}
  <section class="section-wrap section-wrap--white" aria-labelledby="related-heading">
    <div class="section-inner">
      <div class="label-row"><div class="u-rule" aria-hidden="true"></div><span class="u-label">Related Programmes</span></div>
      <h2 class="section-heading reveal" id="related-heading">Other Certify Programmes</h2>
      <div class="what-grid" style="margin-top:32px;">
        <article class="what-card reveal">
          <h3>ETTI</h3>
          <p>Training and internship pathways with universities and industry.</p>
          <a href="etti.html" class="what-card-link">ETTI programme</a>
        </article>
        <article class="what-card reveal reveal-delay-1">
          <h3>ABC5</h3>
          <p>Cross-cutting literacy in AI, blockchain, and cybersecurity.</p>
          <a href="abc5.html" class="what-card-link">ABC5 programme</a>
        </article>
        <article class="what-card reveal reveal-delay-2">
          <h3>ISFRETIC</h3>
          <p>Independent certification framework for emerging-technology competence.</p>
          <a href="isfretic.html" class="what-card-link">ISFRETIC framework</a>
        </article>
      </div>
    </div>
  </section>

  <section class="cta-band" aria-label="Get involved">
    <div class="cta-band-inner">
      <h2 class="cta-band-heading reveal">Interested in this programme?</h2>
      <p class="cta-band-body reveal reveal-delay-1">Contact KBI Hong Kong to learn about upcoming cohorts, partnerships, and how to participate.</p>
      <div class="cta-band-actions reveal reveal-delay-2">
        <a href="../contact.html" class="btn btn-yellow">Contact Us</a>
        <a href="membership.html" class="btn btn-white">Join KBI HK</a>
      </div>
    </div>
  </section>

  <footer class="site-footer" role="contentinfo">
    <div class="footer-inner">
      <div class="footer-brand">
        <div class="footer-logo">
          <div class="footer-logo-mark" aria-hidden="true"><img src="../assets/brand/logo-icon.png" alt="" class="brand-mark-img" width="40" height="40"></div>
          <span class="footer-logo-name">KBI Hong Kong</span>
        </div>
        <p class="footer-tagline">Building Hong Kong's pipeline of emerging technology talent through competitions, research, and community.</p>
        <p class="footer-copyright">&copy; 2026 KBI Hong Kong. All rights reserved.</p>
      </div>
      <div class="footer-cols">
        <div class="footer-col">
          <h3 class="footer-col-heading">Programmes</h3>
          <ul role="list">
            <li><a href="etti.html">ETTI</a></li>
            <li><a href="abc5.html">ABC5</a></li>
            <li><a href="isfretic.html">ISFRETIC</a></li>
            <li><a href="i2ol.html">I&sup2;OL Scheme</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h3 class="footer-col-heading">Community</h3>
          <ul role="list">
            <li><a href="../upcoming events/events.html">Events</a></li>
            <li><a href="membership.html">Membership</a></li>
            <li><a href="../contact.html">Contact</a></li>
          </ul>
        </div>
      </div>
    </div>
  </footer>
  <script src="../kbi-hk.js"></script>
</body>
</html>
'''


def make_training_pages() -> None:
    etti = prog_page(
        filename="etti.html",
        title="ETTI",
        meta="Emerging Tech Training & Internship (ETTI) — structured training and internship pathways connecting students to applied emerging-technology work in Hong Kong.",
        label="Training Programme",
        heading="Emerging Tech Training<br>&amp; Internship (ETTI)",
        lead="Structured training and internship pathways that connect classroom learning to applied emerging-technology work — run in partnership with universities and industry. ETTI is a training programme, not a certification exam.",
        sections=[
            (
                "about",
                "What ETTI Is",
                '''<p class="section-body reveal reveal-delay-1" style="max-width:720px;">ETTI places students in serious, supervised emerging-technology environments — combining taught components with internship-style exposure so participants learn how professional teams actually work on blockchain, data, AI, and related systems.</p>
      <p class="section-body reveal reveal-delay-2" style="max-width:720px;margin-top:16px;">Past Hong Kong initiatives under this family include university-hosted training internships (such as LETTI at Lingnan). New cohorts are announced when partner institutions and industry hosts are confirmed.</p>''',
                "white",
            ),
            (
                "how",
                "How It Works",
                '''<p class="section-body reveal reveal-delay-1" style="max-width:720px;">Typical ETTI pathways include:</p>
      <ul class="section-body reveal reveal-delay-2" style="max-width:720px;margin-top:12px;line-height:1.85;">
        <li>Structured modules in an emerging-technology domain</li>
        <li>Mentored project or lab work with a university or industry host</li>
        <li>Reflection and skills documentation aligned to professional practice</li>
      </ul>
      <p class="section-body reveal reveal-delay-3" style="max-width:720px;margin-top:16px;">ETTI complements — but is separate from — <a href="isfretic.html">ISFRETIC</a>, KBI's independent certification framework. Training through ETTI may prepare you for ISFRETIC assessments when those open in your field.</p>''',
                "mist",
            ),
        ],
    )
  # Fix related cards on etti - hide self link
    etti = etti.replace(
        '''        <article class="what-card reveal">
          <h3>ETTI</h3>
          <p>Training and internship pathways with universities and industry.</p>
          <a href="etti.html" class="what-card-link">ETTI programme</a>
        </article>
        <article class="what-card reveal reveal-delay-1">''',
        '''        <article class="what-card reveal">''',
    )
    (PROG / "etti.html").write_text(etti, encoding="utf-8")

    abc5 = prog_page(
        filename="abc5.html",
        title="ABC5",
        meta="AI, Blockchain, Cybersecurity (ABC5) — KBI Hong Kong's cross-cutting programme for literacy and applied skills across three foundational technology domains.",
        label="Training Programme",
        heading="AI, Blockchain,<br>Cybersecurity (ABC5)",
        lead="A cross-cutting programme building literacy and applied skills across artificial intelligence, blockchain, and cybersecurity — the three domains that increasingly define serious technology work.",
        sections=[
            (
                "about",
                "Why ABC5",
                '''<p class="section-body reveal reveal-delay-1" style="max-width:720px;">Emerging-technology careers rarely sit in a single silo. Builders need to understand how AI systems are governed, how distributed trust works, and how security constraints shape every design decision. ABC5 treats those three domains as one integrated literacy programme.</p>''',
                "white",
            ),
            (
                "covers",
                "What Participants Learn",
                '''<p class="section-body reveal reveal-delay-1" style="max-width:720px;">ABC5 sessions and materials are designed to give students practical orientation across:</p>
      <ul class="section-body reveal reveal-delay-2" style="max-width:720px;margin-top:12px;line-height:1.85;">
        <li><strong>Artificial intelligence</strong> — models, agents, governance, and responsible use</li>
        <li><strong>Blockchain &amp; trust technologies</strong> — ledgers, identity, smart contracts, and policy context</li>
        <li><strong>Cybersecurity</strong> — threat models, secure design, and operational hygiene</li>
      </ul>
      <p class="section-body reveal reveal-delay-3" style="max-width:720px;margin-top:16px;">ABC5 is a training programme. Formal credentials are issued through <a href="isfretic.html">ISFRETIC</a> when assessments are available — not through ABC5 itself.</p>''',
                "mist",
            ),
        ],
    )
    abc5 = abc5.replace(
        '''        <article class="what-card reveal reveal-delay-1">
          <h3>ABC5</h3>
          <p>Cross-cutting literacy in AI, blockchain, and cybersecurity.</p>
          <a href="abc5.html" class="what-card-link">ABC5 programme</a>
        </article>
        <article class="what-card reveal reveal-delay-2">''',
        '''        <article class="what-card reveal reveal-delay-1">''',
    )
    (PROG / "abc5.html").write_text(abc5, encoding="utf-8")


def certifications_redirect() -> None:
    (PROG / "certifications.html").write_text(
        '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="refresh" content="0; url=isfretic.html">
  <link rel="canonical" href="isfretic.html">
  <title>Redirecting…</title>
  <script>location.replace('isfretic.html');</script>
</head>
<body>
  <p>Certification pages are now separate: <a href="isfretic.html">ISFRETIC</a>, <a href="etti.html">ETTI</a>, <a href="abc5.html">ABC5</a>.</p>
</body>
</html>
''',
        encoding="utf-8",
    )


def patch_nav_links() -> int:
    replacements = [
        (r"certifications\.html#isfretic", "isfretic.html"),
        (r"certifications\.html#etti", "etti.html"),
        (r"certifications\.html#abc5", "abc5.html"),
        (r"programme/certifications\.html#isfretic", "programme/isfretic.html"),
        (r"programme/certifications\.html#etti", "programme/etti.html"),
        (r"programme/certifications\.html#abc5", "programme/abc5.html"),
        (r'href="certifications\.html"(?!#)', 'href="isfretic.html"'),
        (r'href="../programme/certifications\.html"(?!#)', 'href="../programme/isfretic.html"'),
        (r'href="programme/certifications\.html"(?!#)', 'href="programme/isfretic.html"'),
    ]
    count = 0
    for html in ROOT.rglob("*.html"):
        if html.name == "certifications.html" and html.parent == PROG:
            continue
        text = html.read_text(encoding="utf-8")
        orig = text
        for pat, repl in replacements:
            text = re.sub(pat, repl, text)
        if text != orig:
            html.write_text(text, encoding="utf-8")
            count += 1
    return count


def patch_programmes_hub() -> None:
    path = PROG / "programmes.html"
    text = path.read_text(encoding="utf-8")
    old = '''      <a href="certifications.html" class="prog-hub-card reveal" aria-label="Certifications — Training and ISFRETIC certification">
        <div class="prog-hub-card-top-bar prog-hub-card-top-bar--prussian"></div>
        <div class="prog-hub-card-body">
          <div class="prog-hub-card-icon" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" width="22" height="22"><path d="M12 2l2.5 5 5.5.75-4 3.9.95 5.5L12 14.5l-4.95 2.65.95-5.5-4-3.9 5.5-.75L12 2z"/><path d="M8 21h8M12 17v4"/></svg>
          </div>
          <div class="prog-hub-card-category">Training & Credentials</div>
          <h3>Certifications &amp; Training</h3>
          <p>Structured clinics in blockchain, data science, and quantum computing — building competition-ready foundations and leading to ISFRETIC certification, recognised internationally by the Königsberger Bridges Institute.</p>
          <div class="prog-hub-card-tags">
            <span class="prog-hub-card-tag">6-Session Clinics</span>
            <span class="prog-hub-card-tag">ISFRETIC Cert</span>
            <span class="prog-hub-card-tag">3 Tracks</span>
          </div>
          <span class="prog-hub-card-cta">
            View certifications
            <svg viewBox="0 0 12 12" fill="none" width="14" height="14" aria-hidden="true"><path d="M2 6h8M6 2l4 4-4 4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </span>
        </div>
      </a>'''
    new = '''      <a href="isfretic.html" class="prog-hub-card reveal" aria-label="ISFRETIC certification framework">
        <div class="prog-hub-card-top-bar prog-hub-card-top-bar--prussian"></div>
        <div class="prog-hub-card-body">
          <div class="prog-hub-card-icon" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" width="22" height="22"><path d="M12 2l2.5 5 5.5.75-4 3.9.95 5.5L12 14.5l-4.95 2.65.95-5.5-4-3.9 5.5-.75L12 2z"/><path d="M8 21h8M12 17v4"/></svg>
          </div>
          <div class="prog-hub-card-category">Certification</div>
          <h3>ISFRETIC</h3>
          <p>KBI's independent certification framework for blockchain, data science &amp; AI, and quantum — competence defined by what you can do, not courses attended.</p>
          <div class="prog-hub-card-tags">
            <span class="prog-hub-card-tag">BCTT · DSAI · QCIT</span>
            <span class="prog-hub-card-tag">A1–C2 Scale</span>
          </div>
          <span class="prog-hub-card-cta">
            View ISFRETIC
            <svg viewBox="0 0 12 12" fill="none" width="14" height="14" aria-hidden="true"><path d="M2 6h8M6 2l4 4-4 4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </span>
        </div>
      </a>

      <a href="etti.html" class="prog-hub-card reveal reveal-delay-1" aria-label="ETTI training programme">
        <div class="prog-hub-card-top-bar prog-hub-card-top-bar--cyan"></div>
        <div class="prog-hub-card-body">
          <div class="prog-hub-card-category">Training</div>
          <h3>ETTI</h3>
          <p>Emerging Tech Training &amp; Internship — university and industry pathways from classroom to applied work.</p>
          <span class="prog-hub-card-cta">View ETTI <svg viewBox="0 0 12 12" fill="none" width="14" height="14" aria-hidden="true"><path d="M2 6h8M6 2l4 4-4 4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
        </div>
      </a>

      <a href="abc5.html" class="prog-hub-card reveal reveal-delay-2" aria-label="ABC5 programme">
        <div class="prog-hub-card-top-bar prog-hub-card-top-bar--yellow"></div>
        <div class="prog-hub-card-body">
          <div class="prog-hub-card-category">Training</div>
          <h3>ABC5</h3>
          <p>AI, Blockchain, Cybersecurity — integrated literacy across the three domains that define modern technology work.</p>
          <span class="prog-hub-card-cta">View ABC5 <svg viewBox="0 0 12 12" fill="none" width="14" height="14" aria-hidden="true"><path d="M2 6h8M6 2l4 4-4 4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
        </div>
      </a>'''
    if old in text:
        text = text.replace(old, new)
        path.write_text(text, encoding="utf-8")


def main() -> None:
    make_isfretic()
    make_training_pages()
    certifications_redirect()
    n = patch_nav_links()
    patch_programmes_hub()
    # Fix isfretic.html nav (created before redirect overwrote certifications source nav)
    patch_nav_links()
    print("Created isfretic.html, etti.html, abc5.html; redirect certifications.html")
    print(f"Updated nav links in {n} files")


if __name__ == "__main__":
    main()
