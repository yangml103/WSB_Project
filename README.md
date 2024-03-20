# WallStreet Bets Analysis Project

This project is designed to scrape data from the WallStreetBets subreddit using Python and perform sentiment analysis on the posts to gauge the community's sentiment over time. It utilizes the Reddit API to fetch posts and comments and employs libraries such as Pandas for data manipulation, NLTK for natural language processing, and VADER for sentiment analysis.

## Features

- **Web Scraping**: Fetches posts and comments from the WallStreetBets subreddit using the Reddit API.
- **Data Processing**: Cleans and prepares the data for analysis, removing unnecessary elements like URLs and emojis using regular expressions.
- **Sentiment Analysis**: Analyzes the sentiment of each post and comment to determine the overall sentiment of the community. This is done using the VADER sentiment analysis tool within the NLTK library.
- **Data Visualization**: Visualizes the results of the sentiment analysis, showing trends over time and identifying periods of particularly positive or negative sentiment.

## Getting Started

### Prerequisites

Before running the scraper, you need to install the required Python libraries. You can do this by running the following command in your terminal:

```
pip install -r requirements.txt
```

This will install the following Python libraries:
- beautifulsoup4
- requests
- pandas
- praw
- nltk
- textblob

## Project Structure

- `requirements.txt`: Lists the Python libraries required for the project.
- `Web_Scraper`: Contains the code for scraping subreddit posts and comments.
- `Data_Processor`: Contains the code for analyzing the scraped data and performing sentiment analysis.

## License

This project is open-source and available under the MIT License. See the LICENSE file for more details.