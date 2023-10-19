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

@nb.jit(nopython=True)
def calculate_max_drawdown(win_loss_percents_np):
    """Calculates the maximum drawdown for a given list of win/loss percentages.
    
    Args:
        win_loss_percents_np (np.array): A numpy array of win/loss percentages.
    
    Returns:
        float: The maximum drawdown.
    """
    max_drawdown = 0

    for i in range(len(win_loss_percents_np)):
        max_drawdown = min(max_drawdown, win_loss_percents_np[i])

    return max_drawdown

@nb.jit(nopython=True)
def calculate_ratio_winning_trades(win_loss_percents_np):
    """Calculates the ratio of winning trades for a given list of win/loss percentages.
    
    Args:
        win_loss_percents_np (np.array): A numpy array of win/loss percentages.
    
    Returns:
        float: The ratio of winning trades.
    """
    num_winning_trades = 0
    num_losing_trades = 0

    for i in range(len(win_loss_percents_np)):
        if win_loss_percents_np[i] > float(0):
            num_winning_trades += 1
        elif win_loss_percents_np[i] < float(0):
            num_losing_trades += 1

    return num_winning_trades / num_losing_trades





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

    


    def simulate(trading_signals_np, price_data_np, metadata=None):
        """Simulates a trading strategy using the given trading signals and price data.
        
        Args:
            trading_signals_np (np.array): A numpy array of trading signals.
            price_data_np (np.array): A numpy array of price data.
        
        Returns:
            a list containing the following
                a nested dataframe containing the following:
                    win_loss_np
                    win_loss_percents_np
                    portfolio_values_np
                another nested dataframe containing the input to the simulation: 
                    trading_signals_np
                    price_data_np
                another nested dataframe containing the metadata passed in:
                    metadata
                a dictionary containing the following:
                    max_drawdown
                    ratio_winning_trades
                    sharpe ratio
                    expectancy 
                    variance
                    
                """
        input_df = pd.DataFrame({
            'trading_signals': trading_signals_np,
            'price_data': price_data_np
        })

        win_loss_np, win_loss_percents_np, portfolio_values_np = calculate_trades_win_loss(price_data_np, trading_signals_np)

        win_loss_df = pd.DataFrame({
            'win_loss': win_loss_np,
            'win_loss_percents': win_loss_percents_np,
            'portfolio_values': portfolio_values_np
        })

        expectancy = calculate_expectancy(win_loss_percents_np)

        variance = calculate_variance(win_loss_percents_np)

        sharpe_ratio = calculate_sharpe_ratio(win_loss_percents_np)

        max_drawdown = calculate_max_drawdown(win_loss_percents_np)

        ratio_winning_trades = calculate_ratio_winning_trades(win_loss_percents_np)

        metadata = metadata # the metadata should be passed in as a dataframe already

        # packcage the stats into a dictionary
        stats = {
            'max_drawdown': max_drawdown,
            'ratio_winning_trades': ratio_winning_trades,
            'sharpe_ratio': sharpe_ratio,
            'expectancy': expectancy,
            'variance': variance
        }

        # package the output into a list
        dataframes = [win_loss_df, input_df, metadata, stats]

        return dataframes






 
