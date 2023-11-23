import matplotlib.pyplot as plt
import numpy as np

from core.generate_bubble_plot import BubblePlotGenerator


class Visualize1DStrategy:

    def __init__(self, simulator_instance):
        self.simulator_instance = simulator_instance

    def visualize(self):
        # Extract data from the simulator
        win_loss_stats = self.simulator_instance.win_loss_stats
        price_data = self.simulator_instance.strategy_instance.price_data
        output = self.simulator_instance.get_results()

        # Extract dates from the price_data index
        dates = price_data.index

        # Create BubblePlotGenerator instance
        bubble_plot_generator = BubblePlotGenerator(output, dates)

        # Generate and display the bubble plot
        bubble_plot_generator.generate_bubble_plot()
