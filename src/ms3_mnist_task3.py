
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from keras.datasets import mnist
import numpy as np
from dotenv import load_dotenv
import matplotlib.pyplot as plt
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load environment variables
load_dotenv(dotenv_path="../ms3_mnist.env")

# Database connection parameters
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", 5437))
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "your_password")
DB_NAME = os.getenv("DB_NAME", "ms3_mnist")

# Function to connect to a specific database
def connect_to_db(dbname):
    return psycopg2.connect(
        dbname=dbname,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

# Function to create the mnist_data table
def create_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS mnist_data (
            id SERIAL PRIMARY KEY,
            label INTEGER,
            image BYTEA
        );
    """)
    logging.info("Table 'mnist_data' created successfully.")

# Function to insert MNIST data into the mnist_data table
def insert_mnist_data(cursor, train_images, train_labels, limit=1000):
    insert_query = "INSERT INTO mnist_data (label, image) VALUES (%s, %s);"
    batch_data = [
        (int(train_labels[i]), psycopg2.Binary(train_images[i].tobytes()))
        for i in range(limit)
    ]
    cursor.executemany(insert_query, batch_data)
    logging.info(f"Inserted {limit} records into 'mnist_data'.")

# Function to fetch and display records from the mnist_data table
def fetch_and_display(cursor, limit=5):
    cursor.execute("SELECT id, label, image FROM mnist_data LIMIT %s;", (limit,))
    records = cursor.fetchall()
    if not records:
        logging.info("No records to display.")
        return
    for record in records:
        id, label, image = record
        image_array = np.frombuffer(image, dtype=np.uint8).reshape(28, 28)
        plt.imshow(image_array, cmap='gray')
        plt.title(f"ID: {id}, Label: {label}")
        plt.axis('off')
        plt.show()

# Main script
try:
    # Connect to the default 'postgres' database to create a new database
    conn = connect_to_db("postgres")
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conn.cursor()
    cursor.execute(f"CREATE DATABASE {DB_NAME};")
    logging.info(f"Database '{DB_NAME}' created successfully.")
except psycopg2.errors.DuplicateDatabase:
    logging.info(f"Database '{DB_NAME}' already exists.")
except Exception as e:
    logging.error(f"Unexpected error during database creation: {type(e).__name__} - {e}")
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()

try:
    # Connect to the newly created database
    conn = connect_to_db(DB_NAME)
    cursor = conn.cursor()
    
    # Create the table
    create_table(cursor)
    
    # Load and process MNIST data
    (train_images, train_labels), _ = mnist.load_data()
    train_images = train_images.reshape(-1, 28 * 28).astype(np.uint8)
    insert_mnist_data(cursor, train_images, train_labels)
    
    # Fetch and display records
    fetch_and_display(cursor)
    
    # Commit the transaction
    conn.commit()
except Exception as e:
    logging.error(f"Unexpected error: {type(e).__name__} - {e}")
    if conn:
        conn.rollback()
finally:
    # Close the cursor and connection
    if cursor:
        cursor.close()
    if conn:
        conn.close()
