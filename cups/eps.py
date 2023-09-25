import requests
import time
import json

# Replace 'YOUR_API_KEY' with your actual Alpha Vantage API key
api_key = 'KPENG67GT2GIT9P7'

# Define the stock symbol you want to retrieve data for
symbol = 'TSLA'  # Replace with the desired stock symbol

EPSvalues = []

# Make API requests to fetch income statement data for the past 5 years
url = f'https://www.alphavantage.co/query?function=EARNINGS&symbol={symbol}&apikey={api_key}&datatype=csv'
response = requests.get(url)
    
if response.status_code == 200:
        data = response.text

        #for i in range(0,100):
        data_dict = json.loads(data)
        data_dict = data_dict["annualEarnings"]
        for i in range(1,7):
            #print(data_dict[i]["fiscalDateEnding"])
            print(data_dict[i]["reportedEPS"])
            EPSvalues.append(float(data_dict[i]["reportedEPS"]))
            
            #print(str(data[i]) + " " + str(i))
        # Extract the EPS value for the year (assuming it's in a consistent position in the CSV data)
            
    # Sleep to comply with Alpha Vantage rate limits (5 requests per minute)

