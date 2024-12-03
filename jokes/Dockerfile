# Base image
FROM python:3.12-slim

# Set the working directory
WORKDIR /jokes

# Copy the application files
COPY app/jokes_main.py /jokes/jokes_main.py

# Copy requirements.txt from tjhe parent directory to the container
COPY ../requirements.txt /jokes/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Default command to run the app
CMD ["python", "jokes_main.py"]
