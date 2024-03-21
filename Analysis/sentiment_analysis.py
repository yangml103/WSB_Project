import pandas as pd
import matplotlib as plt
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

df = pd.read_csv('wsb_posts.csv')

sia = SentimentIntensityAnalyzer()

# Assuming the column with comments is named 'comments'
df['sentiments'] = df['Top Comments'].apply(lambda x: sia.polarity_scores(x))
df['compound'] = df['sentiments'].apply(lambda x: x['compound'])

# Determine sentiment category based on compound score
df['sentiment_type'] = df['compound'].apply(lambda x: 'Positive' if x > 0 else ('Negative' if x < 0 else 'Neutral'))

print(df[['Title', 'sentiment_type']])


"""
# For demonstration, let's create a simple DataFrame
df = pd.DataFrame({'comments': ['I love this!', 'This is terrible.', 'Absolutely fantastic!', 'Not good, not bad.']})

sia = SentimentIntensityAnalyzer()

# Apply sentiment analysis to each comment
df['sentiments'] = df['comments'].apply(lambda x: sia.polarity_scores(x))
df['compound'] = df['sentiments'].apply(lambda x: x['compound'])

# Determine sentiment category based on compound score
df['sentiment_type'] = df['compound'].apply(lambda x: 'Positive' if x > 0 else ('Negative' if x < 0 else 'Neutral'))

print(df[['comments', 'sentiment_type']])



# Load the dataset
df = pd.read_csv('wsb_posts.csv')

# Display the first few rows of the dataframe
print(df.head())
# Example: Drop rows with missing values
df.dropna(inplace=True)

# Example: Remove duplicates
df.drop_duplicates(inplace=True)
# Get a summary of the numerical columns
print(df.describe())




# Example: Saving a dataframe to a new CSV file
df.to_csv('analysis_results.csv', index=False)

"""