# Reddit Subreddit Scraper

This project is a simple Python-based web scraper designed to fetch and analyze data from a specified subreddit. It uses the Reddit API to scrape posts, including details such as title, author, upvotes, and number of comments, and then performs basic data analysis on the collected data.

## Getting Started

To get started with this project, you'll need to have Python installed on your system. This project has been tested with Python 3.8, but it should work with other versions that support the libraries listed in `requirements.txt`.

### Prerequisites

Before running the scraper, you need to install the required Python libraries. You can do this by running the following command in your terminal:

```
pip install -r requirements.txt
```

This will install the following Python libraries:
- beautifulsoup4
- requests
- pandas

### Configuration

You must provide your Reddit API credentials and specify the subreddit you want to scrape in the `config.py` file. Replace the placeholder values with your actual `CLIENT_ID`, `CLIENT_SECRET`, and `USER_AGENT`. Also, specify the `SUBREDDIT` you're interested in and the `POST_LIMIT` for the number of posts to fetch.

Example `config.py`:
```python
# Reddit API Credentials
CLIENT_ID = 'your_client_id_here'
CLIENT_SECRET = 'your_client_secret_here'
USER_AGENT = 'your_user_agent_here'

# Subreddit to scrape
SUBREDDIT = 'name_of_subreddit'

# Number of posts to scrape
POST_LIMIT = 100
```

### Running the Scraper

To run the scraper, execute the `scraper.py` script from your terminal:

```
python scraper.py
```

This will fetch the posts from the specified subreddit and save them to a CSV file named `reddit_posts.csv`.

### Analyzing the Data

After scraping the data, you can analyze it by running the `data_processor.py` script:

```
python data_processor.py
```

This script loads the data from `reddit_posts.csv` and prints out the top 5 authors by total upvotes.

## Project Structure

- `requirements.txt`: Lists the Python libraries required for the project.
- `config.py`: Contains configuration variables such as Reddit API credentials and subreddit details.
- `scraper.py`: The main script for scraping subreddit posts.
- `data_processor.py`: Contains functions for loading and analyzing the scraped data.
- `README.md`: This file, providing an overview of the project and instructions for setting it up and running it.

## License

This project is open-source and available under the MIT License. See the LICENSE file for more details.
