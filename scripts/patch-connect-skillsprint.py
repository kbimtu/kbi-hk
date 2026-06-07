#!/usr/bin/env python3
"""Patch body content for socratic, gatherings, and skillsprint pages."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROG = ROOT / "programme"

PAGES = {
    "socratic.html": {
        "title": "Socratic Circles — KBI Hong Kong",
        "meta": "Socratic Circles — structured KBI HK sessions where teams test ideas through questioning and critique before competitions and presentations.",
        "hero_class": "page-hero--prussian",
        "label": "Connect",
        "h1": "Socratic Circles",
        "intro": "Structured sessions where teams test ideas through questioning and critique — sharpening logic, assumptions, and project foundations before competitions and presentations.",
        "sections": """
  <section class="section-wrap section-wrap--white" id="about" aria-labelledby="about-heading">
    <div class="section-inner">
      <div class="label-row"><div class="u-rule" aria-hidden="true"></div><span class="u-label">About</span></div>
      <h2 class="section-heading reveal" id="about-heading">Thinking through questions, not slides</h2>
      <p class="section-body reveal reveal-delay-1" style="max-width:720px;">A Socratic Circle is not a lecture and not a pitch. It is a facilitated session where a team presents its thinking — and other participants ask questions designed to expose assumptions, test logic, and strengthen the underlying argument.</p>
      <p class="section-body reveal reveal-delay-2" style="max-width:720px;margin-top:16px;">The format is especially valuable before major competitions, project reviews, and public presentations, when teams need honest feedback rather than encouragement alone.</p>
    </div>
  </section>
  <section class="section-wrap section-wrap--mist" id="how" aria-labelledby="how-heading">
    <div class="section-inner">
      <div class="label-row"><div class="u-rule" aria-hidden="true"></div><span class="u-label">How It Works</span></div>
      <h2 class="section-heading reveal" id="how-heading">A typical session</h2>
      <ul class="reveal reveal-delay-1" style="max-width:720px;margin-top:28px;list-style:none;display:flex;flex-direction:column;gap:16px;">
        <li style="font-family:'Inter',sans-serif;font-size:0.9375rem;color:var(--text-muted);line-height:1.75;display:flex;gap:12px;"><span style="color:var(--prussian);font-weight:700;">·</span>A team presents its project, research question, or competition approach in a fixed time.</li>
        <li style="font-family:'Inter',sans-serif;font-size:0.9375rem;color:var(--text-muted);line-height:1.75;display:flex;gap:12px;"><span style="color:var(--prussian);font-weight:700;">·</span>Participants ask questions — no speeches, no premature solutions.</li>
        <li style="font-family:'Inter',sans-serif;font-size:0.9375rem;color:var(--text-muted);line-height:1.75;display:flex;gap:12px;"><span style="color:var(--prussian);font-weight:700;">·</span>A facilitator keeps the discussion rigorous, respectful, and on track.</li>
        <li style="font-family:'Inter',sans-serif;font-size:0.9375rem;color:var(--text-muted);line-height:1.75;display:flex;gap:12px;"><span style="color:var(--prussian);font-weight:700;">·</span>The team leaves with clearer priorities and stronger foundations for the work ahead.</li>
      </ul>
    </div>
  </section>
  <section class="section-wrap section-wrap--white" id="participate" aria-labelledby="participate-heading">
    <div class="section-inner">
      <div class="label-row"><div class="u-rule" aria-hidden="true"></div><span class="u-label">Participate</span></div>
      <h2 class="section-heading reveal" id="participate-heading">For teams and facilitators</h2>
      <p class="section-body reveal reveal-delay-1" style="max-width:720px;">Student teams preparing for IBCOL, IDSOL, IQCOL, ETO, or internal KBI projects can request or join Socratic Circles through KBI HK events. Fellows and Professional Members may also facilitate sessions as part of their membership pathway.</p>
      <p style="margin-top:24px;" class="reveal reveal-delay-2">
        <a href="membership.html" class="btn btn-outline-prussian">Membership pathways</a>
      </p>
    </div>
  </section>""",
        "cta_h": "Join a Socratic Circle",
        "cta_p": "Ask about upcoming sessions or request a circle for your team through KBI HK.",
    },
    "gatherings.html": {
        "title": "KBI Community Gatherings — KBI Hong Kong",
        "meta": "KBI Community Gatherings — regular meet-ups, briefings, and social events connecting KBI Hong Kong members across schools, tracks, and cohorts.",
        "hero_class": "page-hero--prussian",
        "label": "Connect",
        "h1": "KBI Community<br>Gatherings",
        "intro": "Regular meet-ups, briefings, and social events that keep members connected across schools, tracks, and cohorts — the informal layer of a community built on serious engagement.",
        "sections": """
  <section class="section-wrap section-wrap--white" id="about" aria-labelledby="about-heading">
    <div class="section-inner">
      <div class="label-row"><div class="u-rule" aria-hidden="true"></div><span class="u-label">About</span></div>
      <h2 class="section-heading reveal" id="about-heading">Staying connected between programmes</h2>
      <p class="section-body reveal reveal-delay-1" style="max-width:720px;">Competitions, training, and research programmes give members depth. Community Gatherings give them continuity — a regular rhythm of meet-ups where students, alumni, educators, and partners see one another as people, not only as programme participants.</p>
      <p class="section-body reveal reveal-delay-2" style="max-width:720px;margin-top:16px;">Gatherings may include briefings on upcoming KBI activities, informal networking, track-specific meet-ups, or social events tied to the chapter calendar.</p>
    </div>
  </section>
  <section class="section-wrap section-wrap--mist" id="what" aria-labelledby="what-heading">
    <div class="section-inner">
      <div class="label-row"><div class="u-rule" aria-hidden="true"></div><span class="u-label">What Happens</span></div>
      <h2 class="section-heading reveal" id="what-heading">Informal, but intentional</h2>
      <ul class="reveal reveal-delay-1" style="max-width:720px;margin-top:28px;list-style:none;display:flex;flex-direction:column;gap:16px;">
        <li style="font-family:'Inter',sans-serif;font-size:0.9375rem;color:var(--text-muted);line-height:1.75;display:flex;gap:12px;"><span style="color:var(--prussian);font-weight:700;">·</span>Chapter briefings and programme updates</li>
        <li style="font-family:'Inter',sans-serif;font-size:0.9375rem;color:var(--text-muted);line-height:1.75;display:flex;gap:12px;"><span style="color:var(--prussian);font-weight:700;">·</span>Cross-school and cross-track networking</li>
        <li style="font-family:'Inter',sans-serif;font-size:0.9375rem;color:var(--text-muted);line-height:1.75;display:flex;gap:12px;"><span style="color:var(--prussian);font-weight:700;">·</span>Alumni and mentor presence where available</li>
        <li style="font-family:'Inter',sans-serif;font-size:0.9375rem;color:var(--text-muted);line-height:1.75;display:flex;gap:12px;"><span style="color:var(--prussian);font-weight:700;">·</span>A welcoming entry point for new members</li>
      </ul>
    </div>
  </section>
  <section class="section-wrap section-wrap--white" id="join" aria-labelledby="join-heading">
    <div class="section-inner">
      <div class="label-row"><div class="u-rule" aria-hidden="true"></div><span class="u-label">Join In</span></div>
      <h2 class="section-heading reveal" id="join-heading">Open to the KBI community</h2>
      <p class="section-body reveal reveal-delay-1" style="max-width:720px;">Gatherings are announced through KBI HK events, newsletters, and member channels. Most are open to members; some may be cohort- or track-specific. Check the <a href="../upcoming events/events.html">Events page</a> for what is coming up.</p>
    </div>
  </section>""",
        "cta_h": "Come to the next gathering",
        "cta_p": "Join KBI HK membership to receive event announcements, or contact us if your school or group would like to co-host a gathering.",
    },
    "skillsprint.html": {
        "title": "SkillSprint — KBI Hong Kong",
        "meta": "SkillSprint — KBI Hong Kong's series of concentrated emerging-technology workshop editions. The 2026 edition is Emerging-Technology SkillSprint (ETS).",
        "hero_class": "page-hero--night",
        "label": "Training Programme",
        "h1": "SkillSprint",
        "intro": "A series of concentrated workshop editions in emerging technologies. Each year takes a defined theme and delivery context — from FinTech-focused sessions to broader emerging-technology training.",
        "sections": """
  <section class="section-wrap section-wrap--white" id="about" aria-labelledby="about-heading">
    <div class="section-inner">
      <div class="label-row"><div class="u-rule" aria-hidden="true"></div><span class="u-label">About the Series</span></div>
      <h2 class="section-heading reveal" id="about-heading">Short, serious, practical</h2>
      <p class="section-body reveal reveal-delay-1" style="max-width:720px;">SkillSprint is not a single fixed course. It is a programme family: each edition is a time-bound series of workshops designed to give participants practical exposure across selected domains without requiring a full academic term.</p>
      <p class="section-body reveal reveal-delay-2" style="max-width:720px;margin-top:16px;">Editions are named for their focus and year — for example, FinTech SkillSprint in 2025 and Emerging-Technology SkillSprint (ETS) in 2026.</p>
    </div>
  </section>
  <section class="section-wrap section-wrap--mist" id="editions" aria-labelledby="editions-heading">
    <div class="section-inner">
      <div class="label-row"><div class="u-rule" aria-hidden="true"></div><span class="u-label">Editions</span></div>
      <h2 class="section-heading reveal" id="editions-heading">Current and past editions</h2>
      <div class="prog-grid" style="margin-top:40px;">
        <article class="what-card reveal">
          <div class="what-card-icon" aria-hidden="true"><svg viewBox="0 0 22 22" fill="none"><path d="M20 55 L40 20 L60 55 Z" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></svg></div>
          <h3>ETS — Emerging-Technology SkillSprint (2026)</h3>
          <p>The 2026 edition broadens the SkillSprint model to emerging technologies across blockchain, data, AI, and related fields. Dates and venues to be announced.</p>
          <a href="../upcoming events/ets2026.html" class="what-card-link">ETS 2026 event page <svg viewBox="0 0 14 14" fill="none" aria-hidden="true"><path d="M2 7h10M7 2l5 5-5 5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
        </article>
        <article class="what-card reveal reveal-delay-1">
          <div class="what-card-icon" aria-hidden="true"><svg viewBox="0 0 22 22" fill="none"><rect x="3" y="5" width="16" height="14" rx="2" stroke="currentColor" stroke-width="1.5"/></svg></div>
          <h3>FinTech SkillSprint (2025)</h3>
          <p>A workshop series at City University of Hong Kong offering focused training in blockchain, trust technologies, data science, and AI.</p>
          <a href="../event gallery/event-gallery-2025.html#skillsprint-2025" class="what-card-link">2025 gallery <svg viewBox="0 0 14 14" fill="none" aria-hidden="true"><path d="M2 7h10M7 2l5 5-5 5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
        </article>
      </div>
    </div>
  </section>
  <section class="section-wrap section-wrap--white" id="pathway" aria-labelledby="pathway-heading">
    <div class="section-inner" style="max-width:760px;">
      <div class="label-row"><div class="u-rule" aria-hidden="true"></div><span class="u-label">Training &amp; Certification</span></div>
      <h2 class="section-heading reveal" id="pathway-heading">Workshops, not credentials</h2>
      <p class="section-body reveal reveal-delay-1">SkillSprint builds practical literacy and is recorded in KBI membership history. Formal credentials for demonstrated competence are issued separately through <a href="isfretic.html">ISFRETIC</a>. SkillSprint complements longer programmes such as <a href="etti.html">ETTI</a> and <a href="abc5.html">ABC5</a>.</p>
    </div>
  </section>""",
        "cta_h": "Interested in the next SkillSprint?",
        "cta_p": "Register your interest for ETS 2026 or ask about future editions and institutional partnerships.",
    },
}


def patch(filename: str, cfg: dict) -> None:
    path = PROG / filename
    text = path.read_text(encoding="utf-8")
    import re

    text = re.sub(r"<title>.*?</title>", f"<title>{cfg['title']}</title>", text, count=1)
    text = re.sub(
        r'<meta name="description" content="[^"]*">',
        f'<meta name="description" content="{cfg["meta"]}">',
        text,
        count=1,
    )
    body = f"""  <header class="page-hero {cfg['hero_class']}" aria-label="{cfg['h1']}">
    <div class="page-hero-bg" aria-hidden="true" style="position:absolute;inset:0;background:linear-gradient(160deg, var(--night) 0%, var(--prussian) 100%);"></div>
    <div class="page-hero-inner" style="position:relative;z-index:1;">
      <div class="label-row"><div class="u-rule u-rule--white" aria-hidden="true"></div><span class="u-label u-label--light">{cfg['label']}</span></div>
      <h1 class="page-hero-heading">{cfg['h1']}</h1>
      <p class="page-hero-sub" style="max-width:720px;">{cfg['intro']}</p>
    </div>
  </header>
{cfg['sections']}
  <section class="cta-band" aria-label="Get involved">
    <div class="cta-band-inner">
      <div class="label-row" style="justify-content:center;margin-bottom:24px;"><div class="u-rule" aria-hidden="true"></div><span class="u-label u-label--light">Connect</span></div>
      <h2 class="cta-band-heading reveal">{cfg['cta_h']}</h2>
      <p class="cta-band-body reveal reveal-delay-1">{cfg['cta_p']}</p>
      <div class="cta-band-actions reveal reveal-delay-2">
        <a href="../contact.html" class="btn btn-yellow">Contact KBI HK</a>
        <a href="membership.html" class="btn btn-white">Community Hub</a>
      </div>
    </div>
  </section>
"""
    text = re.sub(
        r"  <!-- HERO -->.*?  <footer class=\"site-footer\"",
        body + "\n  <footer class=\"site-footer\"",
        text,
        count=1,
        flags=re.DOTALL,
    )
    text = text.replace("<li><a href=\"etti.html\">ETTI</a></li>", "<li><a href=\"skillsprint.html\">SkillSprint</a></li>\n            <li><a href=\"etti.html\">ETTI</a></li>")
    path.write_text(text, encoding="utf-8")
    print(f"Patched {filename}")


def main() -> None:
    for name, cfg in PAGES.items():
        patch(name, cfg)


if __name__ == "__main__":
    main()
