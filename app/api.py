from flask import Flask, request, jsonify
import numpy as np
import cv2
from model import load_trained_model 
from database_insert import save_to_db

app = Flask(__name__)

try:
    print("Loading model...")
    model = load_trained_model()
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None  # Set to None to prevent crashes

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

        if model:
            prediction = np.argmax(model.predict(image), axis=1)
            save_to_db(prediction[0])
            return jsonify({"prediction": int(prediction[0])})
        else:
            return jsonify({"error": "Model not loaded"}), 500
    except Exception as e:
        print(f"Error during prediction: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(host='0.0.0.0', port=5000, debug=True)
