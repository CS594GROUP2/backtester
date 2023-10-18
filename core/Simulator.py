import numpy as np
import pandas as pd
import numba as nb


# loops through price_data and trading_signals, performing calculations and updating other 3 arrays
@nb.jit(nopython=True)
def win_loss_loop(trading_signals, price_data, portfolio_values, win_loss_percents, win_loss):

    # iterate through trading signals
    for i in range(trading_signals.size):
        # Forward filling portfolio_values:
        if i > 0:
            portfolio_values[i] = portfolio_values[i - 1]

        # if trading signal is positive, store the entry price and starting portfolio value
        if trading_signals[i] > 0:
            entry_price = price_data[i]
            entry_portfolio_value = portfolio_values[i]

        # if trading signal is negative, compare the entry and exit prices and portfolio values and store in arrays
        if trading_signals[i] < 0:
            win_loss_percents[i] = price_data[i] / entry_price
            portfolio_values[i] = win_loss_percents[i] * entry_portfolio_value
            win_loss[i] = portfolio_values[i] - entry_portfolio_value

class Simulator:

    def __init__(self) -> None:
        pass

        def calculate_trades_win_loss(self, price_data, trading_signals, starting_cash):
        """
            Calculates the win/loss percentages and dollar amounts for a given set of trading signals and price data.

            Args:
                price_data: An array of price data to calculate the strategy on
                trading_signals: A matching array of indicators to reflect a trading strategy
                starting_cash: The starting value for the portfolio
            Returns:
                win_loss[]: Holds trade gain/loss in dollar amounts
                win_loss_percents[]: Holds the portfolio percent change as a result of closing trades
                portfolio_values[]: Holds the portfolio value and is only be updated on closing trades
        """

        if starting_cash < 0:
            raise ValueError("starting_cash must be greater than 0")
        if price_data.size != trading_signals.size:
            raise ValueError("price_data and trading_signals must be the same size")

        win_loss = np.zeros_like(trading_signals)
        win_loss_percents = np.zeros_like(trading_signals)
        portfolio_values = np.empty_like(trading_signals)
        
        # start the portfolio_values at starting_cash
        portfolio_values[0] = starting_cash

        # call numba function to efficiently iterate through and compute array values
        win_loss_loop(trading_signals, price_data, portfolio_values, win_loss_percents, win_loss)

        # return all three new arrays
        arrays =[win_loss, win_loss_percents, portfolio_values]

        return arrays
