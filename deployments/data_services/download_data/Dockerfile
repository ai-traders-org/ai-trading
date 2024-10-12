# Use Python image as base
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy all project content to image
COPY . .

# Install application requirements
RUN pip install --no-cache-dir -r requirements.txt

# Set default entry point to launch the application
CMD ["python", "main.py"]
