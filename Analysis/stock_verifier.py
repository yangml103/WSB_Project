import pandas as pd
import matplotlib as plt
import requests
import config
import csv


# Load the ticker_security.csv into a DataFrame
ticker_security_df = pd.read_csv('data/ticker_security.csv')
df_original = pd.read_csv('sentiment_analysis_results.csv')
company = df_original.iloc[0][0]
sentiment = df_original.iloc[0][1]
print(company, sentiment)


alpha_vantage_api_key = config.ALPHA_VANTAGE_API_KEY
#url = f'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=IBM&apikey={alpha_vantage_api_key}'
#r = requests.get(url)
#data = r.json()

#print(data)



# Initialize empty lists for tickers and company names
tickers = []
company_names = []

# Open and read the csv file
with open('data/ticker_security.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        # Assuming the ticker is in the first column and the company name is in the second
        tickers.append(row[0])
        company_names.append(row[1])

# Now tickers and company_names lists are populated with the data from the csv file
print("Tickers:", tickers)
print("Company Names:", company_names)

def getTickerandCompany(title):
    """Pass in the title of the post and return the ticker and company name"""
    if "$" in title:
        cleaned_string = title.split(" ")
        ticker, company = None,None
        for word in cleaned_string:
            if '$' in word:
                company = word.replace("$", "")

                print(company)
            elif word in company_names:
                print(word)
        ticker = company
        company = company_names.index(ticker)
    else:
        cleaned_string = title.split(" ")
        ticker, company = None,None
        for word in cleaned_string:
            if word in company_names:
                company = word
                
        ticker = tickers[company_names.index(company)]
    return ticker, company 



# Specify the path to your CSV file
csv_file_path = 'sentiment_analysis_results.csv'

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
        print(f"Title: {title}, Sentiment: {sentiment_type}")