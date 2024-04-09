import pandas as pd
import matplotlib as plt
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from pathlib import Path
from tools.helper import save_sentiment_analysis_results
from datetime import datetime

"""
Sentiment Analysis - Main File
"""

nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()

def analyze_sentiment_in_file(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Assuming the column with comments is named 'Top Comments'
    df['sentiments'] = df['Top Comments'].apply(lambda x: sia.polarity_scores(x))
    df['compound'] = df['sentiments'].apply(lambda x: x['compound'])
    
    # Determine sentiment category based on compound score
    df['sentiment_type'] = df['compound'].apply(lambda x: 'Positive' if x > 0 else ('Negative' if x < 0 else 'Neutral'))
    
    # Save or return the results as needed
    # Isolate the date from the filename
    filename_parts = file_path.stem.split('_')  # Split the filename without extension
    date_str = filename_parts[-1]  # Assuming the date is always the last part after splitting
        
    # Construct the result file path to save in the 'sentiment_analysis_results' folder with the desired name format
    result_file_name = f"sentiment_analysis_results_for_scraped_data_{date_str}.csv"
    result_file_path = Path('sentiment_analysis_results') / result_file_name
    print(f"Analysis complete. Results saved to {result_file_path}")
    save_sentiment_analysis_results(df, result_file_path) 


def main():
    # Define the directory containing the CSV files 
    # CHANGE IF YOU HAVE A DIFFERENT DIRECTORY NAME 
    directory_path = Path('scraped_posts')
    
    # Iterate through each CSV file in the directory
    for file_path in directory_path.glob('*.csv'):
        print(f"Analyzing {file_path.name}...")
        analyze_sentiment_in_file(file_path)

if __name__ == "__main__":
    main()
