# main.py

from app import setup_database

database = "predictions"
user = "postgres"
password = "postgres"
port = 5432
host = "db"

def main():

    print("Creating databases..")
    setup_database(database = database, user = user, password = password, port = port, host = host)
    print("Database created")

if __name__ == "__main__":
    main()