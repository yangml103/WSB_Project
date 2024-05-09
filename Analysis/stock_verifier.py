import pandas as pd
import matplotlib as plt
import requests
import config
import csv
from pathlib import Path
import string

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

# Load tickers and company names 
tickers, company_names = load_tickers_and_companies('data/ticker_security.csv')

def getTickerandCompany(title):
    """Pass in the title of the post and return the ticker and company name"""
    ticker, company = None,None
    if "$" in title:
        cleaned_string = title.split(" ")
        # Check if 's exists in the word and remove it
        cleaned_string = [word.replace("'s", "") for word in cleaned_string]
        # Remove punctuation from each word in cleaned_string
        cleaned_string = [''.join(char for char in word if char not in string.punctuation).replace("'s", "") for word in cleaned_string]
        for word in cleaned_string:

            if word in tickers:
                ticker = word
                company = company_names[tickers.index(ticker)]
                break
            if word in company_names:
                company = word
                ticker = tickers[company_names.index(company)]
                break
    else:
        cleaned_string = title.split(" ")
        # Check if 's exists in the word and remove it
        cleaned_string = [word.replace("'s", "") for word in cleaned_string]
        # Remove punctuation from each word in cleaned_string
        cleaned_string = [''.join(char for char in word if char not in string.punctuation) for word in cleaned_string]
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
    """Process titles from a CSV file to find and print tickers, and save the results to a file."""
    results = []  # Initialize an empty list to store results
    match_count = 0 # Count the number of matches
    no_match_count = 0 # Count the number of no matches

    with open(csv_file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader, None)  # Skip the header row
        
        for row in csv_reader:
            title = row[0]
            sentiment_type = row[1]
            try:
                ticker, company = getTickerandCompany(title)
                print(f"Ticker: {ticker}, Company: {company}")
                url = f'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol={ticker}&apikey={alpha_vantage_api_key}'
                r = requests.get(url)
                data = r.json()
                keys = list(data['Monthly Time Series'].keys())
                current_month = keys[0]
                prev_month = keys[1]
                current_month_value = data['Monthly Time Series'][current_month]['4. close']
                prev_month_value = data['Monthly Time Series'][prev_month]['1. open']
                value_change = (float(prev_month_value) - float(current_month_value))
                
                if value_change > 0:
                    result = f"{company} is up {value_change}, sentiment: {sentiment_type}"
                    if sentiment_type == "Positive":
                        result += " | Sentiment matched company performance"
                        match_count += 1
                    else:
                        result += " | Sentiment did not match company performance"
                        no_match_count += 1
                else:
                    result = f"{company} is down {value_change}, sentiment: {sentiment_type}"
                    if sentiment_type == "Negative":
                        result += " | Sentiment matched company performance"
                        match_count += 1
                    else:
                        result += " | Sentiment did not match company performance"
                        no_match_count += 1
                
                results.append([title, ticker, company, value_change, sentiment_type, result])
            except Exception as ex:
                print(f"Error processing {title}", ex)
                results.append([title, "N/A", "N/A", "N/A", sentiment_type, "Ticker not found"])

    if no_match_count > 0:
        accuracy = (match_count / (match_count + no_match_count)) * 100
    else:
        accuracy = 100  

    results.append([f"Match count: {match_count} No match count: {no_match_count}, Accuracy = {accuracy}", ])    
    
    # Ensure the directory exists
    folder_path = Path('actual_stock_performance_analysis')
    folder_path.mkdir(parents=True, exist_ok=True)  # This creates the directory if it does not exist
    
    # Define your output file name and path
    output_file_name = f'analysis_results_for_{Path(csv_file_path).stem}.csv'
    output_file_path = folder_path / output_file_name
    
    with open(output_file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Ticker', 'Company', 'Value Change', 'Sentiment Type', 'Result'])  # Write header
        writer.writerows(results)  # Write the results
    
    print(f"Analysis complete. Results saved to {output_file_path}")


# Example usage
# Change file path if your folder name/filename is different
csv_file_path = 'sentiment_analysis_results/sentiment_analysis_results_for_scraped_data_2024-04-9.csv'
process_titles_from_csv(csv_file_path)





