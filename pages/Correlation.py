import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# Load datasets
base_path = os.path.join(os.path.dirname(__file__), "data")
snow_depth_path = os.path.join(base_path, "reshaped_snow_depth.csv")
ground_water_path = os.path.join(base_path, "fixed_ground_water_cleaned.csv")
aqi_path = os.path.join(base_path, "aqi_combined_1980_2024.csv")

# Load data
try:
    snow_depth_data = pd.read_csv(snow_depth_path)
    ground_water_data = pd.read_csv(ground_water_path)
    aqi_data = pd.read_csv(aqi_path)
except FileNotFoundError:
    st.error("One or more datasets not found. Please ensure the files are in the 'data' directory.")
    st.stop()

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
st.markdown("**Interpretation:** This table shows the combined dataset with average snow depth, static water level, and AQI median over the years. It provides a comprehensive view of how these environmental factors interact over time.")

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
st.markdown("**Interpretation:** This heatmap shows the correlation between average snow depth, static water level, and AQI median. A positive correlation indicates that as one variable increases, the other tends to increase, whereas a negative correlation suggests an inverse relationship. This helps in identifying how these environmental factors are interconnected.")

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
st.markdown("**Interpretation:** This scatter plot shows the relationship between average snow depth and average static water level. A positive trend would suggest that higher snowpack contributes to greater groundwater recharge, which is crucial for understanding water resource availability.")

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
st.markdown("**Interpretation:** This scatter plot explores the relationship between average snow depth and average AQI median. A negative correlation could indicate that areas with higher snowpack tend to have better air quality, potentially due to the role of snow in trapping pollutants and reducing dust in the atmosphere.")

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
st.markdown("**Interpretation:** This scatter plot shows the relationship between average static water level and average AQI median. The relationship may not be direct, but it provides insight into how groundwater levels might influence or be influenced by air quality, possibly through factors like vegetation growth and dust suppression.")

# Insights Section
st.header("Insights")
st.markdown(
    """
    - **Snow Depth and Static Water Level**: A positive correlation suggests that snowpack plays an important role in groundwater recharge.
    - **Snow Depth and AQI Median**: A negative correlation may indicate that higher snowpack contributes to better air quality, likely due to reduced airborne particulates.
    - **Static Water Level and AQI Median**: The relationship between groundwater levels and air quality may be indirect, but could be related to vegetation health, dust suppression, and overall environmental stability.
    """
)
