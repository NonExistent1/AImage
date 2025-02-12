# Import necessary libraries
import csv
import os
import sqlite3
from sqlite3 import Error
import subprocess

import kagglehub
from kaggle.api.kaggle_api_extended import KaggleApi

# Get the script path and download path for the kaggle API
script_dir = os.path.dirname(os.path.abspath(__file__))
download_path = os.path.join(script_dir, 'database')

# Set the Kaggle API configuration to use the 'database' folder
KaggleApi().authenticate()
KaggleApi().config_path = download_path
kagglehub.dataset_download("alessandrasala79/ai-vs-human-generated-dataset")

# Connect to the SQLite database
conn = sqlite3.connect('image.db')

# Create the images table
conn.execute(
                '''
                    CREATE TABLE IF NOT EXISTS images(
                        image_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                        image_path TEXT NOT NULL,
                        image_label INTEGER NOT NULL
                    )
                '''
            )

# Import the dataset into the database
# Print the contents of the downloaded dataset
with open(download_path, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)