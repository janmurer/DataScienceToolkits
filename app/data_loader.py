# app/data_loader.py
import numpy as np
from keras.datasets import mnist
from keras.utils import to_categorical
import psycopg2
from io import BytesIO
from tensorflow.keras.utils import to_categorical


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

def load_data_from_db(database, user, host, password, port):
    """
    Fetches all data (image, correct_value) from the input_data table.

    Parameters:
        database (str): Database name.
        user (str): Username for the database.
        host (str): Host of the database.
        password (str): Database password.
        port (int): Database port.

    Returns:
        list of tuples: A list where each tuple contains (id, image_binary, correct_value).
    """
    try:
        # Connect to PostgreSQL
        conn = psycopg2.connect(
            database=database,
            user=user,
            host=host,
            password=password,
            port=port
        )
        cur = conn.cursor()

        # SQL query to fetch data
        query = "SELECT id, image, true_value FROM input_data;"
        cur.execute(query)

        # Fetch all rows
        data = cur.fetchall()
        print(f"Fetched {len(data)} rows from the database.")

        return data

    except Exception as e:
        print(f"Error while fetching data: {e}")
        return []

    finally:
        # Clean up
        if cur:
            cur.close()
        if conn:
            conn.close()

def transform_data_to_numpy(fetched_data):
    """
    Transforms binary images and labels into NumPy arrays and normalizes the data.

    Parameters:
        fetched_data (list of tuples): List containing (image_binary, correct_value).

     Returns:
        tuple: (x_data, y_data, ids)
            - x_data: Normalized image data as a NumPy array of shape (N, 28, 28, 1).
            - y_data: One-hot encoded labels as a NumPy array of shape (N, 10).
            - ids: Array of IDs from the database.
    """
    images = []
    labels = []
    ids = []

    for record_id, image_binary, label in fetched_data:  # Unpack three values
        # Convert binary image back to a NumPy array
        with BytesIO(image_binary) as buffer:
            image = np.load(buffer)

        # Normalize the image to [0, 1]
        image = image.astype("float32") / 255.0

        # Reshape to (28, 28, 1)
        image = np.expand_dims(image, axis=-1)

        images.append(image)
        labels.append(label)
        ids.append(record_id)

    # Convert to NumPy arrays
    x_data = np.array(images)
    y_data = to_categorical(np.array(labels), 10)
    ids = np.array(ids)

    print(f"Transformed {len(x_data)} images and labels into NumPy arrays.")
    return x_data, y_data, ids


