# pages/upload_page.py

import streamlit as st
import time
from utils import glass_container, build_chip, render_section_header
from backend.resume_parser import parse_resume
from backend.career_analyzer import analyze_career_fit


UPLOAD_STYLES = """
<style>
.page-spacer { height: 16px; }
.glass-container.upload-panel {
    border-radius: 28px;
    padding: 2.2rem;
    border: 1px solid rgba(255,255,255,0.08);
    background: rgba(8,12,28,0.8);
    box-shadow: 0 28px 70px rgba(2,5,18,0.5);
}
.glass-container.upload-panel h1 {
    font-size: clamp(2.2rem, 4vw, 3.1rem);
    margin: 0.8rem 0;
}
.step-list {
    display: flex;
    flex-direction: column;
    gap: 1.1rem;
    margin-top: 1.8rem;
}
.step-item {
    display: flex;
    gap: 0.9rem;
    align-items: center;
}
.step-index {
    width: 42px;
    height: 42px;
    border-radius: 16px;
    border: 1px solid rgba(255,255,255,0.18);
    background: rgba(4,8,18,0.8);
    display: grid;
    place-items: center;
    font-weight: 600;
    color: #7dd3fc;
}
.upload-hints {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 1rem;
    margin-top: 1.5rem;
}
.micro-card {
    border-radius: 20px;
    padding: 1.1rem 1.2rem;
    border: 1px solid rgba(255,255,255,0.08);
    background: rgba(5,10,24,0.7);
    font-size: 0.92rem;
    color: #cbd5f5;
}
.trust-banner {
    margin-top: 2rem;
    border-radius: 24px;
    padding: 1.4rem 1.6rem;
    border: 1px solid rgba(125,211,252,0.25);
    background: linear-gradient(135deg, rgba(125,211,252,0.18), rgba(192,132,252,0.12));
    text-align: center;
}
.upload-footer {
    display: flex;
    flex-wrap: wrap;
    gap: 0.8rem;
    justify-content: center;
    font-size: 0.9rem;
    color: rgba(255,255,255,0.7);
}
@media (max-width: 640px) {
    .dropzone { min-height: 280px; }
}
</style>
"""


def upload_page():
    st.markdown(UPLOAD_STYLES, unsafe_allow_html=True)
    st.markdown("<div class='page-spacer'></div>", unsafe_allow_html=True)
    if st.button("← Back Home", type="secondary"):
        st.session_state.page = 'landing'
        st.rerun()

    col_info, col_input = st.columns([1.05, 0.95])

    with col_info:
        with glass_container('upload-panel'):
            st.markdown(build_chip("AI intake", variant="accent"), unsafe_allow_html=True)
            st.markdown(
                """
                <h1>Drop your resume. The copilot handles the rest.</h1>
                <p style="color:#cbd5ff; font-size:1.1rem;">PDF or TXT under 5MB. We extract every relevant signal, normalize the data, and spin up a personalized roadmap in under a minute.</p>
                """,
                unsafe_allow_html=True,
            )
            steps = [
                "Upload resume & confirm file quality",
                "AI extracts skills, tooling, impact, seniority",
                "Matching engine ranks high-fit roles",
                "Roadmap + links render instantly",
            ]
            steps_html = ''.join(
                f"<div class='step-item'><div class='step-index'>{idx}</div><div>{label}</div></div>"
                for idx, label in enumerate(steps, start=1)
            )
            st.markdown(f"<div class='step-list'>{steps_html}</div>", unsafe_allow_html=True)

    with col_input:
        with glass_container('upload-panel'):
            st.markdown('<h3>Upload & analyze</h3>', unsafe_allow_html=True)
            st.markdown('<p style="color:#94a3b8;">Drag & drop or browse a file</p>', unsafe_allow_html=True)

            uploaded_file = st.file_uploader('', type=['pdf', 'txt'], label_visibility="collapsed")
            placeholder = st.empty()

            if uploaded_file is not None:
                st.success(f"Loaded: {uploaded_file.name}")
                if st.button("Analyze profile", use_container_width=True):
                    status_container = placeholder.status("AI is analyzing your profile...", expanded=True)
                    try:
                        with status_container:
                            st.write("📄 Parsing resume and extracting key data points...")
                            time.sleep(0.5)
                            resume_data = parse_resume(uploaded_file)
                            st.session_state.resume_data = resume_data

                            st.write("🧠 Analyzing skills against global market data...")
                            time.sleep(1)
                            career_matches = analyze_career_fit(resume_data['skills'])
                            st.session_state.career_matches = career_matches

                            st.write("✅ Analysis complete! Preparing results...")
                            time.sleep(0.4)

                        status_container.update(label="Analysis complete", state="complete", expanded=False)
                        st.session_state.page = 'results'
                        st.rerun()
                    except Exception as exc:
                        placeholder.empty()
                        st.error(f"Analysis failed. Please check the file format or try again: {exc}")
            else:
                st.info("No file selected yet", icon="ℹ️")

    st.markdown('<div class="trust-banner">🔒 Files stay in-memory. Once you leave, your data leaves with you.</div>', unsafe_allow_html=True)

    render_section_header(
        "Quick wins for perfect parsing",
        "Keep formatting simple and impact quantified—the copilot rewards clarity with better matches.",
        eyebrow="Upload tips",
        align="left",
    )

    hints = [
        ("✨ Tip", "Make your skills section explicit for fastest parsing."),
        ("📏 Formatting", "ATS-friendly layouts parse cleaner than heavy visuals."),
        ("📝 Content", "Quantify achievements so the AI can boost relevance."),
        ("🧪 Iterate", "Upload variations to compare recommendations in seconds."),
    ]
    st.markdown('<div class="upload-hints">', unsafe_allow_html=True)
    for title, copy in hints:
        with glass_container('minimal'):
            st.markdown(f"<div class='micro-card'><strong>{title}</strong><br>{copy}</div>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="upload-footer">
            <span>Need a template? Use our ATS-ready layout.</span>
            <span>Questions? DM the team → support@careercompass.ai</span>
        </div>
        """,
        unsafe_allow_html=True,
    )