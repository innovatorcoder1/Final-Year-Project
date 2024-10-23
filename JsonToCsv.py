import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
import json


def convert_json_to_csv(folder_path, output_csv_file):
    # List to store all data from the JSON files
    all_data = []

    # Iterate over all the files in the folder
    for file_name in os.listdir(folder_path):
        # Check if the file is a JSON file
        if file_name.endswith('.json'):
            file_path = os.path.join(folder_path, file_name)
            
            # Open and read the JSON file
            with open(file_path, 'r') as json_file:
                data = json.load(json_file)
                
                # If the data is a dictionary, convert it to a list of dictionaries
                if isinstance(data, dict):
                    all_data.append(data)
                elif isinstance(data, list):
                    all_data.extend(data)

    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(all_data)

    # Save the DataFrame to a CSV file
    df.to_csv(output_csv_file, index=False)
    print(f"All JSON files have been converted to {output_csv_file} successfully!")

# Example usage
folder_path = 'D:\\MMHS150K\\img_txt'  # Replace with the path to your folder containing JSON files
output_csv_file = 'output_data.csv'       # Replace with the desired output CSV file name

convert_json_to_csv(folder_path, output_csv_file)
