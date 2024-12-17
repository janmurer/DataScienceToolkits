# main.py

from app import setup_database, load_data, prepare_mnist_data, input_mnist_data, ensure_integer_labels, load_data_from_db, transform_data_to_numpy, load_trained_model, predict, save_predictions_to_db

def main():

    print("Creating databases..")
    setup_database(database = "milestone_3", user = "postgres", password = "postgres", port = 5432, host = "db")
    print("Database created")

    print("Starting data loading...")
    (x_train, y_train), (x_test, y_test) = load_data()
    print("Data loaded successfully.")

    print("Prepare data...")
    y_test = ensure_integer_labels(y_test)
    prepared_data = prepare_mnist_data(x_test, y_test)

    print("Inserting data into the database")
    input_mnist_data(database = "milestone_3", user = "postgres", password = "postgres", port = 5432, host = "db", mnist_data = prepared_data)
    print("Data insertion successfully completed")

    print("Fetch data from database...")
    fetched_data = load_data_from_db(database = "milestone_3", user = "postgres", password = "postgres", port = 5432, host = "db")
    x_data, y_data, ids = transform_data_to_numpy(fetched_data)

    print("x_data shape:", x_data.shape)  # Expected: (N, 28, 28, 1)
    print("y_data shape:", y_data.shape)  # Expected: (N, 10)
    print("First label (one-hot):", y_data[0])

    print("Loading the trained model...")
    loaded_model = load_trained_model(filepath='models/mnist_model.keras')

    print("Predciting the values...")
    predicted_labels = predict(loaded_model, x_data)
    print("Prediction successful!")
    print("Prediction of first value:")
    print("True value:")

    print("Saving results to database")
    save_predictions_to_db(database = "milestone_3", user = "postgres", password = "postgres", port = 5432, host = "db", predictions = predicted_labels, input_data_ids = ids)
    print("Results saved to the database")


if __name__ == "__main__":
    main()