# Report "Data Science Toolkits and Architectures"
#### Jan Murer, Frederik Poschenrieder, Jessica Ugowe 


# Milestone_5

## Task 2: Create a Flask Application

### Challenge 1: Ports

As already predicted in the lecture, we got confused by choosing the right ports to interact with our flask application. 

To test the predictive capabilities of our application we used the terminal command:

'curl -X POST http://localhost:5051/predict \
-H "Content-Type: multipart/form-data" \
-F "image=@test_img/image.png"'

Depending on the image that was sent, the response of the application should look as follows:

{
  "prediction": X
}

Milestone 5
Deadline: 17.1.2025 23:59
In the previous lecture you learned about REST APIs and Web Servers. This project aims to integrate the work of the previous lectures into a Web application. Currently, we have a “Back-end” that consists of code that can run a model and store information in a Database. Furthermore, we trained and evaluated (and tracked experiments) some models that might be candidates for our Handwritten-digit classifier service. We would like to expose this functionality to “the world”.
Identical to all previous projects, we expect a report in which you describe what you did. We are particularly interested in how you failed and what solutions you came up with. The report should not be longer than 4000 words (roughly 8 pages).
The following rules apply:
- The branching strategy is consistent and no direct pushes to the master/main branch
- All pull requests to master/main are reviewed by the other team member (add at least one comment to the review)
- All versions in the pip "requirements file" are pinned (they have a fixed version)
- No python packages are installed with superuser rights (sudo), or equivalent in other operating systems
- For each of the python package you add to the requirements file, include the SHA256 hash digest to a table in the report
- Use PEP8
- The pinning of versions also applies to Docker images. Don't use the "latest" tag. All reliable Images on Docker Hub come with specific
version tags.
- We only look at the last commit on your main/master branch before the deadline. Everything else does not exist for us. Make sure you merge your deliverables.
Task 1
Go through a Flask tutorial, for example this one:
https://www.digitalocean.com/community/tutorials/how-to-build-and-deploy-a-flask-application-using-docker-o n-ubuntu-18-04
Task 2
Create a Flask application that allows the following:
- Expose a REST endpoint (for example <base_url>/predict)
- This endpoint should accept a POST Request
- The body of the POST Request should contain an Image out of your dataset (MNIST)
- You can send an image to this REST endpoint using the requests library; example:
(https://stackoverflow.com/questions/60636701/how-to-send-post-request-with-base64-image)
- The Flask app should accept the image from this endpoint and decode it such that you get a numpy
array. Then provide the array to your neural network. Neural network prediction and image should be
saved in the database (as was done in Milestone 3).
- The Flask app should return the prediction to the client (calling the REST API)
In other words: use the requests Python library to send a POST request containing an image with handwritten digits to a REST endpoint provided by Flask, which runs the neural network and returns it’s prediction to the caller.
Note that all parts of this system have to be dockerized (Flask app and database) and can be started with a simple “docker-compose up”
Task 3 (Optional)
Create a simple “Front-end” using Flask templates. A Front-end is what you see in your Browser (the webpage). This Front-end should contain an Upload Form, with which you can select an image on your local computer (https://flask.palletsprojects.com/en/2.0.x/patterns/fileuploads/)
    
The output of the neural network should be represented visually on your webpage as well. If you like, you could display the uploaded image as well
Deliverables:
- We will execute ‘docker-compose up’ and expect a running Flask server
- We will use the requests library to send an Image to your REST endpoint
- We expect the prediction return of the neural network (which digit it thinks is on the image)
- We will check that the relevant data is saved in the database