# 📊 EarthNex Dataset

This folder is used to store datasets required for training and evaluating the EarthNex AI landslide risk monitoring system.

## 📌 Expected Dataset

The environmental risk prediction model expects a CSV file named:

```text
landslide_data.csv
Required Columns
Column	Description
rainfall_mm	Rainfall amount in millimeters
soil_moisture	Soil moisture value
slope_degree	Terrain slope in degrees
elevation_m	Elevation in meters
geology_score	Geological risk score
historical_landslide_count	Number of previous landslides
risk_label	Target risk category
Risk Labels

The risk_label column should contain:

Low
Medium
High
