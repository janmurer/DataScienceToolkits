import numpy as np
from io import BytesIO
from PIL import Image


def ensure_integer_labels(y_data):
    """
    Converts one-hot encoded labels to integer class labels.

    Parameters:
        y_data (numpy.ndarray): One-hot encoded or integer labels.

    Returns:
        numpy.ndarray: Integer class labels.
    """
    return np.argmax(y_data, axis=1) if len(y_data.shape) == 2 else y_data
    
    # Raise an error for invalid input
    raise ValueError("y_data must be either a 1D array of integers or a 2D one-hot encoded array.")

def prepare_mnist_data(x_data, y_data, sample_size=100):
    """
    Prepares a random sample of MNIST data for database insertion.

    Parameters:
        x_data (numpy.ndarray): Image data.
        y_data (numpy.ndarray): Integer labels.
        sample_size (int): Number of samples to prepare.

    Returns:
        list of tuples: [(image_binary, label), ...]
    """
    indices = np.random.choice(len(x_data), sample_size, replace=False)
    prepared_data = []
    for idx in indices:
        image = (x_data[idx] * 255).astype("uint8").squeeze() 
        buffer = BytesIO()
        Image.fromarray(image).save(buffer, format="PNG")
        prepared_data.append((buffer.getvalue(), int(y_data[idx])))
    return prepared_data