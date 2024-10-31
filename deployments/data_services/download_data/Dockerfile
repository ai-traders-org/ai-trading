# Use Python image as base
FROM python:3.10-slim

# Install git and other necessary dependencies
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy all project content to image
COPY . .

# Set the PYTHONPATH to include the src folder
ENV PYTHONPATH=/app/src

# Install application requirements
RUN pip install --no-cache-dir -r requirements.txt

# Set default entry point to launch the application
CMD ["python", "main.py", "--save-type", "s3"]
