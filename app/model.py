# app/model.py
import os
from keras import Sequential, layers
from keras.models import load_model

def build_model(input_shape=(28, 28, 1), num_classes=10):
    model = Sequential(
        [
            layers.Conv2D(
                32, kernel_size=(3, 3), activation="relu", input_shape=input_shape
            ),
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
    return load_model(filepath)
