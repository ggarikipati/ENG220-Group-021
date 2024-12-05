import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# File path for the dataset
file_path = "aqi_combined_1980_2024.csv"

# Load the dataset
data = pd.read_csv(file_path)

# Ensure required columns exist and adapt dynamically
available_columns = data.columns

# Sidebar options
st.sidebar.header("Dashboard Options")

# Year range selection
years = sorted(data["Year"].unique())
selected_years = st.sidebar.slider(
    "Select Year Range",
    int(min(years)),
    int(max(years)),
    (int(min(years)), int(max(years)))
)

# CBSA selection
selected_cbsa = st.sidebar.selectbox("Select CBSA", data["CBSA"].unique())

# Filter data based on selections
filtered_data = data[(data["Year"] >= selected_years[0]) & (data["Year"] <= selected_years[1])]
filtered_data = filtered_data[filtered_data["CBSA"] == selected_cbsa]

# Display header
st.title("Air Quality Viewer Dashboard")

# 1. AQI Days by Category
if all(col in available_columns for col in ["Good", "Moderate", "Unhealthy_for_Sensitive_Groups", "Unhealthy", "Very_Unhealthy", "Hazardous"]):
    st.subheader("AQI Days by Category")
    categories = ["Good", "Moderate", "Unhealthy_for_Sensitive_Groups", "Unhealthy", "Very_Unhealthy", "Hazardous"]
    category_sums = filtered_data[categories].sum()

    # Ensure numeric data for plotting
    category_sums = pd.to_numeric(category_sums, errors="coerce").fillna(0)

    if category_sums.sum() > 0:
        plt.figure(figsize=(8, 6))
        plt.bar(category_sums.index, category_sums.values, color='skyblue')
        plt.title("AQI Days by Category")
        plt.xlabel("Category")
        plt.ylabel("Number of Days")
        plt.grid(axis="y")
        st.pyplot(plt)
        plt.clf()
    else:
        st.warning("No valid data available for AQI Days by Category.")

# 2. Pollutant Days by Year
pollutant_columns = ["#_Days_CO", "#_Days_NO2", "#_Days_O3", "#_Days_PM2.5", "#_Days_PM10"]
if all(col in available_columns for col in pollutant_columns):
    st.subheader("Pollutant Days by Year")

    # Ensure numeric data for pollutants
    for col in pollutant_columns:
        filtered_data[col] = pd.to_numeric(filtered_data[col], errors="coerce").fillna(0)

    # Group data by year and sum pollutants
    yearly_pollutants = filtered_data.groupby("Year")[pollutant_columns].sum()

    if not yearly_pollutants.empty and yearly_pollutants.sum().sum() > 0:
        yearly_pollutants.plot(kind="bar", stacked=True, figsize=(10, 6), color=plt.cm.tab10.colors)
        plt.title("Pollutant Days by Year")
        plt.xlabel("Year")
        plt.ylabel("Number of Days")
        plt.legend(title="Pollutant")
        plt.grid(axis="y")
        st.pyplot(plt)
        plt.clf()
    else:
        st.warning("No valid data available for Pollutant Days by Year.")

# 3. AQI Statistics
if all(col in available_columns for col in ["AQI_Maximum", "AQI_90th_Percentile", "AQI_Median"]):
    st.subheader("AQI Statistics")
    aqi_stats = filtered_data.groupby("Year")["AQI_Maximum", "AQI_90th_Percentile", "AQI_Median"].mean()
    aqi_stats.plot(figsize=(10, 6), marker='o')
    plt.title("AQI Statistics Over Time")
    plt.xlabel("Year")
    plt.ylabel("AQI Value")
    plt.legend(title="Statistic")
    plt.grid(True)
    st.pyplot(plt)
    plt.clf()

# 4. CBSA Summary Table
st.subheader("CBSA Summary Table")
st.write(filtered_data)
