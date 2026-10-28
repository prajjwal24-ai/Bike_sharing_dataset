from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Test 1: Normal Working Day (Valid Data)
def test_predict_normal_day():
    sample_data = {
        "season": 2, "yr": 1, "mnth": 6, "hr": 14,
        "holiday": 0, "weekday": 3, "workingday": 1,
        "weathersit": 1, "temp": 0.6, "atemp": 0.6,
        "hum": 0.5, "windspeed": 0.2
    }
    response = client.post("/predict", json=sample_data)
    assert response.status_code == 200
    assert "predicted_rentals" in response.json()
    assert isinstance(response.json()["predicted_rentals"], int)

# Test 2: Holiday / Bad Weather Scenario (Valid Data)
def test_predict_holiday():
    sample_data = {
        "season": 4, "yr": 1, "mnth": 12, "hr": 2,
        "holiday": 1, "weekday": 0, "workingday": 0,
        "weathersit": 3, "temp": 0.2, "atemp": 0.2,
        "hum": 0.9, "windspeed": 0.4
    }
    response = client.post("/predict", json=sample_data)
    assert response.status_code == 200
    assert "predicted_rentals" in response.json()

# Test 3: Missing Fields (Invalid Data - Should return 422 Error)
def test_predict_missing_data():
    # 'season' aur 'temp' missing hain isme
    incomplete_data = {
        "yr": 1, "mnth": 12, "hr": 2,
        "holiday": 1, "weekday": 0, "workingday": 0,
        "weathersit": 3, "atemp": 0.2,
        "hum": 0.9, "windspeed": 0.4
    }
    response = client.post("/predict", json=incomplete_data)
    # FastAPI khud check karega aur 422 (Unprocessable Entity) error dega
    assert response.status_code == 422