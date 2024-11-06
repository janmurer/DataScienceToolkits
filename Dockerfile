# Use the official Python base image (specifying ARM64 for Apple Silicon compatibility)
FROM --platform=linux/arm64 python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Set environment variable to make sure Python looks for modules in /app
ENV PYTHONPATH="${PYTHONPATH}:/app"

# Copy the requirements.txt file and install the dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Set the default command to run the main.py script
CMD ["python", "main.py"]
