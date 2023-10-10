import numpy as np

class Portfolio:

    # Constructor to initialize the portfolio

    def __init__(self, starting_cash):
        self.starting_cash = starting_cash

    # getters
    
    def get_starting_cash(self) -> float:

        return self.starting_cash

    def calculate_trades_win_loss(self, price_data, trading_signals):
        # create two new numPy array symetric to the trading signals using zeros_like()
        # win_loss[] will hold trade gain/loss in dollar amounts
        win_loss = np.zeros_like(trading_signals)

        # win_loss_percents[] will hold the portfolio percent change as a result of the most recent closing trade
        win_loss_percents = np.zeros_like(trading_signals)

        # for this third array create a structured numpy array to hold the time stamps
        # portfolio_values[] will hold the portfolio value and only be updated on closing trades
        portfolio_values = np.zeros_like(trading_signals, dtype=[('value', 'f'), ('time', 'f')])

        """
        iterate through trading signals and when you encounter a positive trading signal,
		record the price_data[i] as entry_price where "i" is where you encountered the positive signal
		also store testing_on[i] as entry_portfolio_value
		now continue iterating through trading_signals[] until you encounter a negative trading signal
		then multiply the value at price_data[i] (where "i" is where you encounter the negative signal)
		by entry_price store in win_loss_percents[i] and then multiply that by entry_price and store that value in 
		portfolio_values[i]
		take portfolio_values[i] and subtract entry_portfolio_value and store this difference in win_loss[i]
		forward fill all zeros in portfolio_values[] with last_portfolio_value 
        """

        # return all three new arrays
        return win_loss, win_loss_percents, portfolio_values
