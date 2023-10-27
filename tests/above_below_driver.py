import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import pandas as pd
import numpy as np
import pandas_ta as pta
import matplotlib.pyplot as plt

from core.data import Data
from core.signals import SignalGenerator
from core.Simulator import Simulator


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

ma_20 = pta.sma(price_data['Close'], 20)

# generate some trading signals using the above_below method
strategy_instance = signal_generator.above_below(price_data, ma_20, metadata)

# extract the trading signals from the strategy_instance
trading_signals = strategy_instance[0]

# extract the price data from the strategy_instance
price_data_np = strategy_instance[1]

# convert the trading signals numpy array to a pandas dataframe
trading_signals_df = np_to_df_with_index(trading_signals, price_data)




# call the simulator to simulate the trading strategy
simulator = Simulator()

simulation = simulator.simulate(trading_signals, price_data_np, metadata)

# extract the win_loss_df from the simulation
win_loss_df = simulation[0]
print(win_loss_df)

# print the stats from the simulation
print(simulation[3])


# use matplotlib to plot the price data and the moving average overlayed on one chart
fig, ax = plt.subplots(figsize=(16,9))
ax.plot(price_data['Close'], label='Close')
ax.plot(ma_20, label='20 period MA')

print(price_data.index)

normalized_portfolio_values = win_loss_df['portfolio_values'] / win_loss_df['portfolio_values'][0] * price_data_np[0]

ax.plot(price_data.index, normalized_portfolio_values, label='Portfolio Values', color='green')

# create a scatter plot with the trading signals
# use the trading signals to plot the entry points
ax.scatter(trading_signals_df[trading_signals_df['Signals'] == 1].index, 
            ma_20[trading_signals_df['Signals'] == 1], 
            label='Buy', color='green', marker='^', linewidths=5)

# use the trading signals to plot the exit points
ax.scatter(trading_signals_df[trading_signals_df['Signals'] == -1].index, 
            ma_20[trading_signals_df['Signals'] == -1], 
            label='Sell', color='red', marker='v', linewidths=5)

# plot metadata
ax.legend(loc='best')
ax.set_title('Price Data w/ 20 period MA and crossover strategy signals')
ax.set_ylabel('Price')
ax.set_xlabel('Date')

plt.show()








