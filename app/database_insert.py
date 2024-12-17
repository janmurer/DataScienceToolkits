import psycopg2

def input_mnist_data(database, user, host, password, port, mnist_data):
    """
    Inserts the prepared MNIST data into the input_data table.

    Parameters:
        database (str): Name of the database.
        user (str): Database user name.
        host (str): Host address.
        password (str): Password for the database.
        port (int): Port number of the database.
        mnist_data (list of tuples): Prepared data [(image_binary, correct_value), ...].

    Returns:
        None
    """
    try:
        # Open connection to PostgreSQL database
        conn = psycopg2.connect(
            database=database,
            user=user,
            host=host,
            password=password,
            port=port
        )
        cur = conn.cursor()
        
        # Insert MNIST data into the input_data table
        insert_query = """
            INSERT INTO input_data (image, true_value) 
            VALUES (%s, %s);
        """
        cur.executemany(insert_query, mnist_data)  # Bulk insert
        
        # Commit changes
        conn.commit()
        print("Data successfully inserted into the database.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Close cursor and connection
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
