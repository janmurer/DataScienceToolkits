import numpy as np

def convert_to_true_labels(y_data):
    """
    Converts one-hot encoded labels into their true integer class labels.

    Parameters:
        y_data (numpy.ndarray): One-hot encoded labels of shape (N, num_classes).

    Returns:
        numpy.ndarray: True integer class labels of shape (N,).
    """
    # Use np.argmax to get the index of the maximum value in each row
    true_labels = np.argmax(y_data, axis=1)
    return true_labels
