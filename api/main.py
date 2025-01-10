from flask import Flask, request, render_template, redirect, url_for
import numpy as np
import cv2
from app import load_trained_model, save_predictions_to_db, save_input_data_to_db, prepare_image_for_db, load_data_from_db, transform_data_to_numpy, predictor

database = "predictions"
user = "postgres"
password = "postgres"
port = 5432
host = "db"

app = Flask(__name__)

try:
    print("Loading model...")
    model = load_trained_model()
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return render_template('result.html', prediction="No image uploaded")

    try:
        # Prepare the image for database insertion
        image_file = request.files['image']
        image_data = prepare_image_for_db(image_file)

        # Save the prepared image to the database
        save_input_data_to_db(
            database=database, 
            user=user, 
            host=host, 
            password=password, 
            port=port, 
            image_data=image_data
        )

        # Fetch the data from the database for prediction
        fetched_data = load_data_from_db(
            database=database, 
            user=user, 
            host=host, 
            password=password, 
            port=port
        )

        x_data, ids = transform_data_to_numpy(fetched_data)

        if model:
            # Make predictions using the model
            predicted_labels = predictor(model, x_data)
            print("Prediction of first value:", predicted_labels[0])

            # Save predictions to the database
            save_predictions_to_db(
                database=database, 
                user=user, 
                password=password, 
                port=port, 
                host=host, 
                predictions=predicted_labels, 
                input_data_ids=ids
            )

            # Render the result page with the prediction
            return render_template('result.html', prediction=predicted_labels[0])
        else:
            return render_template('result.html', prediction="Model not loaded")
    except Exception as e:
        print(f"Error during prediction: {e}")
        return render_template('result.html', prediction=f"Error: {str(e)}")


if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(host='0.0.0.0', port=5000, debug=True)
