# app/predictor.py
import numpy as np

def predictor(loaded_model, x_data):
    """
    Uses the loaded model to predict the class labels for the given input data.

    Parameters:
        loaded_model: Pretrained model loaded into memory.
        x_data (numpy.ndarray): Input image data, normalized and shaped (N, 28, 28, 1).

    Returns:
        numpy.ndarray: Predicted class labels for the input data.
    """
    # Perform predictions on the input data
    predictions = loaded_model.predict(x_data)
    
    # Convert predictions to class labels using np.argmax
    predicted_labels = np.argmax(predictions, axis=1)
    
    return predicted_labels

