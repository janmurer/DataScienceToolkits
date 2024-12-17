import numpy as np
from io import BytesIO
from PIL import Image
from tensorflow.keras.utils import to_categorical

def test_serialization_deserialization(x_data, y_data, sample_size=5):
    """
    Tests serialization and deserialization of image data to check for data consistency.

    Parameters:
        x_data (numpy.ndarray): Original image data.
        y_data (numpy.ndarray): Integer labels.
        sample_size (int): Number of samples to test.

    Returns:
        None
    """
    # Prepare a small sample for testing
    print("Testing serialization and deserialization...")
    indices = np.random.choice(len(x_data), sample_size, replace=False)
    test_images = x_data[indices]
    test_labels = y_data[indices]

    # Step 1: Serialize images
    serialized_data = []
    for image, label in zip(test_images, test_labels):
        image = (image * 255).astype("uint8").squeeze()  # Rescale to 0-255
        buffer = BytesIO()
        Image.fromarray(image).save(buffer, format="PNG")  # Serialize as PNG
        serialized_data.append((buffer.getvalue(), label))

    # Step 2: Deserialize images
    deserialized_images = []
    for image_binary, label in serialized_data:
        buffer = BytesIO(image_binary)
        deserialized_image = np.array(Image.open(buffer).convert("L"))  # Grayscale
        deserialized_image = deserialized_image.astype("float32") / 255.0  # Normalize
        deserialized_images.append(deserialized_image)

    deserialized_images = np.array(deserialized_images)

    # Step 3: Compare original and deserialized images
    for i in range(sample_size):
        original_image = test_images[i].squeeze()
        deserialized_image = deserialized_images[i]

        # Numerical comparison
        difference = np.abs(original_image - deserialized_image)
        max_diff = np.max(difference)
        mean_diff = np.mean(difference)

        print(f"Sample {i+1}:")
        print(f"Max difference: {max_diff:.5f}")
        print(f"Mean difference: {mean_diff:.5f}")

    print("Serialization and deserialization test completed.")
