import pandas as pd
import yfinance as yf

class GetData:
    def __init__(self) -> None:
        pass

    def get_price_data(start: pd.Timestamp, end: pd.Timestamp, period: str, ticker: str) -> pd.DataFrame:
        """
        Gets price data for a given symbol, start and end date, and period.

        Args:
        start: The start date for the price data.
        end: The end date for the price data.
        period: The period (frequency/interval) for the price data.
            ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']

        Returns:
        A Pandas DataFrame containing the price data, with columns:
            Open, High, Low, Close, Volume, Symbol, ... (additional columns).
        """

        # Get the price data from Yahoo Finance.
        ticker = yf.Ticker(ticker)

        # Get the price data for the given period or by date range.
        if start is not None and end is not None:
            df = ticker.history(start=start, end=end, period=None)
        else:
            df = ticker.history(start=None, end=None, period=period)
        
        # Check for NaN's in the price data.
        if df.isnull().values.any():
            raise ValueError("NaN's found in price data.")

        # Add additional columns to the price data.
        df['Symbol'] = ticker.info.get('symbol')

        return df