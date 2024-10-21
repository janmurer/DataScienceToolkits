"""

Title: Simple MNIST convnet
Author: [fchollet](https://twitter.com/fchollet)
Date created: 2015/06/19
Last modified: 2020/04/21
Description: A simple convnet that achieves ~99% test accuracy on MNIST.
Accelerator: GPU
"""

"""
## Setup
"""

# Import the required libraries. Numpy is used to work with arrays. Keras is used to create and train neural networks.

import numpy as np
import keras
from keras import layers

"""
## Prepare the data
"""

# Model / data parameters
num_classes = 10 # Number of classes represents the 10 possible output classes (digits 0-9)
input_shape = (28, 28, 1) # 28x28 pixel images with 1 channel (grayscale)

# Load the data and split it between train and test sets. The MNIST dataset is loaded from Keras built in datasets. 
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# Scale images to the [0, 1] range. The pixel values are casted to floating point numbers and divided by 255 to scale them to the range [0, 1]. As the input pictures are grayscale, the pixel values range from 0 to 255.
x_train = x_train.astype("float32") / 255
x_test = x_test.astype("float32") / 255
# Make sure images have shape (28, 28, 1). The dimension of the image arrays are expanded by one dimension. The extra dimension is used to represent the color channel (in this case, there is only one channel as the images are grayscale).
x_train = np.expand_dims(x_train, -1)
x_test = np.expand_dims(x_test, -1)
print("x_train shape:", x_train.shape)
print(x_train.shape[0], "train samples")
print(x_test.shape[0], "test samples")


# convert class vectors to binary class matrices. The labels (integers 0-9) are converted to one-hot encoded vectors. This is done to convert multiple classes into a numerical format that should help ML algorithms to understand and provide better results.
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

"""
## Build the model
"""
# The architecture of the model is defined. 
model = keras.Sequential(
    [
        keras.Input(shape=input_shape),
        layers.Conv2D(32, kernel_size=(3, 3), activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Conv2D(64, kernel_size=(3, 3), activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Flatten(),
        layers.Dropout(0.5),
        layers.Dense(num_classes, activation="softmax"),
    ]
)

model.summary()

"""
## Train the model
"""
# Batch size and number of epochs are defined. The model is trained on miti-batches of 128 samples for 15 epochs. 10% of the training data is used for validation. 
batch_size = 128
epochs = 15

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, validation_split=0.1)

"""
## Evaluate the trained model
"""
# The model is evaluated on the test data. When I ran the script, the test accuracy was 99.2% (as promised in the description of the script ;-)). The trained model is very accurate on unseen data. The low loss value (0.022) indicates that the difference between the predicted and actual values is very low.
score = model.evaluate(x_test, y_test, verbose=0)
print("Test loss:", score[0])
print("Test accuracy:", score[1])