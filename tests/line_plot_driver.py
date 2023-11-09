import os
import pandas as pd
from core.signals import SignalGenerator
from core.Simulator import Simulator
from core.visualizer import Visualizer

# import stock data from csv file
current_dir = os.getcwd()
parent_directory = os.path.join(current_dir, '..')
file_name = 'AAPL.csv'
file_path = os.path.join(parent_directory, file_name)
data = pd.read_csv(file_path)

metadata = data.loc[:, "Date"]

# extract closing price data to numpy array
price_data_np = data['Close'].to_numpy()

# construct a signal generator from SignalGenerator in signals.py
signal_generator = SignalGenerator()

# generate some trading signals using the random_signals method
trading_signals = signal_generator.random_signals(len(price_data_np), 0.08, 0.08)

# call the simulator to simulate the trading strategy
simulator = Simulator()
starting_cash = 1000

# extract portfolio_values from the calculate_trades_win_loss method :
trades_win_loss = simulator.calculate_trades_win_loss(price_data_np, trading_signals, starting_cash)
port_values = trades_win_loss[2]

# generate a line plot using visualizer method
visualiser = Visualizer()

visualiser.generate_line_plot(data, port_values, trading_signals)
