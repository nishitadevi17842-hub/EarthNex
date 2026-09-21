# 🤖 EarthNex AI Models

This folder contains trained AI/ML models used by the EarthNex landslide risk monitoring system.

## Current Model

### Environmental Risk Prediction

EarthNex currently uses a Random Forest classifier for the prototype environmental risk prediction module.

### Input Features

The model uses:

- Rainfall
- Soil moisture
- Slope angle
- Elevation
- Geological risk score
- Historical landslide count

### Output

The model classifies the observed risk into:

- 🟢 Low
- 🟡 Medium
- 🔴 High

## Model Training

The final model should be trained using a properly licensed and documented landslide dataset.

The trained model can be saved as:

```text
risk_model.joblib
