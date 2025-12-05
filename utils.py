# utils.py

import streamlit as st
import plotly.graph_objects as go
import contextlib
import re
from html import escape


# Palette tuned to the global neon-glass theme
NEON_PALETTE = {
    "excellent": "#06b6d4",
    "good": "#3b82f6",
    "average": "#fbbf24",
    "poor": "#f87171",
}

# -----------------------------------------------------------------------------
# CHART HELPERS (Dark Mode)
# -----------------------------------------------------------------------------
def _score_color(score: float) -> str:
    if score >= 80:
        return NEON_PALETTE["excellent"]
    if score >= 60:
        return NEON_PALETTE["good"]
    if score >= 40:
        return NEON_PALETTE["average"]
    return NEON_PALETTE["poor"]


def create_gauge_chart(score, title, subtitle: str | None = None):
    """Neon gauge card used across results/roadmap screens."""
    color = _score_color(score)

    steps = [
        {"range": [0, 40], "color": "rgba(248,113,113,0.12)"},
        {"range": [40, 60], "color": "rgba(251,191,36,0.12)"},
        {"range": [60, 80], "color": "rgba(96,165,250,0.12)"},
        {"range": [80, 100], "color": "rgba(45,212,191,0.18)"},
    ]

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=score,
            title={
                "text": f"{title}<br><span style='font-size:0.75em;color:#94a3b8;'>{subtitle or ''}</span>",
                "font": {"size": 14, "color": "#94a3b8", "family": "Space Grotesk"},
            },
            number={"font": {"size": 36, "color": "#f8fafc", "family": "Space Grotesk"}},
            gauge={
                "axis": {
                    "range": [0, 100],
                    "tickwidth": 1,
                    "tickcolor": "#475569",
                    "tickfont": {"color": "#94a3b8", "size": 10},
                },
                "bar": {"color": color, "thickness": 0.78},
                "bgcolor": "rgba(15,23,42,0.4)",
                "borderwidth": 0,
                "steps": steps,
                "threshold": {
                    "line": {"color": "#e2e8f0", "width": 2},
                    "thickness": 0.8,
                    "value": score,
                },
            },
        )
    )

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=10, r=10, t=40, b=0),
        height=190,
    )
    return fig

# -----------------------------------------------------------------------------
# UI HELPERS
# -----------------------------------------------------------------------------
@contextlib.contextmanager
def glass_container(variant: str | None = None):
    """A context manager to create a glass container."""
    classes = "glass-container"
    if variant:
        classes = f"{classes} {variant}"
    st.markdown(f'<div class="{classes}">', unsafe_allow_html=True)
    yield
    st.markdown('</div>', unsafe_allow_html=True)


def build_chip(text: str, variant: str = "neutral", icon: str | None = None) -> str:
    """Return a styled chip element for consistent labeling."""
    icon_html = f"<span class='chip-icon'>{icon}</span>" if icon else ""
    return f"<span class='ui-chip {variant}'>{icon_html}{escape(text)}</span>"


def render_section_header(
    title: str,
    subtitle: str | None = None,
    eyebrow: str | None = None,
    align: str = "center",
):
    """Standardized heading for sections with optional eyebrow + subtitle."""
    classes = f"section-header align-{align}"
    eyebrow_html = f"<div class='section-eyebrow'>{escape(eyebrow)}</div>" if eyebrow else ""
    subtitle_html = f"<p>{escape(subtitle)}</p>" if subtitle else ""
    st.markdown(
        f"""
        <div class="{classes}">
            {eyebrow_html}
            <h2>{escape(title)}</h2>
            {subtitle_html}
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_stat_deck(stats: list[dict]):
    """Render a responsive stat deck from dicts with label/value/icon."""
    cards = []
    for stat in stats:
        label = escape(stat.get("label", ""))
        value = escape(stat.get("value", ""))
        icon = stat.get("icon")
        helper = escape(stat.get("helper", "")) if stat.get("helper") else ""
        icon_html = f"<span class='stat-icon'>{icon}</span>" if icon else ""
        helper_html = f"<div class='stat-helper'>{helper}</div>" if helper else ""
        cards.append(
            (
                "<div class='stat-card'>"
                f"{icon_html}"
                f"<div class='stat-label'>{label}</div>"
                f"<div class='stat-value'>{value}</div>"
                f"{helper_html}"
                "</div>"
            )
        )
    st.markdown(f"<div class='stat-deck'>{''.join(cards)}</div>", unsafe_allow_html=True)


def render_skill_chips(
    skills: list[str],
    variant: str = "have",
    empty_text: str = "No skills to show",
):
    """Render a list of skills as chips with graceful fallback."""
    if not skills:
        return f"<span class='skill-chip {variant}'>{escape(empty_text)}</span>"
    return "".join(
        f"<span class='skill-chip {variant}'>{escape(skill)}</span>" for skill in skills
    )

# -----------------------------------------------------------------------------
# PARSING & REPORTING HELPERS
# -----------------------------------------------------------------------------
def parse_roadmap_step(step_string):
    """
    Parses a string from the AI into a structured dictionary.
    Assumes a format like: "1. Title [Duration]: Description. Resources: Res1, Res2"
    """
    parsed = {
        'step': '',
        'title': '',
        'duration': 'N/A',
        'description': 'No description provided.',
        'resources': []
    }

    # Regex to capture all parts
    pattern = re.compile( 
        r"""(\d+)\.\s* # 1. Step number
        ([^\[:]+)\s* # 2. Title (until [ or :)
        (?:\[([^\]]+)\])?\s* # 3. [Duration] (optional)
        :\s* # Separator :
        (.*?)\s* # 4. Description (non-greedy)
        (?:Resources:\s*(.*))?                       # 5. Resources: ... (optional)
        $""", re.VERBOSE | re.DOTALL
    )

    match = pattern.match(step_string)
    if match:
        parsed['step'] = match.group(1).strip()
        parsed['title'] = match.group(2).strip()
        parsed['duration'] = match.group(3).strip() if match.group(3) else 'N/A'
        parsed['description'] = match.group(4).strip()
        if match.group(5):
            # Split resources by comma and strip whitespace
            parsed['resources'] = [res.strip() for res in match.group(5).split(',') if res.strip()]
    else:
        # Fallback for unstructured strings
        parsed['description'] = step_string

    return parsed

def generate_report(role: dict) -> str:
    """Generate a text report for download"""
    # Imports needed for backend call
    from backend.career_analyzer import get_learning_plan, generate_career_roadmap

    report = f"""
CAREER COMPASS AI - CAREER ANALYSIS REPORT
==========================================

Career Role: {role['role_name']}
Description: {role['description']}

SCORES
------
Skills Match: {role['match_score']}%
Industry Demand: {role['demand_score']}/100
Overall Score: {role['combined_score']}/100

SKILLS YOU HAVE ({len(role['known_skills'])})
-----------------
{chr(10).join('✓ ' + skill for skill in role['known_skills']) if role['known_skills'] else 'None'}

SKILLS TO LEARN ({len(role['missing_skills'])})
---------------
{chr(10).join('○ ' + skill for skill in role['missing_skills']) if role['missing_skills'] else 'None'}

LEARNING PLAN
-------------
"""
    
    if role['missing_skills']:
        learning_plan = get_learning_plan(role)
        total_hours = 0
        for item in learning_plan:
            report += f"\nSkill: {item['skill']}\n"
            report += f"Resource: {item['youtube_link']}\n"
            report += f"Estimated Time: {item['estimated_hours']} hours\n"
            total_hours += item['estimated_hours']
        
        report += f"\nTotal Learning Time: {total_hours} hours ({total_hours//40} weeks)\n"
    
    report += f"""
CAREER PROGRESSION ROADMAP
--------------------------
{generate_career_roadmap(role)}

---
Generated by Career Compass AI
"""
    
    return report