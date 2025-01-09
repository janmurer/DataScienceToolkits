# app/__init__.py

# Import functions from each module to simplify access at the package level
from .data_loader import load_data, load_data_from_db, transform_data_to_numpy
from .model import build_model, load_trained_model, save_model
from .predictor import predict
from .trainer import compile_model, evaluate_model, train_model
from .jokes_functions import setup_jokes_database, fetch_first_joke
from .database_creation import setup_database
from .database_insert import input_mnist_data, save_predictions_to_db, save_to_db
from .database_mnist_preparation import prepare_mnist_data, ensure_integer_labels
from .one_hot_decoder import convert_to_true_labels
