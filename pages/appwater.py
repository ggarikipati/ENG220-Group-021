import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
snow_depth_path = "reshaped_snow_depth.csv"  # Ensure this file is in the same directory
ground_water_path = "fixed_ground_water_cleaned.csv"  # Ensure this file is in the same directory

# Load data
snow_depth_data = pd.read_csv(snow_depth_path)
ground_water_data = pd.read_csv(ground_water_path)

# Streamlit app title
st.title("Water Resource Dashboard")

# Add a back-to-home button
if st.button("⬅️ Back to Home"):
    st.session_state["page"] = "home"
    st.experimental_rerun()

# Sidebar for interactivity
st.sidebar.header("Dashboard Options")
st.sidebar.info("Customize the charts displayed on the dashboard. Select specific sites, thresholds, or top regions.")

# Filters for charts
selected_site = st.sidebar.selectbox(
    "Select Site for Snow Depth Analysis",
    sorted(snow_depth_data["Site"].unique()),
    key="site"
)
threshold = st.sidebar.slider("Dry Year Snow Depth Threshold (in)", 0, 20, 10, key="threshold")
top_n_sites = st.sidebar.slider("Number of Top Sites", 5, 20, 10, key="top_sites")

# Display all charts in sequence
st.header("All Charts")

# 1. Yearly Snow Depth Trends
st.subheader("Yearly Snow Depth Trends")
site_data = snow_depth_data[snow_depth_data["Site"] == selected_site]
if not site_data.empty:
    avg_snow_per_year = site_data.groupby("Water Year")["Snow Depth (in)"].mean().reset_index()
    plt.figure(figsize=(10, 6))
    plt.plot(avg_snow_per_year["Water Year"], avg_snow_per_year["Snow Depth (in)"], marker='o')
    plt.title(f"Yearly Snow Depth Trends at {selected_site}")
    plt.xlabel("Year")
    plt.ylabel("Average Snow Depth (in)")
    plt.grid(True)
    st.pyplot(plt)
    plt.clf()
else:
    st.warning("No data available for the selected site.")

# 2. Static Water Level Trends
st.subheader("Static Water Level Trends")
if "Water Year" in ground_water_data.columns:
    avg_water_level = ground_water_data.groupby("Water Year")["Static Water Level (ft)"].mean().reset_index()
    plt.figure(figsize=(10, 6))
    plt.plot(avg_water_level["Water Year"], avg_water_level["Static Water Level (ft)"], marker='o')
    plt.title("Static Water Level Trends")
    plt.xlabel("Year")
    plt.ylabel("Average Static Water Level (ft)")
    plt.grid(True)
    st.pyplot(plt)
    plt.clf()
else:
    st.warning("Water Year data is not available.")
