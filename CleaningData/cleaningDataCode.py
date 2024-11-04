import pandas as pd
import re
import emoji
from textblob import TextBlob





def clean_text(text):
    # Check if text is a string
    if not isinstance(text, str):
        return ''  # Return empty string or original value if not a string

    # Convert text to lowercase
    text = text.lower()
    # Replace emojis with their corresponding text description
    text = emoji.demojize(text, delimiters=(" ", " "))
    
    # Remove HTML tags
    text = re.sub(r'<.*?>', '', text)
    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    # Remove mentions (e.g., @username)
    text = re.sub(r'@\w+', '', text)
    # Remove hashtags
    text = re.sub(r'#\w+', '', text)
    # Remove numbers
    text = re.sub(r'\d+', '', text)
    # Remove punctuations
    text = re.sub(r'[^\w\s]', '', text)
    # Fix misspelled words using TextBlob
    text = str(TextBlob(text).correct())
    # Remove extra whitespaces
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def load_and_clean_csv(input_csv_file, output_csv_file, text_column):
    try:
        # Load the CSV file
        df = pd.read_csv(input_csv_file)

        # Display the columns in the CSV file
        print("Columns in the CSV file:", df.columns)

        # Check if the specified text column exists
        if text_column in df.columns:
            # Apply the clean_text function, ignoring NaN values
            df[text_column] = df[text_column].apply(clean_text)
        else:
            print(f"The column '{text_column}' was not found in the CSV file.")
            return

        # Save the cleaned DataFrame to a new CSV file
        df.to_csv(output_csv_file, index=False)
        print(f"Cleaned data has been saved to {output_csv_file}.")
        
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_csv_file = r'C:\Users\USER 1\OneDrive\Documents\FinalYearProject\Final-Year-Project\cleaned_data.csv'  # Replace with the path to your input CSV file
output_csv_file = r'C:\Users\USER 1\OneDrive\Documents\FinalYearProject\Final-Year-Project\cleaned_data1.csv'  # Output path
text_column = 'img_text'  # Replace with the actual column name containing the text data

load_and_clean_csv(input_csv_file, output_csv_file, text_column)
