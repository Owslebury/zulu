import yfinance as yf

# Function to fetch and display information for a symbol
def get_symbol_info(symbol):
    try:
        # Add ".L" to the symbol to make it a London Stock Exchange symbol
        lse_symbol = symbol + ".L"
        
        # Fetch information for the modified symbol
        stock = yf.Ticker(lse_symbol)
        
        # Display basic information
        print("Symbol:", lse_symbol)
        print("Name:", stock.info.get("shortName", "N/A"))
        print("Exchange:", stock.info.get("exchange", "N/A"))
        print("Industry:", stock.info.get("industry", "N/A"))
        print("Sector:", stock.info.get("sector", "N/A"))
        
        # Display summary statistics
        print("Market Cap:", stock.info.get("marketCap", "N/A"))
        print("Previous Close Price:", stock.history(period="1d")["Close"].iloc[0])
        print("--------------------------------------------------------")
    except Exception as e:
        print(f"Error fetching information for {lse_symbol}: {str(e)}")

# Read symbols from lse.txt and fetch information for each with ".L" added
with open("lse.txt", "r") as file:
    symbols = file.read().splitlines()

for symbol in symbols:
    get_symbol_info(symbol)
