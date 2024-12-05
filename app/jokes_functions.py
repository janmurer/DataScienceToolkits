import psycopg2

database = "ms3_jokes"
user = "postgres"
password = "postgres"
port = 5432
host = "localhost"

# Function for the Creation of the database
def setup_jokes_database(database, user, host, password, port):
    """
    Sets up the jokes database by creating a 'jokes' table and inserting an initial joke.

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
        
        # Execute a command: create jokes table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS jokes (
                ID SERIAL PRIMARY KEY,
                JOKE TEXT NOT NULL
            );
        """)
        
        # Insert a joke into the jokes table
        cur.execute("INSERT INTO jokes (JOKE) VALUES ('I had a joke about paper today, but it was tearable.')")
        
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

# Function for fetching the first joke
def fetch_first_joke(database, user, host, password, port):
    """
    Fetches and prints the first joke from the 'jokes' table in the database.

    Parameters:
        database (str): Name of the database to connect to.
        user (str): Database user name.
        host (str): Host address of the database.
        password (str): Password for the database user.
        port (int): Port number of the database.

    Returns:
        str: The joke if found, or a message indicating no jokes were found.
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
        
        # Execute the query to fetch the first joke
        cur.execute("SELECT joke FROM jokes ORDER BY id LIMIT 1")
        
        # Fetch the result of the query
        result = cur.fetchone()
        
        if result:
            joke = result[0]
            print(f"Joke: {joke}")
            return joke
        else:
            print("No jokes found in the database.")
            return "No jokes found in the database."
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return f"Error: {e}"
    
    finally:
        # Close cursor and communication with the database
        if 'cur' in locals() and cur:
            cur.close()
        if 'conn' in locals() and conn:
            conn.close()

