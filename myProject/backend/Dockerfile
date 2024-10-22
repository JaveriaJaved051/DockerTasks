# Use an official Python runtime as a base
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the app's source code
COPY . .

# Expose port 5000 and start the Flask app
EXPOSE 5000
CMD ["python", "app.py"]
