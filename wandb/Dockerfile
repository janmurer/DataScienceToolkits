# Use the official Python base image 
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /wandb

# Copy the application files
COPY . /wandb

# Copy the main script
COPY ../wandb /wandb

# Set environment variable to make sure Python looks for modules in /app
ENV PYTHONPATH="/wandb"

# Copy the requirements.txt file and install the dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Set the default command to run the main.py script
CMD ["python", "main_wandb.py"]

# Copy the entrypoint script into the container
COPY docker_entrypoint.sh /usr/local/bin/docker_entrypoint.sh
RUN chmod +x /usr/local/bin/docker_entrypoint.sh

# Use the entrypoint script
ENTRYPOINT ["/usr/local/bin/docker_entrypoint.sh"]