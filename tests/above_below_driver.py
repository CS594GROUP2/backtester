import pandas as pd
import numpy as np
import ta
import matplotlib.pyplot as plt
import sys
sys.path.append('/Users/dreed22/Documents/Github/backtester/')
import core
from core.data import Data
from core.signals import SignalGenerator


# makes a new dataframe and copies the elements from the numpy array into it matching them with the dateTimes from the price data df
def np_to_df_with_index(np_array, df):
    df = pd.DataFrame(index=df.index, columns=['Signals'])
    for i in range(0, np_array.size):
        df.iloc[i] = np_array[i]
    return df


# create an instance of the Data class
data_grabber = Data()


#fetch some historical price data
start = pd.Timestamp('2020-01-01')
end = pd.Timestamp('2021-01-01')
interval = pd.Timedelta('1d')
ticker = 'AAPL'

data = data_grabber.get_price_data(start, end, interval, ticker)

price_data = data[0]

metadata = data[1]

#construct a signal generator from SignalGenerator in signals.py
signal_generator = SignalGenerator()


# use pandas-ta to compute the 20 period moving average of the closing price
ma_20 = ta.trend.sma_indicator(price_data['Close'], 20)

trading_signals = signal_generator.above_below(price_data, ma_20, metadata)[0]

print(trading_signals  )

trading_signals_df = np_to_df_with_index(trading_signals, price_data)


# use matplotlib to plot the price data and the moving average overlayed on one chart
fig, ax = plt.subplots(figsize=(16,9))
ax.plot(price_data['Close'], label='Close')
ax.plot(ma_20, label='20 period MA')
#need to plot the entry and exit signals separately as we want to use different colors


# create a scatter plot with the trading signals
# use the trading signals to plot the entry points
ax.scatter(trading_signals_df[trading_signals_df['Signals'] == 1].index, 
            ma_20[trading_signals_df['Signals'] == 1], 
            label='Buy', color='green', marker='^', linewidths=5)

# use the trading signals to plot the exit points
ax.scatter(trading_signals_df[trading_signals_df['Signals'] == -1].index, 
            ma_20[trading_signals_df['Signals'] == -1], 
            label='Sell', color='red', marker='v', linewidths=5)


ax.legend(loc='best')
ax.set_title('Price Data w/ 20 period MA and crossover strategy signals')
ax.set_ylabel('Price')
ax.set_xlabel('Date')
plt.show()






