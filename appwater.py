import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
snow_depth_path = "reshaped_snow_depth.csv"  # Ensure this file is in the same directory
ground_water_path = "ground_water_cleaned.csv"  # Ensure this file is in the same directory

# Load data
snow_depth_data = pd.read_csv(snow_depth_path)
ground_water_data = pd.read_csv(ground_water_path)

# Streamlit app title
st.title("Water Metrics Dashboard")

# Sidebar for options
st.sidebar.header("Filter Options")

# Snow Depth Filters
st.sidebar.subheader("Snow Depth Data")
snow_selected_site = st.sidebar.selectbox("Select Site", sorted(snow_depth_data["Site"].unique()), key="snow_site")

# Display important data insights directly
st.header("Key Insights")

# 1. Average Snow Depth Over Months
st.subheader("Average Snow Depth Over Months")
snow_depth_avg = snow_depth_data.groupby('Month')['Snow Depth (in)'].mean().reindex([
    'January', 'February', 'March', 'April', 'May', 'June'
])
plt.figure(figsize=(10, 6))
plt.plot(snow_depth_avg.index, snow_depth_avg.values, marker='o', color='b')
plt.title("Average Snow Depth Over Months")
plt.xlabel("Month")
plt.ylabel("Snow Depth (in)")
plt.grid(True)
st.pyplot(plt)
plt.clf()

# Snow Depth Data Section
st.header("Snow Depth Data")

# Line graph: Average snow depth per year for the selected site
st.subheader("Yearly Snow Depth Trends")
site_snow_depth = snow_depth_data[snow_depth_data['Site'] == snow_selected_site]
if not site_snow_depth.empty:
    avg_snow_per_year = site_snow_depth.groupby('Water Year')['Snow Depth (in)'].mean().reset_index()
    plt.figure(figsize=(10, 6))
    plt.plot(avg_snow_per_year['Water Year'], avg_snow_per_year['Snow Depth (in)'], marker='o', label=f"Average Snow Depth at {snow_selected_site}")
    plt.title(f"Snow Depth Trends at {snow_selected_site}")
    plt.xlabel("Year")
    plt.ylabel("Average Snow Depth (in)")
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)
    plt.clf()
else:
    st.warning(f"No data available for site: {snow_selected_site}")

# Additional exploration: Month-by-month trends for the selected year
snow_selected_year = st.sidebar.selectbox("Select Year", sorted(snow_depth_data["Water Year"].unique()), key="snow_year")
st.subheader("Monthly Snow Depth Trends")
filtered_snow = snow_depth_data[
    (snow_depth_data["Site"] == snow_selected_site) & 
    (snow_depth_data["Water Year"] == snow_selected_year)
]

if not filtered_snow.empty:
    avg_snow_filtered = filtered_snow.groupby("Month")["Snow Depth (in)"].mean()
    plt.figure(figsize=(10, 6))
    plt.plot(avg_snow_filtered.index, avg_snow_filtered.values, marker='o', label="Average Snow Depth")
    plt.title(f"Monthly Snow Depth Trends for {snow_selected_site} in {snow_selected_year}")
    plt.xlabel("Month")
    plt.ylabel("Snow Depth (in)")
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)
    plt.clf()
else:
    st.warning(f"No data available for site: {snow_selected_site}, year: {snow_selected_year}")

# Ground Water Data Section
st.header("Ground Water Data")
st.subheader("Static Water Levels")
filtered_ground = ground_water_data[ground_water_data["System Name"] == st.sidebar.selectbox(
    "Select System Name", sorted(ground_water_data["System Name"].unique()), key="ground_system")]

if not filtered_ground.empty:
    st.write(f"Showing data for system: {filtered_ground['System Name'].iloc[0]}")
    plt.figure(figsize=(10, 6))
    plt.scatter(
        filtered_ground["Depth of Well (ft)"], 
        filtered_ground["Static Water Level (ft)"], 
        alpha=0.7, c='blue', edgecolor='k'
    )
    plt.title("Depth of Well vs Static Water Level")
    plt.xlabel("Depth of Well (ft)")
    plt.ylabel("Static Water Level (ft)")
    plt.grid(True)
    st.pyplot(plt)
    plt.clf()
else:
    st.warning("No data available for the selected system.")


