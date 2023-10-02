import pandas as pd
import numpy as np
import ta
import matplotlib.pyplot as plt
import sys
sys.path.append('/Users/dreed22/Documents/Github/backtester/')
import core
from core.data import Data
from core.signals import SignalGenerator


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

print(price_data)
#print(price_data['Close'])

if isinstance(price_data, pd.DataFrame):
    print("\n price_data is a dataframe \n ")

trading_signals = signal_generator.above_below(price_data, ma_20, metadata)



'''

# use matplotlib to plot the price data and the moving average overlayed on one chart
fig, ax = plt.subplots(figsize=(16,9))
ax.plot(price_data['Close'], label='Close')
ax.plot(ma_20, label='20 period MA')
#need to plot the entry and exit signals separately as we want to use different colors

#create a new arrays to distinguish positive and negative signals
pos_signals = np.zeros_like(trading_signals, dtype=np.int8)
neg_signals = np.zeros_like(trading_signals, dtype=np.int8)

# loop through and collect the positive and negative trading signals
for i in range(0, trading_signals.size):
    if trading_signals[i] == 1:
        pos_signals[i] = 1
    elif trading_signals[i] == -1:
        neg_signals[i] = 1

#plot the positive trading signals as green up arrows at the point price_data[i]
ax.scatter(price_data.index, price_data['Close'][pos_signals == 1], marker='^', color='g', label='Buy')

#plot the negative trading signals as red down arrows at the point price_data[i]
ax.scatter(price_data.index, price_data['Close'][neg_signals == 1], marker='v', color='r', label='Sell')


ax.legend(loc='best')
ax.set_title('Price Data w/ 20 period MA and crossover strategy signals')
ax.set_ylabel('Price')
ax.set_xlabel('Date')
plt.show()




'''