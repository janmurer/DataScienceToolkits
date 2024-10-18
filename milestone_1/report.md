# Report "Data Science Toolkits and Architectures"
#### Jan Murer (XX-XXX-XXX), Frederik Poschenrieder (XX-XXX-XXX), Jessica Ugowe (XX-XXX-XXX)


# Milestone_1 

## Introduction
This milestone uses the MNIST dataset which is short for "Modified Natioanl Institute of Standards and Technology".[1] MNIST was constructed from the National Institute of Standards and Technology (NIST) Special Database 3 (SD-3) and Special Databse 1 (SD-1)by remixing the samples which were taken from American Census Bureau employess and high school students.[2] This dataset contains a massive collection of handwritten digits used to train various image processing systems and it is one of the most popular image recognition dataset.

** The goal of this milestone is to checkout('download') the mnist_covnet.py code, run it on our machines and report our processes and findings. **

## Dataset Overview

### Nature of the problem
This is a **classification problem** because we discovered that the model learns to classify images of handwritten digits from 0 to 9.

### Dataset Characteristics
**Size:** The dataset is a collection of 70,000 handwritten digits (0-9), having 60,000 training images with their labels and 10,000 testing images of handwritten digits with their corresponding labels as well to evaluate the performance of the traained model.

**Type of Data:** It consits of 784 grayscale images of size 28x28 pixels. Each pixel value (0-225) represents the grayscale intensty of the corresponding pixel in image with 0 representing white and 225 representing black.[2]



## Prep

We were able to run Arch Linux on a virtual machine using VMware Fusion. For the initial setup we used an Archboot ISO-Image. While we tried mounting the raw Arch image, we found that the setup guide that comes with Archboot helped a lot during the setup process. As we are emulating the system on ARM chips, we are facing a few packages and dependencies that are not running on the ARM architecture yet. ChatGPT also helped a fair bit during the installation. Although the system is running, it still feels a bit buggy (e.g., i3 in combination with picom for transparency causes the system to break). Also when trying to reformat the hard disk of the virtual machine we accidentally wiped the wrong partition, which resulted in having to go through the entire installation process again. 

To prevent major mistakes such as accidentally wiping the system, we prefer using MacOS to complete the milestones. If passing a milestone requires the use of a Linux distribution we have virtual machines that emulate Fedora and Ubuntu. 
To install Python to our Mac Devices we used Homebrew (`brew install python`).

### 3
To "clone" the assigned code from the Keras repository, we simply copied the code and pasted it into a new file in our repository. We were not able to use Git to only clone one script of the Keras repository to our repository. As far as our understanding goes, using git, one can only clone the entire repository to a remote local. One could use the wget tool (e.g., `wget https://github.com/keras-team/keras-io/blob/master/examples/vision/mnist_convnet.py`) to download one single file from a GitHub repository, however in our case copy and pasting it was just fine.

We adjusted the .gitignore file so .pdf files as well as datasets in a local directory would not be pushed to the GitHub repository. 

For our repository we created a rule for the main branch that restricts deletions, requires a pull request before merging and blocks force pushes. This way, it is not possible to directly push to the main branch. As the main branch should only contain running code, we created a dev branch where the merged code from feature branches could be tested before adding it to the main branch. This way, there should be running code on the main branch at all times. For each feature that is to be developed, one creates a new feature branch. This way we hope to prevent merging errors. 

Before running the code, we created a virtual environment. This was done either using the terminal using the venv module or using the "Python: Create Environment" gui option within Visual Studio Code. We prefer using the terminal for this task as it creates a visible folder within the directory instead of an invisible directory, as is being created using Visual Studio Code. 

Before running the assigned code, we activated the virtual environment and installed the necessary libraries and its dependencies (namely TensorFlow, Keras and NumPy). This was done using pip. For reproducibility we created a requirements.txt file using the terminal command `pip freeze`. 

To run the code, we opened the respective directory in Visual Studio Code and ran it by activating our virtual environment (`source venv/bin/activate`). After running the code we added some comments about what certain bits of the code do. This was then pushed to the GitHub repository. After interpreting the results, we dublicated the script and modified it slightly to run the same script with different data. This time we tried the fashion_mnist dataset that is also available using `keras.datasets.fashion_mnist.load_data()`. Without further modification the model scored an accuracy of roughly 89%, which is surprisingly good. Jan tried to train a model to the exact same data-set for the course "Unsupervised Machine Learning" which (after loads of code optimization) yielded him an accuracy of roughly 50%, which is surprisingly bad. 


## References

1. Digital Ocean: [MNIST Dataset] (https://www.digitalocean.com/community/tutorials/mnist-dataset-in-python)

2. Geeks for Geeks: [MNIST Dataset] (https://www.geeksforgeeks.org/mnist-dataset/)


