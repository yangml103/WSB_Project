import pandas as pd
import matplotlib as plt
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from pathlib import Path
from tools.helper import save_sentiment_analysis_results

"""
Sentiment Analysis - Main File
"""


nltk.download('vader_lexicon')

df_original = pd.read_csv('scraped_wsb_posts.csv')
df_copy = df_original.copy()

sia = SentimentIntensityAnalyzer()

# Assuming the column with comments is named 'Top Comments'
df_copy['sentiments'] = df_copy['Top Comments'].apply(lambda x: sia.polarity_scores(x))
df_copy['compound'] = df_copy['sentiments'].apply(lambda x: x['compound'])

# Determine sentiment category based on compound score
df_copy['sentiment_type'] = df_copy['compound'].apply(lambda x: 'Positive' if x > 0 else ('Negative' if x < 0 else 'Neutral'))

print(df_copy[['Title', 'sentiment_type']])

# Function located in tools/helper.py 
save_sentiment_analysis_results(df_copy, 'sentiment_analysis_results.csv') 


# TODO: Isolate company names in sentiment_analysis_results and compare to actual stock performance


