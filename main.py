# Import necessary libraries
import sqlite3
from sqlite3 import Error

import kagglehub
import csv

# Download the dataset
path = kagglehub.dataset_download("alessandrasala79/ai-vs-human-generated-dataset")

# Connect to the SQLite database
conn = sqlite3.connect('image.db')

# Drop the test_images table if it exists
conn.execute(
                '''
                    DROP TABLE IF EXISTS test_images
                '''
)

# Drop the train_images table if it exists
conn.execute(
                '''
                    DROP TABLE IF EXISTS train_images
                '''
)

# Create the images table
conn.execute(
                '''
                    CREATE TABLE IF NOT EXISTS train_images(
                        image_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                        image_name TEXT NOT NULL,
                        image_label INTEGER NOT NULL
                    )
                '''
            )

# Create the test_images table
conn.execute(
                '''
                    CREATE TABLE IF NOT EXISTS test_images(
                        image_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                        image_name TEXT NOT NULL
                    )
                '''
            )

# Import the dataset into the database
# Import the training images
train_path = path + "\\train.csv"
with open(train_path, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        image_name = row[1]
        image_label = row[2]
        if not image_name or not image_label:
            print(f"Skipping row with missing data: {row}")
            continue
        conn.execute(
            '''
                INSERT INTO train_images (image_name, image_label)
                VALUES (?, ?)
            ''',
            (image_name, image_label)
        )
        print(f"Inserted {image_name} with label {image_label} into train_images table.")
        
# Import the test images
test_path = path + "\\test.csv"
with open(test_path, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        if not image_name:
            print(f"Skipping row with missing data: {row}")
            continue
        image_name = row[0]
        conn.execute(
            '''
                INSERT INTO test_images (image_name)
                VALUES (?)
            ''',
            (image_name,)
        )
        print(f"Inserted {image_name} into test_images table.")

# Commit the changes and close the connection
conn.commit()
conn.close()