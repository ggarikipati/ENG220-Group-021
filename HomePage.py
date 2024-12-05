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

# Homepage Title
st.markdown("<div class='title'>Environmental Data Hub</div>", unsafe_allow_html=True)

# Overview Section
st.markdown(
    "<div class='overview'>Explore insights into water resources, air quality, and their interconnections over time. Select one of the dashboards below to begin your analysis:</div>",
    unsafe_allow_html=True
)

# Dashboard Links Section
st.markdown("<div class='dashboard-section'>", unsafe_allow_html=True)

# Water Resource Dashboard Card
st.markdown(
    """
    <div class='dashboard-card'>
        <a href='pages/Water_Resource_Dashboard.py' style='text-decoration: none;'>
            <img src='https://via.placeholder.com/150/1b4965/ffffff?text=Water+Dashboard' alt='Water Dashboard' style='border-radius: 50%;'>
            <div class='dashboard-title'>🌊 Water Resource Dashboard</div>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

# Air Quality Viewer Dashboard Card
st.markdown(
    """
    <div class='dashboard-card'>
        <a href='pages/Air_Quality_Viewer.py' style='text-decoration: none;'>
            <img src='https://via.placeholder.com/150/1b4965/ffffff?text=Air+Quality' alt='Air Quality Dashboard' style='border-radius: 50%;'>
            <div class='dashboard-title'>🌫️ Air Quality Viewer</div>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

# Correlation Dashboard Card
st.markdown(
    """
    <div class='dashboard-card'>
        <a href='pages/Correlation_Dashboard.py' style='text-decoration: none;'>
            <img src='https://via.placeholder.com/150/1b4965/ffffff?text=Correlations' alt='Correlation Dashboard' style='border-radius: 50%;'>
            <div class='dashboard-title'>🔗 Correlation Dashboard</div>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("</div>", unsafe_allow_html=True)

# Coming Soon Section
st.markdown("<div class='coming-soon'>Stay tuned for more insights and dashboards as we expand our analysis capabilities!</div>", unsafe_allow_html=True)

