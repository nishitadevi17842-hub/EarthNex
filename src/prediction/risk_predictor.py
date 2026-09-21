import os
import joblib
import numpy as np
import pandas as pd

from sklearn.ensemble import RandomForestClassifier


FEATURES = [
    "rainfall_mm",
    "soil_moisture",
    "slope_degree",
    "elevation_m",
    "geology_score",
    "historical_landslide_count"
]


class RiskPredictor:

    def __init__(self, model_path="models/risk_model.joblib"):

        self.model_path = model_path
        self.model = None
        self.demo_mode = False

        self.load_model()

    def load_model(self):

        if os.path.exists(self.model_path):

            self.model = joblib.load(self.model_path)

        else:

            self.model = self.create_demo_model()
            self.demo_mode = True

    def create_demo_model(self):

        np.random.seed(42)

        number_of_samples = 1500

        data = pd.DataFrame({

            "rainfall_mm":
                np.random.uniform(0, 300, number_of_samples),

            "soil_moisture":
                np.random.uniform(0.1, 0.95, number_of_samples),

            "slope_degree":
                np.random.uniform(0, 55, number_of_samples),

            "elevation_m":
                np.random.uniform(50, 2500, number_of_samples),

            "geology_score":
                np.random.uniform(0, 1, number_of_samples),

            "historical_landslide_count":
                np.random.randint(0, 12, number_of_samples)
        })

        risk_score = (
            0.0035 * data["rainfall_mm"]
            + 1.8 * data["soil_moisture"]
            + 0.045 * data["slope_degree"]
            + 0.7 * data["geology_score"]
            + 0.09 * data["historical_landslide_count"]
        )

        labels = np.select(
            [
                risk_score < 2.0,
                risk_score < 3.1
            ],
            [
                0,
                1
            ],
            default=2
        )

        model = RandomForestClassifier(
            n_estimators=150,
            random_state=42,
            class_weight="balanced"
        )

        model.fit(data[FEATURES], labels)

        return model

    def predict(self, values):

        input_data = pd.DataFrame(
            [[values[feature] for feature in FEATURES]],
            columns=FEATURES
        )

        prediction = int(
            self.model.predict(input_data)[0]
        )

        probabilities = self.model.predict_proba(
            input_data
        )[0]

        risk_score = float(
            np.dot(
                probabilities,
                [0.2, 0.55, 0.95]
            )
        )

        risk_levels = {
            0: "Low",
            1: "Medium",
            2: "High"
        }

        return {
            "risk_level": risk_levels[prediction],
            "risk_score": risk_score,
            "probabilities": probabilities.tolist(),
            "demo_mode": self.demo_mode
        }
