from tools.helper import fetch_posts, save_posts_to_csv

"""
WSB Scraper - Main Function
"""

def main():
    subreddit_name = 'wallstreetbets'
    posts = fetch_posts(subreddit_name)
    save_posts_to_csv(posts)

if __name__ == "__main__":
    main()

    
