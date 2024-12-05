import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load all AQI datasets
uploaded_files = [
    "aqireport1980.csv",
    "aqireport1985.csv",
    "aqireport1990.csv",
    "aqireport1995.csv",
    "aqireport1998.csv",
    "aqireport2000.csv",
    "aqireport2002.csv",
    "aqireport2004.csv",
    "aqireport2006.csv",
    "aqireport2008.csv",
    "aqireport2010.csv",
    "aqireport2012.csv",
    "aqireport2014.csv",
    "aqireport2016.csv",
    "aqireport2018.csv",
    "aqireport2020.csv",
    "aqireport2022.csv",
    "aqireport2024.csv"
]

def load_data(files):
    dataframes = [pd.read_csv(file) for file in files]
    combined_data = pd.concat(dataframes, ignore_index=True)
    return combined_data

# Load and clean data
data = load_data(uploaded_files)
data["Year"] = pd.to_datetime(data["Date"], errors="coerce").dt.year

# Streamlit app title
st.title("Air Quality Viewer Dashboard")

# Sidebar for interactivity
st.sidebar.header("Dashboard Options")

# Pollutant selection
pollutants = ["PM2.5", "PM10", "NO2", "CO", "O3"]
selected_pollutant = st.sidebar.selectbox("Select a Pollutant to Analyze", pollutants)

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

# Display all charts
st.header("Air Quality Insights")

# 1. Year-to-Year AQI Trends
st.subheader("Year-to-Year AQI Trends")
aqi_trends = filtered_data.groupby("Year")["AQI"].mean().reset_index()
plt.figure(figsize=(10, 6))
plt.plot(aqi_trends["Year"], aqi_trends["AQI"], marker='o', color='blue')
plt.title("Year-to-Year AQI Trends")
plt.xlabel("Year")
plt.ylabel("Average AQI")
plt.grid(True)
st.pyplot(plt)
plt.clf()

# 2. Total Pollutant Values by Year
st.subheader("Total Pollutant Values by Year")
pollutant_totals = filtered_data.groupby("Year")[selected_pollutant].sum().reset_index()
plt.figure(figsize=(10, 6))
plt.bar(pollutant_totals["Year"], pollutant_totals[selected_pollutant], color="green")
plt.title(f"Total {selected_pollutant} Levels by Year")
plt.xlabel("Year")
plt.ylabel(f"Total {selected_pollutant}")
plt.grid(axis="y")
st.pyplot(plt)
plt.clf()

# 3. Proportional Contributions of Pollutants
st.subheader("Proportional Contributions of Pollutants")
pollutant_sums = filtered_data[pollutants].sum()
plt.figure(figsize=(8, 8))
plt.pie(
    pollutant_sums,
    labels=pollutants,
    autopct="%1.1f%%",
    startangle=140,
    colors=plt.cm.tab10.colors
)
plt.title("Proportional Contributions of Pollutants")
st.pyplot(plt)
plt.clf()

# 4. Monthly Averages for Selected Pollutant
st.subheader(f"Monthly Averages of {selected_pollutant}")
filtered_data["Month"] = pd.to_datetime(filtered_data["Date"], errors="coerce").dt.month
monthly_avg = filtered_data.groupby("Month")[selected_pollutant].mean().reset_index()
plt.figure(figsize=(10, 6))
plt.plot(monthly_avg["Month"], monthly_avg[selected_pollutant], marker='o', color='purple')
plt.title(f"Monthly Averages of {selected_pollutant}")
plt.xlabel("Month")
plt.ylabel(f"Average {selected_pollutant}")
plt.grid(True)
st.pyplot(plt)
plt.clf()

# 5. Top Polluted Locations
st.subheader("Top Polluted Locations")
top_locations = filtered_data.groupby("Location")["AQI"].mean().nlargest(10).reset_index()
plt.figure(figsize=(10, 6))
plt.barh(top_locations["Location"], top_locations["AQI"], color="red")
plt.title("Top 10 Most Polluted Locations")
plt.xlabel("Average AQI")
plt.ylabel("Location")
plt.gca().invert_yaxis()
st.pyplot(plt)
plt.clf()

# Heatmap of AQI Levels (if geospatial data is available)
if "Latitude" in data.columns and "Longitude" in data.columns:
    st.subheader("Heatmap of AQI Levels")
    import folium
    from streamlit_folium import folium_static

    aqi_map = folium.Map(location=[filtered_data["Latitude"].mean(), filtered_data["Longitude"].mean()], zoom_start=6)

    for _, row in filtered_data.iterrows():
        folium.CircleMarker(
            location=[row["Latitude"], row["Longitude"]],
            radius=5,
            color="red",
            fill=True,
            fill_opacity=0.6,
            popup=f"AQI: {row['AQI']}"
        ).add_to(aqi_map)

    folium_static(aqi_map)
