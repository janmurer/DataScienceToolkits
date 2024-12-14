import wandb
from wandb.integration.keras import WandbCallback
from wandb.integration.keras import WandbMetricsLogger
from app import load_data, build_model, load_trained_model, save_model, compile_model, evaluate_model, train_model

def main():
    # Initialize W&B
    wandb.init(project="mnist-training", config={
        "epochs": 15,
        "batch_size": 128,
        "architecture": "Conv2D -> MaxPool -> Conv2D -> MaxPool -> Flatten -> Dropout -> Dense",
        "optimizer": "Adam",
        "loss_function": "categorical_crossentropy",
    })

    print("Starting data loading...")
    (x_train, y_train), (x_test, y_test) = load_data()
    print("Data loaded successfully.")

    print("Building model...")
    model = build_model()
    compile_model(model)
    print("Model compiled.")

    print("Starting training...")
    train_model(
        model,
        x_train,
        y_train,
        batch_size=wandb.config.batch_size,
        epochs=wandb.config.epochs,
        validation_split=0.1,
        callbacks=[WandbMetricsLogger()]  # Pass callbacks to train_model
    )
    print("Model trained.")

    print("Saving model...")
    save_model(model)

    print("Loading the trained model...")
    loaded_model = load_trained_model()

    compile_model(loaded_model)
    print("Model loaded and compiled.")

    print("Evaluating model on the test set...")
    test_loss, test_accuracy = evaluate_model(loaded_model, x_test, y_test)

    # Log test metrics to W&B
    wandb.log({"test_loss": test_loss, "test_accuracy": test_accuracy})
    print("Evaluation complete.")
    print(f"Test accuracy of the loaded model: {test_accuracy:.4f}")

    # Save model artifact to W&B
    wandb.save("models/mnist_model.keras")

if __name__ == "__main__":
    main()
