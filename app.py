import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# File path for the combined dataset
file_path = "aqi_combined_1980_2024.csv"

# Load the combined dataset
data = pd.read_csv(file_path)

# Ensure required columns exist
required_columns = ["Year", "Month", "Date", "AQI", "PM2.5", "PM10", "NO2", "CO", "O3"]
missing_columns = [col for col in required_columns if col not in data.columns]
if missing_columns:
    st.error(f"The following required columns are missing: {', '.join(missing_columns)}")
    st.stop()

# Sidebar options
st.sidebar.header("Dashboard Options")

# Pollutant selection
pollutants = ["PM2.5", "PM10", "NO2", "CO", "O3"]
selected_pollutant = st.sidebar.selectbox("Select a Pollutant to Analyze", pollutants)

# Data type selection
data_type_options = {"Measurement": selected_pollutant, "AQI": "AQI"}
selected_data_type = st.sidebar.radio("Select Data Type", list(data_type_options.keys()))

# Year range selection
years = sorted(data["Year"].dropna().unique())
selected_years = st.sidebar.slider(
    "Select Year Range",
    int(min(years)),
    int(max(years)),
    (int(min(years)), int(max(years)))
)

# Filter data based on selection
filtered_data = data[(data["Year"] >= selected_years[0]) & (data["Year"] <= selected_years[1])]

# Display pollutant information
st.sidebar.write(f"**Selected Pollutant**: {selected_pollutant}")

# Display all charts
st.title("Air Quality Viewer Dashboard")

# 1. Year-to-Year Trends
st.subheader(f"Year-to-Year {selected_data_type} Trends")
grouped_data = filtered_data.groupby(["Year", "Month"])[data_type_options[selected_data_type]].mean().reset_index()
plt.figure(figsize=(10, 6))
for year in grouped_data["Year"].unique():
    yearly_data = grouped_data[grouped_data["Year"] == year]
    plt.plot(yearly_data["Month"], yearly_data[data_type_options[selected_data_type]], marker='o', label=str(year))
plt.title(f"Year-to-Year Comparison of {selected_data_type}")
plt.xlabel("Month")
plt.ylabel(selected_data_type)
plt.legend(title="Year")
plt.xticks(range(1, 13), ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
plt.grid(True)
st.pyplot(plt)
plt.clf()

# 2. Total Values by Year
st.subheader(f"Total {selected_data_type} Values by Year")
total_values = filtered_data.groupby("Year")[data_type_options[selected_data_type]].sum().reset_index()
plt.figure(figsize=(10, 6))
plt.bar(total_values["Year"], total_values[data_type_options[selected_data_type]], color="green")
plt.title(f"Total {selected_data_type} by Year")
plt.xlabel("Year")
plt.ylabel(f"Total {selected_data_type}")
plt.grid(axis="y")
st.pyplot(plt)
plt.clf()

# 3. Proportion of Values by Year
st.subheader(f"Proportion of {selected_data_type} by Year")
plt.figure(figsize=(8, 8))
plt.pie(
    total_values[data_type_options[selected_data_type]],
    labels=total_values["Year"],
    autopct='%1.1f%%',
    startangle=90
)
plt.title(f"Proportion of {selected_data_type} by Year")
st.pyplot(plt)
plt.clf()

# 4. Monthly Averages
st.subheader(f"Monthly Averages of {selected_data_type}")
monthly_avg = filtered_data.groupby("Month")[data_type_options[selected_data_type]].mean().reset_index()
plt.figure(figsize=(10, 6))
plt.plot(monthly_avg["Month"], monthly_avg[data_type_options[selected_data_type]], marker='o', color='purple')
plt.title(f"Monthly Averages of {selected_data_type}")
plt.xlabel("Month")
plt.ylabel(f"Average {selected_data_type}")
plt.grid(True)
st.pyplot(plt)
plt.clf()

# Display grouped data
st.subheader("Grouped Data")
st.write(grouped_data)

        folium_static(aqi_map)
