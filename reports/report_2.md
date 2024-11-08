# Report "Data Science Toolkits and Architectures"
#### Jan Murer, Frederik Poschenrieder, Jessica Ugowe 


# Milestone_2

## Task 1

Remember: Clean Git repositories are important. This means it is necessary to make sure that you do not commit files to the Git repository that should not be version controlled and therefore added to the Git commit history. Git only deals with textual files that can be easily read line by line. In simple terms, do not add
data such as pictures, video, music and other "blobs" (such as trained and saved neural network models, to be extremely specific). Git is not a (large, non textual) file sharing tool!
In case you haven’t done it yet, in this task we ask you to write an appropriate ".gitignore" file. A git ignore file prevents you from accidentally adding files to the git staging area by filtering out explicit files, file types and whole folders inside the git repository. Add this file to the root directory of your git project (where your .git folder is). Explain in your report, why you added a certain "ignore" to the file. Note that you will probably continually add more and more entries as you work on the following tasks.
It is important that you version-control the ".gitignore". Do not share it with each other by other means than Git (for example not per E-mail or Slack!). You need to find an appropriate branching strategy for your team to share additions to and deletions from the ".gitignore", while you work on separate feature branches.
Add to the report how you shared changes in the ".gitignore", while you were working on different feature branches (essentially without having to constantly do pull requests into the main/master branch for simple changes to the ".gitignore"). Or, how would you do it?

## Task 2

Add the answers to the following questions to your report:
- What is a Hash function? What are some of the use cases?
- What is a Python module, package and script? How do they differ from one another? - How would you explain a Docker container and volume to a child?
- What is your preference concerning the use of Python virtualenv and Docker? When would you use one or the other?
- What is the Docker build context?
- How can you assess the quality of a python package on PyPI?

## Task 3

Make sure your code has the following functionality (extend if necessary):
- Can load data
- Can train (fit) a neural network on the data
- Can save a fitted model to a ".h5" file (or saved model type for newer Tensorflow 2.0 versions) - Can load a ".h5" file, using Keras (or saved model type for newer Tensorflow 2.0 versions)
- Can perform predictions using a "fitted" model, using Keras

## Task 4

Your code bases are badly structured, as they are essentially a script, which is read top down. This creates Python files that are large and not maintainable. It is good practice to create modules that contain code snippets which "logically" belong together. The modules contain python functions that are imported by other modules and scripts, where they are executed.
- Split your code base into modules (for example the creation of the neural network might be in a "neuralnet_architecture.py" module). Explain the reasoning behind your modularization. Why did you choose to structure the code like this? Please use Python functions that can be imported from your modules.
- There has to be one "main.py" script that calls the code/functions in all the other modules. This is the script that you run with the "python" command.
- The modules usually contain imports (from other modules / packages) and functions (for example "def create_neuralnet(): ...")
- Ensure PEP8 conformity


## Task 5

Create a pip "requirements file" for your code base and explain how you make it work within a virtualenv (step by step).

## Task 6

"Dockerize" your code:
- Install Docker on your machines
- Create a Dockerfile that installs all necessary dependencies and is capable of running Tensorflow/Keras in CPU mode (GPU mode is not necessary).