import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime as dt

class Visualizer:

    def __init__(self) -> None:
        pass

    def visualize_strategy(self, price_data, trading_signals, win_loss_percents, portfolio_values):
        self.generate_line_plot(price_data, portfolio_values, trading_signals)
        self.generate_bubble_plot(win_loss_percents, price_data)
    
    def generate_line_plot(self, price_data, portfolio_values, trading_signals, column_index='Close'):

        """
            Displays a line plot that represents the results of a given trading strategy, with lines to represent
            the price data for the asset, portfolio values, and trading signal indicators. Note that portfolio values
            are normalized relative to the price data

            Args:
                price_data: A Pandas DataFrame containing the price data in OHLCV format
                portfolio_values: A NumPy array containing the portfolio values to be plotted
                trading_signals: A NumPy array containing buy and sell indicators
                column_index: Index for which column in the price_data will be plotted, defaults to 'Close'

        """

        if len(price_data) != len(portfolio_values):
            raise ValueError('price_data must be the same length as portfolio_values')
        if len(portfolio_values) != len(trading_signals):
            raise ValueError('portfolio_values must be the same length as trading_signals')

        try:
            price_data_column = price_data[column_index]
        except KeyError:
            print(f"{column_index} is not a valid index for price_data")

        # create a list of dates for the x-axis
        dates = [dt.strptime(d, "%Y-%m-%d").date() for d in price_data['Date']]

        # graph the price_data values:
        stock_line = plt.plot(dates, price_data_column, label='Asset Price', color='blue', linewidth=1)

        # graph normalized portfolio values to compare to price_data:
        normalized_portfolio_values = portfolio_values / portfolio_values[0] * price_data['Close'][0]
        port_line = plt.plot(dates, normalized_portfolio_values, label='Normalized Portfolio Value', color='green')

        # create a list of dates to match the positive and negative trading signals:
        buy_dates = []
        sell_dates = []

        for i in range(len(trading_signals)):
            if trading_signals[i] > 0:
                buy_dates.append(dates[i])
            elif trading_signals[i] < 0:
                sell_dates.append(dates[i])

        # plot the trading signals using scatter function:

        plt.scatter(buy_dates, price_data_column[trading_signals > 0],
                    label='Buy', color='green', marker='^', linewidths=3)

        plt.scatter(sell_dates, price_data_column[trading_signals < 0],
                    label='Sell', color='red', marker='v', linewidths=3)

        # set labels and display the graph:
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.title('Strategy Result')
        plt.legend(loc='best')

        plt.show()


