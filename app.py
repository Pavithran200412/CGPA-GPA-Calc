import streamlit as st

# Set page config for a premium wide layout
st.set_page_config(
    page_title="GPA & CGPA Calculator",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS to hide Streamlit UI elements and make the iframe fill the screen
st.markdown(
    """
    <style>
    /* Hide Streamlit header and footer */
    header {visibility: hidden; height: 0px;}
    footer {visibility: hidden; height: 0px;}
    #MainMenu {visibility: hidden;}
    
    /* Remove padding around the main content container */
    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        padding-left: 0rem !important;
        padding-right: 0rem !important;
    }
    
    /* Ensure the iframe container takes the full height of the viewport */
    iframe {
        height: 100vh !important;
        width: 100% !important;
        border: none !important;
    }
    
    .stIframe {
        height: 100vh !important;
        width: 100% !important;
    }
    
    body {
        background-color: #0f1117;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Read the HTML content
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Render the HTML file inside the app
st.iframe(html_content, height="stretch")
