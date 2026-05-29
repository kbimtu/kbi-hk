# KBI Hong Kong — Website

**KBI Hong Kong** is the Hong Kong regional chapter of the Königsberger Bridges Institute — a non-profit, youth-run organisation delivering rigorous emerging-technology education and talent development since 2016.

---

## Project Overview

Static multi-page website for KBI Hong Kong, covering programmes, events, membership, sponsors, community, impact, news, and contact. Built with plain HTML, CSS (`kbi-hk.css`), and JavaScript (`kbi-hk.js`). No build system. No server-side processing.

---

## Pages & Entry URIs

### Core Pages

| Page | File | Key Sections / Anchors |
|------|------|------------------------|
| Home | `index.html` | Hero, Stats, About preview, Programmes preview, Events, Sponsors, News, Stakeholder tabs, CTA |
| Programmes | `programmes.html` | `#eto`, `#ibcol`, `#idsol`, `#iqcol`, `#training`, `#community` |
| ETO HK 2026 | `eto2026.html` | Flagship programme — About, 3 Tracks, Streams table, Team types, Timeline, Judging, CTA |
| Events | `events.html` | `#upcoming`, `#past-events` |
| Membership | `membership.html` | `#membership-overview`, `#types`, `#community`, `#apply` |
| Sponsors | `sponsors.html` | `#why-sponsor`, `#tiers`, `#partner`, `#enquiry` |
| Community | `community.html` | `#who-we-are`, `#groups`, `#paths` |
| Impact | `impact.html` | `#numbers`, `#competition`, `#testimonials`, `#alumni` |
| News | `news.html` | `#announcements`, `#insights`, `#press` |
| Contact | `contact.html` | `#enquiry` |
| Competitions | `competitions.html` | `#ibcol`, `#idsol`, `#iqcol` — full track detail |
| Certifications | `certifications.html` | ISFRETIC Training & Certification pathways |
| Collaborations | `collaborations.html` | Campus Ambassadors, KBridge Apprenticeship |
| About (redirect shell) | `about.html` | Thin page linking to About sub-pages |

### About Sub-Pages (created Session 3–4)

| Page | File | Content |
|------|------|---------|
| Who We Are | `about-who-we-are.html` | Mission, values, what KBI HK does |
| Our History | `about-history.html` | Timeline from 2016 founding to present |
| Our Impact | `about-impact.html` | Animated counters, impact stats, competition record |
| Our Team | `about-team.html` | Executive Committee grid + Academic Advisers |
| Media & Brand Kit | `media.html` | Photo gallery, logo assets, press downloads |

### New Standalone Pages (created Session 3–4)

| Page | File | Content |
|------|------|---------|
| FAQ | `faq.html` | Accordion FAQ — Competitions, Membership, ETO HK, Certifications |
| Sibling Organisations | `sisters.html` | Global KBI chapters and partner organisations |
| Scholarships | `scholarships.html` | Scholarships, bursaries, donation pathways |
| Tech Projects | `projects.html` | KBI HK community tech & research projects |

### Event Detail Pages

| File | Event | Date/Venue |
|------|-------|------------|
| `event1.html` | Blockchain Foundations Clinic | Upcoming — HKU |
| `event2.html` | KBI Community Meet-Up March 2026 | Upcoming — The Hive |
| `event3.html` | IQCOL HK 2026 Qualifying Round | Upcoming — CUHK |
| `event4.html` | ETO HK 2025 Finals Day | June 2025 — HKUST |
| `event5.html` | IBCOL HK 2025 Qualifying Round | March 2025 — HKU iDendron |
| `event6.html` | Data Science Fundamentals Bootcamp 2025 | April 2025 — CUHK |
| `event7.html` | KBI HK Community Gathering 2025 | 2025 — The Hive Kennedy Town |
| `event8.html` | ETO HK 2024 Inaugural Edition | June 2024 — CUHK |
| `event9.html` | Quantum Computing Seminar Series 2024 | Oct–Nov 2024 — HKU & HKUST |
| `event10.html` | IBCOL HK 2024 Qualifying Round | 2024 — PolyU |
| `event11.html` | Industry Panel: Blockchain in Financial Services 2024 | 2024 |
| `event12.html` | IDSOL HK 2023 Data Science Olympiad Round | Oct 2023 — CUHK |
| `event13.html` | Smart Contract Developer Workshop 2023 | 2023 |
| `event14.html` | Alumni Reunion & Networking Night 2023 | 2023 — Landmark Mandarin Oriental |
| `event15.html` | IBCOL HK 2022 Qualifying Round | March 2022 — HKUST |

### News Article Pages

| File | Title | Type |
|------|-------|------|
| `news1.html` | ETO HK 2026 Is Now Open | Announcement |
| `news2.html` | Why Blockchain Education Matters for HK Students | Insight |
| `news3.html` | Alumni Spotlight: Dr. Michelle Lam | Interview |
| `news4.html` | Why Quantum Computing Education Cannot Wait | Opinion |
| `news5.html` | KBI HK Chapter Rebuild 2026 | Press Release |
| `news6.html` | Data Science in the Classroom | Insight |
| `news7.html` | IBCOL HK 2026 — Call for Participants | Announcement |
| `news8.html` | Nine Years of KBI Hong Kong | Reflection |

---

## Navigation Structure

### Desktop Navbar

```
[KBI Hong Kong logo]  About ▾  Programmes ▾  Events  Membership  Community  News  Contact
```

**About dropdown (`#dd-about`):**
- Who We Are → `about-who-we-are.html`
- Our History → `about-history.html`
- Our Impact → `about-impact.html`
- Our Team → `about-team.html`
- ── divider ──
- Media & Brand Kit → `media.html`

**Programmes dropdown (`#dd-prog`) — 3-section structure:**
```
[Competitions]
  IBCOL HK → competitions.html#ibcol
  IDSOL HK → competitions.html#idsol
  IQCOL HK → competitions.html#iqcol
── divider ──
[Flagship]
  ETO HK 2026 → eto2026.html
── divider ──
[More]
  Certifications → certifications.html
  Collaborations → collaborations.html
  Tech Projects  → projects.html
```

### Mobile Nav — 3-section structure

```
[About section]
  Who We Are
    Our History (sub)
    Our Impact (sub)
    Our Team (sub)
    Media & Brand Kit (sub)

[Programmes section]
  ETO HK 2026
    IBCOL — Blockchain (sub)
    IDSOL — Data Science (sub)
    IQCOL — Quantum (sub)
    Certifications (sub)
    Collaborations (sub)
    Tech Projects (sub)

[Navigate section]
  Home
  Events
  Membership
  Community
  News & Insights
  Scholarships
  FAQ
  Sibling Organisations
  Contact
```

Active page link is marked with `class="active"` on its mobile nav entry.

---

## Design System

### Colour Tokens (`kbi-hk.css`)

| Token | Value | Usage |
|-------|-------|-------|
| `--prussian` | `#003153` | Primary brand colour — nav, buttons, headings |
| `--night` | `#05070A` | Dark hero backgrounds |
| `--cyan` | `#3CB4FF` | Accent — hover states, italic headings, icons |
| `--yellow` | `#FFD166` | Stat numbers, medal highlights, CTA contrast |
| `--white` | `#FFFFFF` | Light section backgrounds |
| `--mist` | `#F4F6F9` | Subtle section alternation, figcaption backgrounds |
| `--stone` | `#E2E6ED` | Borders, dividers |

### Typography

- **Playfair Display** — headings, section titles, stat numbers, article titles
- **Inter** — body copy, labels, metadata, UI elements

### Key CSS Classes

| Class | Usage |
|-------|-------|
| `.section-wrap` | Standard section padding wrapper |
| `.section-wrap--white` / `--mist` / `--prussian` / `--night` | Section background variants |
| `.section-inner` | Max-width constrained content container |
| `.page-hero` | Top hero with `--prussian` or `--night` background |
| `.page-hero-bg` | Absolute-positioned background image overlay (opacity 0.12–0.13) |
| `.page-hero-inner` | `z-index:1` relative positioned inner content |
| `.event-hero` | Event detail page hero |
| `.article-hero` | News article page hero |
| `.reveal` | Scroll-triggered fade-up animation |
| `.btn-prussian` / `.btn-yellow` / `.btn-outline` | CTA button variants |
| `.tag` | Pill tag (e.g., `.tag--prussian`, `.tag--stone`) |
| `.nav-dropdown-label` | Section label inside dropdown menus |
| `.nav-dropdown-divider` | Horizontal rule divider in dropdown |
| `.nav-mobile-section-label` | Section heading in mobile nav |
| `.nav-mobile-link` / `.nav-mobile-sub` | Mobile nav links (primary / indented) |

---

## Image Strategy

### Hero Background Images

Applied to all main page heroes using the pattern:
```html
<header class="page-hero page-hero--prussian" style="position:relative;overflow:hidden;">
  <div class="page-hero-bg" aria-hidden="true"
    style="position:absolute;inset:0;
           background-image:url('https://sspark.genspark.ai/cfimages?...');
           background-size:cover;background-position:center;opacity:0.12;">
  </div>
  <div class="page-hero-inner" style="position:relative;z-index:1;">
    <!-- content -->
  </div>
</header>
```

**Pages with hero background images:**
`about.html`, `events.html`, `news.html`, `community.html`, `contact.html`, `impact.html`, `membership.html`, `sponsors.html`, `competitions.html`, `certifications.html`, `collaborations.html`

### Contextual Inline Images

Injected into event detail pages (event4–15) and news article pages (news4–8) as `<figure>` elements immediately after the article `<article>` tag, before the first content block:

```html
<figure class="event-inline-figure reveal"
  style="margin:0 0 40px;border-radius:var(--radius-lg);overflow:hidden;">
  <img src="https://sspark.genspark.ai/cfimages?..." alt="descriptive alt text"
    style="width:100%;height:320px;object-fit:cover;display:block;">
  <figcaption style="padding:10px 16px;background:var(--mist);
    font-family:'Inter',sans-serif;font-size:0.8125rem;color:var(--text-faint);">
    Contextual caption matching the event/article content.
  </figcaption>
</figure>
```

News articles use `height:300px` and no `event-inline-figure` class (injected inside `<article class="article-body">`).

### Image Source

All images sourced from `sspark.genspark.ai/cfimages` — a publicly accessible, license-filtered image CDN. Images are thematically matched to each page (Hong Kong university events, fintech panels, blockchain workshops, quantum seminars, alumni gatherings, data science sessions).

---

## JavaScript Interactions (`kbi-hk.js`)

| Feature | Description |
|---------|-------------|
| Programme tabs | `.prog-tab` buttons toggle `.prog-tab-panel` panels by `data-tab` |
| Hash routing | `DOMContentLoaded` + `hashchange` events map URL hash to programme tab and scroll target |
| Audience tabs | `.audience-tab` buttons toggle `.audience-panel` panels by `data-audience` |
| Events tabs | `.events-tab` buttons toggle `.events-tab-panel` panels |
| Nav dropdowns | `.has-dropdown` click/keyboard toggle with `aria-expanded` management |
| Mobile nav | Hamburger toggle `#navHamburger` → `#navMobile` slide open |
| Reveal animations | `IntersectionObserver` triggers `.reveal` elements on scroll |
| Counters | Animated number counters for stats triggered on `IntersectionObserver` |
| Form handling | `membershipForm`, `contactForm`, `sponsorForm`, `newsletterForm` — client-side validation + success message |
| Back to top | `#backToTop` button appears after 60px scroll |
| Nav scroll | `nav-scrolled` class added after 60px scroll |

---

## External Links

| Purpose | URL |
|---------|-----|
| Register Interest 2026 | https://forms.gle/7WwvpwKxkDXtRbK2A |
| IBCOL Competition Rules | https://2026.ibcol.org/competition |
| IDSOL Competition Rules | https://2026.idsol.org/competition |
| IQCOL Competition Rules | https://2026.iqcol.org/competition |
| KBI International | https://kbi.foundation |
| Contact email | hk@kbi.foundation |

---

## File Structure

```
index.html                    — Homepage
about.html                    — About landing (links to sub-pages)
about-who-we-are.html         — Who We Are sub-page
about-history.html            — Our History — timeline 2016–present
about-impact.html             — Our Impact — animated stats
about-team.html               — Our Team — committee grid + advisers
media.html                    — Media & Brand Kit — photo gallery, logos
programmes.html               — Programmes hub (4-tab: Flagship, Olympiads, Training, Community)
eto2026.html                  — ETO HK 2026 flagship page
competitions.html             — IBCOL / IDSOL / IQCOL detail
certifications.html           — ISFRETIC certification pathways
collaborations.html           — Campus Ambassadors, KBridge
projects.html                 — Tech Projects
events.html                   — Events listing (upcoming + past tabs)
event1.html – event15.html    — Event detail pages (event4–15 have contextual inline images)
membership.html               — Membership types, audience tabs, application form
sponsors.html                 — Sponsorship tiers + enquiry form
community.html                — Community groups and paths
impact.html                   — Impact stats, competition record, testimonials
news.html                     — News listing (announcements, insights, press)
news1.html – news8.html       — News article pages (news4–8 have contextual inline images)
contact.html                  — Contact enquiry page
faq.html                      — FAQ accordion page
sisters.html                  — Sibling organisations / global chapters
scholarships.html             — Scholarships and donations
kbi-hk.css                   — Design system (~2,200+ lines)
kbi-hk.js                    — All JS interactions
KBI_Leaflet.pdf              — Organisation leaflet (static asset)
```

---

## Completed Features (All Sessions)

### Session 1–2
- ✅ Full site structure with all core pages
- ✅ `kbi-hk.css` design system — colour tokens, typography, component library
- ✅ `kbi-hk.js` — nav, tabs, reveal animations, counters, hash routing, forms
- ✅ Homepage with hero, stats, programme preview, event cards, sponsor grid, news cards, CTA
- ✅ Programmes page with 4-tab structure and deep-link hash routing
- ✅ ETO HK 2026 dedicated flagship page
- ✅ Membership page with audience tabs and application form
- ✅ Events listing with tabbed upcoming/past layout
- ✅ Event detail pages event1–event3 (upcoming events)
- ✅ News listing with categorised article cards
- ✅ News article pages news1–news3
- ✅ Sponsors, Community, Impact, Contact pages

### Session 3
- ✅ About sub-pages: `about-who-we-are.html`, `about-history.html`, `about-impact.html`, `about-team.html`
- ✅ `media.html` — photo gallery + brand kit
- ✅ `faq.html` — accordion FAQ
- ✅ `sisters.html` — sibling organisations
- ✅ `scholarships.html` — scholarships and donations
- ✅ `projects.html` — tech projects
- ✅ Event detail pages event4–event15 (12 past events with full recap content)
- ✅ News article pages news4–news8 (5 additional articles)
- ✅ Competitions, Certifications, Collaborations expanded detail pages

### Session 4
- ✅ **Programmes dropdown fixed** on all ~37 pages — replaced stale `programmes.html#eto` structure with new 3-section dropdown (Competitions / Flagship / More)
- ✅ **Mobile nav updated** on all ~37 pages — replaced old flat structure with new 3-section layout (About / Programmes / Navigate)
- ✅ **Hero background images** added to 11 main pages: about, events, news, community, contact, impact, membership, sponsors, competitions, certifications, collaborations
- ✅ **Active page marking** on mobile nav links (`class="active"`) for all event and news detail pages

### Session 5
- ✅ **Contextual inline images** injected into event4–event15 (12 past event pages) — full-width figure with caption, thematically matched imagery
- ✅ **Contextual inline images** injected into news4–news8 (5 news article pages) — full-width figure with caption inside article body
- ✅ **README.md** comprehensively updated with all pages, nav structure, image strategy, design system documentation

---

## Known Issues / Pre-existing

- **Nav logo 404**: `KBI HK Icon Square - Prussian Blue Outline + Transparent Background.png` — filename with spaces causes 404 across all pages. Pre-existing issue; fix by renaming file and updating all `<img src="...">` references.
- **Forms**: All forms are client-side only (success message shown, no email sent). Connect to Formspree / Netlify Forms / backend endpoint for real submission.

---

## Not Yet Implemented / Recommended Next Steps

- **Form backend**: Connect membership, contact, sponsor, and newsletter forms to an email delivery service
- **Real team photos**: Headshot images use placeholder paths (`images/headshot-*.jpg`). Supply real photos
- **Sponsor logos**: Sponsor grid uses text placeholders. Replace with actual partner logos
- **Social media links**: Footer social icons link to `#`. Update with real KBI HK handles
- **Analytics**: No tracking implemented. Add privacy-respecting analytics (Plausible, Fathom, etc.)
- **Nav logo**: Rename the PNG logo file to remove spaces (e.g., `kbi-hk-logo.png`) and update all references
- **SEO / Open Graph**: Add `og:image`, `og:title`, `twitter:card` meta tags to all pages
- **Sitemap**: Generate `sitemap.xml` for search engine indexing

---

## Deployment

To publish the website live, use the **Publish tab** in the editor. All files are static and require no server-side processing.

---

*KBI Hong Kong · Est. 2016 · Registered non-profit · hk@kbi.foundation*
