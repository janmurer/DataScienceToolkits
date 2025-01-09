from PIL import Image
import numpy as np
from io import BytesIO 

def prepare_image_for_db(image):
    """
    Prepares an image for database insertion.
 
    Parameters:
        image (numpy.ndarray): Image data (e.g., a single MNIST image).
 
    Returns:
        bytes: Binary representation of the image in PNG format.
    """
    # Rescale the image to 0-255 range and ensure uint8 format
    image = (image * 255).astype("uint8").squeeze()
 
    # Convert the image to PNG format using an in-memory buffer
    buffer = BytesIO()
    Image.fromarray(image).save(buffer, format="PNG")
 
    # Return the binary data of the image
    return buffer.getvalue()