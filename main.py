from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Initialize the FastAPI app
app = FastAPI()

# Load the saved Machine Learning model
model = joblib.load('model.joblib')

# Define the input data format based on the hour.csv columns
class BikeData(BaseModel):
    season: int
    yr: int
    mnth: int
    hr: int
    holiday: int
    weekday: int
    workingday: int
    weathersit: int
    temp: float
    atemp: float
    hum: float
    windspeed: float

# Create an endpoint for making predictions
@app.post("/predict")
def predict_rentals(data: BikeData):
    # Convert the incoming JSON data to a pandas DataFrame
    input_data = pd.DataFrame([data.dict()])
    
    # Make a prediction using the loaded model
    prediction = model.predict(input_data)
    
    # Return the predicted value as an integer
    return {"predicted_rentals": int(prediction[0])}