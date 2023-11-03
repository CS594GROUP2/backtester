import pandas as pd
import numpy as np

class MockData:
    def __init__(self) -> None:
        pass

    def get_price_data(self): 
        # Define the date range and interval
        start = pd.Timestamp('2020-01-01')
        end = pd.Timestamp('2021-01-01')
        interval = pd.Timedelta('1d')

        # Create a date range
        date_range = pd.date_range(start, end, freq=interval)

        # Generate mock stock data
        np.random.seed(0)
        mock_data = {
            'Open': np.random.uniform(125, 135, len(date_range)),
            'High': np.random.uniform(135, 145, len(date_range)),
            'Low': np.random.uniform(125, 135, len(date_range)),
            'Close': np.random.uniform(135, 145, len(date_range)),
            'Volume': np.random.randint(1000000, 5000000, size=len(date_range))
        }

        # Create a DataFrame
        df = pd.DataFrame(mock_data, index=date_range)

        return df
