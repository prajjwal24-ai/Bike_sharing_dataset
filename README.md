# Bike Sharing Prediction API 🚲

This is an end-to-end Machine Learning Case Study to predict the total number of bike rentals based on environmental and seasonal settings. 

The project includes data preprocessing, model training using a Random Forest Regressor, an API built with **FastAPI**, containerization using **Docker**, and an automated CI pipeline using **GitHub Actions**.

## 🚀 Features
- **Machine Learning Model**: Random Forest Regressor trained on the Kaggle Bike Sharing dataset. (Note: The model is compressed to stay under GitHub's 100MB file limit).
- **RESTful API**: Fast and interactive API built with FastAPI.
- **Dockerized**: Fully containerized application for easy deployment across any environment.
- **Continuous Integration (CI)**: Automated testing pipeline using GitHub Actions to ensure code stability on every push.

## 📂 Project Structure
```text
├── .github/workflows/ci.yml # GitHub Actions CI Pipeline
├── Dockerfile               # Docker configuration for containerization
├── main.py                  # FastAPI application code
├── model.joblib             # Compressed Random Forest model
├── requirements.txt         # Python dependencies
├── test_main.py             # PyTest test cases for the API
└── README.md                # Project documentation
