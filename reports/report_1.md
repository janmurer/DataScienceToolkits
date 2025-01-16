# Report "Data Science Toolkits and Architectures"
#### Jan Murer, Frederik Poschenrieder, Jessica Ugowe 


# Milestone_1 

## Introduction

This milestone uses the MNIST dataset which is short for "Modified National Institute of Standards and Technology".[1] MNIST was constructed from the National Institute of Standards and Technology (NIST) Special Database 3 (SD-3) and Special Databse 1 (SD-1) by remixing the samples which were taken from American Census Bureau employess and high school students [2]. This dataset contains a massive collection of handwritten digits used to train various image processing systems and it is one of the most popular image recognition dataset.

**Objective**: The goal of this milestone is to checkout ('download') the `mnist_covnet.py code`, run it on our machines and report our processes and findings.

## Dataset Overview

### Nature of the problem

This is a **classification problem** because we discovered that the model learns to classify images of handwritten digits from 0 to 9.

### Dataset Characteristics

**Size:** The dataset is a collection of 70,000 handwritten digits (0-9), having 60,000 training images with their labels and 10,000 testing images of handwritten digits with their corresponding labels as well to evaluate the performance of the traained model.

**Type of Data:** It consits of 784 grayscale images of size 28x28 pixels. Each pixel value (0-225) represents the grayscale intensity of the corresponding pixel in the image with 0 representing white and 225 representing black.[2]

## Setup 

### System Configuration
The project utilized Arch Linux on a virtual machine using VMware Fusion. The initial setup involved using an Archboot ISO-Image. During the mounting of the raw Arch image, we found that the setup guide that comes with Archboot helped a lot during the setup process as well as ChatGPT. We encountered a challenge during this process which we explained in the challenge and solution part of this report.

To install Python to our Mac devices we used Homebrew (`brew install python`).

### Code Management

Unable to clone scripts directly via Git, the `mnist_convnet.py` from the Keras repository, was manually copied and pasted into a new file in our repository. This was a workaround to the limitation of Git operations because as far as our understanding goes, one can only clone the entire repository to a remote locally. However, one could use the wget tool (e.g., `wget https://github.com/keras-team/keras-io/blob/master/examples/vision/mnist_convnet.py`) to download one single file from a GitHub repository, but in our case copying and pasting was just fine.

### Repository Configuration
We configured our repository to ensure quality:

- **.gitignore**: 
We adjusted the .gitignore file so .pdf files as well as datasets in our local directory were not pushed to the GitHub repository. 

- **Main branch restrictions**: Deletions and direct pushes were blocked and a pull request is required before merging, as the main branch should only contain running code thereby ensuring maintenance and quality.

- **Development branches**: Feature specific branches were created for ongoing developments, which could then be merged into a devlopment branch(dev branch) upon completion, for integrated testing before adding it to the main branch. For each feature that is to be developed, one creates a new feature branch in order to prevent merging errors.

### Virtual Environment
For consistent dependency mangement, a virtual environment was setup using either the terminal `python -m venv .venv`, using the venv module or using the "Python: Create Environment" gui option within Visual Studio Code. We preferred using the terminal for this task as it creates a visible folder within the directory instead of an invisible directory, as is being created using Visual Studio Code. 
This approach ensures that our project dependencies are isolated from global python packages, minimizing conflicts and replicating a clean environment.

### Dependency Management
After setting up the environment, we activated the virtual environment and installed the necessary libraries and its dependencies such as TensorFlow, Keras and NumPy using `pip`. For reproducibility we created a requirements.txt file using the terminal command `pip freeze`. 

## Execution

### Running the Script

The script was ran within Visual Studio Code by opening the respective directory and activating our virtual environment (`source venv/bin/activate`). This process was documented , by adding comments about what certain bits of the code does and then this was pushed to our GitHub repository. 

### Additional Experimentation
Post- initial testing, the script was adapted to run `fashion_mnist` dataset that is also available using `keras.datasets.fashion_mnist.load_data()`. Suprisingly, the model achieved an accuracy of approximately 89% without further modification, contrasting with earlier efforts of Jan to train a model to the exact same data-set for the course "Unsupervised Machine Learning" which (after loads of code optimization) yielded him an accuracy of roughly 50%, which was surprisingly bad. 

Successfully we ran the code on multiple machines (including VM's) using Python 3.12.4 (respectively Python 3.12.7 on the virtual machine) with all the required packages in the requirements.txt file and we used `python --version` to find out what version of Python was installed on our systems. Although the virtual machine was running a slightly older version of python, no problems were faced while running the code. 

## Findings

As already described in the dataset section, the input for the model consists of handwritten digits with 28x28 pixels, which are represented to the neural network as an array of shape (28, 28, 1), where 28x28 indicates the pixel dimensions, and the extra dimension (1) signifies that the images are grayscale. 

The neural network assigns these inputs a probability distribution over 10 possible classes, where each class corresponds to a digit between 0 and 9. The output layer of the network employs a **softmax** activation function, which ensures that the output values form a probability distribution over all classes. The class with the highest probability is then taken as the model's prediction for the digit in the image.

The specific neural network used is called **convolutional neural network (CNN)** specifically designed for image data. The network begins with an **input layer** that has the purpose of only accepting images, that fit the specified input dimensions (array of 28,28,1). It has two **convolutional layers**: the first applies 32 filters of size 3x3 to detect basic features like edges and textures, while the second layer uses 64 filters of the same size to capture more complex patterns in the image. These layers help the network understand different features at varying levels of detail.

Each convolutional layer is followed by a **max-pooling layer**, which reduces the size of the feature maps by downsampling them. This process retains important features while reducing the computational complexity, making the network more efficient. After the convolutional and pooling layers, the feature maps are flattened into a 1D vector, which prepares the data for the fully connected layers.

A **dropout layer** is then applied, which randomly drops 50% of the neurons during training to prevent overfitting, ensuring the model generalizes better to unseen data. Finally, the **fully connected layer** consists of 10 neurons, one for each digit class (0-9), and uses a softmax activation function to output a probability distribution. This allows the model to predict which digit is most likely represented in the input image.

The data is loaded using a built-in Keras function, which retrieves the MNIST dataset via the Keras API, splitting it into training and test sets. The training images are normalized by scaling the pixel values to the range [0, 1] and reshaped to have a shape of (28, 28, 1) so that they can be fed into the model. The labels are one-hot encoded, converting them into a numerical format that can be processed by the neural network for multi-class classification. 

To train the model, small **batches** of 128 samples are created. During each iteration, the model processes one batch at a time, updating its weights based on the error for that batch and then processing the next batch. This process is repeated for 15 **epochs**, meaning the model sees the entire training dataset 15 times. Training in batches allows the model to converge more efficiently by updating weights frequently, while multiple epochs help the model learn the underlying patterns in the data, improving its accuracy over time. The model's performance is monitored using a **validation split**, ensuring it generalizes well to unseen data.

The key dependencies for this task include **NumPy** for numerical operations, and **Keras**, which serves as a high-level neural network API built on top of **TensorFlow**. Keras provides a user-friendly interface for constructing and training deep learning models like CNNs, while TensorFlow handles the low-level operations such as tensor computations and GPU acceleration. Essentially, Keras simplifies the process of defining complex neural network architectures, while TensorFlow acts as the backend that executes these models efficiently. This makes it possible to focus on model design without worrying about the underlying computation details.


## Challenges and Solutions

### Challenge 1 : 
- **Issue**: Initial setup on ARM architecture led to several software compatibility issues and system instability. Although the system was running, it still felt a bit buggy (e.g., i3 in combination with picom for transparency caused the system to break and git-cli for authentification on GitHub did not run on aarch64) and while trying to reformat the hard disk of the virtual machine we accidentally wiped the wrong partition, which resulted in having to go through the entire installation process again.

- **Solution**: To prevent major mistakes such as accidentally wiping the system, we prefer using MacOS to complete the milestones. If passing a milestone requires the use of a Linux distribution we have virtual machines that emulate Fedora and Ubuntu. 

## References

1. Digital Ocean: https://www.digitalocean.com/community/tutorials/mnist-dataset-in-python

2. Geeks for Geeks: https://www.geeksforgeeks.org/mnist-dataset/


