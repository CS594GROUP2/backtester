import matplotlib.pyplot as plt
import numpy as np
from core.signals import SignalGenerator
from core.simulator import Simulator
from core.generate_bubble_plot import BubblePlotGenerator

class Visualize1DStrategy:

    def __init__(self, price_data, strategy, metadata):
        self.price_data = price_data
        self.strategy = strategy
        self.metadata = metadata

    def visualize(self):
        # Construct a signal generator from SignalGenerator in signals.py
        strategy_instance = SignalGenerator(self.price_data['Close'])
        strategy_instance.generate_above_below(self.strategy, self.metadata)

        # Get the output of the SignalGenerator
        strategy_output = strategy_instance.get_results()

        # Construct a simulator
        simulator_instance = Simulator(strategy_instance, self.metadata)
        simulator_instance.simulate()

        # Extract data from the simulator
        win_loss_stats = simulator_instance.win_loss_stats
        simulator_output = simulator_instance.get_results()

        # Extract dates from the price_data index
        dates = self.price_data.index

        # Generate and display the above-below signal plot
        self.above_below_signal_plot(simulator_output)

        # Generate and display the bubble plot
        self.generate_bubble_plot(simulator_output, dates)

    def above_below_signal_plot(self, simulation_output):
        # Variables for the graph
        portfolio_values_graph = simulation_output['win_loss']['portfolio_values']
        price_data_graph = simulation_output['input']['price_data']
        trading_signals_graph = simulation_output['input']['trading_signals']
        normalized_portfolio_values = portfolio_values_graph / portfolio_values_graph[0] * price_data_graph[0]

        # Use matplotlib to plot the price data and the moving average overlaid on one chart
        fig, ax = plt.subplots(figsize=(16, 9))
        ax.plot(simulation_output['input']['price_data'], label='Close')
        ax.plot(self.strategy, label='20 period MA')
        ax.plot(price_data_graph.index, normalized_portfolio_values, label='Portfolio Values', color='green')

        # Create a scatter plot with the trading signals
        ax.scatter(trading_signals_graph[trading_signals_graph == 1].index,
                   self.strategy[trading_signals_graph == 1],
                   label='Buy', color='green', marker='^', linewidths=5)

        # Split trading signals
        ax.scatter(trading_signals_graph[trading_signals_graph == -1].index,
                   self.strategy[trading_signals_graph == -1],
                   label='Sell', color='red', marker='v', linewidths=5)

        # Plot metadata
        ax.legend(loc='best')
        ax.set_title('Price Data w/ 20 period MA and crossover strategy signals')
        ax.set_ylabel('Price')
        ax.set_xlabel('Date')

        plt.show()

    def generate_bubble_plot(self, simulator_output, dates):
        # Create BubblePlotGenerator instance
        bubble_plot_generator = BubblePlotGenerator(simulator_output, dates)

        # Generate and display the bubble plot
        bubble_plot_generator.generate_bubble_plot()
