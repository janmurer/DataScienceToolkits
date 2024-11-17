# Report "Data Science Toolkits and Architectures"
#### Jan Murer, Frederik Poschenrieder, Jessica Ugowe 


# Milestone_2

## Task 1: Repository and Git Management

**Steps Taken**  
- Created a `.gitignore` file at the root directory of the repository to exclude unnecessary files.
- Examples of ignored files include:
  - Temporary files (e.g `*.log`)
  - System-specific files (e.g `.DS_Store`)
- The `.gitignore` is version-controlled to ensure team-wide consistency.
  
**Branching Strategy**  
- Implemented a feature branching model:
  - Changes to `.gitignore` are made in feature branches derived from the `dev` branch.
  - Updates are shared among team members using pull requests to `dev`, avoiding conflicts in the `main` branch.

---

## Task 2: Conceptual Understanding

### Key Questions Answered

**What is a Hash Function?**
Hash functions are important concepts in computer science and are useful in various applications such as Data storage , retrieval and cryptography. They are the central part of the hashing process. The hash function takes the input data and applies a series of mathemathical operations to it resulting in a fixed length string of characters. They generate new values according to a mathematical hashing algorithm known as the hash value or hash[1]. The hash function ensures that even a small change in the input data produces a significantly different hash value[1]. Hash  functions are mainly used in hash tables that store key and value pairs  in a list that is accessible through its index and because the number of keys and value pairs is unlimited, the hash function maps the keys to the table size and the hash value then becomes the index for a specific element. These values are the hash outputs and are referred to as hash value. They have a set length and it can be challenging to determine the length of the original input because ouputs have a set length, which contributes to the overall boost in security.

**Types of Hash Functions**

-	Division Method: This involves didviding the key by a prime number and using the remainder as the hash value. It is necessary to choose the prime number wisely to avoid poor distribution[2].

-	Multiplication Method: A constant AA(0 < A < 1) is used to multiply the key. The fractional part of the product is then multiplied by a prime number to get the hash value. It is less sensitive to the choice of mm(prime number) but more complex than the division method[2].

-	Mid-square Method: This involves squaring the key and the middle digits of the result are taken as the hash value.

-	Folding Method: This method involves dividing the key into equal parts, summing the parts and then taking the modulo with respect to the mm[2].

-	Cryptographic Hash Functions: These functions are designed to be secure and are used in cryptography. Examples include MD5 (Message Digest 5), bcrypt, Argon2, SHA-1(Secure Hash Algorithm 1) and SHA-256 which we used for this milestone[2].

-	Universal Hashing: This uses a family of hash functions to minimize the chance of collision(two different inputs that produce the same hash value) for any given set of inputs[2].

-	Perfect Hashing: This aims to create a collision-free hash function for a static set of keys. It guarantees that no two keys will hash to the same value[2].

**Uses of  Hash Function**
-	Data Integrity: Hash functions ensures that by generating a hash value for an amount of data, such as a file or message, a user can later compare it with the hash value of the received data to verify if any changes or corruption occurred during transmission.

-	Efficient data retrieval: Hash functions enable efficient data retrieval in hash tables by mapping input data (keys) to fixed-size hash codes. In hash tables, data is stored as key-value pairs[1]. The key is processed through the hash function to determine the storage location of its associated value.
Key operations include:
    - insert (key, value): Hash the key to store the value.
    - get (key): Hash the key to retrieve the value.
    - delete (key): Hash the key to remove the value.

-	Digital signatures: Hash functions are essential for securing digital signatures used in message authentication. In this process a hash function transforms the digital signature before both the hashed value known as a message digest and the signature are sent in separate transmissions to the receiver. Upon receipt, the same hash function derives the message digest from the signature, which is then compared with the transmitted message digest to ensure both are the same. In a one-way hashing operation, the hash function indexes the original value or key and enables access to data associated with a specific value or key that's retrieved[1].

-	Password storage: Hash functions are applied in secure password storage by transforming plain-text passwords into hash values before storing them in a database. When a user creates a password, the system hashes it using a cryptographic hash function and saves the resulting hash. When the user logs in, the input password is hashed again, and the new hash is compared to the stored hash. If they match, access is granted. This ensures that even if the hash values are compromised, it remains computationally infeasible to reverse-engineer the original passwords due to the one-way nature of hash functions. Additionally, techniques like salting (adding random data to the password before hashing) are used to protect against precomputed attacks like rainbow tables[1].


-	Fast searching: Hash functions are applied to organize data into "buckets" for easy searching and retrieval. By converting input data (keys) into hash codes, these functions determine the specific bucket where the corresponding value is stored. This minimizes the search scope and speeds up data access.
This approach is widely used in databases and search engines, where rapid search results are critical. 

-	Cryptographic application: Cryptographic hash functions are used to generate digital signatures, authenticate messages and ensure data integrity and authenticity. Hashing algorithms such as Secure Hash Algorithm 2, or SH-2, are widely used in cryptographic applications[1].

-	Space efficiency: Hash functions ensure efficient use of storage space because hash values are typically shorter than the original data making them more compact and easier to store.

-	Blockchain technology: Hash function is widely used in blockchain especially in cryptocurrencies such as Bitcoin. Blockchain is a digital ledger that stores transactional data, and each new record is called a block. Since all participants in a blockchain have access to identical data, ensuring the integrity of previous transactions is critical. This is when hash functions comes into play, as it ensures the integrity and immutability of data stored in blocks.

-	Database management: Hash functions help to search for data records easily. Distributed systems like Cassandra and MongoDB use hash functions for consistent hashing. 

-	Deduplication: In storage systems, hash functions are used to identify duplicate files or data blocks by comparing their hashes e.g. Cloud storage systems use hash-based deduplication to save space.

**What is a Python Package?**
Python Packages are a way to organize and structure Python code into reusable components. A Python package typically consists of an `__init__.py` file (which can be empty or include initialization code) and several modules (individual .py files). The __init__.py file signals to Python that the directory should be treated as a package. Packages enable hierarchical structuring of the module namespace using dot notation (e.g., package_name.module_name), which helps avoid name collisions between modules in different packages, just as modules prevent collisions between global variable names within a single program.

**What is a Python Module?**
In Python, Modules are simply files with the `.py` extension containing Python code that can be imported inside another Python Modules Operations Program. It defines variables, functions, and classesIn simple terms, we can consider a module to be the same as a code library or a file that contains a set of functions that you want to include in your application. 

**What is a Python Script?**
A Python script is a file that generally contains a short self-contained set of instructions, i.e., lines of code, that perform a specific task. They are called scripts because they are read and interpreted by Python line-by-line in order from the first line to the last.

**What is the difference between Python Module, Package and Script?**
The major fifference would be that while modules and packages are intended for reuse and organization, scripts are primarily meant to be run as independent programs.

**How would you explain Docker Container to a child?** 
Imagine you have a magic lunchbox. This lunchbox can hold everything you need to eat your lunch: your sandwich, juice, and snacks. But here’s the cool part: this lunchbox keeps all your food separate from everyone else's, no matter where you take it. A Docker container is like that magic lunchbox, but for computer programs. It carries everything a program needs to work (like files and tools) and keeps it separate from other programs on your computer. So, if one lunchbox spills, the others are still safe!

**How would you explain Docker Volume to a child?**
Now imagine that you have extra snacks that don't fit in the lunchbox or snacks you want to keep for later, like cookies or chips. Instead of carrying them in the lunchbox, you store them in a special snack cabinet at home.Now, even if your lunchbox gets lost, thrown away, or replaced with a new one, the snacks in your cabinet are still safe  and can be added to a new lunchbox anytime you want. In the world of computers, a Docker volume is like that snack cabinet. It’s a special place to store important data that your container (the lunchbox) might need, and even if the container disappears or changes, the data in the volume remains safe and accessible.

**What is your Preference concerning the use of Python virtualenv and Docker? When would you use one?**
Virtualenv and Docker both offer differnet levels of isolation. For simple aplications and local development, virtualenv will be preferred. However, to ship and run complex applications reliably, Docker would be preferred.

**What is Docker build context?**
The Docker build context is the set of files and directories that are accessible to the docker build command when creating a Docker image. When you issue a docker build command, Docker sends the build context (a snapshot of the specified directory and its contents) to the Docker daemon, which then uses it to execute the instructions in the Dockerfile. The positional argument that you pass to the build command specifies the context that you want to use for the build.


**How can you access the quality of a python package on PYPI?**
- Check the Package Popularity
    - Download Statistics: Use tools like pepy.tech to see the number of times the package has been downloaded. Higher download counts often indicate that the package is popular and widely used.
    - Star Ratings and Reviews: While PyPI itself doesn’t have a rating system, you can check if the package is hosted on GitHub or another repository where it may have stars or user feedback.

- Review the Package Details on PyPI
    - Version Number: Packages with higher version numbers (e.g., 1.x.x as opposed to 0.x.x) often indicate more mature and stable software.
    - Release Frequency: Check the release history to see how frequently the package is updated. Frequent updates can signify active maintenance, while a long gap might indicate an abandoned project.
    - Maintainers and Author Information: Look at who maintains the package. Packages maintained by well-known organizations or active developers may be more reliable.

- Examine the Documentation
    - Comprehensive Documentation: Check if the package has a well-documented README on PyPI or links to detailed documentation. Good documentation is a sign of quality and commitment from the developers.

- Analyze the Code Repository
    - Number of Contributors: A higher number of contributors can suggest a larger community behind the package, which may lead to better support and improvements.
    - Open Issues and Pull Requests: A large number of unresolved issues or stale pull requests may be a red flag for maintenance problems.
    - Commit History: Recent commits suggest that the project is actively maintained.

---

## Task 3. Functional Code Requirements

We added created a function that stores the model to a newly created folder called "models".
Initially we stored the file as h5 as outlined in the exercise, but this gave as a warning, saying h5 is a deprecated format. After we got the ok from the lecturers we changed the file format to the newer .keras format.

---

## Task 4: Code Modularization

We divided the original code into logically structured modules. __init__.py imports/evokes the neccessary functions from all the modules. The script main.py "glues" the application together. PEP8 conformity was ensured using the packages isort, black and flake8.

---

## Task 5: Creating a `requirements.txt` File

**Steps Taken**

We printed the required packages and dependencies for our application by running the command `pip freeze`
in the terminal (the virtual environement must be active). This prints all required packages and the respective versions. 

The terminal output can be copied and pasted in a file named requirements.in. From there on we used a package called pip-tools and used the command `pip-compile --generate-hashes requirements.in` to generate a requirements.txt including the respecting hashes. 

For some reason the tool was not able to generate hashes for the package setuptools. We had to manually add the hash for this packages by checking the package on PyPI (https://pypi.org/project/pip/) and download it from there. Then we directly calulated the hash using the tool shasum with the command `shasum -a 256 setuptools-75.2.0.tar.gz`. We manually added the terminal output to our requirements.txt.

---

## Task 6: Dockerization

**Steps Taken**
- Installed Docker on local machines.
- Created a Dockerfile.
- Built and ran the docker image.

To build and run the docker image, please refer to the Setup section in the `README.md` file at the root of this GitHub repository.

---

## References
1. [TechTarget on Hashing](https://www.techtarget.com/searchdatamanagement/definition/hashing)
2. [GeeksforGeeks on Hash function](https://www.geeksforgeeks.org/hash-functions-and-list-types-of-hash-functions/)