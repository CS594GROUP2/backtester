import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import timeit

import pandas as pd
import pandas_ta as pta
import numpy as np
import matplotlib.pyplot as plt

from core.data import Data
from core.signals import SignalGenerator
from core.simulator import Simulator

# DATA
# create an instance of the Data class
data_grabber = Data()

price_data = pd.read_csv('AAPL.csv', index_col='Date', parse_dates=True)
metadata = {'start': price_data.index[0], 'end': price_data.index[-1],
            'interval': '1d', 'ticker': 'AAPL', 'indicator': 'SMA', "params": {'length': 20}}
ma_20 = pta.sma(price_data['Close'], 20)


# SIGNAL GENERATOR
# construct an array of random strategies from SignalGenerator in signals.py
num_strategies = 100
data_length = len(price_data['Close'])
strategy_instances = np.empty(num_strategies, dtype=SignalGenerator)

for i in range(num_strategies):
    strategy_instances[i] = SignalGenerator(price_data['Close'])
    strategy_instances[i].generate_random(data_length, 0.08, 0.08)

index = pd.Index(range(num_strategies))

# SIMULATOR
simulator = Simulator(strategy_instances[0], 0.04)
results = simulator.simulate_all_helper(strategy_instances, index)


print(results)

exectution_time = timeit.timeit(lambda: simulator.simulate_all_helper(strategy_instances, index), number=1000)


print(f"total execution time: {exectution_time} seconds")
