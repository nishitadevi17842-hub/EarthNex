import os
import joblib
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)


FEATURES = [
    "rainfall_mm",
    "soil_moisture",
    "slope_degree",
    "elevation_m",
    "geology_score",
    "historical_landslide_count"
]

TARGET = "risk_label"

MODEL_PATH = "models/risk_model.joblib"
DATASET_PATH = "data/landslide_data.csv"


def load_dataset():

    if not os.path.exists(DATASET_PATH):

        raise FileNotFoundError(
            f"Dataset not found: {DATASET_PATH}"
        )

    data = pd.read_csv(DATASET_PATH)

    required_columns = FEATURES + [TARGET]

    missing_columns = [
        column
        for column in required_columns
        if column not in data.columns
    ]

    if missing_columns:

        raise ValueError(
            "Missing columns: "
            + str(missing_columns)
        )

    return data


def prepare_data(data):

    label_mapping = {
        "Low": 0,
        "Medium": 1,
        "High": 2
    }

    data = data.copy()

    data[TARGET] = data[TARGET].map(
        label_mapping
    )

    if data[TARGET].isnull().any():

        raise ValueError(
            "risk_label must contain "
            "Low, Medium, or High."
        )

    X = data[FEATURES]

    y = data[TARGET].astype(int)

    return X, y


def train_model(X_train, y_train):

    model = RandomForestClassifier(

        n_estimators=250,

        random_state=42,

        class_weight="balanced",

        n_jobs=-1
    )

    model.fit(
        X_train,
        y_train
    )

    return model


def evaluate_model(model, X_test, y_test):

    predictions = model.predict(X_test)

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    print("\n" + "=" * 50)
    print("EARTHNEX MODEL EVALUATION")
    print("=" * 50)

    print(
        f"\nAccuracy: {accuracy:.4f}"
    )

    print("\nClassification Report:")

    print(
        classification_report(
            y_test,
            predictions,
            target_names=[
                "Low",
                "Medium",
                "High"
            ],
            zero_division=0
        )
    )

    print("Confusion Matrix:")

    print(
        confusion_matrix(
            y_test,
            predictions
        )
    )

    return accuracy


def save_model(model):

    os.makedirs(
        "models",
        exist_ok=True
    )

    joblib.dump(
        model,
        MODEL_PATH
    )

    print(
        f"\n✅ Model saved to: {MODEL_PATH}"
    )


def main():

    print("🌍 EarthNex Model Training")

    data = load_dataset()

    print(
        f"Dataset size: {len(data)} rows"
    )

    X, y = prepare_data(data)

    X_train, X_test, y_train, y_test = train_test_split(

        X,
        y,

        test_size=0.20,

        random_state=42,

        stratify=y
    )

    print(
        f"Training samples: {len(X_train)}"
    )

    print(
        f"Testing samples: {len(X_test)}"
    )

    model = train_model(
        X_train,
        y_train
    )

    evaluate_model(
        model,
        X_test,
        y_test
    )

    save_model(model)


if __name__ == "__main__":
    main()
