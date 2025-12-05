# pages/results_page.py

import html
import streamlit as st
from utils import (
    glass_container,
    create_gauge_chart,
    build_chip,
    render_section_header,
    render_stat_deck,
    render_skill_chips,
)
from backend.career_analyzer import get_job_application_links


RESULTS_STYLES = """
<style>
.results-hero {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    gap: 1.6rem;
    margin-bottom: 2rem;
}
.hero-card {
    border-radius: 28px;
    padding: 2rem;
    border: 1px solid rgba(255,255,255,0.08);
    background: rgba(7,9,22,0.82);
    box-shadow: 0 30px 80px rgba(2,5,18,0.5);
}
.hero-card h2 { margin: 0.4rem 0 0.6rem; }
.hero-card p { color: rgba(245,246,255,0.75); }
.profile-metadata {
    display: flex;
    flex-wrap: wrap;
    gap: 0.6rem;
    margin-top: 1rem;
}
.profile-metadata span {
    border-radius: 18px;
    padding: 0.4rem 0.9rem;
    border: 1px solid rgba(255,255,255,0.12);
    background: rgba(255,255,255,0.03);
    font-size: 0.9rem;
}
.skill-panel {
    border-radius: 26px;
    padding: 1.7rem;
    border: 1px solid rgba(255,255,255,0.08);
    background: rgba(6,10,24,0.78);
}
.skill-panel h4 { margin: 0 0 0.8rem; }
.job-link-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(190px, 1fr));
    gap: 0.9rem;
    margin-top: 1rem;
}
.job-link {
    border-radius: 24px;
    border: 1px solid rgba(125,211,252,0.3);
    padding: 0.95rem 1.2rem;
    background: linear-gradient(135deg, rgba(7,12,28,0.9), rgba(9,14,32,0.85));
    color: #e0f2ff;
    font-weight: 600;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 0.9rem;
    box-shadow: inset 0 1px 0 rgba(255,255,255,0.05), 0 15px 35px rgba(2,6,20,0.45);
    transition: transform 220ms ease, border 220ms ease, box-shadow 220ms ease;
}
.job-link:hover {
    transform: translateY(-4px);
    border-color: rgba(125,211,252,0.65);
    box-shadow: 0 25px 50px rgba(4,9,30,0.55);
}
.job-link-icon {
    width: 42px;
    height: 42px;
    border-radius: 14px;
    background: rgba(125,211,252,0.15);
    display: grid;
    place-items: center;
    font-size: 1.2rem;
}
.job-link-name {
    flex: 1;
    color: #f8fafc;
    font-size: 0.98rem;
}
.job-link-arrow {
    font-size: 1.1rem;
    color: #7dd3fc;
}
.tab-shell { margin-top: 1rem; }
.tab-body {
    padding: 1.2rem 0;
}
.gauge-stack {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 1rem;
}
.micro-pill {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    border-radius: 20px;
    padding: 0.35rem 0.9rem;
    border: 1px solid rgba(255,255,255,0.12);
    background: rgba(255,255,255,0.03);
    font-size: 0.85rem;
}
.role-divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.12), transparent);
    margin: 1.6rem 0;
}
</style>
"""

def results_page():
    st.markdown(RESULTS_STYLES, unsafe_allow_html=True)

    c1, c2 = st.columns([3, 1])
    with c1:
        st.markdown(build_chip("Analysis complete", variant="accent"), unsafe_allow_html=True)
        st.markdown("<h1>Career match intelligence</h1>", unsafe_allow_html=True)
    with c2:
        if st.button("New Upload", type="secondary"):
            st.session_state.reset_session()
            st.rerun()

    resume_data = st.session_state.resume_data or {}
    matches = st.session_state.career_matches

    if not matches:
        st.warning("No matches found. Please re-upload your resume.")
        return

    profile_name = html.escape(resume_data.get('name', 'Your Profile'))
    skill_count = len(resume_data.get('skills', []))
    first_match = matches[0]

    # Hero summary
    st.markdown(
        f"""
        <div class="results-hero">
            <div class="hero-card">
                {build_chip('Profile decoded', variant='accent')}
                <h2>{profile_name}</h2>
                <p>We mapped {skill_count} unique skills and surfaced your strongest-fit roles.</p>
                <div class="profile-metadata">
                    <span>{skill_count} skills parsed</span>
                    <span>{len(matches)} matching roles</span>
                </div>
            </div>
            <div class="hero-card">
                <h3 style="margin:0">Skill DNA</h3>
                <div class="skill-panel">
                    {render_skill_chips(resume_data.get('skills', []), variant='have', empty_text='No core skills detected.')}
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    render_stat_deck(
        [
            {"label": "Overall Fit", "value": f"{first_match.get('combined_score', 0)}%", "icon": "🎯"},
            {"label": "Market Demand", "value": f"{first_match.get('demand_score', 0)}/100", "icon": "📈"},
            {"label": "Skills Parsed", "value": str(skill_count), "icon": "🧬"},
            {"label": "Roles Matched", "value": str(len(matches)), "icon": "🛰️"},
        ]
    )

    render_section_header(
        "Top recommendations",
        "We keep the layout minimal so you can compare roles without digging through noise.",
        eyebrow="Calibrated matches",
        align="left",
    )

    tab_names = [match['role_name'] for match in matches[:3]]
    tabs = st.tabs(tab_names)

    for idx, tab in enumerate(tabs):
        with tab:
            match = matches[idx]
            known = match.get('known_skills', [])
            missing = match.get('missing_skills', [])

            m_col1, m_col2 = st.columns([1, 2])

            with m_col1:
                with glass_container():
                    st.markdown("<h5>Match pulse</h5>", unsafe_allow_html=True)
                    st.plotly_chart(
                        create_gauge_chart(match.get('combined_score', 0), "Overall Fit"),
                        use_container_width=True,
                    )
                    st.plotly_chart(
                        create_gauge_chart(match.get('demand_score', 0), "Market Demand"),
                        use_container_width=True,
                    )

                if st.button(f"View Roadmap →", key=f"btn_{idx}", use_container_width=True):
                    st.session_state.selected_role = match
                    st.session_state.roadmap_steps = None
                    st.session_state.page = 'roadmap'
                    st.rerun()

            with m_col2:
                with glass_container():
                    st.markdown(
                        f"""
                        <div class='match-tab'>
                            <div class='micro-pill'>Rank #{idx + 1}</div>
                            <h2>{html.escape(match['role_name'])}</h2>
                            <p>{html.escape(match.get('description', 'No description available.'))}</p>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

                st.markdown("#### Skill gap analysis")
                c_a, c_b = st.columns(2)
                with c_a:
                    with glass_container():
                        st.markdown(f"**✅ Skills matched ({len(known)})**")
                        st.markdown(
                            render_skill_chips(known, variant="have", empty_text="None detected"),
                            unsafe_allow_html=True,
                        )
                with c_b:
                    with glass_container():
                        st.markdown(f"**🚀 Skills to acquire ({len(missing)})**")
                        st.markdown(
                            render_skill_chips(
                                missing, variant="need", empty_text="You are fully qualified!"
                            ),
                            unsafe_allow_html=True,
                        )

                st.markdown('<div class="role-divider"></div>', unsafe_allow_html=True)
                with glass_container():
                    st.markdown("<h5>🌐 Live job signals</h5>", unsafe_allow_html=True)
                    job_links = get_job_application_links(role_name=match['role_name'], known_skills=known)
                    if job_links:
                        cards = ''.join(
                            f"<a class='job-link' href='{html.escape(link['url'])}' target='_blank'>"
                            f"<span class='job-link-icon'>{link.get('icon', '🔗')}</span>"
                            f"<span class='job-link-name'>{html.escape(link['platform'])}</span>"
                            "<span class='job-link-arrow'>↗</span>"
                            "</a>"
                            for link in job_links
                        )
                        st.markdown(f'<div class="job-link-grid">{cards}</div>', unsafe_allow_html=True)
                    else:
                        st.info("Job search links could not be generated for this role.", icon="ℹ️")