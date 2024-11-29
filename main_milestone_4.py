import os
import wandb
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping

# Initialize W&B
wandb.init(project="ml-docker-project", config={
    "epochs": 10,
    "batch_size": 32,
    "learning_rate": 0.001,
})

# Define a simple model
model = Sequential([
    Dense(128, activation='relu', input_shape=(10,)),  # Adjust input size as needed
    Dense(64, activation='relu'),
    Dense(1, activation='sigmoid'),
])

# Compile the model
model.compile(optimizer=Adam(learning_rate=wandb.config.learning_rate),
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Log model summary
model.summary(print_fn=wandb.log)

# Generate dummy data
import numpy as np
x_train = np.random.rand(1000, 10)
y_train = np.random.randint(0, 2, 1000)

# Train the model and log metrics
history = model.fit(
    x_train, y_train,
    epochs=wandb.config.epochs,
    batch_size=wandb.config.batch_size,
    validation_split=0.2,
    callbacks=[
        wandb.keras.WandbCallback()  # Automatically logs metrics, parameters, and gradients
    ]
)

# Save and upload the trained model
model.save("trained_model.h5")
wandb.save("trained_model.h5")
