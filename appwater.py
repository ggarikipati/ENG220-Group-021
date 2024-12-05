import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# File paths for the cleaned datasets
snow_depth_path = "reshaped_snow_depth.csv"  # Update with the path to your file
ground_water_path = "ground_water_cleaned.csv"  # Update with the path to your file

# Load datasets
snow_depth_data = pd.read_csv(snow_depth_path)
ground_water_data = pd.read_csv(ground_water_path)

# Streamlit app title
st.title("Water Resource Data Dashboard")

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
    
    # Line plot for snow depth and water equivalent
    if not filtered_snow.empty:
        st.subheader(f"Snow Depth and Water Equivalent for {selected_site} ({selected_year})")
        for metric_type in filtered_snow["Type"].unique():
            metric_data = filtered_snow[filtered_snow["Type"] == metric_type]
            plt.plot(metric_data["Month"], metric_data["Value"], marker='o', label=metric_type)
        
        plt.title(f"Snow Metrics for {selected_site} in {selected_year}")
        plt.xlabel("Month")
        plt.ylabel("Value")
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
        plt.scatter(
            filtered_ground["Depth of Well (ft)"], 
            filtered_ground["Static Water Level (ft)"], 
            alpha=0.7, c='blue', edgecolor='k'
        )
        plt.title(f"Depth of Well vs Static Water Level ({selected_system})")
        plt.xlabel("Depth of Well (ft)")
        plt.ylabel("Static Water Level (ft)")
        plt.grid(True)
        st.pyplot(plt)
        plt.clf()
    else:
        st.warning("No data available for the selected system.")
