# Base image
FROM python:3.12-slim

# Set the working directory
WORKDIR /database

# psycopg2 requirements
RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*

# Copy the application files
COPY ../app /database/app

# Copy the main script
COPY ../database /database

COPY ../models /database/models

# Copy requirements.txt from the parent directory to the container
COPY requirements.txt /database/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Default command to run the app
CMD ["python", "main.py"]
