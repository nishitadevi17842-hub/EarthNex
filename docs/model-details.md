# 🧠 EarthNex AI Model Details

## 1. Overview

EarthNex uses machine learning to estimate observed landslide risk from environmental and historical information.

The prototype uses a Random Forest classifier as the baseline environmental risk model.

The system produces three risk categories:

- Low
- Medium
- High

---

## 2. Environmental Features

The model accepts the following features:

| Feature | Description |
|---|---|
| rainfall_mm | Recorded or estimated rainfall |
| soil_moisture | Soil moisture level |
| slope_degree | Terrain slope angle |
| elevation_m | Elevation of the monitored location |
| geology_score | Encoded geological risk indicator |
| historical_landslide_count | Historical landslide occurrence count |

---

## 3. Model

### Random Forest Classifier

Random Forest is used as the initial baseline because it can handle nonlinear relationships between multiple environmental features and does not require extensive feature scaling.

Configuration:

- Number of estimators: 250
- Random state: 42
- Class weighting: Balanced
- Parallel processing: Enabled

---

## 4. Data Pipeline

```text
Raw Environmental Data
          ↓
Data Validation
          ↓
Feature Selection
          ↓
Train/Test Split
          ↓
Random Forest
          ↓
Risk Classification
          ↓
Low / Medium / High
