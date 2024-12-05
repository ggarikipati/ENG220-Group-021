import streamlit as st

# Custom Styles
st.markdown(
    """
    <style>
    .main {
        background-color: #eef2f3;
        font-family: 'Arial', sans-serif;
    }
    .title {
        color: #1b4965;
        font-size: 3em;
        font-weight: bold;
        text-align: center;
        margin-bottom: 30px;
    }
    .overview {
        color: #333333;
        font-size: 1.3em;
        text-align: center;
        margin: 20px;
        padding: 10px;
        background-color: #ffffff;
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .dashboard-section {
        display: flex;
        justify-content: space-around;
        margin: 30px;
    }
    .dashboard-card {
        text-align: center;
        padding: 20px;
        background-color: #ffffff;
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s;
        width: 250px;
    }
    .dashboard-card:hover {
        transform: scale(1.05);
    }
    .dashboard-title {
        color: #1b4965;
        font-size: 1.5em;
        margin-top: 10px;
    }
    .coming-soon {
        color: #666666;
        font-style: italic;
        margin-top: 20px;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<div class='title'>Environmental Data Hub</div>", unsafe_allow_html=True)

st.markdown(
    "<div class='overview'>Explore insights into water resources, air quality, and their interconnections over time. Use the sidebar to navigate through the dashboards.</div>",
    unsafe_allow_html=True
)

# Sidebar navigation
st.sidebar.title("Dashboard Navigation")
st.sidebar.info("Select a dashboard to explore different datasets and insights.")

dashboard = st.sidebar.radio(
    "Go to:",
    ("Home", "Water Resource Dashboard", "Air Quality Viewer", "Correlation Dashboard")
)

if dashboard == "Home":
    st.markdown("<div class='overview'>Welcome to the Environmental Data Hub! Use the sidebar to navigate to individual dashboards.</div>", unsafe_allow_html=True)

elif dashboard == "Water Resource Dashboard":
    st.markdown("[Click here to view the Water Resource Dashboard](pages/appwater.py)")

elif dashboard == "Air Quality Viewer":
    st.markdown("[Click here to view the Air Quality Viewer Dashboard](pages/app.py)")

elif dashboard == "Correlation Dashboard":
    st.markdown("[Click here to view the Correlation Dashboard](pages/Correlation.py)")
