
import os
import time
import logging
import psycopg2
import numpy as np
from psycopg2 import sql
from keras.models import load_model
from keras.datasets import mnist
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv(dotenv_path='milestone_env')  # Ensure this matches your env file's name

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Database connection parameters
DB_HOST = os.getenv("DB_HOST", "postgres")
DB_PORT = int(os.getenv("DB_PORT", 5432))
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "your_secure_password")
DB_NAME = os.getenv("DB_NAME", "milestone_3")


# Function to connect to the database
def connect_db():
    try:
        logging.info(f"Connecting to database {DB_NAME} on {DB_HOST}:{DB_PORT}...")
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            dbname=DB_NAME
        )
        logging.info("Connected to the PostgreSQL database.")
        return conn
    except psycopg2.OperationalError as e:
        logging.error(f"Error connecting to database: {e}")
        return None


# Function to initialize the database
def initialize_db(conn):
    try:
        logging.info("Starting database initialization...")
        cursor = conn.cursor()
        
        # First check if tables exist
        cursor.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public'
            AND table_name IN ('input_data', 'predictions');
        """)
        existing_tables = cursor.fetchall()
        logging.info(f"Existing tables found: {existing_tables}")

        logging.info("Executing CREATE TABLE for input_data...")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS input_data (
                id SERIAL PRIMARY KEY,
                image BYTEA NOT NULL
            );
        """)
        
        logging.info("Executing CREATE TABLE for predictions...")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS predictions (
                id SERIAL PRIMARY KEY,
                input_id INTEGER REFERENCES input_data(id) ON DELETE CASCADE,
                prediction INTEGER NOT NULL
            );
        """)
        
        # Verify tables were created
        cursor.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public'
            AND table_name IN ('input_data', 'predictions');
        """)
        tables_after_creation = cursor.fetchall()
        logging.info(f"Tables after creation: {tables_after_creation}")
        
        conn.commit()
        logging.info("Tables created successfully.")

    except Exception as e:
        logging.error(f"Error initializing database: {str(e)}")
        logging.error(f"Error type: {type(e)}")
        conn.rollback()
        raise  # Re-raise the exception to see the full error
    finally:
        cursor.close()

# Function to insert an image into the database
def insert_input_data(conn, image_array):
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO input_data (image) VALUES (%s) RETURNING id;", (psycopg2.Binary(image_array.tobytes()),))
        input_id = cursor.fetchone()[0]
        conn.commit()
        logging.info(f"Inserted input data with ID: {input_id}")
        return input_id
    except Exception as e:
        logging.error(f"Error inserting input data: {e}")
        conn.rollback()
        return None


# Function to predict an image
def predict_image(model, conn, input_id):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT image FROM input_data WHERE id = %s;", (input_id,))
        image_data = cursor.fetchone()[0]
        image_array = np.frombuffer(image_data, dtype=np.uint8).reshape(28, 28)

        # Preprocess the image
        processed_image = image_array.astype('float32') / 255.0
        processed_image = np.expand_dims(processed_image, axis=0)  # Batch dimension
        processed_image = np.expand_dims(processed_image, axis=-1)  # Channel dimension

        prediction = model.predict(processed_image)
        predicted_label = np.argmax(prediction, axis=1)[0]

        # Insert prediction into predictions table
        cursor.execute("INSERT INTO predictions (input_id, prediction) VALUES (%s, %s) RETURNING id;", (input_id, predicted_label))
        prediction_id = cursor.fetchone()[0]
        conn.commit()
        logging.info(f"Prediction stored with ID: {prediction_id} (Label: {predicted_label})")
        return predicted_label
    except Exception as e:
        logging.error(f"Error predicting image: {e}")
        conn.rollback()
        return None


# Main script
def main():

    # Initial delay to allow time for log inspection
    logging.info(f"Application startup delayed for 1 minute... Start time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    time.sleep(120)  # 2-minute delay
    logging.info(f"Application execution begins at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    conn = None
    while not conn:
        conn = connect_db()
        if not conn:
            logging.info("Retrying database ....")
            time.sleep(5)

    # Initialize the database
    initialize_db(conn)

    # Load the trained model
    model_path = '/app/model/model.keras' 
    model = load_model(model_path)
    logging.info("Neural network model loaded successfully.")

    # Load MNIST test dataset
    (_, _), (test_images, _) = mnist.load_data()
    sample_image = test_images[0]  # Use the first test image

    # Insert image and predict
    input_id = insert_input_data(conn, sample_image)

    # Add a 2 minutes times out.
    logging.info("Pausing for 2 minutes before moving to model predictions...")
    time.sleep(120)  # Pause for 120 seconds

    if input_id:
        predict_image(model, conn, input_id)

    conn.close()


if __name__ == "__main__":
    main()
