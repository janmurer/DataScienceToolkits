# Report "Data Science Toolkits and Architectures"
#### Jan Murer, Frederik Poschenrieder, Jessica Ugowe 


# Milestone_5

This milestone involves building and deploying a Flask application with a neural network for image prediction, using Docker for containerisation. The application exposes a REST API to accept image inputs and provides predictions based on a neural network trained on the MNIST dataset.

## Tasks Overview

### Task 1: Flask Tutorial

In this task, we completed a tutorial on how to build and deploy a Flask application using Docker. The tutorial used an Ubuntu 18.04 system. You can follow the [DigitalOcean Flask tutorial](https://www.digitalocean.com/community/tutorials/how-to-build-and-deploy-a-flask-application-using-docker-on-ubuntu-18-04) to understand the steps involved.

By the end of the tutorial, we had a foundational understanding of how to:
- Set up a Flask application
- Containerize the application with Docker
- Deploy the application in a Docker container

---

### Task 2: Creating a Flask Application

In Task 2, we developed a Flask application that exposes a REST API endpoint to predict handwritten digits from the MNIST dataset. Here are the specifics of what was implemented:

#### Key Features:
- **REST API Endpoint**: 
  - We created a POST request endpoint at `<base_url>/predict`.
  - This endpoint accepts an image from the MNIST dataset as input.
  
- **POST Request Handling**: 
  - The Flask app accepts a Base64-encoded image in the body of the POST request.
  - The `requests` Python library is used to send the POST request containing the image to the Flask app (for example, by a client or another service).
  
- **Image Processing**:
  - The Flask application decodes the Base64 image and converts it into a numpy array.
  - The image array is passed to the pre-trained neural network model, which was trained on the MNIST dataset.

- **Neural Network Prediction**:
  - The neural network model generates a prediction based on the input image.
  - The prediction, along with the image, is saved in a database (as was done in Milestone 3).

- **Response to Client**: 
  - The Flask app sends back the prediction as a response to the client.

The entire application was dockerised and can be started with the following command:

```bash
    docker-compose up
```
---

### Task 3: Creating a Front-end using Flask templates

In this optional task, we added a simple front-end to the Flask application using Flask templates. This allows users to upload an image from their local machine and view the neural network’s prediction on a web page. In this task we really benefitted from our stable back-end infrastructure. The front-end was created extremely fast, compared to the other task. We created a simple flask app with only two routes, for which we used simple templates.

#### Key Features

- **File Upload Form**:
  - A form is provided on the webpage that allows users to select an image file from their computer.
  
- **Prediction Display**:
  - Once the image is uploaded, the Flask app processes it and makes a prediction using the neural network.
  - The result is displayed on the webpage.

- **Image Display**:
  - The uploaded image is also displayed on the webpage, making it easier to verify the prediction.

---


## Challenges 

1. Ports

      As already predicted in the lecture, we got confused by choosing the right ports to interact with our flask application. Also one group member was having issues with ports that were already blocked. This issue could only be resolved by changing the respective ports, as killing the process that blocked the port was not possible. 

2. Database adaption / Reusing previously created functions

      Renaming the existing database and adapting the previously created functions to the new milestone was quite time consuming, as debugging required rebuilding the whole container. 

3. Lack of global variables

      Maintenance of the code became increasingly difficult, as some environnement variables were not set globally. This mainly concerns the database access. The project would certainly benefit of restructuring for easier maintenance. 

4. Adapting to changing requirements

    It took quite some time for us to adapt to the changing requirements of the new task. We could for example not just reuse the existing database from milestones 3 and 4, as we had a different data structure (We had 'true values' to each immage, that we stored in the previous milestones, that we did not have in our external data now). The functions we have build needed quite some wiggling around to adapt to the new requirements. For future projects we would put more time into the whole process of preparing our functions, so they can better deal with future changes.

---

## Conclusion

This milestone concludes our project, where we developed and deployed a Flask application with a neural network for digit image prediction. Looking back on this project, we are really pleased with what we have accomplished. Working as a team of three taught us a lot: not just about the tech stuff like Flask, Docker, and machine learning, but also about how to divide work, help each other out when stuck, and bring different pieces together into one working system. Sure, there were some tough moments and plenty of debugging sessions, but that is part of what made finishing the project feel so rewarding. In the end, we built something we are genuinely proud of, and more importantly, something that works! It is pretty cool to see how all these different technologies we learnt about came together into a real, working application. 😎



