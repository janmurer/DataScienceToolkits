import wandb
from wandb.integration.keras import WandbMetricsLogger
import tensorflow as tf
from app import load_data, save_model, evaluate_model

def build_model(architecture):
    """Build the model based on the given architecture."""
    if architecture == "simple":
        model = tf.keras.Sequential([
            tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
            tf.keras.layers.MaxPooling2D((2, 2)),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(64, activation='relu'),
            tf.keras.layers.Dense(10, activation='softmax')
        ])
    elif architecture == "complex":
        model = tf.keras.Sequential([
            tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
            tf.keras.layers.MaxPooling2D((2, 2)),
            tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
            tf.keras.layers.MaxPooling2D((2, 2)),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dropout(0.5),
            tf.keras.layers.Dense(10, activation='softmax')
        ])
    else:
        raise ValueError("Unknown architecture type")
    return model

def compile_model(model, optimizer, loss_function, learning_rate):
    """Compile the model with specified optimizer and loss function."""
    if optimizer == "Adam":
        opt = tf.keras.optimizers.Adam(learning_rate=learning_rate)
    elif optimizer == "SGD":
        opt = tf.keras.optimizers.SGD(learning_rate=learning_rate)
    else:
        raise ValueError("Unsupported optimizer")
    
    model.compile(optimizer=opt, loss=loss_function, metrics=["accuracy"])

def main():
    # Initialize W&B and set configurations dynamically
    wandb.init(project="mnist-experiments", config={
        "architecture": "simple",  # Options: "simple", "complex"
        "epochs": 10,
        "batch_size": 64,
        "learning_rate": 0.001,
        "loss_function": "categorical_crossentropy",  # Options: "categorical_crossentropy", "sparse_categorical_crossentropy"
        "optimizer": "SGD",  # Options: "Adam", "SGD"
    })

    config = wandb.config

    print("Starting data loading...")
    (x_train, y_train), (x_test, y_test) = load_data()
    print("Data loaded successfully.")

    print("Building model...")
    model = build_model(config.architecture)
    compile_model(model, config.optimizer, config.loss_function, config.learning_rate)
    print("Model compiled.")

    print("Starting training...")
    model.fit(
        x_train, y_train,
        batch_size=config.batch_size,
        epochs=config.epochs,
        validation_split=0.1,
        callbacks=[WandbMetricsLogger()]
    )
    print("Model trained.")

    print("Saving model...")
    save_model(model)

    print("Evaluating model on the test set...")
    test_loss, test_accuracy = evaluate_model(model, x_test, y_test)

    # Log test metrics to W&B
    wandb.log({"test_loss": test_loss, "test_accuracy": test_accuracy})
    print("Evaluation complete.")
    print(f"Test accuracy of the model: {test_accuracy:.4f}")

    wandb.finish()

if __name__ == "__main__":
    main()
