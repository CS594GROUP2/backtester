import pandas as pd
import yfinance as yf
from get_data import get_price_data

def main():
    try:
        # Test invalid period
        start = pd.Timestamp('2023-01-01')
        end = pd.Timestamp('2023-01-10')
        invalid_period = pd.Timedelta( 3, 'm')  # 3 minutes
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

    #test intraday time_aggregates
    valid_periods = [pd.Timedelta( 1 , 'm' )
                     pd.Timedelta( 5 , 'm' )
                     pd.Timedelta( 1 , 'h' )
                    ]
    start = pd.Timestamp('2022-12-25')
    end = pd.Timestamp('2022-12-31')
    ticker = 'AAPL'


    for period in valid_periods:
        data = get_price_data(start, end, period, ticker)
        print(f"Test Pass: Valid Period ({period})")
        print(data.head())
        print("\n")


    #test daily time_aggregates
    valid_periods = [pd.Timedelta( 1 , 'd' )
                     pd.Timedelta( 5 , 'd' )
                    ]
    start = pd.Timestamp('2022-01-01')
    end = pd.Timestamp('2022-12-31')
    ticker = 'AAPL'


    for period in valid_periods:
        data = get_price_data(start, end, period, ticker)
        print(f"Test Pass: Valid Period ({period})")
        print(data.head())
        print("\n")


if __name__ == '__main__':
    main()

