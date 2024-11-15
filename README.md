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
├── reports/
│   ├── report_1.md
│   └── report_2.md
├── src/
│   └── mnist_covnet.py
├── .dockerignore
├── .gitignore
├── Dockerfile
├── README.md
├── main.py
└── requirements.txt
```
    
* app/: Contains all modules for our application to work
* reports/: Contains markdown files documenting the process of our work on milestones and logs findings and challenges we faced completing the milestones
* src/: Contains the foundational code for our application
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

5. **Open the respective directory in Virtual Studio** 

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

3. **Open the respective directory in Virtual Studio** 

    This is the directory or folder where you cloned the repository into in File explorer. 
 
4. **Build the Docker image**
    
    `docker buildx build -t mnist_app`

5. **Run the Docker image**

    `docker run mnist_app`

## Contributions
This was carried out by Murer Jan, Ugowe Jessica and Poschenrieder Frederik. Feel free to send a pull request or create an issue if you feel there was something we could have done better. We would greatly appreciate learning from you. **T for Thanks.**