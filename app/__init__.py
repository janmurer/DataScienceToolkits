# app/__init__.py

# Import functions from each module to simplify access at the package level
from .data_loader import load_data
from .model import build_model, save_model, load_trained_model
from .trainer import compile_model, train_model, evaluate_model
from .predictor import predict
