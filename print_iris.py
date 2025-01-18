# Author: Lily Song
# Date: 2025-01-17
# Description: This script reads the Iris.csv dataset and prints each line.

# Import necessary library
import csv  # CSV module to handle reading CSV files

# Define the path to the Iris.csv file
file_path = "data/Iris.csv"

# Open the CSV file and read its contents
try:
    with open(file_path, mode="r") as file:
        # Create a CSV reader object
        reader = csv.reader(file)

        # Print each line in the CSV file
        for line in reader:
            print(line)
except FileNotFoundError:
    print(f"Error: The file {file_path} was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
