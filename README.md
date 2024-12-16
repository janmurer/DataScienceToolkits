# Group 2: Data Science Toolkits and Architectures

## About This Repository
Welcome to our GitHub repository. This repository serves as a central hub for sharing code, resources, and documentation related to several milestones that are assigned to us. 


## Repository Structure

The repository is organized as follows:
```plaintext
├── app/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── model.py
│   ├── predictor.py
│   └── trainer.py
|── model/
│   └── model.keras
|── python_service/
│   ├── app.py
│   ├── docker-compose.yml
│   ├── Dockerfile
│   └── milestone_3.env
├── reports/
│   ├── report_1.md
|   ├── report_2.md
│   └── report_3.md
├── src/
│   ├── mnist_covnet.py
|   ├── ms3_mnist_task3.py
|   └── train_model.py
├── .dockerignore
├── .gitignore
├── Dockerfile
├── README.md
├── main.py
├── ms3_mnist.env
└── requirements.txt
```
    
* app/: Contains all modules for our application to work
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


## Milestone 3

### Overview

The goal of this milestone is to introduce a relational database that can store the input and output of our Neural Network. The database should be connected to our main python application through a Docker Network, which allows us to interact with it through it's host name (IP Address) and port.

### Setup


1. **Install Docker Compose**

    If not installed kindly use the link below:

    https://docs.docker.com/compose/gettingstarted/

    However, if you are using Docker Desktop, and have completed all setups from the other Milestones above, kindly skip this step.

2. **Clone the repository and open the respective directory in Visual Studio as stated in the Milestones above.**

3. **Fetch and visualize samples from the database**

    Start the PostgreSQL Database `docker run --name ms3-postgres -e POSTGRES_PASSWORD=your_password -p 5437:5432 -d postgres`

    Create a file named **ms3_mnist.env** in the root directory and add it to .gitignore, it should look like the description below

        DB_HOST=localhost
        DB_PORT=5437
        DB_USER=postgres
        DB_PASSWORD=your_password
        DB_NAME=ms3_mnist
        your_password=your_password

    *Note that the everything after the **=** in ms3_mnist.env should be assigned something, so **your_password and DB_PASSWORD** should be assigned the same thing after the **=** sign* 

    Change directory `cd src`

    Run the Python Script `python ms3_mnist_task3.py`

    *If you successfully carried out the steps, you should now be able to see the image of a number on your machine. Congrats!*

    After the successful completion above, stop, remove the Container and verify no conflicting Containers are running using:
     
    `docker stop ms3-postgres`

    `docker rm ms3-postgres`

    `docker ps -a`

4. **Run Multi Docker Container Application**

    Create a file named **milestone_3.env** in the python_service directory and add it to .gitignore, it should look like the description below

        DB_HOST=postgres
        DB_PORT=5432
        DB_USER=postgres
        DB_PASSWORD=your_password
        DB_NAME=milestone_3

    Change directory using `cd python_service`
    
    Run `docker-compose up`

     *Kindly note that a successful run is one whose container logs exit with **code 0**, if this is your case, Congratulations once again. After the successful run, use PGADMIN to check whether there is a database in PostgreSQL called "milestone_3" and it contains two tables namely "input_data" and "predictions". Did you see the tables?*


## Contributions
This was carried out by Murer Jan, Ugowe Jessica and Poschenrieder Frederik. Feel free to send a pull request or create an issue if you feel there was something we could have done better. We would greatly appreciate learning from you. **T for Thanks.**




























