# app/data_loader.py
import numpy as np
from keras.datasets import mnist
from keras.utils import to_categorical
import psycopg2
from io import BytesIO
from tensorflow.keras.utils import to_categorical
from PIL import Image


def load_data():
    """
    Loads and preprocesses the MNIST dataset.

    Returns:
        tuple: ((x_train, y_train), (x_test, y_test))
    """
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train = np.expand_dims(x_train.astype("float32") / 255, -1)
    x_test = np.expand_dims(x_test.astype("float32") / 255, -1)
    y_train = to_categorical(y_train, 10)
    y_test = to_categorical(y_test, 10)
    return (x_train, y_train), (x_test, y_test)

def load_data_from_db(database, user, host, password, port):
    """
    Fetches all data from the input_data table.

    Returns:
        list of tuples: [(id, image_binary, true_value), ...]
    """
    try:
        conn = psycopg2.connect(database=database, user=user, host=host, password=password, port=port)
        cur = conn.cursor()
        cur.execute("SELECT id, image, true_value FROM input_data;")
        data = cur.fetchall()
        print(f"Fetched {len(data)} rows from the database.")
        return data
    except Exception as e:
        print(f"Error while fetching data: {e}")
        return []
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def transform_data_to_numpy(fetched_data):
    """
    Transforms binary images and labels into NumPy arrays.

    Returns:
        tuple: (x_data, y_data, ids)
    """
    images, labels, ids = [], [], []
    for record_id, image_binary, label in fetched_data:
        try:
            buffer = BytesIO(image_binary)
            image = np.array(Image.open(buffer).convert("L"))  # Grayscale
            images.append(image.astype("float32") / 255.0)
            labels.append(label)
            ids.append(record_id)
        except Exception as e:
            print(f"Failed to process image ID {record_id}: {e}")
            continue
    x_data = np.expand_dims(np.array(images), axis=-1)  # Reshape to (N, 28, 28, 1)
    y_data = to_categorical(np.array(labels), 10)
    ids = np.array(ids)
    return x_data, y_data, ids