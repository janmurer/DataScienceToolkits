# main.py

from app import setup_jokes_database, fetch_first_joke

def main():

    print("Creating jokes database..")
    setup_jokes_database(database = "ms3_jokes", user = "postgres", password = "postgres", port = 5433, host = "db")
    print("Now we test our jokes database and select our favourite joke:")
    fetch_first_joke(database = "ms3_jokes", user = "postgres", password = "postgres", port = 5433, host = "db")


if __name__ == "__main__":
    main()
