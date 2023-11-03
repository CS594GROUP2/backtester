import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import pandas as pd
import numpy as np
import pandas_ta as pta
import matplotlib.pyplot as plt

from core.data import Data
from core.signals import SignalGenerator, generate_signals
from core.Simulator import Simulator

# create an instance of the Data class
data_grabber = Data()

price_data = price_data = pd.read_csv('AAPL.csv', index_col='Date', parse_dates=True)
metadata = {'start': price_data.index[0], 'end': price_data.index[-1], 'interval': '1d', 'ticker': 'AAPL', 'indicator': 'SMA', "params": {'length': 20}}
ma_20 = pta.sma(price_data['Close'], 20)

#construct a signal generator from SignalGenerator in signals.py
signal_generator = SignalGenerator(price_data['Close'], metadata)
# signal_generator.generate_random(100, 0.5, 0.5)
signal_generator.generate_above_below(ma_20)

strategy_instance = signal_generator.get_results()

print(strategy_instance)




# # generate some trading signals using the above_below method
# # signal_generator.generate_above_below(ma_20, price_data['Close'], metadata)

# # strategy_instance = signal_generator.get_results()

# strategy_instance = signal_generator.generate_above_below(ma_20, price_data['Close'], metadata)

# # extract the trading signals from the strategy_instance
# trading_signals = strategy_instance[0]

# # extract the price data from the strategy_instance
# price_data_np = strategy_instance[1]


# print("Strategy Instance:\n")
# print(strategy_instance)



# simulation_metadata = {}
# """ 
# # make a trading signals df with the trading signals and the index from the price data
# trading_signals_df = pd.DataFrame(trading_signals)
# trading_signals_df.index = price_data.index

# """



# # # call the simulator to simulate the trading strategy
# # simulator = Simulator()

# # simulation = simulator.simulate(signal_generator, simulation_metadata)

# # print(simulator.win_loss_percents)

# # # print the stats from the simulation
# # print(simulator.stats)

# """ 
# # use matplotlib to plot the price data and the moving average overlayed on one chart
# fig, ax = plt.subplots(figsize=(16,9))
# ax.plot(price_data['Close'], label='Close')
# ax.plot(ma_20, label='20 period MA')

# print(price_data.index)

# normalized_portfolio_values = win_loss_df['portfolio_values'] / win_loss_df['portfolio_values'][0] * price_data_np[0]


# ax.plot(price_data.index, normalized_portfolio_values, label='Portfolio Values', color='green')

# # create a scatter plot with the trading signals
# # use the trading signals to plot the entry points
# ax.scatter(trading_signals_df[trading_signals_df['Signals'] == 1].index, 
#             ma_20[trading_signals_df['Signals'] == 1], 
#             label='Buy', color='green', marker='^', linewidths=5)

# # use the trading signals to plot the exit points
# ax.scatter(trading_signals_df[trading_signals_df['Signals'] == -1].index, 
#             ma_20[trading_signals_df['Signals'] == -1], 
#             label='Sell', color='red', marker='v', linewidths=5)

# # plot metadata
# ax.legend(loc='best')
# ax.set_title('Price Data w/ 20 period MA and crossover strategy signals')
# ax.set_ylabel('Price')
# ax.set_xlabel('Date')

# plt.show()

#  """






