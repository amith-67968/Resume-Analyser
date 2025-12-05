# pages/roadmap_page.py

import html
import streamlit as st
import pandas as pd
from utils import (
    glass_container,
    parse_roadmap_step,
    generate_report,
    build_chip,
    render_section_header,
    render_stat_deck,
    render_skill_chips,
)
from backend.career_analyzer import get_learning_plan, generate_career_roadmap


ROADMAP_STYLES = """
<style>
.roadmap-hero {
    border-radius: 34px;
    padding: 2.6rem;
    border: 1px solid rgba(255,255,255,0.12);
    background: linear-gradient(135deg, rgba(125,211,252,0.16), rgba(192,132,252,0.12));
    text-align: center;
    box-shadow: 0 32px 90px rgba(3,6,20,0.55);
    margin-bottom: 2rem;
}
.roadmap-hero h1 { margin: 0.5rem 0 0.8rem; font-size: clamp(2.3rem, 4vw, 3.4rem); }
.roadmap-hero p { max-width: 720px; margin: 0 auto; line-height: 1.7; color: rgba(245,246,255,0.78); }
.stage-track {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
    gap: 0.8rem;
    margin-top: 1.8rem;
}
.stage-pill {
    border-radius: 999px;
    padding: 0.65rem 1rem;
    border: 1px solid rgba(255,255,255,0.2);
    display: flex;
    justify-content: center;
    gap: 0.45rem;
    font-weight: 600;
}
.stage-pill.complete { background: rgba(16,185,129,0.2); color: #4ade80; border-color: rgba(16,185,129,0.4); }
.stage-pill.active { background: rgba(125,211,252,0.2); color: #7dd3fc; border-color: rgba(125,211,252,0.5); }

.skill-lanes {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 1.2rem;
    margin-top: 1.2rem;
}
.lane-card {
    border-radius: 24px;
    border: 1px solid rgba(255,255,255,0.08);
    background: rgba(6,10,22,0.8);
    padding: 1.4rem;
}
.lane-card h4 { margin: 0 0 0.6rem; }

.goal-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 1rem;
    margin-top: 1.2rem;
}
.goal-card {
    border-radius: 22px;
    border: 1px solid rgba(255,255,255,0.08);
    background: rgba(5,9,20,0.75);
    padding: 1.3rem;
    min-height: 180px;
}
.goal-duration { font-size: 0.85rem; color: #fcd34d; }

.timeline-shell {
    margin-top: 1.5rem;
    position: relative;
    padding-left: 28px;
}
.timeline-shell::before {
    content: '';
    position: absolute;
    left: 12px;
    top: 0;
    bottom: 0;
    width: 2px;
    background: linear-gradient(180deg, rgba(125,211,252,0.6), rgba(192,132,252,0));
}
.timeline-card {
    position: relative;
    margin-bottom: 1.5rem;
    border-radius: 24px;
    border: 1px solid rgba(255,255,255,0.08);
    background: rgba(7,11,24,0.82);
    padding: 1.4rem 1.6rem 1.2rem;
    box-shadow: inset 0 0 0 1px rgba(255,255,255,0.02);
}
.timeline-card::before {
    content: '';
    position: absolute;
    left: -22px;
    top: 18px;
    width: 12px;
    height: 12px;
    border-radius: 50%;
    background: #7dd3fc;
    box-shadow: 0 0 0 8px rgba(125,211,252,0.15);
}
.resource-list { margin: 0.5rem 0 0; padding-left: 1.2rem; color: rgba(245,246,255,0.8); }

.learning-banner {
    margin-top: 1.5rem;
    border-radius: 22px;
    padding: 1.4rem;
    border: 1px solid rgba(124,58,237,0.4);
    background: rgba(124,58,237,0.15);
    color: #f4f3ff;
}

@media (max-width: 640px) {
    .timeline-shell { padding-left: 20px; }
    .timeline-card::before { left: -18px; }
}
</style>
"""

def roadmap_page():
    st.markdown(ROADMAP_STYLES, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("← Back to Results", type="secondary"):
        st.session_state.page = 'results'
        st.rerun()

    role = st.session_state.selected_role
    if not role:
        st.warning("No role selected. Please go back to the results page and select a role.")
        return

    known_skills = role.get('known_skills', [])
    missing_skills = role.get('missing_skills', [])
    fit_score = role.get('combined_score', 0)
    demand_score = role.get('demand_score', 0)
    match_score = role.get('match_score', 0)

    if st.session_state.roadmap_steps is None:
        with st.spinner("🤖 AI is crafting your personalized career steps..."):
            try:
                roadmap_steps = generate_career_roadmap(role)
                st.session_state.roadmap_steps = roadmap_steps
            except Exception as exc:
                st.error(f"Could not generate roadmap: {exc}")
                return

    roadmap_steps = st.session_state.roadmap_steps or []

    # Hero section with progress indicators
    stage_labels = [
        ("Discover", "complete"),
        ("Upskill", 'active' if missing_skills else 'complete'),
        ("Build", '' if missing_skills else 'active'),
        ("Launch", '')
    ]
    progress_html = ''.join(
        f'<div class="stage-pill {state}">{label}</div>'
        for label, state in stage_labels
    )

    st.markdown(
        f"""
        <div class="roadmap-hero">
            {build_chip('Personalized strategy', variant='accent')}
            <h1>Your pathway to {html.escape(role['role_name'])}</h1>
            <p>{html.escape(role.get('description', 'Move with intention using your AI mentor.'))}</p>
            <div class="stage-track">{progress_html}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    render_stat_deck(
        [
            {"label": "Match score", "value": f"{match_score}%", "icon": "🎯"},
            {"label": "Overall fit", "value": f"{fit_score}%", "icon": "🌌"},
            {"label": "Industry demand", "value": f"{demand_score}/100", "icon": "📈"},
            {"label": "Skills ready", "value": str(len(known_skills)), "icon": "✅"},
        ]
    )

    # Skill momentum section
    render_section_header(
        "Skill momentum",
        "Celebrate what is already compounding while keeping the next steps in focus.",
        eyebrow="Signal lanes",
        align="left",
    )
    with glass_container():
        st.markdown(
            f"""
            <div class="skill-lanes">
                <div class="lane-card">
                    <h4>✅ Ready arsenal ({len(known_skills)})</h4>
                    {render_skill_chips(known_skills, variant='have', empty_text='Add more skills to your resume to populate this lane.')}
                </div>
                <div class="lane-card">
                    <h4>📚 Next up ({len(missing_skills)})</h4>
                    {render_skill_chips(missing_skills, variant='need', empty_text='No gaps detected — nice!')}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Micro goals based on roadmap preview
    if roadmap_steps:
        with glass_container():
            st.markdown('### ✨ Momentum milestones')
            st.markdown('<p style="color:#94a3b8">High-leverage steps curated for the next sprint.</p>', unsafe_allow_html=True)

            cards_html = []
            for step_string in roadmap_steps[:3]:
                parsed = parse_roadmap_step(step_string)
                title = html.escape(parsed.get('title', 'Next Step'))
                desc = html.escape(parsed.get('description', ''))
                duration = html.escape(parsed.get('duration', 'N/A'))
                cards_html.append(
                    (
                        '<div class="goal-card">'
                        f'<div class="goal-duration">⏱ {duration}</div>'
                        f'<h5>{title}</h5>'
                        f'<p>{desc}</p>'
                        '</div>'
                    )
                )

            cards_markup = ''.join(cards_html)
            st.markdown(f'<div class="goal-grid">{cards_markup}</div>', unsafe_allow_html=True)

    # --- Personalized Learning Plan (with links) ---
    if role['missing_skills']:
        st.markdown("<h3 style='margin-top: 2rem;'>📚 Personalized learning plan</h3>", unsafe_allow_html=True)

        # Fetch the learning plan data (Backend Call)
        learning_plan = get_learning_plan(role)
        
        # Create DataFrame
        df_data = []
        total_hours = 0
        for item in learning_plan:
            df_data.append({
                'Skill': item['skill'],
                'Resource Link': item["youtube_link"],
                'Estimated Time': f"{item['estimated_hours']} hours"
            })
            total_hours += item['estimated_hours']
        
        df = pd.DataFrame(df_data)

        # Display the DataFrame
        with glass_container():
            st.dataframe(
                df,
                use_container_width=True,
                hide_index=True,
                column_config={"Resource Link": st.column_config.LinkColumn("▶️ YouTube Tutorial", display_text="Watch Link")}
            )
        
        # Display total time with custom dark-mode styling
        st.markdown(
            f"""
            <div class="learning-banner">
                <strong>Total learning time:</strong> {total_hours} hours ({total_hours//40} weeks @ 40h/week)
            </div>
            """,
            unsafe_allow_html=True,
        )

    else:
        st.success("🎉 You have all the required skills for this role! Proceed to the career progression roadmap below.")

    st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)

    # --- CAREER PROGRESSION ROADMAP (Timeline) ---
    st.markdown(f'<h3 style="margin-top: 2rem;">🛣️ Career progression roadmap</h3>', unsafe_allow_html=True)
    with glass_container():
        if not roadmap_steps:
            st.info("Roadmap steps are still loading. Please rerun the analysis if this persists.")
        else:
            st.markdown('<div class="timeline-shell">', unsafe_allow_html=True)
            for step_string in roadmap_steps:
                step = parse_roadmap_step(step_string)
                title = html.escape(step.get('title', 'Next Step'))
                description = html.escape(step.get('description', ''))
                duration = html.escape(step.get('duration', 'N/A'))
                badge = html.escape(step.get('step', '?'))

                resources = step.get('resources', [])
                resources_html = ''
                if resources:
                    items = ''.join(f'<li>{html.escape(resource)}</li>' for resource in resources)
                    resources_html = f'<ul class="resource-list">{items}</ul>'

                st.markdown(
                    f"""
                    <div class="timeline-card">
                        <div style="display:flex; justify-content:space-between; gap:1rem; flex-wrap:wrap;">
                            <div style="font-weight:600; font-size:1.05rem;">Step {badge}: {title}</div>
                            <div style="color:#fcd34d; font-weight:600;">⏳ {duration}</div>
                        </div>
                        <p style="margin-top:0.6rem; color:#cbd5f5;">{description}</p>
                        {resources_html}
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
    st.divider()
    
    # Download report button 
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.download_button(
            label="📥 Download Full Career Report",
            data=generate_report(role), # Helper function call
            file_name=f"career_report_{role['role_name'].replace(' ', '_')}.txt",
            mime="text/plain",
            key="download_btn"
        )