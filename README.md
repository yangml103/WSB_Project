# WallStreet Bets Analysis Project

This project is designed to scrape data from the WallStreetBets subreddit using Python and perform sentiment analysis on the posts to gauge the community's sentiment over time. It utilizes the Reddit API to fetch posts and comments and employs libraries such as Pandas for data manipulation, NLTK for natural language processing, and VADER for sentiment analysis.

## Features

- **Web Scraping**: Fetches posts and comments from the WallStreetBets subreddit using the Reddit API.
- **Data Processing**: Cleans and prepares the data for analysis, removing unnecessary elements like URLs and emojis using regular expressions.
- **Sentiment Analysis**: Analyzes the sentiment of each post and comment to determine the overall sentiment of the community. This is done using the VADER sentiment analysis tool within the NLTK library.
- **Data Visualization**: Visualizes the results of the sentiment analysis, showing trends over time and identifying periods of particularly positive or negative sentiment.

## Getting Started

### Prerequisites

If you are running the code in VSCode, I would recommend starting a python virtual environment to run the code. To do so, press Ctrl+Shift+P and select "Python: Create Virtual Environment". Then, select the environment you would like to use, and install the dependencies.

If not using a virtual environment, you can install the dependencies by using:

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

After making sure you've created a `config.py` file following the format in `config_example.py`:

First run the `wsb_scraper.py` to scrape the data from the subreddit.

Then, run the `sentiment_analysis.py` to analyze the data and perform sentiment analysis.

Finally, run `stock_verifier.py` to verify the sentiment of the posts against the stock price.

The data from the subreddit will be saved in the `scraped_posts` directory.

The results of the sentiment analysis will be saved in the `sentiment_analysis_results` directory.

The results of the stock verification will be saved in the `actual_stock_performance_analysis` directory.

## Project Structure

- `requirements.txt`: Lists the Python libraries required for the project.
- `Web_Scraper`: Contains the code for scraping subreddit posts and comments.
- `Data_Processor`: Contains the code for analyzing the scraped data and performing sentiment analysis.

## License

This project is open-source and available under the MIT License. See the LICENSE file for more details.