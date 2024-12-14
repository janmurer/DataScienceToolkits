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
│   ├── jokes_functions.py
│   ├── model.py
│   ├── one_hot_decoder.py
│   ├── predictor.py
│   └── trainer.py
│
├── database/
│   ├── Dockerfile
│   └── main.py
│
├── jokes/
│   ├── Dockerfile
│   └── main.py
│
├── model/
│   └── model.keras
│
├── reports/
│   ├── report_1.md
│   ├── report_2.md
│   └── report_3.md
│
├── src/
│   ├── mnist_covnet.py
│   ├── ms3_mnist_task3.py
│   └── train_model.py
│
├── .dockerignore
├── .gitignore
├── compose.yaml
├── docker-compose.yml
├── Dockerfile
├── main.py
├── pgadmin-servers.json
├── README.md
├── requirements.in
├── requirements.txt
└── wait_for_model.sh
```
    
* app/: Contains all modules for our application to work
* database/: Contains a docker file and a scrpit that handles the database operations. (Though it accesses functions from app/)
* jokes/: Contains a dockerfile and a scrpit that handles the jokes database of task 2. Itz is not executed by default and has to be manually accessed by removing uncommenting the relevant chunks in the docker-compose file.
* reports/: Contains markdown files documenting the process of our work on milestones and logs findings and challenges we faced completing the milestones
* src/: Contains the foundational code for our application(mnist_covnet.py) and other scripts
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

1. **Install Virtual Studio** 

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


<<<<<<< HEAD
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

=======
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

4. **Build the Docker image**
    
    `docker build -f wandb/Dockerfile -t mnist_wandb .`

5. **Run the Docker container**

    `docker run --env-file .env mnist_wandb`

6. **See and track the performance of your model on wandb.ai**
>>>>>>> c82538e (update report_4.md, update README.md)

## Contributions
This was carried out by Murer Jan, Ugowe Jessica and Poschenrieder Frederik. Feel free to send a pull request or create an issue if you feel there was something we could have done better. We would greatly appreciate learning from you. **T for Thanks.**


















