# app/trainer.py
from keras.optimizers import Adam

def compile_model(model):
    model.compile(loss="categorical_crossentropy", optimizer=Adam(), metrics=["accuracy"])

def train_model(model, x_train, y_train, batch_size=128, epochs=15, validation_split=0.1):
    model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, validation_split=validation_split)

def evaluate_model(model, x_test, y_test):
    score = model.evaluate(x_test, y_test, verbose=0)
    print("Test loss:", score[0])
    print("Test accuracy:", score[1])
    return score
