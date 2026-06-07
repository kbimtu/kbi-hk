# -*- coding: utf-8 -*-
"""Event recap copy for gallery pages (2018–2026)."""

from events_recaps_archive import ARCHIVE_RECAPS

# Each recap: list of (heading, paragraph or None, optional bullet list), optional closing string

EVENT_RECAPS = {
    "dgjs-blockchain": {
        "sections": [
            ("Overview", "This programme was designed to give younger learners a first encounter with blockchain-related thinking, including trust, records, encryption, and digital systems. Rather than pushing advanced theory, the sessions emphasised simple explanations, guided discovery, and interactive participation."),
            ("What students explored", None, [
                "Basic ideas behind blockchain and why trust matters in digital systems.",
                "Introductory cryptography concepts through simple demonstrations and classroom activities.",
                "Early exposure to structured problem-solving and technology vocabulary.",
            ]),
            ("Why it mattered", "DGJS Blockchain Cryptography 2025 reflected KBI HK's belief that emerging technology education can begin earlier than many people expect, provided it is taught with clarity and care. The programme created a foundation for confidence, curiosity, and later progression into more advanced learning opportunities."),
        ],
        "closing": "This programme was one of KBI HK's 2025 school-based outreach efforts to make technical learning more accessible at an earlier stage.",
    },
    "solomon-seminar": {
        "sections": [
            ("Overview", "The seminar focused on making two often-hyped technologies feel understandable and relevant to younger learners. By grounding the session in core ideas rather than buzzwords, students were invited to think critically about what AI and blockchain are, what they are not, and where they may matter in real life."),
            ("Session focus", None, [
                "AI and blockchain explained in accessible terms.",
                "Common misconceptions addressed directly.",
                "Real-world examples used to connect concepts with practical relevance.",
                "Preparation for the upcoming student pitch activity.",
            ]),
            ("Why it mattered", "The seminar helped students move from passive familiarity to active understanding. It also demonstrated KBI HK's approach to introductory education: make complex topics approachable without making them shallow."),
        ],
    },
    "solomon-pitch": {
        "sections": [
            ("Overview", "The Junior Elevator Pitch challenged students to express a technology idea in a short format with clarity and confidence. It encouraged them not only to understand emerging technology concepts, but also to explain them persuasively to others."),
            ("What students practiced", None, [
                "Distilling a technical idea into a short, audience-friendly message.",
                "Speaking with confidence under time constraints.",
                "Connecting innovation with relevance, purpose, and impact.",
            ]),
            ("Why it mattered", "Events like this help students realise that technical fluency and communication fluency grow together. The competition created a gentle but meaningful first step into public speaking, idea framing, and innovation storytelling."),
        ],
    },
    "work-world-1": {
        "sections": [
            ("Overview", "This session invited students to think about employability in a changing technological landscape. Rather than focusing only on jobs, it focused on narrative, positioning, and how students can show evidence of capability through their work and portfolios."),
            ("Key themes", None, [
                "How AI and automation are changing work and expectations.",
                "Why portfolio-building matters more than ever.",
                "How students can tell clearer career stories.",
                "The value of intentional skill development in uncertain futures.",
            ]),
            ("Why it mattered", "Work World War 1 helped students reframe career preparation as an active design process. It also aligned with KBI HK's broader emphasis on future-readiness through competence, communication, and evidence of work."),
        ],
    },
    "ccc-debate": {
        "sections": [
            ("Overview", "Held after the exam season, the workshop created a space for students to re-engage intellectually through debate and guided discussion. Emerging technology topics gave the session relevance, while the debate format sharpened reasoning and expression."),
            ("What students practiced", None, [
                "Building structured arguments.",
                "Responding to opposing views with clarity.",
                "Discussing emerging technology topics critically rather than passively.",
                "Translating ideas into persuasive speech.",
            ]),
            ("Why it mattered", "This workshop reflected KBI HK's view that emerging technology education is not only technical. It also requires judgement, articulation, and the ability to reason publicly about fast-changing issues."),
        ],
    },
    "work-world-2": {
        "sections": [
            ("Overview", "Building on the first roadshow, this session focused again on how students can position themselves in a rapidly changing environment. The discussion encouraged participants to move from abstract anxiety about the future of work toward concrete preparation and self-presentation."),
            ("Focus areas", None, [
                "Future-of-work awareness.",
                "Portfolio as evidence, not decoration.",
                "Career storytelling in a technology-shaped market.",
                "Student agency in shaping their own trajectory.",
            ]),
            ("Why it mattered", "The second session reinforced that future-readiness is not a one-time talk but an ongoing practice. It helped students connect skills, experiences, and reflection into a more coherent professional narrative."),
        ],
    },
    "dbs-coaching": {
        "sections": [
            ("Overview", "The coaching session was designed for students preparing for higher-level problem solving and competition settings. It emphasised disciplined thinking, preparation strategy, and stronger technical confidence in an Olympiad context."),
            ("What the session supported", None, [
                "Advanced competition preparation.",
                "More disciplined approaches to technical work.",
                "Exposure to higher standards of performance and reasoning.",
            ]),
            ("Why it mattered", "Coaching initiatives like this extend KBI HK's role beyond event hosting into capability development. They help students not only participate, but prepare with greater seriousness and direction."),
        ],
    },
    "dgjs-internship": {
        "sections": [
            ("Overview", "The internship gave students a rare chance to step outside a school context and experience a live technology environment. It helped bridge early exposure to blockchain with a broader understanding of how innovation ecosystems function."),
            ("What students experienced", None, [
                "Exposure to a professional innovation environment at HKSTP.",
                "A closer look at technology work beyond the classroom.",
                "An early sense of how emerging technologies connect to real industries and spaces.",
            ]),
            ("Why it mattered", "Experiences like this are important because they make technology pathways feel more concrete. For younger learners especially, seeing the environment around innovation can be as formative as learning the concepts themselves."),
        ],
    },
    "cyber-wg": {
        "sections": [
            ("Overview", "This working group was not a public-facing competition or workshop, but a more focused convening around cybersecurity themes. It created space for discussion, expert exchange, and early coordination on future directions and initiatives."),
            ("Focus", None, [
                "Cybersecurity as a cross-cutting concern in emerging technology.",
                "Expert dialogue on current and relevant security issues.",
                "Coordination around future initiatives and thematic exploration.",
            ]),
            ("Why it mattered", "As KBI HK's programming expands, cybersecurity cannot remain a side topic. The working group marked an important step toward giving security a more intentional place within the organisation's educational and strategic activity."),
        ],
    },
    "skillsprint-2025": {
        "sections": [
            ("Overview", "Designed as a concentrated learning series, FinTech SkillSprint gave participants practical exposure across several key domains rather than a single narrow topic. Its structure suited learners looking for a serious but accessible entry point into applied emerging-technology training."),
            ("What participants built", None, [
                "Exposure to blockchain and trust technology concepts.",
                "Foundational engagement with data science and AI.",
                "Short-form, skills-oriented learning linked to career exploration.",
            ]),
            ("Why it mattered", "The series reflected KBI HK's effort to create shorter, more flexible formats for technical development. It also showed how interdisciplinary training can help students explore adjacent fields before choosing a deeper pathway."),
        ],
    },
    "science-exhibition": {
        "sections": [
            ("Overview", "KBI HK's role in this event highlighted its commitment not only to internal programming, but also to wider science and student engagement platforms. By supporting delegate participation, the organisation contributed to cross-cultural exchange and a broader science-learning experience."),
            ("What the delegation involved", None, [
                "Engagement with local student science exhibits.",
                "Participation in exhibition-related activities.",
                "International student exchange and hosted delegation support.",
            ]),
            ("Why it mattered", "This event positioned KBI HK within a wider educational ecosystem, not only as a programme organiser but also as a collaborative supporting body. It showed how emerging-technology education can sit meaningfully alongside broader scientific culture and exchange."),
        ],
    },
    "eto-2025": {
        "sections": [
            ("Overview", "As a flagship event, ETO 2025 brought together finalists, related activities, and the broader emerging-technology vision into one shared platform. Hosting the event in Hong Kong reinforced the city's role as a meeting point for youth talent, technical ambition, and international exchange."),
            ("What defined the event", None, [
                "Three-day international programme in Hong Kong.",
                "Global participation from blockchain and data science finalists.",
                "A unified emerging-technologies framing across disciplines.",
            ]),
            ("Why it mattered", "ETO 2025 represented more than a competition. It signalled a broader effort to connect different technology domains, celebrate youth technical work on an international stage, and strengthen Hong Kong's place within that network."),
        ],
    },
}

EVENT_RECAPS.update(ARCHIVE_RECAPS)

SDG_2026_RECAP = {
    "sections": [
        ("Bridging SDGs, Competition Work, and Emerging Tech", "The HK SDG Summit 2026 was KBI Hong Kong's first formal collaboration with the Hong Kong Global Goals Council (GGC), adding a new layer to the chapter's long-standing competition ecosystem. Instead of only sending teams to olympiads, KBI HK brought concrete ETO 2025 projects and a structured emerging-technology workshop into a youth-led SDG summit context."),
        (None, "As a supporting organisation, KBI HK co-delivered the ETO 2025 SDG Awards in partnership with GGC, recognising one standout ETO/IBCOL/IDSOL project for each of the 17 Sustainable Development Goals. The awards turned abstract SDG icons into specific student-led solutions, showing how competition work maps directly onto global challenges."),
        (None, "In parallel, KBI HK ran a focused \"Accelerate Your Action: Bridging Possibility and Practicality\" workshop track for summit delegates — a rapid introduction to blockchain and trust technologies (BCTT), data science and AI (DSAI), and quantum computing and information theory (QCIT), then guidance in shaping ideas into implementable projects using the ETO Project Model Canvas."),
        ("Seventeen Goals, Seventeen Projects", "The ETO 2025 SDG Awards segment celebrated teams whose projects embodied each SDG in practice, drawing from IBCOL and IDSOL finalists across multiple regions. Highlights included:", [
            "SDG 1: No Poverty — Shufola (IBCOL25 BD‑26, Bangladesh): government-backed financing on a permissioned blockchain, with smart contracts and AI analytics for fairer food systems.",
            "SDG 2: Zero Hunger — Kaz Wheat Chain (IBCOL25 KZ‑68, Kazakhstan): digitising Kazakhstan's wheat supply chain for more trusted, faster, sustainable trade.",
            "SDG 3: Good Health and Well-being — DeOrphan Protocol (IBCOL25 HK‑35, Hong Kong): transparent, patient-directed funding for rare-disease cures.",
            "SDG 4: Quality Education — HOLOMED (IDSOL25 SR‑36, Suriname): AR converting 2D medical images into 3D models for learning.",
            "SDG 5: Gender Equality — WashWatch (IDSOL25 HK‑07, Hong Kong): AI detecting social washing by comparing claims with actions.",
            "SDG 6: Clean Water and Sanitation — SenseCore (IDSOL25 BD‑31, Bangladesh): IoT-based smart irrigation for water-stressed contexts.",
            "SDG 7: Affordable and Clean Energy — MEHR (IBCOL25 IR‑04, Iran): decentralised digital product passport protocol for solar panels.",
            "SDG 8: Decent Work and Economic Growth — AITHOS (IDSOL25 NL‑08, Netherlands): startup marketing copilot chaining reasoning models and live trend signals.",
            "SDG 9: Industry, Innovation and Infrastructure — TYCHICUS (IBCOL25 HK‑32, Hong Kong): verifiable, privacy-preserving audit trail for AI training data.",
            "SDG 10: Reduced Inequalities — Sentio (IDSOL25 BD‑33, Bangladesh): generative AI for emotion-centred learning across neurodiverse populations.",
            "SDG 11: Sustainable Cities and Communities — URBANOVA (IDSOL25 CN‑58, China): urban data for climate-resilient cities.",
            "SDG 12: Responsible Consumption and Production — BETTERNATIVE (IDSOL25 NL‑09, Netherlands): computer vision for traceable, eco-friendly shopping alternatives.",
            "SDG 13: Climate Action — CertiCrete (IBCOL25 CA‑06, Canada): secure auditing for carbon neutrality in sustainable materials.",
            "SDG 14: Life Below Water — AquaTune (IDSOL25 SE‑53, Sweden): data-driven acoustic simulation for underwater music training.",
            "SDG 15: Life on Land — Forest Lost, Fever Cost (IDSOL25 MO‑52, Macao): mapping forest loss to predict zoonotic disease hotspots.",
            "SDG 16: Peace, Justice and Strong Institutions — SafePass (IBCOL25 BD‑38, Bangladesh): blockchain ecosystem for ethical labour migration.",
            "SDG 17: Partnerships for the Goals — WhistleChain (IBCOL25 HK‑70, Hong Kong): secure whistleblower evidence platform with vetted attorneys.",
        ]),
        (None, "Framed within the summit's \"Accelerate Your Action\" theme, the awards showed how competition projects can evolve into SDG-aligned interventions across countries and disciplines."),
        ("The KBI x GGC Workshop: From Idea to Implementable Project", "As part of the summit programme, KBI HK delivered \"Accelerate Your Action: Bridging Possibility and Practicality\" in two back-to-back sections for secondary delegates (Grade 9–12 / Form 3–6), welcoming up to 20 GGC delegates per session with existing project ideas and defined problem spaces.", [
            "Rapidfire introduction to BCTT, DSAI, and QCIT — tied to solution design, not abstract theory.",
            "ETO Project Model Canvas (ETO‑PMC) as the central tool for implementable projects.",
            "Pre-workshop briefing package, solution design patterns presentation, and digital/printed ETO‑PMC worksheets.",
        ]),
        (None, "Workshop rundown (per 45‑minute session): 10:00–10:10 rapidfire Q&A on fundamentals; 10:10–10:30 solution design patterns by problem space; 10:30–10:45 ETO‑PMC design lab with live Q&A. Facilitated by Gabriel Chan, Kate Cruz Pun, and Kimmie Tang at CDNIS (two identical sessions on Saturday 7 March 2026)."),
        ("Why this event matters for KBI HK", "For KBI Hong Kong, the collaboration signalled a move from being \"the competition people\" to helping young innovators connect emerging technologies with global-issues leadership — recognising ETO 2025 teams through SDG-framed awards while equipping summit delegates with practical methods for emerging-tech-backed projects."),
    ],
    "closing": "The partnership with youth-led GGC reflects KBI HK's commitment to empowering students to own their spaces, while bringing the structure, rigour, and technical literacy needed to make those spaces more impactful over time.",
    "details_html": '''
              <div class="gallery-event-details">
                <h3>Event details</h3>
                <dl class="gallery-details-grid">
                  <div><dt>Date</dt><dd>Early March 2026 (workshop sessions on Saturday 7 March 2026)</dd></div>
                  <div><dt>Venue</dt><dd>Canadian International School of Hong Kong (CDNIS)</dd></div>
                  <div><dt>Format</dt><dd>Supporting organisation · SDG awards · emerging-tech ideation workshop (two 45‑minute sections)</dd></div>
                  <div><dt>Programme</dt><dd>ETO 2025 SDG Awards · BCTT/DSAI/QCIT crash course · ETO Project Model Canvas design lab</dd></div>
                  <div><dt>Partners</dt><dd>Hong Kong Global Goals Council · KBI Hong Kong · ETO / IBCOL / IDSOL network</dd></div>
                  <div><dt>Audience</dt><dd>Youth accelerators, NGOs, clubs, and KBI HK partners</dd></div>
                </dl>
              </div>''',
}


def render_recap(event_id):
    """Return recap HTML block for an event id, or empty string."""
    import html as html_mod

    if event_id == "hk-sdg-summit-2026":
        data = SDG_2026_RECAP
    elif event_id in EVENT_RECAPS:
        data = EVENT_RECAPS[event_id]
    else:
        return ""

    parts = ['<div class="gallery-event-recap">']
    for sec in data["sections"]:
        if len(sec) == 2:
            title, para = sec
            bullets = None
        else:
            title, para, bullets = sec[0], sec[1], sec[2]
        if title:
            parts.append(f"<h3>{html_mod.escape(title)}</h3>")
        if para:
            parts.append(f"<p>{html_mod.escape(para)}</p>")
        if bullets:
            is_sdg = any(str(b).startswith("SDG ") for b in bullets)
            ul_cls = ' class="gallery-sdg-list"' if is_sdg else ""
            parts.append(f"<ul{ul_cls}>")
            for b in bullets:
                if is_sdg and " — " in b:
                    goal, rest = b.split(" — ", 1)
                    parts.append(
                        f"<li><strong>{html_mod.escape(goal)}</strong> — {html_mod.escape(rest)}</li>"
                    )
                else:
                    parts.append(f"<li>{html_mod.escape(b)}</li>")
            parts.append("</ul>")
    if data.get("details_html"):
        parts.append(data["details_html"])
    if data.get("closing"):
        parts.append(
            f'<p class="gallery-event-closing">{html_mod.escape(data["closing"])}</p>'
        )
    parts.append("</div>")
    return "\n            ".join(parts)
