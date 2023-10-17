import numpy as np
import pandas as pd
import numba as nb


# loops through price_data and trading_signals, performing calculations and updating other 3 arrays
@nb.jit(nopython=True)
def win_loss_loop(trading_signals, price_data, portfolio_values, win_loss_percents, win_loss):

    # iterate through trading signals
    for i in range(trading_signals.size):
        # Forward Filling values:
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
        # create two new numPy array symetric to the trading signals using zeros_like()

        # win_loss[] will hold trade gain/loss in dollar amounts
        win_loss = np.zeros_like(trading_signals)

        # win_loss_percents[] will hold the portfolio percent change as a result of the most recent closing trade
        win_loss_percents = np.zeros_like(trading_signals)

        # portfolio_values[] will hold the portfolio value and only be updated on closing trades
        portfolio_values = np.empty_like(trading_signals)

        # start the portfolio_values at starting_cash
        portfolio_values[0] = starting_cash

        # call numba function to efficiently iterate through and compute array values
        win_loss_loop(trading_signals, price_data, portfolio_values, win_loss_percents, win_loss)

        # return all three new arrays
        arrays =[win_loss, win_loss_percents, portfolio_values]

        return arrays
