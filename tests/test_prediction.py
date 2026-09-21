from src.prediction.risk_predictor import RiskPredictor


def test_prediction_returns_valid_result():

    predictor = RiskPredictor()

    data = {

        "rainfall_mm": 120,

        "soil_moisture": 0.70,

        "slope_degree": 30,

        "elevation_m": 800,

        "geology_score": 0.60,

        "historical_landslide_count": 3
    }

    result = predictor.predict(data)

    assert result["risk_level"] in [
        "Low",
        "Medium",
        "High"
    ]

    assert 0 <= result["risk_score"] <= 1


def test_prediction_contains_probabilities():

    predictor = RiskPredictor()

    data = {

        "rainfall_mm": 200,

        "soil_moisture": 0.85,

        "slope_degree": 40,

        "elevation_m": 1000,

        "geology_score": 0.80,

        "historical_landslide_count": 6
    }

    result = predictor.predict(data)

    assert "probabilities" in result

    assert len(
        result["probabilities"]
    ) == 3
