# Report "Data Science Toolkits and Architectures"
#### Jan Murer, Frederik Poschenrieder, Jessica Ugowe 


# Milestone_2

## Task 1

Remember: Clean Git repositories are important. This means it is necessary to make sure that you do not commit files to the Git repository that should not be version controlled and therefore added to the Git commit history. Git only deals with textual files that can be easily read line by line. In simple terms, do not add
data such as pictures, video, music and other "blobs" (such as trained and saved neural network models, to be extremely specific). Git is not a (large, non textual) file sharing tool!
In case you haven’t done it yet, in this task we ask you to write an appropriate ".gitignore" file. A git ignore file prevents you from accidentally adding files to the git staging area by filtering out explicit files, file types and whole folders inside the git repository. Add this file to the root directory of your git project (where your .git folder is). Explain in your report, why you added a certain "ignore" to the file. Note that you will probably continually add more and more entries as you work on the following tasks.
It is important that you version-control the ".gitignore". Do not share it with each other by other means than Git (for example not per E-mail or Slack!). You need to find an appropriate branching strategy for your team to share additions to and deletions from the ".gitignore", while you work on separate feature branches.
Add to the report how you shared changes in the ".gitignore", while you were working on different feature branches (essentially without having to constantly do pull requests into the main/master branch for simple changes to the ".gitignore"). Or, how would you do it?

We restructured our GitHub repository in order to work the "git"-way. New feature branches should be derived from the dev branch which should always contain the most up-to-date version of our code. 

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

DONE

## Task 4

Your code bases are badly structured, as they are essentially a script, which is read top down. This creates Python files that are large and not maintainable. It is good practice to create modules that contain code snippets which "logically" belong together. The modules contain python functions that are imported by other modules and scripts, where they are executed.
- Split your code base into modules (for example the creation of the neural network might be in a "neuralnet_architecture.py" module). Explain the reasoning behind your modularization. Why did you choose to structure the code like this? Please use Python functions that can be imported from your modules.
- There has to be one "main.py" script that calls the code/functions in all the other modules. This is the script that you run with the "python" command.
- The modules usually contain imports (from other modules / packages) and functions (for example "def create_neuralnet(): ...")
- Ensure PEP8 conformity

We refracted the original code into several modules. __init__.py imports/evokes the neccessary functions from all the modules. The script main.py "glues" the application together. PEP8 conformity was ensured using the packages isort, black and flake8.


## Task 5

Create a pip "requirements file" for your code base and explain how you make it work within a virtualenv (step by step).

We printed the required packages and dependencies for our application by running the command `pip freeze`
in the terminal (the virtual environement must be active). This prints all required packages and the respective versions. 

The terminal output can be copied and pasted in a file named requirements.in. From there on we used a package called pip-tools and used the command `pip-compile --generate-hashes requirements.in` to generate a requirements.txt including the respecting hashes. 

For some reason the tool was not able to generate hashes for the package setuptools. We had to manually add the hash for this packages by checking the package on PyPI (https://pypi.org/project/pip/) and download it from there. Then we directly calulated the hash using the tool shasum with the command `shasum -a 256 setuptools-75.2.0.tar.gz`. We manually added the terminal output to our requirements.txt.


## Task 6

"Dockerize" your code:
- Install Docker on your machines
- Create a Dockerfile that installs all necessary dependencies and is capable of running Tensorflow/Keras in CPU mode (GPU mode is not necessary).

To build and run the docker image, please refer to the Setup section in the README.md file at the root of this GitHub repository.
# Milestone_2 

##What is a Hash Function?
First of all what is hashing? Hashising is the process of transforming a given key or a string of characters into another value. 
Hash functions are important concepts in computer science and are duseful in various applications such as Data storage , retrieval and cryptography. They are the central part of the hashing process. The hash function takes the input data and applies a series of mathemathical operations to it resulting in a fixed length string of characters. They generate new values according to a mathematical yhasing algorithm known as the hash value or hash[1]. The hash function ensures that even a small change in the input data produces a significantly different hash value[1]. Hash  functions are mainly used in hash tables , which are essential for efficient data management.  Hash table stores key and value pairs  in a list that is accessible through its index and because the number of keys and value pairs is unlimited, the hash function maps the keys to the table size and the hash value then becomes the index for a specific element. These values are the hash outputs and rae referred to as hash value. They have a set length and it can be challenging to determine the length of the original input because ouputs have a set length , which contributes to the overall boost in security. in a list that is accessible through its index and because the number of keys and value pairs is unlimited, the hash function maps the keys to the table size and the hash value then becomes the index for a specific element.

 ###Types of Hash Function
1.	Division Method: This involves didviding the key by a prime number and using the remainder as the hash value. It is necessary to choose the prime number wisely to avoid poor distribution.

2.	Multiplication Method: A constant AA(0 < A < 1) is used to multiply the key. The fractional part of the product is then multiplied by a prime number to get the hash value. It is less sensitive to the cdhoice of mm(prime number) but more complex than the division method
3.	Mid-square Method: This involves squaring the key and the middle digits of the result are taken as the hash value.
4.	Folding Method: This method involves dividing the key into equal parts, summing the parts and then taking the modulo with respect to the mm
5.	Cryptographic Hash Functions: These functions are designed to be secure and are used in cryptography. Examples include MD5 (Message Digest 5), bcrypt, Argon2, SHA-1(Secure Hash Algorithm 1) and SHA-256 which we used for this milestone.
6.	Universal Hashing: This uses a family of hash functions to minimize the chance of collision(two different inputs that produce the same hash value) for any given set of inputs.
7.	Perfect Hashing: This aims to create a collision-free hash function for a static set of keys. It guarantees that no two keys will hash to the same value

##Uses of  Hash Function
1.	Data Integrity: Hash functions ensures that by generating a hash value for an amount of data, such as a file or message, a user can later compare it with the hash value of the received data to verify if any changes or corruption occurred during transmission.

2.	Efficient data retrieval: Hash functions enable efficient data retrieval in hash tables by mapping input data (keys) to fixed-size hash codes. In hash tables, data is stored as key-value pairs. The key is processed through the hash function to determine the storage location of its associated value.
Key operations include:
insert (key, value): Hash the key to store the value.
get (key): Hash the key to retrieve the value.
delete (key): Hash the key to remove the value.

3.	Digital signatures: Hash functions are essential for securing digital signatures used in message authentication. In this process a hash function transforms the digital signature before both the hashed value -- known as a message digest -- and the signature are sent in separate transmissions to the receiver. Upon receipt, the same hash function derives the message digest from the signature, which is then compared with the transmitted message digest to ensure both are the same. In a one-way hashing operation, the hash function indexes the original value or key and enables access to data associated with a specific value or key that's retrieved.

4.	Password storage: Hash functions are applied in secure password storage by transforming plain-text passwords into hash values before storing them in a database. When a user creates a password, the system hashes it using a cryptographic hash function and saves the resulting hash. When the user logs in, the input password is hashed again, and the new hash is compared to the stored hash. If they match, access is granted. This ensures that even if the hash values are compromised, it remains computationally infeasible to reverse-engineer the original passwords due to the one-way nature of hash functions. Additionally, techniques like salting (adding random data to the password before hashing) are used to protect against precomputed attacks like rainbow tables.


5.	Fast searching: Hash functions are applied to organize data into "buckets" for easy searching and retrieval. By converting input data (keys) into hash codes, these functions determine the specific bucket where the corresponding value is stored. This minimizes the search scope and speeds up data access.
This approach is widely used in databases and search engines, where rapid search results are critical. 

6.	Cryptographic application: Cryptographic hash functions are used to generate digital signatures, authenticate messages and ensure data integrity and authenticity. Hashing algorithms such as Secure Hash Algorithm 2, or SH-2, are widely used in cryptographic applications.

7.	Space efficiency: Hash functions ensure efficient use of storage space because hash values are typically shorter than the original data making them more compact and easier to store.

8.	Blockchain technology: Hash function is widely used in blockchain especially in cryptocurrencies such as Bitcoin. Blockchain is a digital ledger that stores transactional data, and each new record is called a block. Since all participants in a blockchain have access to identical data, ensuring the integrity of previous transactions is critical. This is when hash functions comes into play, as it ensures the integrity and immutability of data stored in blocks.

9.	Database management: Hash functions help to search for data records easily. Distributed systems like Cassandra and MongoDB use hash functions for consistent hashing. 

10.	Deduplication: In storage systems, hash functions are used to identify duplicate files or data blocks by comparing their hashes e.g. Cloud storage systems use hash-based deduplication to save space.

## What is a Python Package
Python Packages are a way to organize and structure Python code into reusable components. A Python package usually consists of several modules.Packages allow for a hierarchical structuring of the module namespace using dot notation. In the same way that modules help avoid collisions between global variable names, packages help avoid collisions between module names.



## What is a Python Module
In Python, Modules are simply files with the “.py” extension containing Python code that can be imported inside another Python Modules Operations Program. It defines variables, functions, and classesIn simple terms, we can consider a module to be the same as a code library or a file that contains a set of functions that you want to include in your application. 

## What is a Python Script
A Python script is a file that generally contains a short self-contained set of instructions, i.e., lines of code, that perform a specific task. They are called scripts because they are read and interpreted by Python line-by-line in order from the first line to the last.

## Difference between Python Module, Package and Script
The major fifference would be that while modules and packages are intended for reuse and organization, scripts are primarily meant to be run as independent programs.

## How to explain Docker container and volume to a child
### Docker container: 
Imagine you have a magic lunchbox. This lunchbox can hold everything you need to eat your lunch: your sandwich, juice, and snacks. But here’s the cool part: this lunchbox keeps all your food separate from everyone else's, no matter where you take it. A Docker container is like that magic lunchbox, but for computer programs. It carries everything a program needs to work (like files and tools) and keeps it separate from other programs on your computer. So, if one lunchbox spills, the others are still safe!

### Docker Volume: 
Now imagine that you have extra snacks that don't fit in the lunchbox or snacks you want to keep for later, like cookies or chips. Instead of carrying them in the lunchbox, you store them in a special snack cabinet at home.Now, even if your lunchbox gets lost, thrown away, or replaced with a new one, the snacks in your cabinet are still safe  and can be added to a new lunchbox anytime you want. In the world of computers, a Docker volume is like that snack cabinet. It’s a special place to store important data that your container (the lunchbox) might need, and even if the container disappears or changes, the data in the volume remains safe and accessible.

## What is your Preference concerning the use of Python virtualenv and Docker? When would you use one?


## What is Docker build context?
The Docker build context is the set of files and directories that are accessible to the docker build command when creating a Docker image. When you issue a docker build command, Docker sends the build context (a snapshot of the specified directory and its contents) to the Docker daemon, which then uses it to execute the instructions in the Dockerfile. The positional argument that you pass to the build command specifies the context that you want to use for the build.


## How can you access the quality of a python package on PYPI?










References
https://www.techtarget.com/searchdatamanagement/definition/hashing
