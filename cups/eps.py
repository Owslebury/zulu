import requests
import time
import json

# Replace 'YOUR_API_KEY' with your actual Alpha Vantage API key
api_key = 'KPENG67GT2GIT9P7'

# Define the stock symbol you want to retrieve data for
symbol = 'TSCO'  # Replace with the desired stock symbol

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
            print(data_dict[i])
            EPSvalues.append(float(data_dict[i]["reportedEPS"]))
            
            #print(str(data[i]) + " " + str(i))
        # Extract the EPS value for the year (assuming it's in a consistent position in the CSV data)

EPSvalues.reverse()

def has_eps_growth_over_years(eps_data):
    if len(eps_data) < 5:
        return False

    # Initialize a counter to keep track of years with growth >= 15%
    growth_count = 0

    for i in range(1, len(eps_data)):
        growth_percentage = ((eps_data[i] - eps_data[i-1]) / abs(eps_data[i-1])) * 100
        if growth_percentage >= 15:
            growth_count += 1

    # Check if there are at least 4 years with growth >= 15%
    if growth_count >= 4:
        return True
    else:
        return False

# Sample EPS data

# Check if there is at least 4 out of 5 years with >= 15% growth
result = has_eps_growth_over_years(EPSvalues)

if result:
    print("There are at least 4 out of 5 years with >= 15% growth.")
else:
    print("There are less than 4 years with >= 15% growth.")

    # Sleep to comply with Alpha Vantage rate limits (5 requests per minute)

