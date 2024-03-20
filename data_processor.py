import pandas as pd

def load_data(filename="reddit_posts.csv"):
    """
    Loads the data from a CSV file into a pandas DataFrame.
    
    :param filename: The filename of the CSV file to load.
    :return: A pandas DataFrame containing the loaded data.
    """
    try:
        df = pd.read_csv(filename)
        print(f"Data loaded from {filename}")
        return df
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return None

def analyze_data(df):
    """
    Performs basic analysis on the DataFrame such as top authors by post upvotes.
    
    :param df: The pandas DataFrame containing the Reddit posts data.
    """
    if df is not None and not df.empty:
        top_authors = df.groupby('author')['upvotes'].sum().sort_values(ascending=False).head(5)
        print("Top 5 authors by total upvotes:")
        print(top_authors)
    else:
        print("DataFrame is empty. No data to analyze.")

def main():
    """
    Main function to load and analyze the Reddit posts data.
    """
    filename = "reddit_posts.csv"
    df = load_data(filename)
    analyze_data(df)

if __name__ == "__main__":
    main()
