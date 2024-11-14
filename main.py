# main.py

from app.data_loader import load_data
from app.model import build_model, load_trained_model, save_model
from app.trainer import compile_model, evaluate_model, train_model


def main():
    print("Starting data loading...")
    (x_train, y_train), (x_test, y_test) = load_data()
    print("Data loaded successfully.")

    print("Building model...")
    model = build_model()
    compile_model(model)
    print("Model compiled.")

    print("Starting training...")
    train_model(model, x_train, y_train)
    print("Model trained.")

    print("Saving model...")
    save_model(model)

    print("Loading the trained model...")
    loaded_model = load_trained_model()

    compile_model(loaded_model)
    print("Model loaded and compiled.")

    print("Evaluating model on the test set...")
    test_loss, test_accuracy = evaluate_model(loaded_model, x_test, y_test)
    print("Evaluation complete.")
    print(f"Test accuracy of the loaded model: {test_accuracy:.4f}")


if __name__ == "__main__":
    main()
