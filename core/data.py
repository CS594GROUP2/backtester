import pandas as pd
import yfinance as yf

class TimedeltaConverter:
    def __init__(self):
        self.mapping = {
            pd.Timedelta(minutes=1): '1m',
            pd.Timedelta(minutes=2): '2m',
            pd.Timedelta(minutes=5): '5m',
            pd.Timedelta(minutes=15): '15m',
            pd.Timedelta(minutes=30): '30m',
            pd.Timedelta(minutes=60): '60m',
            pd.Timedelta(hours=1): '1h',
            pd.Timedelta(minutes=90): '90m',
            pd.Timedelta(days=1): '1d',
            pd.Timedelta(days=5): '5d',
            pd.DateOffset(weeks=1): '1wk',
            pd.DateOffset(months=1): '1mo',
            pd.DateOffset(months=3): '3mo',
            pd.DateOffset(months=6): '6mo',
            pd.DateOffset(years=1): '1y',
            pd.DateOffset(years=2): '2y',
            pd.DateOffset(years=5): '5y',
            pd.DateOffset(years=10): '10y',
            pd.offsets.YearBegin(): 'ytd',
            None: 'max'
        }
        
        # Create reverse mapping
        self.reverse_mapping = {v: k for k, v in self.mapping.items()}

    def to_pd(self, timedelta):
        return self.reverse_mapping.get(timedelta)

    def to_string(self, timedelta):
        return self.mapping.get(timedelta)

class Data:
    def __init__(self) -> None:
        self.timedelta_converter = TimedeltaConverter()
    
    def get_price_data(self, start: pd.Timestamp, end: pd.Timestamp, interval: pd.Timedelta, ticker: str) -> pd.DataFrame:
        """
        Gets price data for a given symbol, start and end date, and period.

        Args:
        start: The start date for the price data.
        end: The end date for the price data.
        interval: The period (frequency/interval) for the price data.
                [1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo]

        Returns:
        A Pandas DataFrame containing the price data, with columns:
            Open, High, Low, Close, Volume, Symbol, Period, Start, End
        """

        # Get the price data from Yahoo Finance.
        ticker = yf.Ticker(ticker)
        interval = self.timedelta_converter.to_string(interval)

        df = ticker.history(start=start, end=end, interval=interval)

        
        # Check for NaN's in the price data.
        if df.isnull().values.any():
            raise ValueError("NaN's found in price data.")

        # Add additional columns to the price data.
        df['Symbol'] = ticker.info.get('symbol')
        df["interval"] = interval
        df["Start"] = start
        df["End"] = end

        return df

