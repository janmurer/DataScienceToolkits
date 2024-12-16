
import os
import numpy as np
import tensorflow as tf
from sqlalchemy import create_engine, Column, Integer, LargeBinary, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql import exists
import pickle

# Database configuration
DATABASE_URL = os.getenv('DATABASE_URL')
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()

# Define database models
class InputData(Base):
    __tablename__ = 'input_data'
    
    id = Column(Integer, primary_key=True)
    data = Column(LargeBinary)
    predictions = relationship("Prediction", back_populates="input_data")

class Prediction(Base):
    __tablename__ = 'predictions'
    
    id = Column(Integer, primary_key=True)
    input_id = Column(Integer, ForeignKey('input_data.id'))
    prediction = Column(Float)
    input_data = relationship("InputData", back_populates="predictions")

def test_database_connection():
    try:
        # Test connection
        connection = engine.connect()
        print("Successfully connected to the database!")
        # List all tables
        from sqlalchemy import inspect
        inspector = inspect(engine)
        print("\nAvailable tables:")
        for table_name in inspector.get_table_names():
            print(f"- {table_name}")
        connection.close()
        return True
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return False

def init_database():
    try:
        # Create tables if they don't exist
        Base.metadata.create_all(engine)
        print("Database tables created successfully!")
    except Exception as e:
        print(f"Error creating database tables: {e}")

def load_model():
    try:
        # Load the saved model from the mounted volume
        model = tf.keras.models.load_model('/app/model/model.keras')
        print("Model loaded successfully!")
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

def load_sample():
    # Load MNIST dataset as an example
    (x_train, _), (_, _) = tf.keras.datasets.mnist.load_data()
    # Take first sample
    sample = x_train[0]
    return sample

def save_input_to_db(session, input_data):
    # Serialize the numpy array
    serialized_data = pickle.dumps(input_data)
    
    # Create new input data record
    new_input = InputData(data=serialized_data)
    session.add(new_input)
    session.commit()
    print("Input data saved to database successfully!")
    return new_input

def load_input_from_db(session, input_id):
    # Load and deserialize input data
    input_record = session.query(InputData).filter_by(id=input_id).first()
    if input_record:
        print("Successfully loaded input data from database!")
        return pickle.loads(input_record.data)
    print("No input data found in database!")
    return None

def save_prediction(session, input_id, pred):
    # Save prediction with reference to input
    new_prediction = Prediction(input_id=input_id, prediction=float(pred))
    session.add(new_prediction)
    session.commit()
    print("Prediction saved to database successfully!")

def main():
    print("\nTesting database connection...")
    if not test_database_connection():
        print("Exiting due to database connection failure.")
        return

    print("\nInitializing database...")
    init_database()
    
    # Create session
    session = Session()
    
    try:
        # Load model
        print("\nLoading model...")
        model = load_model()
        if model is None:
            print("Exiting due to model loading failure.")
            return
        
        # Load sample data
        print("\nLoading sample data...")
        sample = load_sample()
        
        # Save input to database
        print("\nSaving input to database...")
        input_record = save_input_to_db(session, sample)
        
        # Load input from database
        print("\nLoading input from database...")
        loaded_sample = load_input_from_db(session, input_record.id)
        
        if loaded_sample is not None:
            # Prepare data for prediction
            processed_sample = loaded_sample.reshape(1, 28, 28, 1) / 255.0
            
            # Make prediction
            print("\nMaking prediction...")
            prediction = model.predict(processed_sample)
            predicted_class = np.argmax(prediction[0])
            
            # Save prediction to database
            print("\nSaving prediction to database...")
            save_prediction(session, input_record.id, predicted_class)
            
            print(f"\nFinal prediction result: {predicted_class}")
        
    except Exception as e:
        print(f"\nAn error occurred: {e}")
    finally:
        session.close()
        print("\nDatabase session closed.")

if __name__ == "__main__":
    main()