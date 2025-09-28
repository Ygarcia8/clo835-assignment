# Use the official Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements first (to leverage Docker layer caching)
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the application port
EXPOSE 8080

# Run the application
CMD ["python", "app.py"]

# test build again
