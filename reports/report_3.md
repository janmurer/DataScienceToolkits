# Report "Data Science Toolkits and Architectures"
#### Jan Murer, Frederik Poschenrieder, Jessica Ugowe 


# Milestone_3

## Task 1 - Understanding Docker Compose
Install docker-compose. And got through this:
https://docs.docker.com/compose/gettingstarted/
**Which services are being used for the application (described in the link above)? How do they relate to the host names in terms of computer networks?**

There are two services used. One called "web", which is the web app created in flask and one called "redis", that is a redis image from the docker hub.

**What ports are being used (within the application and in the docker-compose file)?**

The "web" service, internally listens to port 5000 in the container, while it is exposed externally the port 8000. For the "redis" service, the default port 6379 is used both internally and externally. 
Within the application, the "redis" service is then accessed via the 6379 port. 

**How does the host machine (e.g. your computer) communicate with the application inside the Docker container. Which ports are exposed from the application to the host machine?**

The host machine communicates with the Flask application in the web service via the exposed port 8000. When you access localhost on port 8000, the request is forwarded to port 5000 inside the web container, where the Flask application is running.

The Redis service does not have additional port mappings for the host machine in this configuration but is accessible to the web container via the Docker network on port 6379.

**What is localhost, why is it useful in the domain of web applications?**

localhost is your own computer used as the server, where the application is running. This allows you to develop applications locally, where you can easily test and develop withount needing an external server for your app to run on.


## Task 2 - First Steps with PostgreSQL

PostgreSQL is a widely used open source object-relational database system. It is generally a SQL database, while it has some NoSQL-like features. For instance it can handle json and xml files.



- Run a PostgreSQL Server (with the most current version) using a Docker image from the official
PostgreSQL Docker Hub page
- Make sure you expose the correct ports when running the Docker container (read the documentation on
Docker Hub)
- Find an appropriate Python package (Postgres adapter) that allows you to communicate with the
database server
- Write a little python script that:
1. Connects to the database server using "localhost:port". You will have to enter a username and
password too (again, read the docs)
2. Creates a database called "ms3_jokes"(very specific tip: Python packages that want to be PEP 249
compliant, assume that you always work in Database "Transactions". PostgreSQL does not make
such an assumption. Read more about Database Isolation Levels, if you are interested)
3. Creates a Table called "jokes". The table should have an attribute "ID" which is it's primary key
and another Attribute "JOKE" of character type "TEXT"
4. Inserts your favorite joke into that table
5. Selects your favorite joke (now in the database), and fetches it from the database
6. Prints your favorite joke. You should see your joke in its full glory.
- Download the PGADMIN Tool (https://www.pgadmin.org/download/). It also exists as a Docker Image :).
Connect to your running PostgreSQL Database. Can you see your database and table?
- If you stopped and deleted the Docker container running the database and restarted it. Would your
joke still be in the database? Why or why not?