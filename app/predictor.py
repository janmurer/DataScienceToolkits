# app/predictor.py
import numpy as np

def predict(model, x_test):
    predictions = model.predict(x_test)
    return np.argmax(predictions, axis=1)
