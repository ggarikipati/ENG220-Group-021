import streamlit as st

# Initialize session state for navigation
if "page" not in st.session_state:
    st.session_state["page"] = "home"

# Function to switch pages
def switch_page(page_name):
    st.session_state["page"] = page_name
    st.experimental_rerun()

# Custom CSS for styling
st.markdown(
    """
    <style>
    body {
        background-color: #f9fafb;
        font-family: Arial, sans-serif;
    }
    .main-title {
        font-size: 3em;
        color: #1b4965;
        text-align: center;
        margin-bottom: 20px;
    }
    .subtitle {
        font-size: 1.5em;
        color: #5a5a5a;
        text-align: center;
        margin-bottom: 40px;
    }
    .button-container {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin-top: 50px;
    }
    .dashboard-button {
        background-color: #eef2f3;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        width: 250px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        transition: background-color 0.3s ease, transform 0.2s ease;
        cursor: pointer;
    }
    .dashboard-button:hover {
        background-color: #d9e4ea;
        transform: scale(1.05);
    }
    .dashboard-title {
        font-size: 1.5em;
        color: #1b4965;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .dashboard-description {
        font-size: 1em;
        color: #5a5a5a;
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        color: #5a5a5a;
        font-size: 0.9em;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Homepage layout
if st.session_state["page"] == "home":
    st.markdown("<div class='main-title'>🌍 Environmental Data Hub</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='subtitle'>Explore insights into water resources, air quality, and their interconnections.</div>",
        unsafe_allow_html=True,
    )
    
    # Dashboard buttons
    if st.button("🌊 Water Resource Dashboard"):
        switch_page("appwater")
    if st.button("🌫️ Air Quality Viewer"):
        switch_page("app")
    if st.button("🔗 Correlation Dashboard"):
        switch_page("correlation")

# Footer
st.markdown(
    """
    <div class='footer'>
        Made with ❤️ by Ariel Arrellin | Powered by Streamlit
    </div>
    """,
    unsafe_allow_html=True,
)


