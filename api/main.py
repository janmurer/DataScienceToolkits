from flask import Flask, request, jsonify
import numpy as np
import cv2
from app import load_trained_model, save_predictions_to_db, save_input_data_to_db, predict, prepare_image_for_db


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

def predict():
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
        save_input_data_to_db(database = database, user = user, host = host, password = password, port = port, image_data = image2)

        if model:
            predictions = np.argmax(model.predict(image), axis=1)
            predictions = predictions[0]
            save_predictions_to_db(database = database, user = user, host = host, password = password, port = port, predictions = predictions, input_data_ids = 1)
            return jsonify({"prediction": int(predictions)})
        else:
            return jsonify({"error": "Model not loaded"}), 500
    except Exception as e:
        print(f"Error during prediction: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(host='0.0.0.0', port=5000, debug=True)
