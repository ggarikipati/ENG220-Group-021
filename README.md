# ENG-220 Group 021: Environmental Dashboard Project

## Overview

This project focuses on building interactive dashboards to analyze and visualize environmental data for **New Mexico**. Our work is divided into two main dashboards and an additional correlation analysis, providing insights into air quality, water resources, and their interconnections.

## Dashboards

### 1. Air Quality Dashboard
- **Focus:** Air quality data from 1980 to 2024.
- **Features:**
  - Visualizes air quality trends over time.
  - Displays AQI (Air Quality Index) category distribution.
  - Shows pollutant data by year (e.g., CO, NO2, O3, PM2.5, PM10).
  - Provides summary statistics for selected CBSAs (Core-Based Statistical Areas).
- **Data Source:** [EPA.gov](https://www.epa.gov/) and [Air Quality Monitoring Data](https://waterdata.usgs.gov/monitoring-location/08315500/#period=P7D&showMedian=true&dataTypeId=continuous-00054-0).

### 2. Water Resource Dashboard
- **Focus:** Snow depth and groundwater data in New Mexico.
- **Features:**
  - Yearly trends in snow depth for selected sites.
  - Static water level trends across years.
  - Snow-water level correlations.
  - Regional resource contribution analysis.
  - Identification of top sites with significant resource decline.
- **Data Sources:** [USGS Water Monitoring Data](https://waterdata.usgs.gov/monitoring-location/08315500/#period=P7D&showMedian=true&dataTypeId=continuous-00054-0) and cleaned datasets on snow depth and groundwater levels.

### 3. Correlation Dashboard
- **Focus:** Exploring relationships between air quality and water resource data.
- **Features:**
  - Analyzes environmental interactions across different regions.
  - Highlights potential correlations between snow depth, groundwater levels, and air quality indicators.

## Project Details

This project was developed using **Streamlit** and **Python**. Although group members had no prior Python experience, code was adapted and edited with assistance from ChatGPT. 

### Team Members
- **Sumo Alexandre**
- **Ariel Arrellin**
- **Ryan Garcia**
- **Timothy Saucier**
- **Mitchell Snyder**
- **Christian Talamantes**

## How to Run the Dashboards

1. **Install Requirements:**
   - Ensure Python 3.x is installed.
   - Install required libraries:
     ```bash
     pip install streamlit pandas matplotlib
     ```

2. **Run the Air Quality Dashboard:**
   ```bash
   streamlit run app.py
   ```

3. **Run the Water Resource Dashboard:**
   ```bash
   streamlit run appwater.py
   ```

4. **Place Datasets:**
   - Ensure the following files are in the same directory as the app scripts:
     - `aqi_combined_1980_2024.csv`
     - `reshaped_snow_depth.csv`
     - `fixed_ground_water_cleaned.csv`

## Data Sources

- **Air Quality Data:** [EPA.gov](https://www.epa.gov/) and [Air Quality Monitoring Data](https://waterdata.usgs.gov/monitoring-location/08315500/#period=P7D&showMedian=true&dataTypeId=continuous-00054-0).
- **Water Resources Data:** [USGS Water Monitoring Data](https://waterdata.usgs.gov/monitoring-location/08315500/#period=P7D&showMedian=true&dataTypeId=continuous-00054-0) and cleaned datasets derived from New Mexico environmental studies.

## Acknowledgments

Special thanks to ChatGPT for aiding in Python coding and streamlining the development process.
