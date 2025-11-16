from flask import Blueprint, render_template

bp = Blueprint("portfolio", __name__)


@bp.route("/portfolio")
def portfolio():
    hero = {
        "name": "Avery Quinn",
        "roles": ["CS Student", "Creative Coder", "Full-Stack Dev"],
        "tagline": "Design-forward developer crafting ultra-fast experiences.",
        "bio": (
            "I'm a computer science student obsessed with building polished, human-centered interfaces "
            "and performant systems. Here's a snapshot of the playground where I experiment with "
            "motion, micro-interactions, and emerging tech."
        ),
        "cta_primary": {"label": "Download Résumé", "url": "#"},
        "cta_secondary": {"label": "Let's Talk", "url": "#contact"},
    }

    stats = [
        {"label": "Projects", "value": "24", "detail": "concept-to-launch"},
        {"label": "Hackathons", "value": "12", "detail": "global podium finishes"},
        {"label": "Coffee", "value": "∞", "detail": "fueling late-night builds"},
    ]

    projects = [
        {
            "title": "NeuroEdge Studio",
            "subtitle": "Realtime AI dashboard for the creative industry",
            "description": "Designed a cinematic data canvas with GPU-accelerated visuals, sub-100ms interactions, and adaptive layouts.",
            "tags": ["WebGL", "FastAPI", "WebSockets", "UX"],
            "image": "https://images.unsplash.com/photo-1483478550801-ceba5fe50e8e?auto=format&fit=crop&w=1200&q=80",
            "link": "#",
        },
        {
            "title": "Pulseboard",
            "subtitle": "Low-latency ops board for campus mobility",
            "description": "Built an offline-first PWA with predictive routing, gradient theming, and tactile micro-interactions.",
            "tags": ["TypeScript", "PWA", "GraphQL", "Design Systems"],
            "image": "https://images.unsplash.com/photo-1469474968028-56623f02e42e?auto=format&fit=crop&w=1200&q=80",
            "link": "#",
        },
        {
            "title": "Aurora Compiler",
            "subtitle": "DSL + compiler toolkit for shader artists",
            "description": "Created a playful syntax, VS Code extension, and visual debugger that transforms creative coding workflows.",
            "tags": ["Rust", "Compilers", "VS Code", "DX"],
            "image": "https://images.unsplash.com/photo-1520607162513-77705c0f0d4a?auto=format&fit=crop&w=1200&q=80",
            "link": "#",
        },
    ]

    experiences = [
        {
            "role": "Product Engineering Intern",
            "company": "Nova Labs",
            "timeframe": "2023 — Present",
            "summary": "Prototyped motion-heavy dashboards and shipped production-ready React + Flask surfaces.",
            "highlights": [
                "Cut render times by 38% via memoized data flows",
                "Partnered with design to build a living design system",
            ],
        },
        {
            "role": "Research Fellow",
            "company": "Human-Computer Interaction Lab",
            "timeframe": "2022 — 2023",
            "summary": "Explored tangible interfaces and spatial computing for inclusive education.",
            "highlights": [
                "Co-authored paper on adaptive haptics",
                "Built AR storytelling toolkit adopted by 4 classrooms",
            ],
        },
        {
            "role": "Freelance Creative Technologist",
            "company": "Self-Initiated",
            "timeframe": "Ongoing",
            "summary": "Partner with early-stage founders to transform sketches into launch-ready experiences.",
            "highlights": [
                "End-to-end delivery of 7 branded microsites",
                "Integrated analytics + A/B testing for rapid learning",
            ],
        },
    ]

    skill_groups = [
        {"title": "Core Stack", "stack": ["Python", "TypeScript", "Rust", "Go", "SQL", "GraphQL"]},
        {"title": "Frameworks", "stack": ["React", "Next.js", "Flask", "FastAPI", "Tailwind", "Framer Motion"]},
        {"title": "Tooling", "stack": ["Figma", "Notion", "Blender", "Docker", "AWS", "Vite"]},
    ]

    spotlights = [
        {
            "title": "Current focus",
            "description": "Building ambient computing prototypes that blur the line between physical and digital worlds.",
        },
        {
            "title": "Recent win",
            "description": "Led a team of 4 to sweep a 48-hour hackathon with an adaptive transit assistant.",
        },
        {
            "title": "What's next",
            "description": "Exploring generative UI systems + compiler-assisted design workflows.",
        },
    ]

    contact = {
        "email": "hello@avery.codes",
        "location": "Remote • Earth",
        "availability": "Open for internships, freelance collaborations, and research labs",
    }

    return render_template(
        "portfolio.html",
        hero=hero,
        stats=stats,
        projects=projects,
        experiences=experiences,
        skill_groups=skill_groups,
        spotlights=spotlights,
        contact=contact,
    )
