from flask import Flask, request, jsonify
import numpy as np
import cv2
from app import load_trained_model, save_predictions_to_db, save_input_data_to_db, prepare_image_for_db, load_data_from_db, transform_data_to_numpy


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

@app.route('/predict', methods=['POST'])
def main():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    try:
        image_file = request.files['image']
        image_bytes = image_file.read()
        image_np = np.frombuffer(image_bytes, np.uint8)
        image = cv2.imdecode(image_np, cv2.IMREAD_GRAYSCALE)
        image = cv2.resize(image, (28, 28)) / 255.0
        image = image.reshape(1, 28, 28, 1)
        image2 = prepare_image_for_db(image)
        image2 = [(image2,)]

        save_input_data_to_db(
            database=database, 
            user=user, 
            host=host, 
            password=password, 
            port=port, 
            image_data=image2
        )

        fetched_data = load_data_from_db(
            database=database, 
            user=user, 
            host=host, 
            password=password, 
            port=port
        )

        x_data, ids = transform_data_to_numpy(fetched_data)

        if model:
            predicted_labels = model.predict(x_data)
            predicted_labels = np.argmax(predicted_labels, axis=1)
            print("Prediction of first value:", predicted_labels[0])

            print("Saving results to database")
            save_predictions_to_db(
                database=database, 
                user=user, 
                password=password, 
                port=port, 
                host=host, 
                predictions=predicted_labels, 
                input_data_ids=ids
            )
            # Return a success response with predictions
            return jsonify({"predictions": predicted_labels.tolist()}), 200
        else:
            return jsonify({"error": "Model not loaded"}), 500
    except Exception as e:
        print(f"Error during prediction: {e}")
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(host='0.0.0.0', port=5000, debug=True)
