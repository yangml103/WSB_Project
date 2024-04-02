import pandas as pd
import matplotlib as plt
import requests
import config
import csv


# Load the ticker_security.csv into a DataFrame
ticker_security_df = pd.read_csv('data/ticker_security.csv')
df_original = pd.read_csv('sentiment_analysis_results.csv')

# Note API limit is 25 per day

alpha_vantage_api_key = config.ALPHA_VANTAGE_API_KEY



def load_tickers_and_companies(csv_file_path):
    """Load tickers and company names from a CSV file into lists."""
    tickers = []
    company_names = []
    
    with open(csv_file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            # Assuming the ticker is in the first column and the company name is in the second
            tickers.append(row[0])
            company_names.append(row[1])
    
    return tickers, company_names

# Example usage
tickers, company_names = load_tickers_and_companies('data/ticker_security.csv')
#print("Tickers:", tickers)
#print("Company Names:", company_names)

def getTickerandCompany(title):
    """Pass in the title of the post and return the ticker and company name"""
    if "$" in title:
        cleaned_string = title.split(" ")
        ticker, company = None,None
        for word in cleaned_string:
            if '$' in word:
                ticker = word.replace("$", "")
                company = company_names[tickers.index(ticker)]
                break
            if word in company_names:
                company = word
                ticker = tickers[company_names.index(company)]
                break
    else:
        cleaned_string = title.split(" ")
        ticker, company = None,None
        for word in cleaned_string:
            if word in company_names:
                company = word
                ticker = tickers[company_names.index(company)]
                break
            if word in tickers:
                ticker = word
                company = company_names[tickers.index(ticker)]
                break
    return ticker, company 

def process_titles_from_csv(csv_file_path):
    """Process titles from a CSV file to find and print tickers."""
    # Open the CSV file for reading
    with open(csv_file_path, mode='r', encoding='utf-8') as file:
        # Create a CSV reader object
        csv_reader = csv.reader(file)
        
        # Skip the header row
        next(csv_reader, None)
        
        # Iterate through each row in the CSV
        for row in csv_reader:
            # Each row is a list where the first item is the title and the second is the sentiment_type
            title = row[0]
            sentiment_type = row[1]
            #print(f"Title: {title}, Sentiment: {sentiment_type}")
            try:
                ticker, company = getTickerandCompany(title)
                print(ticker, company)

                # Access stock market API to get closing value this month and opening value last month
                url = f'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol={ticker}&apikey={alpha_vantage_api_key}'
                r = requests.get(url)
                data = r.json()
                keys = list(data['Monthly Time Series'].keys())
                current_month = keys[0]
                prev_month = keys[1]
                current_month_value = data['Monthly Time Series'][current_month]['4. close'] # closing value this month
                prev_month_value = data['Monthly Time Series'][prev_month]['1. open'] # opening value this month
                #print("Current: "+current_month_value)
                #print("Previous: "+prev_month_value)
                value_change = (int(prev_month_value) - int(current_month_value)) 
                #print("Change:",value_change)
                if value_change > 0:
                    print(f"{company} is up {value_change}, sentiment: {sentiment_type}")
                    if sentiment_type == "positive":
                        print(f"Sentiment matched company performance")
                    else:
                        print(f"Sentiment did not match company performance")
                else:
                    print(f"{company} is down {value_change}, sentiment: {sentiment_type}")
                    if sentiment_type == "negative":
                        print(f"Sentiment matched company performance")
                    else:
                        print(f"Sentiment did not match company performance")
            except:
                print(f"{title} ticker not found")

# Example usage
csv_file_path = 'sentiment_analysis_results.csv'
process_titles_from_csv(csv_file_path)





