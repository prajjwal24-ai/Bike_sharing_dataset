# Use an official lightweight Python image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file first (this helps with caching)
COPY requirements.txt .

# Install all the required Python libraries
RUN pip install --no-cache-dir -r requirements.txt

# Copy all the remaining files (main.py, test_main.py, model.joblib) into the container
COPY . .

# Expose port 8000 so we can access the FastAPI app
EXPOSE 8000

# Command to start the FastAPI server using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]