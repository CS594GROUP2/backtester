import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import pandas as pd
import pandas_ta as pta

from core.data import Data
from core.visualize_1d_strategy import Visualize1DStrategy

# DATA
# create an instance of the Data class
data_grabber = Data()

# Mock Data
# price_data = pd.read_csv('AAPL.csv', index_col='Date', parse_dates=True)
# metadata = {'start': price_data.index[0], 'end': price_data.index[-1], 'interval': '1d', 'ticker': 'AAPL', 'indicator': 'SMA', "params": {'length': 20}}
# ma_20 = pta.sma(price_data['Close'], 20)

#fetch some historical price data
start = pd.Timestamp('2020-01-01')
end = pd.Timestamp('2021-01-01')
interval = pd.Timedelta('1d')
ticker = 'AAPL'

data = data_grabber.get_price_data(start, end, interval, ticker)

price_data = data[0]

metadata = data[1]

ma_20 = pta.sma(price_data['Close'], 20)

# Pass price_data and strategy (ma_20) to Visualize1DStrategy (as well as metadata)
visualizer = Visualize1DStrategy(price_data, ma_20, metadata)
visualizer.visualize()
