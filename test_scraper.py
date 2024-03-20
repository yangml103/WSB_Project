import praw
import config
import csv
# Initialize PRAW with your client credentials
reddit = praw.Reddit(
    client_id=config.CLIENT_ID,
    client_secret=config.CLIENT_SECRET,
    user_agent=config.USER_AGENT
)

# Choose the subreddit
subreddit = reddit.subreddit('wallstreetbets')

# Open a CSV file to write the posts
with open('wsb_posts.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(['Title', 'URL', 'Top Comments'])
# Fetch the top posts from the subreddit

    for post in subreddit.hot(limit=10):
        post.comments.replace_more(limit=0)
        top_comments = []
        for comment in post.comments.list()[:5]:  # Adjust to fetch more or fewer comments
            top_comments.append(comment.body)

        # Write post details
        writer.writerow([post.title, post.url, top_comments])
