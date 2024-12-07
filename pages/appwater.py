import streamlit as st

# Custom Styles for Homepage
st.markdown(
    """
    <style>
    .main-container {
        background-color: #f9fafb;
        padding: 20px;
        font-family: Arial, sans-serif;
    }
    .title {
        text-align: center;
        font-size: 3em;
        color: #1b4965;
        margin-bottom: 20px;
        font-weight: bold;
    }
    .subtitle {
        text-align: center;
        font-size: 1.5em;
        color: #5a5a5a;
        margin-bottom: 40px;
    }
    .rectangle {
        background-color: #eef2f3;
        border-radius: 12px;
        padding: 30px;
        margin: 20px auto;
        text-align: center;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        width: 80%;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .rectangle:hover {
        background-color: #d9e4ea;
    }
    .rectangle-title {
        font-size: 1.8em;
        color: #1b4965;
        font-weight: bold;
    }
    .rectangle-description {
        font-size: 1em;
        color: #5a5a5a;
        margin-top: 10px;
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        color: #5a5a5a;
        font-size: 0.9em;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Main Page Title
st.markdown("<div class='title'>🌍 Environmental Data Hub</div>", unsafe_allow_html=True)

# Subtitle
st.markdown(
    "<div class='subtitle'>Explore insights into water resources, air quality, and their interconnections.</div>",
    unsafe_allow_html=True
)

# Navigation Buttons
if st.button("🌊 Water Resource Dashboard"):
    st.experimental_set_query_params(page="appwater")
if st.button("🌫️ Air Quality Viewer"):
    st.experimental_set_query_params(page="app")
if st.button("🔗 Correlation Dashboard"):
    st.experimental_set_query_params(page="Correlation")

# Footer Section
st.markdown(
    """
    <div class='footer'>
        Made with ❤️ by [Your Name] | Powered by Streamlit
    </div>
    """,
    unsafe_allow_html=True
)


