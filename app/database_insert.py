# app/data_loader.py
import psycopg2
from PIL import Image
from io import BytesIO
import numpy as np

def save_input_data_to_db(database, user, host, password, port, image_data):
    """
    Inserts image data into the input_data table.

    Parameters:
        mnist_data (list of tuples): Prepared data [(image_binary, label), ...].
    """
    try:
        conn = psycopg2.connect(database=database, user=user, host=host, password=password, port=port)
        cur = conn.cursor()
        cur.execute("DELETE FROM input_data;")  
        cur.executemany("INSERT INTO input_data (image) VALUES (%s, %s);", image_data)
        conn.commit()
        print("Data successfully inserted into the database.")
    except Exception as e:
        print(f"Error during data insertion: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()



def save_predictions_to_db(database, user, password, port, host, predictions, input_data_ids):
    """
    Inserts predictions into the predictions table.

    Parameters:
        database (str): Database name.
        user (str): Username for the database.
        password (str): Password for the database.
        port (int): Port number for the database.
        host (str): Host of the database.
        predictions (list or numpy.ndarray): Predicted values.
        input_data_ids (list or numpy.ndarray): Corresponding input_data IDs.

    Returns:
        None
    """
    conn = None
    cur = None  # Initialize to None to prevent unbound local errors
    
    try:
        # Convert inputs to standard Python types
        predictions = [int(pred) for pred in predictions]
        input_data_ids = [int(record_id) for record_id in input_data_ids]

        # Connect to PostgreSQL
        conn = psycopg2.connect(
            database=database,
            user=user,
            password=password,
            port=port,
            host=host
        )
        cur = conn.cursor()

        # SQL query to insert predictions
        insert_query = """
            INSERT INTO predictions (input_data_id, predicted_value)
            VALUES (%s, %s);
        """

        # Prepare data for bulk insert
        insert_data = list(zip(input_data_ids, predictions))

        # Execute the bulk insert
        cur.executemany(insert_query, insert_data)
        conn.commit()
        print(f"Successfully inserted {len(predictions)} predictions into the database.")

    except Exception as e:
        print(f"Error while inserting predictions: {e}")

    finally:
        # Ensure clean-up of resources
        if cur:
            cur.close()
        if conn:
            conn.close()
