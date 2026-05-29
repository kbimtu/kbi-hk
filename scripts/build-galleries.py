# -*- coding: utf-8 -*-
"""Generate event gallery year pages (2021 layout) with recaps and photo grids."""
import html
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from events_recaps import render_recap  # noqa: E402

GALLERY = ROOT / "event gallery"
IMAGES = ROOT / "images"
TEMPLATE = GALLERY / "event-gallery-2021.html"

CYAN_TAGS = {
    "Teaching", "Training", "Workshop", "School programme", "School Outreach",
    "Training series", "Scientific visit", "Mentorship", "Coaching", "Internship",
    "Outreach Seminar", "Skillsprint", "Outreach", "Kick-off Session", "Crash Course",
    "Internship Series", "Lecture Series", "Training Sessions", "Training Series",
    "Professional Training", "Preparation Session", "FinTech Competition",
    "Greater Bay Area Competition", "Foundational Course", "Regional Finals",
    "Member Participation", "Career Futures", "Working Group", "Internship Experience",
}
YELLOW_TAGS = {
    "Flagship Event", "Supporting organisation", "Supporting Organisation",
    "Competition", "Finals", "International Finals", "First International Finals",
    "Regional Competition", "International Delegation",
}

RECAP_CSS = """
    .gallery-event-section { scroll-margin-top: 100px; }
    .gallery-event-recap { margin: 12px 0 20px; max-width: 760px; }
    .gallery-event-recap h3 {
      font-family: 'Playfair Display', serif;
      font-size: 1.0625rem;
      font-weight: 600;
      color: var(--prussian);
      margin: 22px 0 8px;
    }
    .gallery-event-recap h3:first-child { margin-top: 0; }
    .gallery-event-recap p,
    .gallery-event-recap li {
      font-family: 'Inter', sans-serif;
      font-size: 0.9rem;
      line-height: 1.75;
      color: var(--text-muted);
    }
    .gallery-event-recap ul { margin: 8px 0 14px; padding-left: 1.25rem; }
    .gallery-event-recap li { margin-bottom: 6px; }
    .gallery-event-closing {
      font-family: 'Playfair Display', serif;
      font-style: italic;
      font-size: 0.95rem;
      color: var(--prussian);
      margin-top: 18px;
      padding-left: 16px;
      border-left: 3px solid var(--yellow);
    }
    .gallery-event-details {
      margin-top: 24px;
      padding: 20px 24px;
      background: #fff;
      border: 1px solid var(--stone);
      border-radius: var(--radius-md);
    }
    .gallery-details-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 14px 20px;
      margin-top: 12px;
    }
    .gallery-details-grid dt {
      font-family: 'Inter', sans-serif;
      font-size: 0.6875rem;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--prussian);
      margin-bottom: 4px;
    }
    .gallery-details-grid dd {
      font-family: 'Inter', sans-serif;
      font-size: 0.875rem;
      color: var(--text-muted);
      line-height: 1.6;
      margin: 0;
    }
    .gallery-sdg-list li { margin-bottom: 10px; }
    .gallery-sdg-list strong { color: var(--ink); }
"""


def tag_class(tag):
    if tag in YELLOW_TAGS:
        return "gallery-event-tag gallery-event-tag--first"
    if tag in CYAN_TAGS:
        return "gallery-event-tag gallery-event-tag--cyan"
    return "gallery-event-tag"


def esc(s):
    return html.escape(s, quote=True)


def photos_html(paths, alt_prefix=""):
    if not paths:
        return ""
    hint = (
        '<span class="photo-strip-item-hint" aria-hidden="true">'
        '<svg viewBox="0 0 24 24" aria-hidden="true">'
        '<path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7" fill="none" stroke="currentColor" '
        'stroke-width="2" stroke-linecap="round"/></svg></span>'
    )
    items = []
    for rel in paths[:12]:
        alt = esc(alt_prefix or rel.split("/")[-1])
        safe = rel.replace("&", "&amp;").replace('"', "&quot;")
        items.append(
            f'''          <button type="button" class="photo-strip-item" data-caption="{alt}" aria-label="View larger image">
            <img src="../images/{safe}" alt="{alt}" loading="lazy" decoding="async">
            {hint}
          </button>'''
        )
    return f'''        <div class="photo-strip-wrap">
          <div class="photo-strip-scroll" tabindex="0" role="region" aria-label="Event photos — scroll horizontally">
            <div class="photo-strip-track">
{chr(10).join(items)}
            </div>
          </div>
        </div>'''


def list_folder(folder_substr, limit=3):
    if not folder_substr or not IMAGES.exists():
        return []
    matches = [d for d in IMAGES.iterdir() if d.is_dir() and folder_substr.lower() in d.name.lower()]
    if not matches:
        return []
    folder = matches[0]
    files = sorted([f for f in folder.rglob("*") if f.is_file() and f.suffix.lower() in (".jpg", ".jpeg", ".png", ".webp", ".gif")])
    out = []
    for f in files[:limit]:
        out.append(str(f.relative_to(IMAGES)).replace("\\", "/"))
    return out


def event_section(num, ev, delay=""):
    tag = ev["tag"]
    date = ev["date"]
    venue = ev["venue"]
    title = ev["title"]
    desc = ev["desc"]
    eid = ev.get("id", "")
    if "images" in ev:
        imgs = ev["images"]
    elif ev.get("image_folder"):
        imgs = list_folder(ev["image_folder"], ev.get("image_limit", 6))
    else:
        imgs = []
    grid = photos_html(imgs, title)
    grid_block = f"\n{grid}\n" if grid else ""
    delay_cls = f" {delay}" if delay else ""
    recap = render_recap(eid)
    recap_block = f"\n            {recap}\n" if recap else ""
    return f'''      <section class="gallery-event-section reveal{delay_cls}" id="{eid}">
        <div class="gallery-event-header">
          <div class="gallery-event-num">{num:02d}</div>
          <div class="gallery-event-header-body">
            <div class="gallery-event-meta">
              <span class="{tag_class(tag)}">{esc(tag)}</span>
              <span class="gallery-event-date">{esc(date)}</span>
              <span class="gallery-event-venue">{esc(venue)}</span>
            </div>
            <h2 class="gallery-event-title">{esc(title)}</h2>
            <p class="gallery-event-desc">{esc(desc)}</p>{recap_block}
          </div>
        </div>{grid_block}      </section>'''


def year_nav(prev_file, prev_label, next_file, next_label):
    prev = ""
    if prev_file:
        prev = f'''      <a href="{prev_file}" class="gallery-nav-arrow">
        <svg viewBox="0 0 16 16" fill="none"><path d="M10 12L6 8l4-4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
        {prev_label}
      </a>'''
    else:
        prev = '<span></span>'
    nxt = ""
    if next_file:
        nxt = f'''      <a href="{next_file}" class="gallery-nav-arrow">
        {next_label}
        <svg viewBox="0 0 16 16" fill="none"><path d="M6 4l4 4-4 4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </a>'''
    else:
        nxt = '<span></span>'
    return f'''  <div class="gallery-year-nav">
    <div class="gallery-year-nav-inner">
{prev}
      <a href="../upcoming events/events.html#past-events" class="gallery-nav-center">↑ All Events</a>
{nxt}
    </div>
  </div>'''


PAGES = [
    {
        "file": "event-gallery-2018.html",
        "title": "2017–2018 Event Gallery",
        "year_label": "2017–2018",
        "intro": "2017–2018 marked the founding phase of KBI Hong Kong and the arrival of the first International Blockchain Olympiad. It was a period of first principles teaching, institutional beginnings, and the creation of a more structured emerging-technology programme ecosystem in the city.",
        "prev": None, "next": ("event-gallery-2019.html", "2019 Gallery"),
        "events": [
            {"id": "first-principles", "tag": "Foundational Course", "date": "February 2018", "venue": "CityUHK",
             "title": "Blockchain From First Principles Teaching Course",
             "desc": "This foundational short course, Blockchain From First Principles, was taught by Dr. Lawrence Ma and hosted at CityUHK. It introduced students to core blockchain concepts, paradigms, and platforms, while explaining why blockchain matters beyond surface-level hype.",
             "images": list_folder("2018.02.27 First Principles", 3)},
            {"id": "ibcol-2018", "tag": "First International Finals", "date": "May 2018", "venue": "CityUHK with University of Waterloo",
             "title": "International Blockchain Olympiad 2018 (IBCOL 2018)",
             "desc": "The International Blockchain Olympiad 2018 was convened by Dr. Lawrence Ma, with finals co-hosted by City University of Hong Kong and the University of Waterloo. Student teams presented blockchain and distributed ledger applications from technical, business, and legal perspectives.",
             "images": list_folder("2018.05.30 Blockchain", 3)},
        ],
    },
    {
        "file": "event-gallery-2019.html",
        "title": "2019 Event Gallery",
        "year_label": "2019",
        "intro": "In 2019, KBI Hong Kong deepened its local activity through training sessions while helping deliver the second International Blockchain Olympiad in Hong Kong. The year brought together technical preparation, international participation, and a stronger public presence for blockchain education.",
        "prev": ("event-gallery-2018.html", "2017–2018 Gallery"),
        "next": ("event-gallery-2020.html", "2020 Gallery"),
        "events": [
            {"id": "ibcol-training-2019", "tag": "Training Sessions", "date": "February 2019", "venue": "CityUHK",
             "title": "IBCOL HK Training Sessions",
             "desc": "A series of IBCOL HK training sessions covered both technical and legal perspectives, with modules led by speakers including Heidy Ho and Natalie Lau. The programme helped prepare teams for the 2019 competition cycle with a broader understanding of blockchain work.",
             "images": list_folder("2019.02.25 IBCOL HK Training", 3)},
            {"id": "ibcol-2019-finals", "tag": "International Finals", "date": "July 2019", "venue": "CityUHK / HKSTP InnoCentre",
             "title": "International Blockchain Olympiad 2019 (IBCOL 2019)",
             "desc": "City University of Hong Kong hosted the 2019 IBCOL finals in partnership with Hong Kong Science and Technology Park and the Hong Kong Blockchain Society. Thirty-four teams gathered in Hong Kong, presenting at CityU and exhibiting at HKSTP InnoCentre before the final pitch and awards ceremony.",
             "images": list_folder("2019.07.05 IBCOL 2019", 3)},
        ],
    },
    {
        "file": "event-gallery-2020.html",
        "title": "2020 Event Gallery",
        "year_label": "2020",
        "intro": "2020 marked a major shift in format as programmes moved online and into hybrid delivery during the pandemic. It also marked the debut of the International Data Science Olympiad, signalling a broader expansion of KBI Hong Kong's competition and training ecosystem.",
        "prev": ("event-gallery-2019.html", "2019 Gallery"),
        "next": ("event-gallery-2021.html", "2021 Gallery"),
        "events": [
            {"id": "cbp-training", "tag": "Professional Training", "date": "September 2019 – April 2020", "venue": "CityUHK / Online",
             "title": "Certified Blockchain Professional Training Course",
             "desc": "This multi-month Certified Blockchain Professional course, delivered in partnership with City University of Hong Kong, combined on-campus and online teaching to deepen participants' understanding of blockchain technology and its applications.",
             "images": list_folder("2020.04 Certified Blockchain", 3)},
            {"id": "hkbcool-2020", "tag": "Regional Finals", "date": "June 2020", "venue": "Online",
             "title": "HKBCOL 2020 Hong Kong Regional Finals",
             "desc": "The Hong Kong regional finals for the Blockchain Olympiad moved fully online in 2020, with local teams presenting blockchain solutions remotely while competing for places at the international finals.",
             "images": list_folder("2020.06 HKBCOL", 3)},
            {"id": "ibcol-2020", "tag": "International Finals", "date": "July 2020", "venue": "Online",
             "title": "International Blockchain Olympiad 2020 (IBCOL 2020)",
             "desc": "The 2020 International Blockchain Olympiad finals were held online, preserving an international platform for student blockchain projects despite global travel and gathering restrictions.",
             "images": list_folder("2020.07 International Blockchain", 3)},
        ],
    },
    {
        "file": "event-gallery-2021.html",
        "title": "2021 Event Gallery",
        "year_label": "2021",
        "intro": "In 2021, international programming continued under hybrid and cross-border conditions. KBI Hong Kong remained connected to the wider competition network as major blockchain events were delivered through a mix of in-person and online formats.",
        "prev": ("event-gallery-2020.html", "2020 Gallery"),
        "next": ("event-gallery-2022.html", "2022 Gallery"),
        "events": [
            {"id": "hkbcool-training-2021", "tag": "Training Series", "date": "September – November 2020", "venue": "Online / Hybrid",
             "title": "HKBCOL 2021 Blockchain Training Series",
             "desc": "This free multi-week training series prepared students for the Hong Kong Blockchain Olympiad 2021 through structured teaching across blockchain fundamentals, design, and development tracks.",
             "images": list_folder("2021.04 HKBCOL 2021", 2)},
            {"id": "hkbcool-2021", "tag": "Regional Competition", "date": "April 2021", "venue": "CityUHK / Online",
             "title": "Hong Kong Blockchain Olympiad 2021 (HKBCOL 2021)",
             "desc": "City University of Hong Kong and the Hong Kong Blockchain Society co-organised HKBCOL 2021, where teams including Credify and Infi.io earned Bronze, Gold, and Best Prototype awards for blockchain solutions in credentials and project finance."},
            {"id": "ibcol-2021", "tag": "International Finals", "date": "October 2021", "venue": "Dhaka / Online",
             "title": "International Blockchain Olympiad 2021 (IBCOL 2021)",
             "desc": "The IBCOL 2021 grand finale took place as a hybrid event in Dhaka and online, with Hong Kong-linked teams such as EduChain receiving recognition including an Award of Merit for education-focused blockchain solutions."},
        ],
    },
    {
        "file": "event-gallery-2022.html",
        "title": "2022 Event Gallery",
        "year_label": "2022",
        "intro": "In 2022, KBI Hong Kong's ecosystem expanded beyond blockchain alone into broader fintech and Greater Bay Area activity. Through the Fintech Olympiad and GBA International Blockchain Olympiad, students across Hong Kong and the region engaged with real-world problem solving and cross-border participation.",
        "prev": ("event-gallery-2021.html", "2021 Gallery"),
        "next": ("event-gallery-2023.html", "2023 Gallery"),
        "events": [
            {"id": "ftol-2022", "tag": "FinTech Competition", "date": "May 2022", "venue": "Online",
             "title": "Fintech Olympiad 2022",
             "desc": "Fintech Olympiad 2022 challenged Greater Bay Area university students to propose real-world fintech solutions through an online competition programme hosted by City University of Hong Kong with support from HSBC and the Hong Kong Blockchain Society."},
            {"id": "gba-ibcol-2022", "tag": "Greater Bay Area Competition", "date": "August 2022", "venue": "Online / Gather Town",
             "title": "Greater Bay Area International Blockchain Olympiad 2022 (GBA IBCOL 2022)",
             "desc": "GBA IBCOL 2022 brought together secondary and tertiary teams from across Mainland China, Hong Kong, and Macao through a virtual platform hosted on Gather Town, addressing real-world problems with blockchain under sector-specific themes."},
        ],
    },
    {
        "file": "event-gallery-2023.html",
        "title": "2023 Event Gallery",
        "year_label": "2023",
        "intro": "In 2023, KBI-linked activity in Hong Kong centred on local blockchain teaching, student preparation, and the Hong Kong Blockchain Olympiad, alongside the International Blockchain Olympiad finals held in Amsterdam. The year connected classroom exposure, local competition, and international presentation on a single pathway.",
        "prev": ("event-gallery-2022.html", "2022 Gallery"),
        "next": ("event-gallery-2024.html", "2024 Gallery"),
        "events": [
            {"id": "hkbu-lectures-2023", "tag": "Lecture Series", "date": "April 2023", "venue": "HKBU",
             "title": "HKBU Blockchain Lectures 2023",
             "desc": "The HKBU Blockchain Lectures 2023 introduced students to core blockchain concepts and real-world applications while connecting that learning to Olympiad-related opportunities."},
            {"id": "hkbcool-2023", "tag": "Regional Competition", "date": "September 2023", "venue": "Inno Network, HKPC",
             "title": "Hong Kong Blockchain Olympiad 2023 (HKBCOL 2023)",
             "desc": "HKBCOL 2023 brought Hong Kong teams together at HKPC's Inno Network to present blockchain solutions, compete for regional recognition, and qualify for the international stage."},
            {"id": "ibcol-2023", "tag": "International Finals", "date": "November 2023", "venue": "Hogeschool Inholland, Amsterdam",
             "title": "International Blockchain Olympiad 2023 at DigiQuest",
             "desc": "The IBCOL 2023 finals were held as part of DigiQuest 2023 at Hogeschool Inholland, where teams presented blockchain projects in an international, in-person setting.",
             "images": ["IBCOL-DigiQuest-2023-11-17 DSC00188.jpg"]},
        ],
    },
    {
        "file": "event-gallery-2024.html",
        "title": "2024 Event Gallery",
        "year_label": "2024",
        "intro": "2024 was a dense year with local blockchain and data-science finals, school partnerships, crash courses, mentorship sessions, and international delegation activity in Amsterdam. Training, competition, and international representation fit together within one annual cycle.",
        "prev": ("event-gallery-2023.html", "2023 Gallery"),
        "next": ("event-gallery-2025.html", "2025 Gallery"),
        "events": [
            {"id": "hkage-kickoff", "tag": "Kick-off Session", "date": "February – April 2024", "venue": "HKPC, Hong Kong",
             "title": "HKAGE x HKBCOL Kick-off Session",
             "desc": "The HKAGE x HKBCOL Kick-off Session introduced HKAGE students and teachers to the Hong Kong Blockchain Olympiad 2024 structure, timeline, and training pathway."},
            {"id": "dgjs-training", "tag": "School Outreach", "date": "March 2024", "venue": "Diocesan Girls Junior School (DGJS)",
             "title": "DGJS Blockchain Training Session",
             "desc": "This focused blockchain training session at DGJS gave junior students a first look at core concepts and how blockchain can be applied in practice."},
            {"id": "idsol-crash", "tag": "Crash Course", "date": "May 2024", "venue": "Hong Kong",
             "title": "IDSOL Crash Course Cohort",
             "desc": "The IDSOL Crash Course Cohort prepared IDSOL 2024 participants in Hong Kong for data science problem-solving and competition tasks through a crash course in natural language processing."},
            {"id": "idsol-hk-2024-finals", "tag": "Finals", "date": "October 2024", "venue": "City University of Hong Kong",
             "title": "IDSOL HK 2024 Hong Kong Finals",
             "desc": "The IDSOL HK 2024 finals brought together local teams to present data science and AI solution designs and determine Hong Kong's representatives for the international stage in Amsterdam."},
            {"id": "letti-2024", "tag": "Internship Series", "date": "July – August 2024", "venue": "Lingnan University",
             "title": "Lingnan Emerging Tech Training Internship (LETTI) 2024",
             "desc": "The LETTI 2024 series introduced Lingnan University students to emerging technologies, cryptography fundamentals, and consensus concepts through online lessons and an interactive game."},
            {"id": "hkage-mentorship", "tag": "Mentorship Session", "date": "August 2024", "venue": "Hong Kong Science and Technology Parks (HKSTP)",
             "title": "HKAGE x HKBCOL Mentorship Session at HKSTP",
             "desc": "HKAGE and HKBCOL collaborated on a mentorship session at HKSTP that exposed students to blockchain applications and the wider innovation ecosystem."},
            {"id": "idsol-crash-hk", "tag": "Crash Course", "date": "August 2024", "venue": "Hong Kong Science and Technology Parks (HKSTP)",
             "title": "IDSOL HK 2024 Crash Course",
             "desc": "This concentrated crash course gave IDSOL HK participants rapid technical ramp-up in preparation for the October data science finals."},
            {"id": "ibcol-hk-2024", "tag": "Finals", "date": "August 2024", "venue": "Hong Kong Productivity Council",
             "title": "IBCOL HK 2024 Hong Kong Finals",
             "desc": "The IBCOL HK 2024 finals brought local teams together to present blockchain projects and determine Hong Kong's representatives for the international stage."},
            {"id": "ibcol-socratic", "tag": "Preparation Session", "date": "August 2024", "venue": "Hong Kong Science and Technology Parks (HKSTP)",
             "title": "IBCOL 2024 Socratic Session",
             "desc": "The IBCOL 2024 Socratic Session gave teams space to test and refine their thinking through structured questioning and feedback ahead of IBCOL 2024."},
            {"id": "eto-delegation-2024", "tag": "International Delegation", "date": "November 2024", "venue": "Amsterdam",
             "title": "ETO 2024 HKSAR Delegation in Amsterdam",
             "desc": "A Hong Kong delegation, including THEi participants, travelled to Amsterdam for the Emerging Technologies Olympiad, where they competed and engaged with international peers and judges."},
        ],
    },
    {
        "file": "event-gallery-2025.html",
        "title": "2025 Event Gallery",
        "year_label": "2025",
        "intro": "2025 is the busiest page and is grouped by programme type rather than pure chronology. The year includes school programmes, youth training, career roadshows, delegation support, science exhibition participation, and ETO 2025 in Hong Kong, while SkillSprint emerges as a major recurring training initiative.",
        "prev": ("event-gallery-2024.html", "2024 Gallery"),
        "next": ("event-gallery-2026.html", "2026 Gallery"),
        "events": [
            {"id": "dgjs-blockchain", "tag": "School Outreach", "date": "February 2025", "venue": "DGJS",
             "title": "DGJS Blockchain Cryptography 2025",
             "desc": "A multi-week programme at DGJS introduced primary students to blockchain and cryptography through structured lessons and hands-on activities."},
            {"id": "generation-tech", "tag": "Member Participation", "date": "March 2025", "venue": "The Quayside, Hong Kong",
             "title": "Generation Tech 2025 Member Participation",
             "desc": "KBI HK members participated in Generation Tech 2025 from kick-off through finals, gaining exposure to industry-style problem solving, teamwork, and applied presentation experience."},
            {"id": "solomon-seminar", "tag": "Outreach Seminar", "date": "April 2025", "venue": "Online",
             "title": "Solomon Learning x KBI AI and Blockchain Seminar",
             "desc": "This one-hour seminar introduced around 50 Grade 7–10 students to AI and blockchain from first principles."},
            {"id": "solomon-pitch", "tag": "Student Showcase", "date": "May 2025", "venue": "Hong Kong",
             "title": "Solomon Learning Junior Elevator Pitch 2025",
             "desc": "Following the earlier seminar, students delivered one-minute elevator pitches on AI and blockchain ideas."},
            {"id": "work-world-1", "tag": "Career Futures", "date": "May 2025", "venue": "HKU",
             "title": "Enactus HK x KBI HK Work World War 1",
             "desc": "The first Work World War roadshow stop at HKU explored career stories and portfolios in a job market increasingly shaped by AI and automation."},
            {"id": "ccc-debate", "tag": "Workshop", "date": "June 2025", "venue": "CCC Chuen Yuen College, Hong Kong",
             "title": "Elite Plus x KBI HK CCC Chuen Yuen College Post-Exam Debate Workshop",
             "desc": "Co-presented by Elite Plus Co. Ltd. and KBI HK, this post-exam debate workshop strengthened structured argument and communication through emerging-technology themes."},
            {"id": "work-world-2", "tag": "Career Futures", "date": "June 2025", "venue": "CityUHK",
             "title": "Enactus HK x KBI HK Work World War 2",
             "desc": "The second Work World War stop at CityU continued the roadshow on future-of-work scenarios and portfolio-building."},
            {"id": "dbs-coaching", "tag": "Coaching", "date": "June 2025", "venue": "Diocesan Boys School",
             "title": "Diocesan Boys School Olympiad Coaching 2025",
             "desc": "This Olympiad coaching session at DBS supported students preparing for advanced competition work."},
            {"id": "dgjs-internship", "tag": "Internship Experience", "date": "July 2025", "venue": "HKSTP",
             "title": "DGJS Blockchain 2025 Internship",
             "desc": "DGJS students participated in a two-day blockchain internship at Hong Kong Science and Technology Parks."},
            {"id": "cyber-wg", "tag": "Working Group", "date": "July 2025", "venue": "Hong Kong",
             "title": "KBI Cybersecurity Working Group",
             "desc": "The KBI Cybersecurity Working Group brought together invited experts to explore security themes and coordinate emerging cybersecurity-related initiatives."},
            {"id": "skillsprint-2025", "tag": "Skillsprint", "date": "July – September 2025", "venue": "CityU",
             "title": "FinTech SkillSprint 2025",
             "desc": "FinTech SkillSprint 2025 was a workshop series at CityU offering short, focused training in blockchain, trust technologies, data science, and AI."},
            {"id": "science-exhibition", "tag": "Supporting Organisation", "date": "August 2025", "venue": "Hong Kong Central Library",
             "title": "58th Joint School Science Exhibition Supporting Organisation Delegation",
             "desc": "As a supporting organisation of the 58th Joint School Science Exhibition, KBI helped host student delegate teams from NIS Shymkent, Kazakhstan."},
            {"id": "eto-2025", "tag": "Flagship Event", "date": "October 2025", "venue": "DGS Swire Blueprint",
             "title": "Emerging Technologies Olympiad 2025 (ETO 2025)",
             "desc": "ETO 2025 was hosted in Hong Kong SAR over three days, bringing together blockchain and data science finalists from around the world."},
        ],
    },
    {
        "file": "event-gallery-2026.html",
        "title": "2026 Event Gallery",
        "year_label": "2026",
        "intro": "The 2026 page is still early in the cycle, so it should feel lighter and more reflective than 2025. Rather than positioning the year around competition, the page can emphasise scientific exposure, civic engagement, and broader perspectives on technology and society.",
        "prev": ("event-gallery-2025.html", "2025 Gallery"),
        "next": None,
        "events": [
            {"id": "hk-sdg-summit-2026", "tag": "Supporting Organisation", "date": "March 2026", "venue": "CDNIS, Hong Kong",
             "title": "HK SDG Summit 2026",
             "desc": "Deepening global goals work with real projects, SDG awards, and emerging-tech solution design — KBI HK's first formal collaboration with the Hong Kong Global Goals Council at CDNIS.",
             "image_folder": "2026.03.07 Global Goals Council"},
        ],
    },
]


def build_page(page):
    tpl = TEMPLATE.read_text(encoding="utf-8")
    head_end = tpl.index("</head>") + len("</head>")
    head = tpl[:head_end]
    if ".gallery-event-recap" not in head:
        head = head.replace("  </style>\n</head>", RECAP_CSS + "\n  </style>\n</head>", 1)
    head = head.replace("<title>2021 Event Gallery — KBI Hong Kong</title>", f"<title>{esc(page['title'])} — KBI Hong Kong</title>")

    # Fix nav programme links in template fragment we'll reuse from file
    nav_body = tpl[tpl.index("<body>"):tpl.index("<!-- Page Hero -->")]

    prev = page["prev"]
    nxt = page["next"]
    prev_file = prev[0] if prev else None
    prev_label = prev[1] if prev else ""
    next_file = nxt[0] if nxt else None
    next_label = nxt[1] if nxt else ""

    sections = []
    for i, ev in enumerate(page["events"], 1):
        delay = "" if i == 1 else f"reveal-delay-{(i-1) % 3}"
        sections.append(event_section(i, ev, delay))
    main = "\n\n      <hr class=\"gallery-section-divider\">\n\n".join(sections)

    yl = page["year_label"]
    footer = tpl[tpl.index("<!-- ═══ FOOTER ═══"):]
    out = f'''{nav_body}
  <!-- Page Hero -->
  <header class="gallery-page-hero">
    <div class="gallery-page-hero-inner">
      <p class="gallery-page-eyebrow">Event Recap &amp; Gallery</p>
      <h1><em>{esc(yl)}</em> Recap &amp; Gallery</h1>
      <p class="gallery-page-hero-sub">{esc(page["intro"])}</p>
    </div>
  </header>

{year_nav(prev_file, prev_label, next_file, next_label)}

  <!-- Gallery Main -->
  <main class="gallery-main" id="main-content">
    <div class="gallery-main-inner">

{main}

    </div>
  </main>

  <div id="lightbox" role="dialog" aria-modal="true" aria-label="Photo viewer">
    <button id="lightboxClose" type="button" aria-label="Close photo viewer">&#x2715;</button>
    <button id="lightboxPrev" type="button" class="lightbox-nav lightbox-nav--prev" aria-label="Previous photo">&#x2039;</button>
    <button id="lightboxNext" type="button" class="lightbox-nav lightbox-nav--next" aria-label="Next photo">&#x203A;</button>
    <img id="lightboxImg" src="" alt="">
    <p id="lightboxCaption"></p>
  </div>

{footer}'''

    # Fix nav paths in output
    fixes = [
        ('href="../about/about-history.html" class="gallery-nav-center">↑ Back to History Archive</a>',
         'href="../upcoming events/events.html#past-events" class="gallery-nav-center">↑ All Events</a>'),
        ('href="../sponsors.html', 'href="../programme/sponsors.html'),
        ('href="../competitions.html', 'href="../programme/i2ol.html'),
    ]
    for old, new in fixes:
        out = out.replace(old, new)

    return head + out


def events_list_tag_class(tag):
    if tag in YELLOW_TAGS:
        return "tag tag--yellow"
    if tag in CYAN_TAGS:
        return "tag tag--cyan"
    return "tag tag--stone"


def render_past_events_list():
    import re

    lines = []
    delay_idx = 0
    first_year = True
    for page in reversed(PAGES):
        year_m = re.search(r"(\d{4})", page["file"])
        year = year_m.group(1) if year_m else page["year_label"]
        margin = "0 0 16px" if first_year else "32px 0 16px"
        border = "" if first_year else "padding-top:8px;border-top:1px solid var(--stone);"
        first_year = False
        lines.append(
            f'        <h3 class="past-events-year" style="font-family:\'Playfair Display\',serif;font-size:1.25rem;color:var(--prussian);margin:{margin};{border}">{year}</h3>'
        )
        for ev in page["events"]:
            eid = ev["id"]
            title = esc(ev["title"])
            date = esc(ev["date"])
            venue = esc(ev["venue"])
            tag = ev["tag"]
            tag_cls = events_list_tag_class(tag)
            delay = f" reveal-delay-{delay_idx % 4}" if delay_idx < 4 else ""
            delay_idx += 1
            meta = f"{date} · {venue}" if venue else date
            lines.append(
                f'        <a href="../event gallery/{page["file"]}#{eid}" class="past-event-item reveal{delay}" style="text-decoration:none;color:inherit;">\n'
                f'          <div class="past-event-date">{year}</div>\n'
                f'          <div class="past-event-title">{title}</div>\n'
                f'          <div style="font-family:\'Inter\',sans-serif;font-size:0.8125rem;color:var(--text-faint);margin-top:4px;">{meta}</div>\n'
                f'          <div class="past-event-tag"><span class="{tag_cls}">{esc(tag)}</span></div>\n'
                f"        </a>"
            )
    return "\n".join(lines) + "\n"


def sync_events_html():
    events_path = ROOT / "upcoming events" / "events.html"
    html = events_path.read_text(encoding="utf-8")
    start_marker = '      <div class="past-events-list">'
    end_marker = "\n\n\n  </section>"
    start = html.index(start_marker) + len(start_marker)
    end = html.index(end_marker, start)
    new_block = "\n" + render_past_events_list()
    html = html[:start] + new_block + html[end:]
    events_path.write_text(html, encoding="utf-8")
    print("Updated events.html past events list")


def main():
    for page in PAGES:
        path = GALLERY / page["file"]
        path.write_text(build_page(page), encoding="utf-8")
        print(f"Wrote {path.name} ({len(page['events'])} events)")
    sync_events_html()


if __name__ == "__main__":
    main()
