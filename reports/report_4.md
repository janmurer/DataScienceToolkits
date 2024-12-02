# Report "Data Science Toolkits and Architectures"
#### Jan Murer, Frederik Poschenrieder, Jessica Ugowe 


# Milestone_4

## Task 1: Experiment Management

### Key Questions Answered

**What is Experiment Management and why is it important?**

Experiment management seeks to track progress and experiments systematically. It is used to organize code versions, datasets, hyperparameters, metrics and results. This is mainly to ensure reproducibility, efficiency and collaboration. In easier terms, filenaming such as 'machine_learning_model_xy_v7_final_version2_approved.py' shall be prevented.

In a nutshell tools like WANDB.ai help with:
- Experiment Tracking
    - Logs of all relevant details about the experiments (hyperparameters, metrics, model configurations)
- Visualization of Metrics
- Collaboration and Reproducibility
    - Experiemnt data can be stored on the cloud.
- Model Versioning
    - Management of trained models and datasets
- Scalability

**What is a Metric in ML?**

A metric is a qunatitative measure used to evaluate the performance of a model. Metrics also help to compare different models against each other.

**What is Precision and Recall? Why is there often a trade-off between them?**

- Precision: Ratio of true positive predictions relative to all positive predictions made by the model.

    $\text{Precision} = \frac{\text{True Positives}}{\text{True Positives} + \text{False Positives}}$

- Recall: Ratio of true positive predictions to all actual positive cases.

    $\text{Recall} = \frac{\text{True Positives}}{\text{True Positives} + \text{False Negatives}}$

- Trade-off: Increasing precision often reduces recall and vice versa. By simply classifing everything as Positive one would achieve a Recall of 1, but an essentially useless model. High precesion means fewer false positives and a high recall means fewer false negatives. How the metrics are interpreted ultimately depends on the use case of the model. In medical applications eliminating minimizing false negatives may be more important than false positives, whereas in credit assessment classification minimizing false positives (garanting a credit to a "bad" lender) may be more important.

**What is AUROC (Area under Receiver Operating Characteristic Curve) Metric?**

The AUROC measures a model's abilitiy to distingish between classes. It represents the area under the ROC curve, where the curve plots the true positive rate against the false positive rate. 

![AUROC](https://glassboxmedicine.com/wp-content/uploads/2019/02/roc-curve-v2.png)

**What is a Confusion Matrix?**

A confusion matrix is a summary table used to evaluate the performance of a classification model. It shows the counts of correct and incorrect predictions for each class. 

|                | Predicted Positive | Predicted Negative |
|----------------|--------------------|--------------------|
| **Actual Positive** | True Positive (TP)   | False Negative (FN)  |
| **Actual Negative** | False Positive (FP)  | True Negative (TN)   |

## Task 2: 

**Choose an appropriate metric for optimizing your ML Model. What is the reasoning behind it?**

The MNIST dataset is balanced, all classes are equally represented in the data. Therefore, the chosen metric for optimization is Accuracy. Accuracy offers a great interpretability and is a rather straightforward metric. Lastly accuracy is a standard metric in benchmarks for MNIST and allows for seamingless comparison among different models and architectures. 

Instrument your code with Weights & Biases (within a Docker container). Choose an appropriate metric for optimizing your ML Model. What is the reasoning behind it?
Note you can make a new Dockerfile (you don’t need to use docker-compose)
Your code should:
- Login to W&B (Tip: you can use ENTRYPOINT in a Dockerfile to run a shell script that logs you in (see below))
- Train a Model
- Save and upload the trained model
- Log the value of the loss function (graphically)
- Log your metric (graphically), Tip use a Keras Metric
- (Optional) Log your current Git commit, also try to enforce that you have to first commit all changes before W&B allows you to sync with the cloud otherwise you might log the wrong commit hash (and others do not use the same code as you do when they want to reproduce the experiment by checking out the commit hash). You can create a shell script for that (get Git commit hash and save as Environment Variable, use Python code to retrieve the variable and save it in W&B)
- (Optional) Upload the output of the predict function as a file to W&B
- Try to play with your Neural Network, by changing parameters or even its architecture. Make sure that you log those changes automatically to W&B. Compare the runs on W&B, how do the metrics/loss change? It is not necessary to “optimize” your model. Possible changes to the training:
- Architecture (add a Layer, delete a Layer, change hidden units) - Different loss function
- Different optimizer
- Batch size, Learning rate, ...
Please read carefully (W&B Login):
- After creating an account at W&B you will get a W&B “Token”. This token has to remain secret, it acts like a password. So do not commit/push the token in/top Git/GitHub, or others may gain access and change your W&B Account. If you uploaded the token by mistake, then change it in the W&B settings immediately. Since your Git repos are public, these keys will be stolen by web scrapers in very little time.
Note: Secret sharing among collaborators is a big topic in itself. There is a plugin called “git secrets” that allows sharing secrets via Git/GitHub by always first encrypting the secrets before they are pushed to a Git Repository. Collaborators are part of a “key chain” and can decrypt the secret on their machines locally. If you are interested in this, you can try setting up “git secrets”. GitHub also allows you to store secrets for specific repositories. You can also look into that.
- In order to do the login properly. You should save this token in a file that you will put into your .gitignore. (I usually call this file .env)
- The script that Docker runs in its entrypoint can access this .env file and save the token as an Environment Variable.
- Your entrypoint script (might be called docker_entrypoint.sh) may look like this:
This shell script is executed as an entrypoint when the docker image is run with “docker run ..”. Whatever is in CMD (or the command that is run by f.e. “docker run <image> <command>) will be executed by ‘exec “$@”’, after wandb login was run. $WANDB_TOKEN is a reference to the environment variable. So inside the .env file you should have a WANDB_TOKEN=<your_secret_token_which_you_should_never_share_or_upload_to_github_ever> (without the $ sign).
When you run the docker container, you can add the –-env_file argument: “docker run –-env_file=.env <image> python3 main.py”
Docker will load whatever Environment Variables are defined in “.env” (in our case WANDB_TOKEN). The entrypoint script above is executed and $WANDB_TOKEN reads the Environment Variable WANDB_TOKEN that contains your secret token. “wandb login” logs you into the WANDB Cloud Service (first you need to install the wandb Python client through the requirements file).
Again: Do not version control .env, otherwise you leak your secret token to the world. In case this happens, change the token immediately in the W&B settings on their Web page (after you logged in on the Web page with username/password).
 
## Task 3
Use Jupyter Notebook to analyze your data.
- Load your data into a Numpy Array (f.e. If you have Image data, load an image and you should get an array with dimensions (width, height, channels), where channels is 3 in an RGB image (Red,Green and Blue colors).
- Use Numpy to analyze your data. F.e. you could create a histogram of the color channels, or the distribution of words in your training set (in case you have text data). Use Matplotlib to plot figures.
- Analyze the output of your Training runs from Task 2. This means:
download the ground truth of your data set and the predictions your Neural Network made. You may try to create a Confusion Matrix with Scikit-Learn.
Deliverables:
- We want to see your training runs in Task 2. So make your W&B Projects public and add the links to your reports
- Also, version control your Jupyter Notebooks from Task 3. Use Markdown within the Jupyter Notebooks to tell us what you were attempting to do.
Bonus points from now on:
Add the link to the issue to your report if you want to claim Bonus points (as a helper).