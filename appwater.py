import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
snow_depth_path = "reshaped_snow_depth.csv"  # Ensure this file is in the same directory
ground_water_path = "ground_water_cleaned.csv"  # Ensure this file is in the same directory

# Load data
snow_depth_data = pd.read_csv(snow_depth_path)
ground_water_data = pd.read_csv(ground_water_path)

# Ensure a consistent year column exists in both datasets
if "Water Year" not in ground_water_data.columns:
    ground_water_data["Water Year"] = pd.to_datetime(ground_water_data["DATA_COLLECTION_DT"], errors="coerce").dt.year

# Streamlit app title
st.title("Water Metrics Dashboard")

# Sidebar for options
st.sidebar.header("Filter Options")

# Snow Depth Filters
st.sidebar.subheader("Snow Depth Data")
snow_selected_site = st.sidebar.selectbox("Select Site", sorted(snow_depth_data["Site"].unique()), key="snow_site")
snow_selected_year = st.sidebar.selectbox("Select Year", sorted(snow_depth_data["Water Year"].unique()), key="snow_year")

# Ground Water Filters
st.sidebar.subheader("Ground Water Data")
ground_selected_system = st.sidebar.selectbox("Select System Name", sorted(ground_water_data["System Name"].unique()), key="ground_system")

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

# 2. Top 10 Systems By Static Water Level
st.subheader("Top 10 Systems By Static Water Level")
top_10_static_levels = ground_water_data.nlargest(10, 'Static Water Level (ft)')
plt.figure(figsize=(12, 6))
plt.barh(top_10_static_levels['System Name'], top_10_static_levels['Static Water Level (ft)'], color='skyblue')
plt.title("Top 10 Systems By Static Water Level")
plt.xlabel("Static Water Level (ft)")
plt.ylabel("System Name")
plt.gca().invert_yaxis()
plt.grid(True, axis='x', linestyle='--', alpha=0.7)
st.pyplot(plt)
plt.clf()

# 3. Depth of Well vs Static Water Level
st.subheader("Depth of Well vs Static Water Level")
plt.figure(figsize=(10, 6))
plt.scatter(
    ground_water_data['Depth of Well (ft)'], 
    ground_water_data['Static Water Level (ft)'], 
    alpha=0.7, 
    c=ground_water_data['Static Water Level (ft)'], 
    cmap='viridis', 
    edgecolor='k'
)
plt.title("Depth of Well vs Static Water Level")
plt.xlabel("Depth of Well (ft)")
plt.ylabel("Static Water Level (ft)")
plt.colorbar(label="Static Water Level (ft)")
plt.grid(True)
st.pyplot(plt)
plt.clf()

# 4. Comparison of Water Depth and Snow Depth Over Years
st.subheader("Comparison of Water Depth and Snow Depth Over Years")
combined_data = snow_depth_data.groupby("Water Year")["Snow Depth (in)"].mean().reset_index()
combined_data = combined_data.rename(columns={"Snow Depth (in)": "Average Snow Depth (in)"})
water_depth_avg = ground_water_data.groupby("Water Year")["Static Water Level (ft)"].mean().reset_index()
water_depth_avg = water_depth_avg.rename(columns={"Static Water Level (ft)": "Average Water Level (ft)"})

plt.figure(figsize=(12, 6))
plt.plot(combined_data["Water Year"], combined_data["Average Snow Depth (in)"], label="Average Snow Depth (in)", marker='o')
plt.plot(water_depth_avg["Water Year"], water_depth_avg["Average Water Level (ft)"], label="Average Water Level (ft)", marker='o')
plt.title("Average Snow Depth vs Water Depth Over Years")
plt.xlabel("Year")
plt.ylabel("Depth")
plt.legend()
plt.grid(True)
st.pyplot(plt)
plt.clf()

# Allow user to explore datasets below
st.header("Explore the Data")

# Snow Depth Data Section
st.subheader("Snow Depth Data")
filtered_snow = snow_depth_data[
    (snow_depth_data["Site"] == snow_selected_site) & 
    (snow_depth_data["Water Year"] == snow_selected_year)
]

if not filtered_snow.empty:
    st.write(f"Showing data for site: {snow_selected_site}, year: {snow_selected_year}")
    st.write(filtered_snow)
    avg_snow_filtered = filtered_snow.groupby("Month")["Snow Depth (in)"].mean()
    plt.figure(figsize=(10, 6))
    plt.plot(avg_snow_filtered.index, avg_snow_filtered.values, marker='o', label="Average Snow Depth")
    plt.title("Snow Depth Trends")
    plt.xlabel("Month")
    plt.ylabel("Snow Depth (in)")
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)
    plt.clf()
else:
    st.warning("No data available for the selected site and year.")

# Ground Water Data Section
st.subheader("Ground Water Data")
filtered_ground = ground_water_data[ground_water_data["System Name"] == ground_selected_system]

if not filtered_ground.empty:
    st.write(f"Showing data for system: {ground_selected_system}")
    st.write(filtered_ground)

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

