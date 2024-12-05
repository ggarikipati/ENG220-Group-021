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

# Sidebar for interactivity
st.sidebar.header("Dashboard Options")

# Chart selection
chart_selection = st.sidebar.selectbox(
    "Select a Chart to Display",
    [
        "Yearly Snow Depth Trends",
        "Static Water Level Trends",
        "Snow Depth vs Static Water Level Correlation",
        "Top Sites with Greatest Resource Decline",
        "Cumulative Snow Depth Over Time",
        "Regional Resource Contribution",
        "Snow Depth Variability Over Years",
        "Trend of Dry Years"
    ]
)

# Filters for charts
selected_site = st.sidebar.selectbox("Select Site", sorted(snow_depth_data["Site"].unique()), key="site")
threshold = st.sidebar.slider("Dry Year Snow Depth Threshold (in)", 0, 20, 10, key="threshold")
top_n_sites = st.sidebar.slider("Number of Top Sites", 5, 20, 10, key="top_sites")

# Display charts based on selection
if chart_selection == "Yearly Snow Depth Trends":
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

elif chart_selection == "Static Water Level Trends":
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

elif chart_selection == "Snow Depth vs Static Water Level Correlation":
    st.subheader("Snow Depth vs Static Water Level Correlation")
    combined_data = snow_depth_data.groupby("Water Year")["Snow Depth (in)"].mean().reset_index()
    if "Water Year" in ground_water_data.columns:
        combined_data = combined_data.merge(
            ground_water_data.groupby("Water Year")["Static Water Level (ft)"].mean().reset_index(),
            on="Water Year",
            how="inner"
        )
        plt.figure(figsize=(10, 6))
        plt.scatter(
            combined_data["Snow Depth (in)"], 
            combined_data["Static Water Level (ft)"], 
            alpha=0.7, edgecolor='k'
        )
        plt.title("Correlation Between Snow Depth and Static Water Level")
        plt.xlabel("Average Snow Depth (in)")
        plt.ylabel("Average Static Water Level (ft)")
        plt.grid(True)
        st.pyplot(plt)
        plt.clf()
    else:
        st.warning("Data for correlation is not available.")

elif chart_selection == "Top Sites with Greatest Resource Decline":
    st.subheader("Top Sites with Greatest Resource Decline")
    snow_decline = snow_depth_data.groupby("Site")["Snow Depth (in)"].agg(["first", "last"])
    snow_decline["Decline"] = snow_decline["first"] - snow_decline["last"]
    top_decline_sites = snow_decline.nlargest(top_n_sites, "Decline")["Decline"].reset_index()
    plt.figure(figsize=(10, 6))
    plt.barh(top_decline_sites["Site"], top_decline_sites["Decline"], color="skyblue")
    plt.title("Top Sites with Greatest Snow Depth Decline")
    plt.xlabel("Decline in Snow Depth (in)")
    plt.ylabel("Site")
    plt.grid(True, axis="x")
    st.pyplot(plt)
    plt.clf()

elif chart_selection == "Cumulative Snow Depth Over Time":
    st.subheader("Cumulative Snow Depth Over Time")
    cumulative_snow = snow_depth_data.groupby("Water Year")["Snow Depth (in)"].sum().reset_index()
    plt.figure(figsize=(10, 6))
    plt.fill_between(cumulative_snow["Water Year"], cumulative_snow["Snow Depth (in)"], alpha=0.4, color="blue")
    plt.title("Cumulative Snow Depth Over Time")
    plt.xlabel("Year")
    plt.ylabel("Cumulative Snow Depth (in)")
    plt.grid(True)
    st.pyplot(plt)
    plt.clf()

elif chart_selection == "Regional Resource Contribution":
    st.subheader("Regional Resource Contribution")
    regional_snow = snow_depth_data.groupby("Site")["Snow Depth (in)"].sum().reset_index()
    plt.figure(figsize=(10, 6))
    plt.pie(
        regional_snow["Snow Depth (in)"], 
        labels=regional_snow["Site"], 
        autopct="%1.1f%%", 
        startangle=140
    )
    plt.title("Regional Contribution to Snow Depth")
    st.pyplot(plt)
    plt.clf()

elif chart_selection == "Snow Depth Variability Over Years":
    st.subheader("Snow Depth Variability Over Years")
    plt.figure(figsize=(10, 6))
    snow_depth_data.boxplot(column="Snow Depth (in)", by="Water Year", grid=False, showmeans=True)
    plt.title("Snow Depth Variability Over Years")
    plt.suptitle("")
    plt.xlabel("Year")
    plt.ylabel("Snow Depth (in)")
    plt.grid(True)
    st.pyplot(plt)
    plt.clf()

elif chart_selection == "Trend of Dry Years":
    st.subheader("Trend of Dry Years")
    dry_years = snow_depth_data[snow_depth_data["Snow Depth (in)"] < threshold]
    dry_years_count = dry_years.groupby("Water Year")["Site"].count().reset_index()
    plt.figure(figsize=(10, 6))
    plt.bar(dry_years_count["Water Year"], dry_years_count["Site"], color="red")
    plt.title(f"Trend of Dry Years (Threshold: {threshold} in)")
    plt.xlabel("Year")
    plt.ylabel("Number of Dry Sites")
    plt.grid(True, axis="y")
    st.pyplot(plt)
    plt.clf()

