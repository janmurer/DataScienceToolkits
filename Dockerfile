# Use the official Python base image 
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# psycopg2 requirements
RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container at /app
COPY . /app

# Set environment variable to make sure Python looks for modules in /app
ENV PYTHONPATH="/app"

# Copy the requirements.txt file and install the dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Set the default command to run the main.py script
CMD ["python", "main.py"]
