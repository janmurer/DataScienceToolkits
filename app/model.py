# app/model.py
import os
from keras import Sequential, layers, Input
from keras.models import load_model

def build_model(input_shape=(28, 28, 1), num_classes=10):
    model = Sequential(
        [
            Input(shape=input_shape),
            layers.Conv2D(
                32, kernel_size=(3, 3), activation="relu"),
            layers.MaxPooling2D(pool_size=(2, 2)),
            layers.Conv2D(64, kernel_size=(3, 3), activation="relu"),
            layers.MaxPooling2D(pool_size=(2, 2)),
            layers.Flatten(),
            layers.Dropout(0.5),
            layers.Dense(num_classes, activation="softmax"),
        ]
    )
    return model

def save_model(model, filepath="models/mnist_model.keras"):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    
    model.save(filepath)
    print(f"Model saved to '{filepath}'.")

def load_trained_model(filepath="models/mnist_model.keras"):
    
    try:
        # Load the saved model from the mounted volume
        model = load_model('models/mnist_model.keras')
        print("Model loaded successfully!")
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        return None