import praw
import config
# Initialize PRAW with your client credentials
reddit = praw.Reddit(
    client_id=config.client_id,
    client_secret=config.client_secret,
    user_agent=config.user_agent
)

# Choose the subreddit
subreddit = reddit.subreddit('wallstreetbets')

# Fetch the top posts from the subreddit
for post in subreddit.hot(limit=10):  # Adjust limit as needed
    print(f"Title: {post.title}")
    print(f"URL: {post.url}")
    print("Comments:")
    post.comments.replace_more(limit=0)  # Limit to top-level comments; adjust as needed
    for comment in post.comments.list()[:5]:  # Adjust to fetch more or fewer comments
        print(f"- {comment.body}")
    print("\n---\n")