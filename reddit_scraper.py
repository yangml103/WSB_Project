import requests
from bs4 import BeautifulSoup
import pandas as pd
from config import CLIENT_ID, CLIENT_SECRET, USER_AGENT, SUBREDDIT, POST_LIMIT

def get_reddit_data(subreddit, post_limit):
    """
    Fetches posts from a specified subreddit using Reddit's API.
    
    :param subreddit: The subreddit to scrape.
    :param post_limit: The number of posts to fetch.
    :return: A list of dictionaries containing post data.
    """
    base_url = f"https://www.reddit.com/r/{subreddit}/.json"
    headers = {'User-Agent': USER_AGENT}
    params = {'limit': post_limit}
    response = requests.get(base_url, headers=headers, params=params)
    
    if response.status_code == 200:
        posts = []
        data = response.json()
        for post in data['data']['children']:
            post_data = {
                'title': post['data']['title'],
                'author': post['data']['author'],
                'upvotes': post['data']['ups'],
                'comments': post['data']['num_comments'],
                'permalink': f"https://www.reddit.com{post['data']['permalink']}"
            }
            posts.append(post_data)
        return posts
    else:
        print(f"Failed to fetch data from Reddit. Status code: {response.status_code}")
        return []

def save_to_csv(posts, filename="reddit_posts.csv"):
    """
    Saves the list of post dictionaries to a CSV file.
    
    :param posts: The list of post dictionaries.
    :param filename: The filename for the CSV file.
    """
    if posts:
        df = pd.DataFrame(posts)
        df.to_csv(filename, index=False)
        print(f"Data saved to {filename}")
    else:
        print("No data to save.")

if __name__ == "__main__":
    posts = get_reddit_data(SUBREDDIT, POST_LIMIT)
    save_to_csv(posts)
