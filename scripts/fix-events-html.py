#!/usr/bin/env python3
"""Clean up events.html markup and replace inline styles with CSS classes."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PATH = ROOT / "upcoming events" / "events.html"

text = PATH.read_text(encoding="utf-8")

# Hero
text = text.replace(
    '<header class="page-hero page-hero--night" aria-label="Events page header" style="position:relative;overflow:hidden;">\n'
    '  <div class="page-hero-bg" aria-hidden="true" style="position:absolute;inset:0;background:linear-gradient(160deg, var(--night) 0%, var(--prussian) 100%);background-size:cover;background-position:center;opacity:0.13;"></div>\n'
    '  <div class="page-hero-inner" style="position:relative;z-index:1;">',
    '<header class="page-hero page-hero--night" aria-label="Events page header">\n'
    '  <div class="page-hero-grid" aria-hidden="true"></div>\n'
    '  <div class="page-hero-inner">',
)

# Tabs bar
text = text.replace(
    '<div style="border-bottom:1px solid var(--stone);background:var(--white);">\n'
    '  <div style="max-width:var(--max-width);margin:0 auto;padding:0 24px;">',
    '<div class="events-tabs-bar">\n'
    '  <div class="events-tabs-inner">',
)

# Section heading margins via utility-ish inline removal
text = text.replace(
    '<h2 class="section-heading reveal" id="upcoming-heading" style="margin-bottom:40px;">',
    '<h2 class="section-heading reveal section-heading--spaced" id="upcoming-heading">',
)
text = text.replace(
    '<h2 class="section-heading reveal" id="past-heading" style="margin-bottom:16px;">',
    '<h2 class="section-heading reveal" id="past-heading">',
)
text = text.replace(
    '<p class="section-body reveal reveal-delay-1" style="max-width:640px;margin-bottom:32px;">',
    '<p class="section-body reveal reveal-delay-1 section-body--narrow">',
)

# Featured ETO card
text = text.replace(
    '<div id="eto-eastern-2026" style="background:linear-gradient(135deg,var(--ink),var(--prussian));border-radius:var(--radius-lg);overflow:hidden;margin-bottom:40px;display:grid;grid-template-columns:1fr 2fr;min-height:280px;" class="reveal">\n'
    '        <div style="position:relative;overflow:hidden;display:flex;align-items:center;justify-content:center;padding:40px;border-right:1px solid rgba(255,255,255,0.06);">\n'
    '          <div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;opacity:0.08;">\n'
    '            <svg viewBox="0 0 120 120" fill="none" style="width:120px;"><path d="M60 10L75 40H105L82 62L92 92L60 75L28 92L38 62L15 40H45L60 10Z" stroke="white" stroke-width="3" stroke-linejoin="round"/></svg>\n'
    '          </div>\n'
    '          <div style="text-align:center;position:relative;">\n'
    '            <div style="font-family:\'Playfair Display\',serif;font-size:2.25rem;font-weight:700;color:var(--white);line-height:1.1;">9–11 Oct</div>\n'
    '            <div style="font-family:\'Playfair Display\',serif;font-size:1.5rem;font-weight:500;color:rgba(255,255,255,0.5);">2026</div>\n'
    '          </div>\n'
    '        </div>\n'
    '        <div style="padding:36px 40px;display:flex;flex-direction:column;justify-content:center;">\n'
    '          <div style="display:flex;gap:8px;margin-bottom:14px;flex-wrap:wrap;">\n'
    '            <span class="tag tag--night">Conference</span>\n'
    '            <span class="tag" style="background:rgba(255,209,102,0.15);color:var(--yellow);">Flagship</span>\n'
    '          </div>\n'
    '          <h3 style="font-size:1.5rem;color:var(--white);margin-bottom:12px;">ETO Eastern Conference 2026</h3>\n'
    '          <p style="font-family:\'Inter\',sans-serif;font-size:0.9375rem;color:rgba(255,255,255,0.52);line-height:1.8;margin-bottom:24px;">',
    '<div id="eto-eastern-2026" class="evt-featured-card evt-featured-card--eto reveal">\n'
    '        <div class="evt-featured-aside">\n'
    '          <div class="evt-featured-aside-bg" aria-hidden="true">\n'
    '            <svg viewBox="0 0 120 120" fill="none"><path d="M60 10L75 40H105L82 62L92 92L60 75L28 92L38 62L15 40H45L60 10Z" stroke="white" stroke-width="3" stroke-linejoin="round"/></svg>\n'
    '          </div>\n'
    '          <div class="evt-featured-date-block">\n'
    '            <div class="evt-featured-date-main">9–11 Oct</div>\n'
    '            <div class="evt-featured-date-sub">2026</div>\n'
    '          </div>\n'
    '        </div>\n'
    '        <div class="evt-featured-body">\n'
    '          <div class="evt-featured-tags">\n'
    '            <span class="tag tag--night">Conference</span>\n'
    '            <span class="tag tag--featured">Flagship</span>\n'
    '          </div>\n'
    '          <h3 class="evt-featured-title">ETO Eastern Conference 2026</h3>\n'
    '          <p class="evt-featured-desc">',
)

text = text.replace(
    '</p>\n'
    '          <div style="display:flex;gap:12px;flex-wrap:wrap;">\n'
    '            <a href="https://forms.gle/7WwvpwKxkDXtRbK2A"',
    '</p>\n'
    '          <div class="evt-featured-actions">\n'
    '            <a href="https://forms.gle/7WwvpwKxkDXtRbK2A"',
    1,
)

# Featured ETS card
text = text.replace(
    '<div id="ets-2026" style="background:linear-gradient(135deg,var(--deep-blue),var(--prussian));border-radius:var(--radius-lg);overflow:hidden;margin-bottom:40px;display:grid;grid-template-columns:1fr 2fr;min-height:280px;" class="reveal">\n'
    '        <div style="position:relative;overflow:hidden;display:flex;align-items:center;justify-content:center;padding:40px;border-right:1px solid rgba(255,255,255,0.06);">\n'
    '          <div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;opacity:0.08;">\n'
    '            <svg viewBox="0 0 120 120" fill="none" style="width:120px;"><path d="M20 55 L40 20 L60 55 Z" stroke="white" stroke-width="3" stroke-linejoin="round"/><line x1="28" y1="45" x2="52" y2="45" stroke="white" stroke-width="3"/></svg>\n'
    '          </div>\n'
    '          <div style="text-align:center;position:relative;">\n'
    '            <div style="font-family:\'Playfair Display\',serif;font-size:2rem;font-weight:700;color:var(--white);line-height:1.1;">2026</div>\n'
    '            <div style="font-family:\'Inter\',sans-serif;font-size:0.75rem;font-weight:600;letter-spacing:0.12em;text-transform:uppercase;color:rgba(255,255,255,0.45);margin-top:8px;">Hong Kong</div>\n'
    '          </div>\n'
    '        </div>\n'
    '        <div style="padding:36px 40px;display:flex;flex-direction:column;justify-content:center;">\n'
    '          <div style="display:flex;gap:8px;margin-bottom:14px;flex-wrap:wrap;">\n'
    '            <span class="tag tag--night">SkillSprint Series</span>\n'
    '            <span class="tag" style="background:rgba(255,209,102,0.15);color:var(--yellow);">Training</span>\n'
    '          </div>\n'
    '          <h3 style="font-size:1.5rem;color:var(--white);margin-bottom:12px;">Emerging-Technology SkillSprint (ETS)</h3>\n'
    '          <p style="font-family:\'Inter\',sans-serif;font-size:0.9375rem;color:rgba(255,255,255,0.52);line-height:1.8;margin-bottom:24px;">',
    '<div id="ets-2026" class="evt-featured-card evt-featured-card--ets reveal">\n'
    '        <div class="evt-featured-aside">\n'
    '          <div class="evt-featured-aside-bg" aria-hidden="true">\n'
    '            <svg viewBox="0 0 120 120" fill="none"><path d="M20 55 L40 20 L60 55 Z" stroke="white" stroke-width="3" stroke-linejoin="round"/><line x1="28" y1="45" x2="52" y2="45" stroke="white" stroke-width="3"/></svg>\n'
    '          </div>\n'
    '          <div class="evt-featured-date-block">\n'
    '            <div class="evt-featured-date-main">2026</div>\n'
    '            <div class="evt-featured-date-label">Hong Kong</div>\n'
    '          </div>\n'
    '        </div>\n'
    '        <div class="evt-featured-body">\n'
    '          <div class="evt-featured-tags">\n'
    '            <span class="tag tag--night">SkillSprint Series</span>\n'
    '            <span class="tag tag--featured">Training</span>\n'
    '          </div>\n'
    '          <h3 class="evt-featured-title">Emerging-Technology SkillSprint (ETS)</h3>\n'
    '          <p class="evt-featured-desc">',
)

text = text.replace(
    '<a href="../contact.html" class="btn btn-yellow btn--sm">Register Interest</a>\n'
    '            <a href="ets2026.html" class="btn btn-ghost-light btn--sm">Full Event Details</a>\n'
    '          </div>\n'
    '        </div>\n'
    '      </div>\n\n'
    '      <!-- Newsletter CTA -->',
    '<a href="../contact.html" class="btn btn-yellow btn--sm">Register Interest</a>\n'
    '            <a href="ets2026.html" class="btn btn-ghost-light btn--sm">Full Event Details</a>\n'
    '          </div>\n'
    '        </div>\n'
    '      </div>\n\n'
    '      <!-- Newsletter CTA -->',
)

# Fix ETS actions wrapper - the ETO card still has old div close - need second replace for ets actions
text = text.replace(
    '          <div style="display:flex;gap:12px;flex-wrap:wrap;">\n'
    '            <a href="../contact.html" class="btn btn-yellow btn--sm">Register Interest</a>',
    '          <div class="evt-featured-actions">\n'
    '            <a href="../contact.html" class="btn btn-yellow btn--sm">Register Interest</a>',
    1,
)

# Newsletter
text = text.replace(
    '<div style="margin-top:48px;background:var(--mist);border:1px solid var(--stone);border-radius:var(--radius-lg);padding:32px 36px;display:flex;align-items:center;gap:28px;flex-wrap:wrap;" class="reveal">\n'
    '        <div style="flex:1;min-width:220px;">\n'
    '          <h4 style="font-size:1.0625rem;margin-bottom:6px;">Don\'t miss a KBI HK event.</h4>\n'
    '          <p style="font-family:\'Inter\',sans-serif;font-size:0.875rem;color:var(--text-muted);">Subscribe to receive event announcements directly in your inbox.</p>\n'
    '        </div>\n'
    '        <form style="display:flex;gap:10px;flex-shrink:0;" id="newsletterForm" novalidate>\n'
    '          <label for="evt-nl-email" class="sr-only">Email address</label>\n'
    '          <input type="email" id="evt-nl-email" class="newsletter-input" placeholder="your@email.com" style="min-width:220px;background:rgba(0,49,83,0.06);border-color:var(--stone);color:var(--text-main);" required>',
    '<div class="evt-newsletter-cta reveal">\n'
    '        <div class="evt-newsletter-cta-copy">\n'
    '          <h4>Don\'t miss a KBI HK event.</h4>\n'
    '          <p>Subscribe to receive event announcements directly in your inbox.</p>\n'
    '        </div>\n'
    '        <form class="evt-newsletter-form" id="newsletterForm" novalidate>\n'
    '          <label for="evt-nl-email" class="sr-only">Email address</label>\n'
    '          <input type="email" id="evt-nl-email" class="newsletter-input" placeholder="your@email.com" required>',
)

# Past events cleanup
text = text.replace(
    ' style="font-family:\'Inter\',sans-serif;font-size:0.8125rem;color:var(--text-faint);margin-top:4px;"',
    '',
)
text = text.replace(
    '<div style="font-family:\'Inter\',sans-serif;font-size:0.8125rem;color:var(--text-faint);margin-top:4px;">',
    '<div class="past-event-meta">',
)
text = text.replace(' class="past-event-meta">', ' class="past-event-meta">', 1)  # noop guard

# Fix meta divs that lost class when style removed
import re
text = re.sub(
    r'(<div class="past-event-title">[^<]+</div>\n)\s*<div>([^<]+)</div>',
    r'\1          <div class="past-event-meta">\2</div>',
    text,
)

text = re.sub(
    r'<h3 class="past-events-year" style="[^"]*">',
    '<h3 class="past-events-year">',
    text,
)
text = re.sub(
    r' class="past-event-item([^"]*)" style="text-decoration:none;color:inherit;"',
    r' class="past-event-item\1"',
    text,
)

text = text.replace('\n      <br>\n\n      <div class="past-events-list">', '\n\n      <div class="past-events-list">')

PATH.write_text(text, encoding="utf-8")
print("events.html updated")
