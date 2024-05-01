import pandas as pd

# File for testing data on s and p companies 

def isolate_ticker_security(input_file, output_file):
    # Read the input CSV file
    df = pd.read_csv(input_file)
    
    # Select only the 'Symbol' and 'Security' columns
    df_subset = df[['Symbol', 'Security']]
    
    # Save the selected columns to a new CSV file
    df_subset.to_csv(output_file, index=False)

# Call the function with the input and output file paths
#isolate_ticker_security('data/s_and_p_companies.csv', 'data/ticker_security.csv')

