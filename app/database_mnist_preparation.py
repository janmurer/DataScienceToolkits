import numpy as np
from io import BytesIO

def ensure_integer_labels(y_data):
    """
    Ensures that the label data (y_data) is in integer form. 
    If y_data is one-hot encoded, it converts it to integer class labels.

    Parameters:
        y_data (numpy.ndarray): Label data, which may be in one-hot encoded or integer form.

    Returns:
        numpy.ndarray: A 1D array of integer class labels.
    """
    # Check if y_data is already in integer form
    if len(y_data.shape) == 1:
        return y_data  # Already in integer form

    # Convert one-hot encoded labels to integer class labels using np.argmax
    if len(y_data.shape) == 2:
        y_data = np.argmax(y_data, axis=1)
        return y_data
    
    # Raise an error for invalid input
    raise ValueError("y_data must be either a 1D array of integers or a 2D one-hot encoded array.")

def prepare_mnist_data(x_data, y_data, sample_size=100):
    """
    Prepares a random sample of MNIST image and label data for database insertion.

    Parameters:
        x_data (numpy.ndarray): MNIST image data.
        y_data (numpy.ndarray): MNIST labels.
        sample_size (int): Number of random rows to sample.

    Returns:
        list of tuples: A list of (image_binary, label) ready for insertion.
    """
    # Randomly select `sample_size` indices
    random_indices = np.random.choice(len(x_data), sample_size, replace=False)

    prepared_data = []

    for idx in random_indices:
        image = x_data[idx]
        label = y_data[idx]

        # Convert image (numpy array) to binary (BYTEA)
        with BytesIO() as buffer:
            np.save(buffer, image)  # Save as binary format
            image_binary = buffer.getvalue()  # Get binary data
        
        # Append the (image_binary, label) tuple
        prepared_data.append((image_binary, int(label)))
    
    return prepared_data
