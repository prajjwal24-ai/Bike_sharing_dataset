from fastapi.testclient import TestClient
from main import app

# Create a test client using your FastAPI app
client = TestClient(app)

def test_predict():
    # Define some sample data to send to the API
    sample_data = {
        "season": 1,
        "yr": 0,
        "mnth": 1,
        "hr": 8,
        "holiday": 0,
        "weekday": 6,
        "workingday": 0,
        "weathersit": 1,
        "temp": 0.24,
        "atemp": 0.2879,
        "hum": 0.81,
        "windspeed": 0.0
    }
    
    # Make a POST request to the /predict endpoint
    response = client.post("/predict", json=sample_data)
    
    # Check if the request was successful (Status Code 200)
    assert response.status_code == 200
    
    # Check if the response contains the predicted_rentals key
    assert "predicted_rentals" in response.json()