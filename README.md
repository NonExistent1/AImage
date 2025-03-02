# AImage

This project is a machine learning program that determines whether a user inputted image is AI generated or not. It populates it's SQLite database by pulling a .csv from the Kaggle project and uploading each item into the database. It's backend is in Python. The front end uses the ipywidgets library to connect with Jupyter Notebook. It uses a Convolutional Neural Network for the machine learning algorithm with TensorFlow. 

With the current settings, creating a model takes approxiamately 3 days.

It uses this Kaggle database: https://www.kaggle.com/datasets/alessandrasala79/ai-vs-human-generated-dataset. 

NOTE: this program will not work on a computer with a CPU that does not support AVX instruction sets

## Table of Contents

- [Installation](#installation)
- [Usage (Loading the Model)](#usage)
- [Usage (Creating the Model)](#usage)
- [Viewing the Reporting and Visualization](#usage)


## Installation

1. Install Microsoft Visual C++ Visual Studio 2015-2022
    a. Can be found here: https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170#visual-studio-2015-2017-2019-and-2022
2. Install Python 3.12.9
    a. Can be found here: https://www.python.org/downloads/release/python-3129/
    b. Make sure to select the "add Python to PATH" option in the installer
    c. Also make sure to disable the path limit
3. Restart your computer
4. Open a powershell terminal and enter "cd *Directory to c964 folder*"
5. Create a virtual environment by entering "py -m venv venv"
6. Activate the virtual environment by entering "venv/Scripts/activate"
7. Install dependencies by entering "pip install -r requirements.txt"
8. To start the server enter "jupyter notebook"
9. If it doesn't automatically open, open a web browser and enter the URL or File provided in the terminal (Should look something like this: file:///C:/Users/Username/AppData/Roaming/jupyter/runtime/jpserver-30688-open.html)

## Usage (Loading the Model)

After following the installation steps, you can prepare the program and make predictions with an existing model

1. Double-click on notebook.ipynb in the browser
2. Run the code in the following sections:
    a. Import Necessary Resources
    b. Prepare the Data
    c. Load the Model
3. Once these are done running, run the Predictions section
4. After running the Predictions section an upload button will appear
5. Click on the upload button and upload an image that you want a prediction for
    a. NOTE: If you upload an image with transparency you will get warning and the prediction will be more inaccurate
6. After uploading the image the AI will give you a value between 0 and 1, it's prediction, and a preview of the uploaded image
    a. The value represents its prediction, with closer to 1 being AI generated and closer to 0 being Human-Created 

## Usage (Creating the Model)

After following the installation steps, you can prepare the program and make predictions with a new model

1. Double-click on notebook.ipynb in the browser
2. Run all of the code in the Setup and Preparation section
3. Once these are done running, run the Predictions section
4. After running the Predictions section an upload button will appear
5. Click on the upload button and upload an image that you want a prediction for
    a. NOTE: If you upload an image with transparency you will get warning and the prediction will be more inaccurate
6. After uploading the image the program will give you a value between 0 and 1, it's prediction, and a preview of the uploaded image
    a. The value represents its prediction, with closer to 1 being AI generated and closer to 0 being Human-Created 

## Viewing the Reporting and Visualizations

After following the Usage steps, you can view reporting and data visualizations

1. Navigate to the Reporting and Visualizations section
2. Run the Example Training Image Data section
    a. This section shows 16 example images after the preprocessing steps have occurred
3. Run the Data Makeup section
    a. This section shows the makeup of the initial dataset, how many images there are total along with how many AI images and how many human-created images.
4. Run the Model Metrics Section
    a. This section shows the metrics of the model that is currently in use
    b. It shows the precision, recall, and accuracy values


If you have created a new model:
1. Run the Loss While Training Section
    a. This will show a graph of the loss values over time during training
2. Run the Accuracy while Training Section
    a. This will show a graph of the accuracy values over time during training