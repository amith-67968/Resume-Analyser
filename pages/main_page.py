# pages/main_page.py

import streamlit as st
from utils import (
    glass_container,
    build_chip,
    render_section_header,
    render_stat_deck,
)

LANDING_STYLES = """
<style>
.page-spacer { height: 28px; }
.hero-shell {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    gap: 2rem;
    align-items: stretch;
    margin-bottom: 2.5rem;
}
.hero-content h1 {
    font-size: clamp(2.8rem, 5vw, 4.3rem);
    line-height: 1.05;
    margin: 0.8rem 0;
}
.hero-content p {
    color: rgba(244, 246, 255, 0.8);
    font-size: 1.15rem;
    line-height: 1.7;
    margin: 0;
}
.cta-row {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
    margin-top: 2.2rem;
    align-items: center;
}
.ghost-link {
    padding: 0.85rem 1.4rem;
    border-radius: 20px;
    border: 1px solid rgba(255,255,255,0.18);
    color: #f8fafc;
    font-weight: 600;
    text-decoration: none;
    transition: opacity 220ms ease;
}
.ghost-link:hover { opacity: 0.8; }
.hero-panel {
    border-radius: 30px;
    padding: 2.2rem;
    border: 1px solid rgba(255,255,255,0.12);
    background: linear-gradient(135deg, rgba(125,211,252,0.08), rgba(192,132,252,0.08));
    box-shadow: 0 30px 80px rgba(2,5,20,0.55);
    display: flex;
    flex-direction: column;
    gap: 1.4rem;
}
.panel-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.panel-row strong { font-size: 2.1rem; }
.signal-track {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
}
.signal-card {
    border-radius: 18px;
    padding: 1rem;
    border: 1px solid rgba(255,255,255,0.1);
    background: rgba(4,8,18,0.6);
    min-height: 110px;
}
.signal-card span { font-size: 1.7rem; display:block; margin-bottom:0.3rem; }
.feature-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 1.2rem;
    margin-top: 1.5rem;
}
.feature-card {
    border-radius: 24px;
    padding: 1.6rem;
    border: 1px solid rgba(255,255,255,0.08);
    background: rgba(8,12,28,0.7);
    box-shadow: inset 0 0 0 1px rgba(255,255,255,0.02);
    transition: transform 260ms ease, border 260ms ease;
}
.feature-card:hover { transform: translateY(-5px); border-color: rgba(125,211,252,0.35); }
.feature-card h3 { margin: 0.6rem 0; }
.process-track {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 1rem;
    margin-top: 2rem;
}
.process-step {
    position: relative;
    border-radius: 22px;
    padding: 1.5rem 1.3rem;
    border: 1px solid rgba(255,255,255,0.1);
    background: rgba(5,10,22,0.7);
    overflow: hidden;
}
.process-step::after {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(120deg, rgba(255,255,255,0.08), transparent 60%);
    opacity: 0;
    transition: opacity 260ms ease;
}
.process-step:hover::after { opacity: 1; }
.process-index {
    font-size: 0.82rem;
    letter-spacing: 0.25em;
    text-transform: uppercase;
    color: #94a3b8;
}
.signal-band {
    margin-top: 3rem;
    border-radius: 26px;
    padding: 1.6rem 1.8rem;
    border: 1px solid rgba(125,211,252,0.25);
    background: linear-gradient(135deg, rgba(125,211,252,0.14), rgba(192,132,252,0.12));
    box-shadow: 0 30px 80px rgba(2,5,18,0.45);
    display: flex;
    flex-direction: column;
    gap: 0.6rem;
    text-align: center;
}
@media (max-width: 640px) {
    .cta-row { flex-direction: column; align-items: stretch; }
    .signal-track { grid-template-columns: 1fr; }
}
</style>
"""


def main_page():
    st.markdown(LANDING_STYLES, unsafe_allow_html=True)
    st.markdown('<div class="page-spacer"></div>', unsafe_allow_html=True)

    # Hero Section
    col1, col2 = st.columns([1.1, 0.9])
    with col1:
        st.markdown(build_chip("AI Career Copilot", variant="accent"), unsafe_allow_html=True)
        st.markdown(
            """
            <div class="hero-content">
                <h1>Steer your career with a calm, precision-grade dashboard.</h1>
                <p>Career Compass decodes your resume, distills the strongest signals, and assembles a living roadmap so you always know the next best move.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown('<div class="cta-row">', unsafe_allow_html=True)
        if st.button("Start instant analysis", key="start_btn"):
            st.session_state.page = 'upload'
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown(
            """
            <div class="hero-panel">
                <div class="panel-row">
                    <span>Live readiness score</span>
                    <strong>92%</strong>
                </div>
                <div class="signal-track">
                    <div class="signal-card">
                        <span>🧠</span>
                        <strong>Skill Graph</strong>
                        <p>Signals normalized across 500+ tech roles.</p>
                    </div>
                    <div class="signal-card">
                        <span>🛰️</span>
                        <strong>Job Radar</strong>
                        <p>Real-time role demand + curated listings.</p>
                    </div>
                    <div class="signal-card">
                        <span>🧭</span>
                        <strong>Roadmap AI</strong>
                        <p>Adaptive sprints with effort estimates.</p>
                    </div>
                    <div class="signal-card">
                        <span>🔐</span>
                        <strong>Private Vault</strong>
                        <p>In-memory parsing, never stored.</p>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    render_stat_deck(
        [
            {"label": "Professionals Guided", "value": "12K+", "icon": "🌍"},
            {"label": "Role-Match Satisfaction", "value": "94%", "icon": "💠"},
            {"label": "Time to Signal", "value": "< 60s", "icon": "⚡"},
            {"label": "Paths Simulated", "value": "500+", "icon": "🧩"},
        ]
    )

    render_section_header(
        "What you'll unlock",
        "Streamlined modules keep the interface calm while surfacing only the signal you need to decide.",
        eyebrow="Experience pillars",
    )

    feature_cards = [
        ("🧬", "360° Profile Graph", "Parse context-rich skills, tools, seniority, and quantified impact."),
        ("🎯", "Role Intelligence", "Match against live market demand and curated IC/lead roles."),
        ("📚", "Learning Navigator", "Micro-sprints with resource links, pacing, and effort ranges."),
        ("🛡️", "Data Privacy", "Files processed in-memory with single-session retention."),
    ]
    st.markdown('<div class="feature-grid">', unsafe_allow_html=True)
    for icon, title, copy in feature_cards:
        st.markdown(
            f"""
            <div class="feature-card">
                <span style=\"font-size:1.8rem\">{icon}</span>
                <h3>{title}</h3>
                <p>{copy}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    st.markdown('</div>', unsafe_allow_html=True)

    render_section_header(
        "Flow with confidence",
        "Each stage is intentionally minimal so you stay focused on decisions, not UI noise.",
        eyebrow="Journey map",
    )

    workflow_data = [
        ("01", "Secure Upload", "Drop a PDF/TXT. Signals never leave the encrypted session."),
        ("02", "Signal Extraction", "Resume intelligence cleans, tags, and scores every keyword."),
        ("03", "Career Match", "Vector similarity plus labor insights surface your best-fit roles."),
        ("04", "Roadmap Launch", "Get a phased learning sprint plus live job boards in one tap."),
    ]
    st.markdown('<div class="process-track">', unsafe_allow_html=True)
    for idx, title, desc in workflow_data:
        st.markdown(
            f"""
            <div class="process-step">
                <div class="process-index">{idx}</div>
                <h4>{title}</h4>
                <p>{desc}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="signal-band">
            <strong>✨ Built for strategic operators.</strong>
            <p>Less dashboard clutter, more direct signal. Your AI copilot blends resume intelligence, labor-market telemetry, and adaptive learning plans—so momentum always feels calm and intentional.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )