
import requests
import time
import json

# Replace 'YOUR_API_KEY' with your actual Alpha Vantage API key
api_key = 'KPENG67GT2GIT9P7'

# Define the stock symbol you want to retrieve data for
symbol = 'AAPL'  # Replace with the desired stock symbol

# Make API requests to fetch income statement data for the past 5 years
for year in range(5):
    url = f'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={symbol}&apikey={api_key}&datatype=csv'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.text

        #for i in range(0,100):
        data_dict = json.loads(data)
        data_dict = data_dict["annualReports"]
        for i in range(0,5):
            print(data_dict[i]["fiscalDateEnding"])
            print(data_dict[i]["netIncome"])
            
            #print(str(data[i]) + " " + str(i))
        # Extract the EPS value for the year (assuming it's in a consistent position in the CSV data)

        
    else:
        print(f'Error fetching data for {year + 1} year(s) ago')

    # Sleep to comply with Alpha Vantage rate limits (5 requests per minute)
    time.sleep(12)  # Sleep for 12 seconds between requests

