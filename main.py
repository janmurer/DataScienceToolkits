from app.data_loader import load_data
from app.model import build_model, save_model, load_trained_model
from app.trainer import compile_model, train_model, evaluate_model
from app.predictor import predict

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
    save_model(model, "mnist_model.h5")
    print("Model saved to mnist_model.h5")

    print("Loading the trained model...")
    loaded_model = load_trained_model("mnist_model.h5")
    print("Model loaded.")

    print("Evaluating model...")
    evaluate_model(loaded_model, x_test, y_test)

    print("Running predictions...")
    predictions = predict(loaded_model, x_test[:10])
    print("Predicted classes for the first 10 test images:", predictions)

if __name__ == "__main__":
    main()
