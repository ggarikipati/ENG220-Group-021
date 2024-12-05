import streamlit as st

# Custom Styles
st.markdown(
    """
    <style>
    .main {
        background-color: #f4f4f4;
    }
    .title {
        color: #2b6777;
        font-size: 2.5em;
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
    }
    .overview {
        color: #2d4059;
        font-size: 1.2em;
        margin: 20px;
    }
    .dashboard-button {
        text-align: center;
        margin: 20px;
    }
    .placeholder {
        color: #4a4a4a;
        font-style: italic;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Homepage Title
st.markdown("<div class='title'>Environmental Data Dashboard</div>", unsafe_allow_html=True)

# Overview Section
st.markdown("<div class='overview'>Welcome to the Environmental Data Dashboard! Use this platform to explore insights into water resources, air quality, and their interconnections over time. Select one of the following dashboards to begin:</div>", unsafe_allow_html=True)

# Navigation Buttons
st.header("Dashboards")

# Button for Water Resource Dashboard
if st.button("🌊 Water Resource Dashboard"):
    st.markdown("[Go to Water Resource Dashboard](appwater.py)")

# Button for Air Quality Viewer Dashboard
if st.button("🌫️ Air Quality Viewer Dashboard"):
    st.markdown("[Go to Air Quality Viewer Dashboard](appair.py)")

# Placeholder for Correlations Dashboard
st.header("Correlations Dashboard")
st.markdown(
    """
    This dashboard will explore correlations between water resources and air quality data.
    Stay tuned for updates!
    """
)
