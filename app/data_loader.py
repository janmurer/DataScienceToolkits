# app/data_loader.py
import numpy as np
from keras.datasets import mnist
from keras.utils import to_categorical

def load_data():
    # Load and preprocess data
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    
    # Normalize and reshape data
    x_train = np.expand_dims(x_train.astype("float32") / 255, -1)
    x_test = np.expand_dims(x_test.astype("float32") / 255, -1)
    
    # Convert labels to one-hot encoding
    y_train = to_categorical(y_train, 10)
    y_test = to_categorical(y_test, 10)
    
    return (x_train, y_train), (x_test, y_test)
