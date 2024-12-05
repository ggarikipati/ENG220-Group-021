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

# Tabs for datasets
tab1, tab2 = st.tabs(["Snow Depth Data", "Ground Water Data"])

# Snow Depth Data Tab
with tab1:
    st.header("Snow Depth Data")

    # Dropdown filters for Site and Year
    selected_site = st.selectbox("Select Site", sorted(snow_depth_data["Site"].unique()))
    selected_year = st.selectbox("Select Year", sorted(snow_depth_data["Water Year"].unique()))

    # Filter data based on selections
    filtered_snow = snow_depth_data[
        (snow_depth_data["Site"] == selected_site) & 
        (snow_depth_data["Water Year"] == selected_year)
    ]

    # Line plot for snow depth trends
    if not filtered_snow.empty:
        st.subheader(f"Snow Depth Trends for {selected_site} ({selected_year})")
        avg_snow = filtered_snow.groupby("Month")["Snow Depth (in)"].mean()
        plt.figure(figsize=(10, 6))
        plt.plot(avg_snow.index, avg_snow.values, marker='o', label="Average Snow Depth")
        plt.title("Average Snow Depth Over Months")
        plt.xlabel("Month")
        plt.ylabel("Snow Depth (in)")
        plt.legend()
        plt.grid(True)
        st.pyplot(plt)
        plt.clf()
    else:
        st.warning("No data available for the selected site and year.")

# Ground Water Data Tab
with tab2:
    st.header("Ground Water Data")

    # Dropdown filter for System Name
    selected_system = st.selectbox("Select System Name", sorted(ground_water_data["System Name"].unique()))

    # Filter data based on selection
    filtered_ground = ground_water_data[ground_water_data["System Name"] == selected_system]

    if not filtered_ground.empty:
        st.subheader(f"Metrics for {selected_system}")

        # Display filtered data
        st.write(filtered_ground)

        # Scatter plot for depth of well vs static water level
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

        # Bar chart for top static water levels
        top_static_levels = filtered_ground.nlargest(10, "Static Water Level (ft)")
        plt.figure(figsize=(12, 6))
        plt.barh(top_static_levels["System Name"], top_static_levels["Static Water Level (ft)"], color='skyblue')
        plt.title("Top Static Water Levels")
        plt.xlabel("Static Water Level (ft)")
        plt.ylabel("System Name")
        plt.grid(True, axis='x', linestyle='--', alpha=0.7)
        st.pyplot(plt)
        plt.clf()

    else:
        st.warning("No data available for the selected system.")
