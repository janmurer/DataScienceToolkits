# Group 2: Data Science Toolkits and Architectures

## About This Repository
Welcome to our GitHub repository. This repository serves as a central hub for sharing code, resources, and documentation related to several milestones that are assigned to us. 


## Repository Structure

The repository is organized as follows:
```plaintext
├── app/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── database_creation.py
│   ├── database_insert.py
|   ├── database_mnist_preparation.py
|   ├── image_prep.py
│   ├── jokes_functions.py
│   ├── model.py
│   ├── one_hot_decoder.py
│   ├── predictor.py
│   └── trainer.py
│
├── database/
│   ├── Dockerfile
|   ├── main.py
│   └── pgadmin-servers.json
│
├── model/
│   ├── Dockerfile
│   └── main.py
│
├── reports/
|   ├── img/
|   |    └── wandb_workspace.png
│   ├── report_1.md
│   ├── report_2.md
|   ├── report_3.md
|   ├── report_4.md
│   └── report_5.md
│
├── src/
│   ├── mnist_covnet.py
│   ├── ms3_mnist_task3.py
│   └── train_model.py
│
├── webservice/
|   ├── templates/
|   |   ├── index.html
|   |   └── result.html
│   ├── Dockerfile
|   ├── main.py
│   └── wait_for_model.sh
|
├── .dockerignore
├── .gitignore
├── compose.yaml
├── README.md
├── requirements.in
└── requirements.txt
```
    
* app/: Contains all modules for our application to work
* database/: Contains a docker file and a scrpit that handles the database operations. (Though it accesses functions from app/)
* model/: Contains a dockerfile and a scrpit that handles the process of training, saving, loading, and evaluating a machine learning model. 
* reports/: Contains markdown files documenting the process of our work on milestones, logs findings and challenges we faced completing the milestones
* src/: Contains the foundational code for our application(mnist_covnet.py) and other scripts.
* webservice/: Sets up the foundation of our web-based application designed to interact with users through a web interface.
* .dockerignore: Specifies files or directories to exclude when building the Docker image.
* .gitignore: Lists files or folders that should not be tracked by Git.
* compose.yaml: A multi-container environment for our machine learning web service, integrating model management, a PostgreSQL database, a Flask API, and PgAdmin via Docker Compose.
* requirements.txt: List of packages and dependencies to run the application

## Getting Started

To contribute to this repository:

Clone the repository to your local machine

`git clone https://github.com/janmurer/DataScienceToolkits`


## Contribution Guidelines

Please follow these guidelines:

1. Branching: Create a new branch for each milestone or feature you work on.
2. Commits: Write clear and descriptive commit messages
3. Pull Requests: Submit a pull request when ready to merge, the pull request must be reviewed and approved by at least one team member.
4. main: The main branch exclusively contains running code. It is not possible to directly merge to the main branch. Merge your work to the dev branch first and make sure the code works, before creating a PR to the main branch.


## Milestone 1

### Overview

The goal of milestone_1 is to checkout code (https://github.com/keras-team/keras-io/blob/master/examples/vision/mnist_convnet.py) and make it run on a local machine. Furthermore, Git should be used to version control the code. 

### Setup

1. **Install Visual Studio** 

    If not installed kindly use the link below:

    https://code.visualstudio.com/Download

2. **Installing Python**

    Install by running the following command in your terminal (macoOS/Linux only - install Homebrew first, if not already installed). We recommend to install Python 3.12.4.

    `brew install python`

3. **Create a virtual environemnt**

    `python -m venv .venv`

4. **Clone the repository using**

    `git clone https://github.com/janmurer/DataScienceToolkits.git`

5. **Open the respective directory in Visual Studio** 

    This is the directory or folder where you cloned the repository into in File explorer. 
 
6. **Activate the virtual environment**

    Run the following command in your terminal

    `source venv/bin/activate`

8. **Install the required Libraries**
    
     `pip install -r requirements.txt`

7. **Run the code**

    `python mnist_convnet.py`


## Milestone 2

### Overview

In this milestone we should refract the code (mnist.covnet.py) from the previous milestone into several modules. Furthermore, the application should be "dockerized" to address the problem "It works on my machine ¯\\\_(ツ)\_/¯".

### Setup

Assuming you completed all setup-steps from Milestone 1:

1. **Install Docker** 

    If not installed kindly use the link below:

    https://docs.docker.com/get-started/get-docker/

    Make sure the application is running in order to proceed with the next steps

2. **Clone the repository using**

    `git clone https://github.com/janmurer/DataScienceToolkits.git`

3. **Open the respective directory in Visual Studio** 

    This is the directory or folder where you cloned the repository into in File explorer. 
 
4. **Build the Docker image**
    
    `docker build -t mnist_app .`

5. **Run the Docker image**

    `docker run mnist_app`



## Milestone 3

### Overview

The goal of this milestone is to introduce a relational database that can store the input and output of our Neural Network. The database should be connected to our main python application through a Docker Network, which allows us to interact with it through it's host name (IP Address) and port.

### Setup


1. **Install Docker Compose**

    If not installed kindly use the link below:

    https://docs.docker.com/compose/gettingstarted/

    However, if you are using Docker Desktop, and have completed all setups from the other Milestones above, kindly skip this step.

2. **Clone the repository and open the respective directory in Visual Studio as stated in the Milestones above.**

3. **Run Multi Docker Container Application**
    
    Run `docker-compose up`

4. **Check the tables using PgAdmin**

    If you would like to access the tables, you can access your localhost on port 5050 via your browser. This should redirect you to the login page. Here you can enter username 'admin@admin.com' and password 'admin'. This will the open the connection and you will be prompted to enter the database password, which is 'postgres'. Now you can use the interface to access the database.


## Milestone 4

### Overview

In this milestone we should create a wandb-account to essentially log and visualize the performance of our MNIST-model. 

### Setup

Assuming you completed all setup-steps from Milestone 1-3:


1. **Clone the repository using**

    `git clone https://github.com/janmurer/DataScienceToolkits.git`

2. **Open the respective directory in Virtual Studio** 

    This is the directory or folder where you cloned the repository into in File explorer. 

3. **Store your wandb key in an .env file at the root of your directory**

    `WANDB_TOKEN=YourActualWANDBAPIKey`

    Make sure to never share/publish your token. Otherwhise bad things will happen. 

4. **Build the docker image** 
    
    `docker build -f wandb/Dockerfile -t wandb_mnist .`

5. **Change the directory to the root folder of this project**

6. **Run the docker image in interactive mode with the .env variable**

    `docker run -it --env-file .env wandb_mnist /bin/bash`

7. **Once in interactive mode, install the text editor nano**

    `apt-get update && apt-get install -y nano`

8. **Open the corresponding script for hyperparameter tuning**
    
    `nano /wandb/main_wandb.py`.

9. **Modify hyperparameter as desired**

10. **Save the changes and exit the file (Ctrl + O, Enter, Ctrl - X)**

11. **Run the script**

    `python /wandb/main_wandb.py`
    
12. **Modify hyperparameter as often as desired**

13. **Log into your wandb.ai account and see how your models compared**

14. **See and track the performance of your model on wandb.ai**


## Milestone 5

### Overview

In this milestone we integrated our previous work into a web application. We created a new script called api.py that accepts a POST Request and returns a prediction to the client. 

### Setup

Assuming you completed all setup-steps from Milestone 1-4:

1. **Clone the repository using**

    `git clone https://github.com/janmurer/DataScienceToolkits.git`

2. **Open the respective directory in Virtual Studio** 

    This is the directory or folder where you cloned the repository into in File explorer. 

3. **Build the Docker-Container**

    `docker-compose up`

    *Note:*

    If you run the command for the first time, building will take a few minutes. This is because the model needs to be trained first. Also all neccessary databases need to be initialized. 
    
    If you run the command `docker compose up` again, and the volume where the trained model is stored still exists, you can start using the webservice right away. 

4. **Interact with the Webservice**

    - To interact with the webservice you can either use the Webinterface that is accessible at port 5051 and upload an image from your machine to get a number predicted. E.g., If you are hosting the service on your local machine, use your web browser of choice and visit http://localhost:5051/ (or the according equivalent for your operating system).

    - You can also interact with the webservice using your terminal. Use the command
    `curl -X POST http://localhost:5051/predict \
        -H "Content-Type: multipart/form-data" \
        -F "image=@/path/to/your/image.png" \
        -H "Accept: application/json"`
    
    This will return the prediction in json-structure. Only send .png-images and .jpeg-images, as these are the only filetypes accepted by the service. 

5. **Database**

    If you for whatever reason want to check the database, use port 5050. This will take you to pgAdmin, where you first have to sign in. You will be prompted to enter the database password, which is "postgres". You will find a database called predictions, which contains two tables. The table "input_data" stores the latest provided image, while the table "predictions" stores the latest corresponding prediction.


## Contributions
This was carried out by Murer Jan, Ugowe Jessica and Poschenrieder Frederik. Feel free to send a pull request or create an issue if you feel there was something we could have done better. We would greatly appreciate learning from you. **T for Thanks.**
