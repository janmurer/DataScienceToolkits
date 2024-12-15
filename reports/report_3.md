# Report "Data Science Toolkits and Architectures"
#### Jan Murer, Frederik Poschenrieder, Jessica Ugowe 


# Milestone_3

## Task 1: 

---

## Task 2:

---

## Task 3: Visualizing Samples from the Database

### Key Questions Answered

**How do you need to represent/ transform image data to save it to a relational database?**

There are various ways To represnt / transform image data to save it to  a relational database however the method to choose depends on factors like performance requirement, ease of maintenence, database caplabilities  and how frequently you need to retrieve or modify the image data. 
-   Storing Images as Binary Large Objects (BLOBS): A BLOB is a single database unit that is made up of a group’s binary data. Mostly, they are used to save multimedia objects like video, sound, and image files(1). IT's pros include the fact that it simplifies backup, restore and transactional consistency  however large images can bloat the database  potebtially impacting performance and database backup and restore times increase as the database size grows. To do this we crate a table with a BLOB column e.g BYTEA in PostgreSQL, use our application code to read the image file as a byte arry abd then insert or update the row with the byte array.

- Storing images as Base64-Encoded Strings: It involves converting the image file’s bytes to a Base64 string in your application code, inserting that string into a VARCHAR or TEXT column in our database and when retrieving, decode the Base64 string back into binary form before serving. This is compatable with systems that expect textual data and this can simplify certain serialization or JSON-based APIs if we need to transmit images as text. However this method has the potential to increases storage size due to Base64 encoding overhead and it be slower to decode back into binary format for image processing.

- Storing Images Externally and Saving References: Instead of placing the image binary data directly in the database, we store the image file on a file system, a CDN, or an object storage service (like Amazon S3, Google Cloud Storage, or Azure Blob Storage), keep only a reference (URL, file path, or object key) in the database and when retrieving, the application uses the stored URL or path to fetch the image from the external source. Using this approach ensures the Database remains lean; only references are stored and this can potentially improve performance and scalability. However, it does come with its cons which includes a more complex setup: requires managing file systems or external storage and ensuring consistency between the database refrences and external files.

- Storing Derived Metadata and Thumbnails in the Database: this involves storing only metadata(e.g., height, width, format, camera EXIF data) and possibly a small thumbnail image in the database, while the full-resolution image is stored externally this ensures quick access to metadata and small previews from within queries and also reduces database storage requirements since only thumbnails and metadata are stored. However full-size image retrieval still depends on external storage.


**How is your data structured?**

The MNIST dataset consists of a large collection of 28x28 pixel grayscale images of handwritten digits (0 through 9). Each image is represented as a 2D NumPy array of shape (28, 28) with each element being an unsigned 8-bit integer (values from 0 to 255). Along with the images, the dataset provides corresponding labels (0–9) indicating which digit is depicted.

When loaded `(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()`, we get:

    (x_train, y_train): 60,000 training images and their labels.
    (x_test, y_test): 10,000 test images and their labels.
    Where:
    x_train and x_test are NumPy arrays of shape (60000, 28, 28) and y_train and y_test are one-dimensional arrays containing the integer labels for each corresponding image.
    

**Explain how you would define your relational database tables in terms of their attributes to save your data. What kind of data types could you use?**

To store the MNIST images and labels ina relational database (such as PostgreSQL), we need to consider how to first represent the image and its metadata(label,  possibly dimension). A straightfoward schemma might be to create a table that includes sttributes such as

-   id: this will be a serial primary key that provides a unique identifier for each stored image.
-   label_id: this attribute will use an INT data type as MNIST labels are digits (0-9) so we can dirrectly store the label as an integer.
-   image_data: this attribute will contain binary data that will allow us to preserve the exact byte structure of the image. We can use PostgreSQL BYTEA to achieve this.
-   width, height and channel attributes could also be included as separate attributes using INT data type. 


**What additional relational database table attributes might make sense to easily query your data (f.e. find all pictures of giraffes)?**

In a situation such as finding all pictures of giraffes, we could have an attribute called label_name that is text based or we could create a seperate table for the labels especially if we ahve a table that maps numeric labels to descriptive names then we can reference label_id from a table we create called labels that contains label_id and label_name in the table we created in no.2 this way we will be able to join the two tables together to write a query to find all pictures of a giraffe or better still we could create multiple descriptors per image, that is we have seperate tag tables and a junction table to handle many-to-many relationships.

**Steps taken to repeat Task 2**

-   Python Script(ms3_mnist_task3) Functionality:
    -   Connect to the PostgreSQL database using credentials from the .env file.
    -   Create a new database, ms3_mnist.
    -   Create a table, mnist_data
    -   Load the MNIST dataset using Keras.
    -   Insert the first 1,000 MNIST samples into the mnist_data table.
    -   Fetch some of the inserted samples and display them using Matplotlib.

-   Started the PostgreSQL Container using `docker run --name ms3-postgres -e POSTGRES_PASSWORD=your_password -p 5437:5432 postgres`
-   Ran the Python Script

---

## Task 4: Multi-Docker Container Application

**Steps Taken**
-   Folder structure as follows:
    -   python_service folder: Contains the Python app (app.py), docker-compose.yml which onfigures both the PostgreSQL and Python services, Dockerfile, and .env file (milestone_3.env).
    -   model folder: Stores the pre-trained model (model.keras) which was trained with train_model.py script in src folder.
    
-   Docker Compose Configuration:
    -   Configured PostgreSQL as a service with:
        -   A volume (postgres_data) to persist database data.
        -   Environment variables (POSTGRES_USER, POSTGRES_PASSWORD, and POSTGRES_DB) to configure the database.
        -   A healthcheck to ensure the database is ready before starting the Python service.
    -   Configured the Python service to:
        -   Use a custom Dockerfile (python_service/Dockerfile).
        -   Mount the model folder as a volume so the container can access the pre-trained model.

-   Create the Python Service
    -   App Functionality:
        -   Connect to the PostgreSQL database and check if the required tables exist.
        -   Create the input_data and predictions tables if they do not already exist.
        -   Load the pre-trained neural network model (model.keras) using Keras.
        -   Load a sample image from the MNIST dataset.
        -   Insert the sample image into the input_data table.
        -   Predict the label for the inserted image using the loaded model.
        -   Save the prediction result in the predictions table with a reference to the input image via a foreign key.

-   Configured a Dockerfile for the Python service to:
    -   Install Python dependencies from requirements.txt.
    -   Copy the app.py file into the container.
    -   Set up the container to run python app.py.

-    Run the Milestone
    -   Ran docker-compose up --build from the python_service folder to start both services.


## Challenges
**Challenges Faced in ms3_mnist (Task 3)**
1. Environment File Confusion

    Problem: Confusion about the .env file placement and usage. At one point, the .env file for ms3_mnist was not being detected when running the script.
    Solution: Ensured that ms3_mnist.env was in the root folder and adjusted the load_dotenv path in the script.

2. Database Authentication Error

    Problem: The script failed to connect to the PostgreSQL database due to incorrect password or authentication errors.
    Solution: Double-checked the database password in the .env file and ensured the DB_HOST was set correctly to localhost.

**Challenges Faced in milestone_3 (Task 4)**
1. Docker Compose File Placement

    Problem: Initially, the docker-compose.yml file was placed outside the python_service folder, leading to confusion about which .env file was being used.
    Solution: Moved the docker-compose.yml file to the python_service folder to ensure the correct .env file (milestone_3.env) was used.

2. PostgreSQL Password Configuration

    Problem: PostgreSQL required a password, but the container logs showed an error because it was not correctly passed.
    Solution: Copied the output and pasted it on Google, viewed stackoverflow answers, read webpages still to no avail. However, we found a solution to the problem on a [Github issue](https://github.com/forem/forem/issues/6563) written by henrynguyen6677, we implemented this and our problem was solved like magic.

3.  Container Dependency:

    Problem: The Python service attempted to start before PostgreSQL was ready.
    Solution: Fixed by adding a healthcheck and depends_on configuration in Docker Compose.

4. Several path related problems

**General Challenges**
1. Understanding Docker and Docker Compose

    Problem: Initial difficulty in understanding Docker Compose, volumes, and how containers interact.
    Solution: Gradually built the understanding by running individual Docker commands (docker run) and later transitioning to docker-compose.

2. Handling Errors Gracefully

    Problem: Various errors (e.g., connection failures, missing environment variables, cursor issues) needed to be handled effectively.
    Solution: Added robust error handling and logging to provide clear feedback when things went wrong.

---

## References
1. [GeeksforGeeks on Blob](https://www.geeksforgeeks.org/blob-full-form/)


