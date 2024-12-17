import psycopg2

database = "milestone_3"
user = "postgres"
password = "postgres"
port = 5432
host = "localhost"

# Function for the Creation of the database
def setup_database(database, user, host, password, port):
    """
    Sets up the milestone_3 database by creating an 'input' and 'predictions' table.

    Parameters:
        database (str): Name of the database to connect to.
        user (str): Database user name.
        host (str): Host address of the database.
        password (str): Password for the database user.
        port (int): Port number of the database.

    Returns:
        None
    """
    try:
        # Open connection to the PostgreSQL database
        conn = psycopg2.connect(
            database=database,
            user=user,
            host=host,
            password=password,
            port=port
        )
        
        # Open a cursor to perform database operations
        cur = conn.cursor()
        
        # Execute a command: create input_data table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS input_data (
                id SERIAL PRIMARY KEY,
                image BYTEA NOT NULL,
                true_value SMALLINT NOT NULL CHECK (true_value >= 0 AND true_value <= 9)
            );
        """)

        # Execute a command: create predictions table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS predictions (
                id SERIAL PRIMARY KEY,
                predicted_value SMALLINT NOT NULL CHECK (predicted_value >= 0 AND predicted_value <= 9),
                input_data_id INTEGER NOT NULL,
                FOREIGN KEY (input_data_id) REFERENCES input_data(id) ON DELETE CASCADE
            );
        """)
        
        # Make the changes to the database persistent
        conn.commit()
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Close cursor and communication with the database
        if cur:
            cur.close()
        if conn:
            conn.close()


