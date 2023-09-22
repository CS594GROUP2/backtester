import pandas as pd
from core import Data


def main():
    print("Welcome to the Stock Price Data Retrieval Tool!")

    # Ask the user for input
    ticker = input("Enter the stock ticker symbol (e.g., AAPL): ")

    # Prompt the user to choose between period and date range
    choice = input("Do you want to specify a period (P) or a date range (D)? ").strip().lower()

    if choice == "p":
        # User wants to specify a period
        period = input("Enter the data period (e.g., 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max): ")
        start_date = None
        end_date = None
    elif choice == "d":
        # User wants to specify a date range
        start_date = input("Enter the start date (YYYY-MM-DD): ")
        end_date = input("Enter the end date (YYYY-MM-DD): ")
        interval = None
    else:
        print("Invalid choice. Please choose 'P' for period or 'D' for date range.")
        return

    try:
        # convert to pandas data types
        start_date = pd.Timestamp(start_date) if start_date else None
        end_date = pd.Timestamp(end_date) if end_date else None
        interval = str(interval)

        # Get price data using the GetData class
        data = Data.get_price_data(start=start_date, end=end_date, interval=interval, ticker=ticker)

        # Display the retrieved data
        print("Price data for {} from {} to {}:".format(ticker, start_date, end_date))
        print(data)
    except Exception as e:
        print("An error occurred:", str(e))


# if __name__ == "__main__":
#     main()

start_date = pd.Timestamp("2021-01-01")
end_date = pd.Timestamp("2021-12-31")
interval = pd.Timedelta("1d")

market_data = Data()
data = market_data.get_price_data(start=start_date, end=end_date, interval=interval, ticker="AAPLAA")

print(data)
print(data.columns)