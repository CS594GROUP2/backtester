import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import pandas as pd
import pandas_ta as pta

from core.mockdata import MockData
from core.signals import SignalGenerator
from core.simulator import Simulator

# HELPER FUNCTIONS
# makes a new dataframe and copies the elements from the numpy array into it matching them with the dateTimes from the price data df
def np_to_df_with_index(np_array, df):
    df = pd.DataFrame(index=df.index, columns=['Signals'])
    for i in range(0, np_array.size):
        df.iloc[i] = np_array[i]
    return df

# DATA
mock_data = MockData()
price_data = mock_data.get_price_data()


# ADDTIIONAL DATA
# generate a moving average
ma_20 = pta.sma(price_data['Close'], 20)

metadata = {
    'start': '2021-01-01',
    'end': '2021-12-31',
    'interval': '1d',
    'ticker': 'AAPL'
}


# SIGNAL GENERATOR
signal_generator = SignalGenerator(price_data, metadata)

# random signals
signal_generator.generate_random(20, .5, .5)
for item in signal_generator.get_results():
    print("item: \n", item)
    print("\n\n")

# above below signals
signal_generator.generate_above_below(ma_20)
for item in signal_generator.get_results():
    print("item: \n", item)
    print("\n\n")


# RESULTS
trading_signals = signal_generator.get_results()[0]
price_data = signal_generator.get_results()[1]
metadata = signal_generator.get_results()[2]

trading_signals_df = np_to_df_with_index(trading_signals, price_data)
price_data_used = price_data['Close']



# SIMULATOR
# simulator = Simulator()
# simulation = simulator.simulate(trading_signals, price_data_used, metadata)


# RESULTS
# print("Simulation Results: \n", simulation)