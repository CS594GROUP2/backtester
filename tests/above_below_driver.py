import pandas as pd
import numpy as np
import ta
import matplotlib.pyplot as plt
from core import signals
from core import Data


# create an instance of the Data class
data_grabber = Data()

#fetch some historical price data

start = pd.Timestamp('2020-01-01')
end = pd.Timestamp('2021-01-01')
interval = pd.Timedelta('1d')
ticker = 'AAPL'

price_data = data_grabber.get_price_data(start, end, interval, ticker)

# use pandas-ta to compute the 20 period moving average of the closing price
ma_20 = ta.trend.sma_indicator(price_data['Close'], 20)

'''

here we are going to generate some signals using the above_below function
then we are going to want to plot them on an overlay with the price_data
as well as the moving average to create a demonstratration of the 
above_below strategy

'''


# use matplotlib to plot the price data and the moving average overlayed on one chart
fig, ax = plt.subplots(figsize=(16,9))
ax.plot(price_data['Close'], label='Close')
ax.plot(ma_20, label='20 period MA')
#need to plot the entry and exit signals separately as we want to use different colors
ax.legend(loc='best')
ax.set_title('Price Data w/ 20 period MA and crossover strategy signals')
ax.set_ylabel('Price')
ax.set_xlabel('Date')
plt.show()




