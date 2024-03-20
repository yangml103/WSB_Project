import praw
import config
import csv

def initialize_reddit():
    """Initialize and return a Reddit instance using PRAW."""
    reddit = praw.Reddit(
        client_id=config.CLIENT_ID,
        client_secret=config.CLIENT_SECRET,
        user_agent=config.USER_AGENT
    )
    return reddit


def fetch_posts(subreddit_name, limit=15):
    """Fetch posts from a given subreddit."""
    reddit = initialize_reddit()
    subreddit = reddit.subreddit(subreddit_name)
    return subreddit.hot(limit=limit)

def fetch_top_comments(post, limit=10):
    """Fetch top comments from a given post."""
    post.comments.replace_more(limit=0)
    top_comments = [comment.body for comment in post.comments.list()[:limit]]
    return top_comments

def save_posts_to_csv(posts, filename='wsb_posts.csv'):
    """Save posts and their top comments to a CSV file."""
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'URL', 'Top Comments'])
        for post in posts:
            top_comments = fetch_top_comments(post)
            # Join comments with a newline for better readability in the CSV
            comments_str = "\n".join(top_comments)
            writer.writerow([post.title, post.url, comments_str])

def main():
    subreddit_name = 'wallstreetbets'
    posts = fetch_posts(subreddit_name)
    save_posts_to_csv(posts)

if __name__ == "__main__":
    main()

    
