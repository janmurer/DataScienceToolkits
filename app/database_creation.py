import psycopg2

database = "predictions"
user = "postgres"
password = "postgres"
port = 5432
host = "localhost"

import psycopg2
from psycopg2 import sql

def setup_database(database, user, host, password, port):
    """
    Ensures the specified database exists and sets up the required tables.
    
    Parameters:
        database (str): The name of the database to connect to or create.
        user (str): The PostgreSQL username.
        host (str): The host address of the PostgreSQL server.
        password (str): The password for the PostgreSQL user.
        port (int): The port number for the PostgreSQL server.
    """
    conn = None
    cur = None
    try:
        # Connect to the default 'postgres' database to check or create the target database
        conn = psycopg2.connect(
            dbname="postgres",
            user=user,
            host=host,
            password=password,
            port=port
        )
        conn.autocommit = True  # Enable autocommit for database creation
        cur = conn.cursor()

        # Check if the target database exists
        cur.execute(
            sql.SQL("SELECT 1 FROM pg_database WHERE datname = %s"),
            [database]
        )
        if not cur.fetchone():
            # Create the database if it does not exist
            cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(database)))
            print(f"Database '{database}' created successfully.")
        else:
            print(f"Database '{database}' already exists.")

        # Close the connection to 'postgres' and switch to the target database
        cur.close()
        conn.close()

        # Connect to the target database
        conn = psycopg2.connect(
            dbname=database,
            user=user,
            host=host,
            password=password,
            port=port
        )
        cur = conn.cursor()

        # Create the `input_data` table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS input_data (
                id SERIAL PRIMARY KEY,
                image BYTEA NOT NULL
            );
        """)

        # Create the `predictions` table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS predictions (
                id SERIAL PRIMARY KEY,
                predicted_value SMALLINT NOT NULL CHECK (predicted_value >= 0 AND predicted_value <= 9),
                input_data_id INTEGER NOT NULL,
                FOREIGN KEY (input_data_id) REFERENCES input_data(id) ON DELETE CASCADE
            );
        """)

        # Commit the changes
        conn.commit()
        print("Tables created successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Safely close the cursor and connection
        if cur:
            cur.close()
        if conn:
            conn.close()
