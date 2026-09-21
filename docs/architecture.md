# 🏗️ EarthNex System Architecture

## 1. System Overview

EarthNex is an AI-powered landslide risk monitoring system that combines environmental data with camera-based terrain analysis.

The system processes multiple inputs, performs AI-based risk assessment, and provides:

- Risk classification
- Dynamic risk visualization
- Early-warning alerts
- Camera-based terrain analysis
- Safer route support
- Offline-oriented monitoring

---

## 2. Overall Architecture

```text
                    🌍 EARTHNEX
                         │
                         ▼
              ┌─────────────────────┐
              │    Data Collection  │
              └──────────┬──────────┘
                         │
          ┌──────────────┼──────────────┐
          │              │              │
          ▼              ▼              ▼
     🌧️ Rainfall    💧 Soil Data    ⛰️ Terrain
          │              │              │
          └──────────────┼──────────────┘
                         │
                         ▼
              📷 Camera / Image Input
                         │
                         ▼
              ┌─────────────────────┐
              │ Data Preprocessing  │
              └──────────┬──────────┘
                         │
            ┌────────────┴────────────┐
            │                         │
            ▼                         ▼
   🤖 Environmental AI       📷 Image Analysis
            │                         │
            │                         │
            └────────────┬────────────┘
                         ▼
                🧠 Risk Fusion
                         │
                         ▼
              ┌─────────────────────┐
              │  Risk Assessment    │
              └──────────┬──────────┘
                         │
             ┌───────────┼───────────┐
             │           │           │
             ▼           ▼           ▼
          🟢 LOW     🟡 MEDIUM    🔴 HIGH
             │           │           │
             └───────────┼───────────┘
                         │
                         ▼
                🗺️ Dynamic Risk Map
                         │
                         ▼
                  🚨 Alert System
                         │
                         ▼
                 🛣️ Safe Route
                         │
                         ▼
                 👤 User / Authority
