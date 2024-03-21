import pandas as pd
from pathlib import Path
import logging

"""
Helper Functions for Analysis
"""

def save_sentiment_analysis_results(df, file_path):
    """
    Saves the sentiment analysis results to a CSV file if the results do not already exist.
    
    Parameters:
    - df (pd.DataFrame): The DataFrame containing the sentiment analysis results.
    - file_path (str): The path to the CSV file where the results should be saved.
    """
    if not isinstance(df, pd.DataFrame):
        logging.error("Input is not a pandas DataFrame.")
        return

    try:
        if Path(file_path).exists():
            existing_df = pd.read_csv(file_path)
            if not df[['Title', 'sentiment_type']].reset_index(drop=True).equals(existing_df.reset_index(drop=True)):
                df[['Title', 'sentiment_type']].to_csv(file_path, index=False)
            else:
                logging.info("The file with the exact same sentiment analysis results already exists. No new file saved.")
        else:
            df[['Title', 'sentiment_type']].to_csv(file_path, index=False)
    except Exception as e:
        logging.error(f"Failed to save sentiment analysis results: {e}")

# Usage example
# save_sentiment_analysis_results(df_copy, 'sentiment_analysis_results.csv')