import pandas as pd
import yfinance as yf
from get_data import get_price_data

def main():
    try:
        # Test invalid period
        start = pd.Timestamp('2023-01-01')
        end = pd.Timestamp('2023-01-10')
        invalid_period = pd.Timedelta('3T')  # 3 minutes
        ticker = 'AAPL'
        get_price_data(start, end, invalid_period, ticker)
    except ValueError as e:
        print(f"Test: Invalid Period\n{e}\n")

    try:
        # Test data from 1800s
        start = pd.Timestamp('1800-01-01')
        end = pd.Timestamp('1800-12-31')
        period = '1d'
        ticker = 'AAPL'
        get_price_data(start, end, period, ticker)
    except ValueError as e:
        print(f"Test: Data from 1800s\n{e}\n")

    valid_periods = ['1m', '1d', '1mo', '3mo', '6mo', '1y']
    start = pd.Timestamp('2023-01-01')
    end = pd.Timestamp('2023-12-31')
    ticker = 'AAPL'

    for period in valid_periods:
        try:
            data = get_price_data(start, end, period, ticker)
            print(f"Test: Valid Period ({period})")
            print(data.head())
            print("\n")
        except ValueError as e:
            print(f"Test: Valid Period ({period})\n{e}\n")

if __name__ == '__main__':
    main()

