import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import pandas as pd
import numpy as np
import numba as nb
import pandas_ta as pta
import matplotlib.pyplot as plt

from core.data import Data
from core.signals import SignalGenerator
from core.simulator import Simulator

# DATA
# create an instance of the Data class
data_grabber = Data()

price_data = pd.read_csv('AAPL.csv', index_col='Date', parse_dates=True)
metadata = {'start': price_data.index[0], 'end': price_data.index[-1], 'interval': '1d', 'ticker': 'AAPL', 'indicator': 'SMA', "params": {'length': 20}}
ma_20 = pta.sma(price_data['Close'], 20)


# SIGNAL GENERATOR
#construct a signal generator from SignalGenerator in signals.py
strategy_instance = SignalGenerator(price_data['Close'])
# signal_generator.generate_random(100, 0.5, 0.5)
strategy_instance.generate_above_below(ma_20, metadata)

strategy_output = strategy_instance.get_results()

print("strategy output:\n")
print(strategy_output)


# SIMULATOR
simulator = Simulator(strategy_instance)
# simulation_stats = simulator.simulate()
simulation_output = simulator.get_results()

print(simulation_output.keys())
print(simulation_output['stats'])


# GRAPHING



