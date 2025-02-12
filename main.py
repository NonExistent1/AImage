# Import necessary libraries
import sqlite3
from sqlite3 import Error

import kagglehub
import csv

# Download the dataset
path = kagglehub.dataset_download("alessandrasala79/ai-vs-human-generated-dataset")

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
