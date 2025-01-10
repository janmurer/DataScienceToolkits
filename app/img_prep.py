from PIL import Image
import cv2
import numpy as np
from io import BytesIO

def prepare_image_for_db(image_file):
    """
    Prepares an uploaded image file for database insertion.

    Parameters:
        image_file (werkzeug.datastructures.FileStorage): The uploaded image file.

    Returns:
        list: A list containing a tuple of binary representation of the processed image in PNG format.
    """
    # Read the file and convert to bytes
    image_bytes = image_file.read()

    # Decode the image into a NumPy array
    image_np = np.frombuffer(image_bytes, np.uint8)
    image = cv2.imdecode(image_np, cv2.IMREAD_GRAYSCALE)

    # Resize and normalize the image
    image = cv2.resize(image, (28, 28)) / 255.0
    image = image.reshape(1, 28, 28, 1)

    # Convert to 0-255 range and uint8
    image = (image * 255).astype("uint8").squeeze()

    # Convert the image to PNG format using an in-memory buffer
    buffer = BytesIO()
    Image.fromarray(image).save(buffer, format="PNG")

    # Return the binary data wrapped in the required structure
    return [(buffer.getvalue(),)]
