#!/bin/bash

MODEL_PATH="/app/models/mnist_model.keras"
echo "Waiting for the model file at $MODEL_PATH..."

# Loop until the file exists
while [ ! -f "$MODEL_PATH" ]; do
  echo "Model file not found. Waiting..."
  sleep 5
done

echo "Model file found! Starting application..."
exec python main.py  # Replace with your actual command for db_app
