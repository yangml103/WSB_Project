import praw
import config
import csv
import re
from pathlib import Path
import pandas as pd

"""
Helper Functions for Web Scraper
"""

def initialize_reddit():
    """Initialize and return a Reddit instance using PRAW."""
    reddit = praw.Reddit(
        client_id=config.CLIENT_ID,
        client_secret=config.CLIENT_SECRET,
        user_agent=config.USER_AGENT
    )
    return reddit

ticker_data = pd.read_csv('data/ticker_security.csv')
tickers = ticker_data.iloc[:,0].tolist()
company_names = ticker_data.iloc[:,1].tolist()

def fetch_posts(subreddit_name, limit=25):
    """Fetch posts from a given subreddit.
    Limit is the number of posts to fetch
    """
    reddit = initialize_reddit()
    subreddit = reddit.subreddit(subreddit_name)
    filtered_posts = []

    for post in subreddit.hot(limit=limit):
        post_title = post.title.lower()
        post_body = post.selftext.lower()
    
        # # Check if post contains $ticker or company name
        # if any(f'${ticker.lower()}' in post_title or f'${ticker.lower()}' in post_body for ticker in tickers) or any(company.lower() in post_title or company.lower() in post_body for company in company_names):
        #     filtered_posts.append(post, ticker.lower(), company.lower())
        
        # Find matching tickers and company names
        matching_tickers = [ticker for ticker in tickers if f'${ticker.lower()}' in post_title or f'${ticker.lower()}' in post_body]
        matching_companies = [company for company in company_names if company.lower() in post_title or company.lower() in post_body]

        # If there are any matches, append them to filtered_posts
        if matching_tickers or matching_companies:
            filtered_posts.append((post, matching_tickers, matching_companies))
        
    return filtered_posts

def fetch_top_comments(post, limit=5):
    """Fetch top comments from a given post.
    Limit is the number of comments to fetch
    """
    post.comments.replace_more(limit=0) # Don't include replies to comments
    top_comments = [comment.body for comment in post.comments.list()[:limit]]
    # Define a regex pattern to match the unwanted text
    pattern = re.compile(
        r"(\*\*User Report\*\*.*?Account Age.*?years.*?\[.*?\]\(http://discord\.gg/wsbverse\))|"
        r"(!\[img\]\(emote\|t5_2th52\|\d+\))|"
        r"(https?://preview\.redd\.it/[\w./?=&-]+)|"
        r"\*\*User Report\*\*\|.*?\n|"    # Matches the beginning of the table header
        r".*?\n|"  # Matches the table header separator
        r"\*\*Total Submissions\*\* \| \d+ \| \*\*First Seen In WSB\*\* \| \d+ year[s]? ago\n|"  # Matches the first row of the table
        r"\*\*Total Comments\*\* \| \d+ \| \*\*Previous Best DD\*\* \|.*?\n|"  # Matches the second row of the table
        r"\*\*Account Age\*\* \| \d+ year[s]? \| \| \n|"  # Matches the third row of the table
        r"\[\*\*Join WSB Discord\*\*\]\(http://discord\.gg/wsbverse\)",  # Matches the Discord link
        re.DOTALL
    )

    # Remove the matched patterns from each comment
    cleaned_comments = [re.sub(pattern, '', comment) for comment in top_comments]
    
    return cleaned_comments 

def save_posts_to_csv(posts, filename='scraped_wsb_posts.csv'):
    """Save posts and their top comments to a CSV file if the content has changed."""
    # Prepare data for comparison
    new_data = []
    for post_tuple in posts:
        post, matching_tickers, matching_companies = post_tuple
        top_comments = fetch_top_comments(post)
        comments_str = "\n".join(top_comments)
        tickers_str = ", ".join(matching_tickers)
        companies_str = ", ".join(matching_companies)
        new_data.append([post.title, post.url, comments_str, tickers_str, companies_str])
    
    new_df = pd.DataFrame(new_data, columns=['Title', 'URL', 'Top Comments', 'Matching Tickers', 'Matching Companies'])
    
    if Path(filename).exists():
        existing_df = pd.read_csv(filename)
        if not new_df.equals(existing_df):
            new_df.to_csv(filename, index=False, encoding='utf-8')
            print("Updated the CSV file with new data.")
        else:
            print("The existing CSV file already contains the same data. No update needed.")
    else:
        new_df.to_csv(filename, index=False, encoding='utf-8')
        print("Created a new CSV file with the data.")

