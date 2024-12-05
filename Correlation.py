import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
snow_depth_path = "reshaped_snow_depth.csv"
ground_water_path = "fixed_ground_water_cleaned.csv"
aqi_path = "aqi_combined_1980_2024.csv"

# Load data
snow_depth_data = pd.read_csv(snow_depth_path)
ground_water_data = pd.read_csv(ground_water_path)
aqi_data = pd.read_csv(aqi_path)

# Merge datasets
snow_avg = snow_depth_data.groupby("Water Year")["Snow Depth (in)"].mean().reset_index()
water_avg = ground_water_data.groupby("Water Year")["Static Water Level (ft)"].mean().reset_index()
aqi_avg = aqi_data.groupby("Year")["AQI_Median"].mean().reset_index()
aqi_avg.rename(columns={"Year": "Water Year"}, inplace=True)

# Merge into a single DataFrame
correlation_data = snow_avg.merge(water_avg, on="Water Year", how="inner")
correlation_data = correlation_data.merge(aqi_avg, on="Water Year", how="inner")

# Streamlit app title
st.title("Correlation Dashboard")

# Display merged data
st.header("Combined Dataset Overview")
st.write(correlation_data)

# Correlation Heatmap without seaborn
st.header("Correlation Heatmap")
plt.figure(figsize=(10, 6))
corr_matrix = correlation_data.drop(columns="Water Year").corr()
plt.imshow(corr_matrix, cmap="coolwarm", aspect="auto")
plt.colorbar(label="Correlation Coefficient")
plt.xticks(range(len(corr_matrix.columns)), corr_matrix.columns, rotation=45, ha="right")
plt.yticks(range(len(corr_matrix.columns)), corr_matrix.columns)
plt.title("Correlation Between Variables")
for i in range(len(corr_matrix.columns)):
    for j in range(len(corr_matrix.columns)):
        plt.text(j, i, f"{corr_matrix.iloc[i, j]:.2f}", ha="center", va="center", color="black")
st.pyplot(plt)
plt.clf()

# Snow Depth vs Static Water Level
st.header("Snow Depth vs Static Water Level")
plt.figure(figsize=(10, 6))
plt.scatter(
    correlation_data["Snow Depth (in)"],
    correlation_data["Static Water Level (ft)"],
    alpha=0.7, edgecolor="k"
)
plt.title("Snow Depth vs Static Water Level")
plt.xlabel("Average Snow Depth (in)")
plt.ylabel("Average Static Water Level (ft)")
plt.grid(True)
st.pyplot(plt)
plt.clf()

# Snow Depth vs AQI Median
st.header("Snow Depth vs AQI Median")
plt.figure(figsize=(10, 6))
plt.scatter(
    correlation_data["Snow Depth (in)"],
    correlation_data["AQI_Median"],
    alpha=0.7, edgecolor="k"
)
plt.title("Snow Depth vs AQI Median")
plt.xlabel("Average Snow Depth (in)")
plt.ylabel("Average AQI Median")
plt.grid(True)
st.pyplot(plt)
plt.clf()

# Static Water Level vs AQI Median
st.header("Static Water Level vs AQI Median")
plt.figure(figsize=(10, 6))
plt.scatter(
    correlation_data["Static Water Level (ft)"],
    correlation_data["AQI_Median"],
    alpha=0.7, edgecolor="k"
)
plt.title("Static Water Level vs AQI Median")
plt.xlabel("Average Static Water Level (ft)")
plt.ylabel("Average AQI Median")
plt.grid(True)
st.pyplot(plt)
plt.clf()

# Insights Section
st.header("Insights")
st.markdown(
    """
    - **Snow Depth and Static Water Level**: Positive correlation suggests that snowpack contributes to groundwater recharge.
    - **Snow Depth and AQI Median**: Negative correlation might indicate better air quality with higher snowpack.
    - **Static Water Level and AQI Median**: Explores the relationship between groundwater and air quality, which may be indirect but relevant for environmental health.
    """
)

)
