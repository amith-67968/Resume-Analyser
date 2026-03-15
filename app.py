# app.py

"""
Career Compass AI - Main Streamlit Application Entry Point
A web app that analyzes resumes and provides career guidance
"""
import streamlit as st

# Import Page Modules
from pages.main_page import main_page
from pages.upload_page import upload_page
from pages.results_page import results_page
from pages.roadmap_page import roadmap_page


# -----------------------------------------------------------------------------
# 1. PAGE CONFIGURATION
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Career Compass AI",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -----------------------------------------------------------------------------
# 2. GLOBAL STYLING (Moved from the original app.py)
# -----------------------------------------------------------------------------
# All CSS is kept here as it's a global configuration.
with open("career_compass_theme.css", "r") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# 3. STATE MANAGEMENT
# -----------------------------------------------------------------------------
if 'page' not in st.session_state:
    st.session_state.page = 'landing'
if 'resume_data' not in st.session_state:
    st.session_state.resume_data = None
if 'career_matches' not in st.session_state:
    st.session_state.career_matches = None
if 'selected_role' not in st.session_state:
    st.session_state.selected_role = None
if 'roadmap_steps' not in st.session_state:
    st.session_state.roadmap_steps = None


def reset_session():
    st.session_state.resume_data = None
    st.session_state.career_matches = None
    st.session_state.selected_role = None
    st.session_state.page = 'landing'
    st.session_state.roadmap_steps = None


st.session_state['reset_session'] = reset_session  # Make reset available


# -----------------------------------------------------------------------------
# 4. APP ENTRY POINT (Routing)
# -----------------------------------------------------------------------------
def main():
    """Main application controller (Router)"""
    if st.session_state.page == 'landing':
        main_page()
    elif st.session_state.page == 'upload':
        upload_page()
    elif st.session_state.page == 'results':
        results_page()
    elif st.session_state.page == 'roadmap':
        roadmap_page()


if __name__ == "__main__":
    main()
