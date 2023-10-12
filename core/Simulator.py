import numpy as np
import pandas as pd
import numba as nb

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

    for i in range(len(win_loss_percents_np)):
        if win_loss_percents_np[i] > 0:
            num_winning_trades += 1

    return num_winning_trades / len(win_loss_percents_np)




class Simulator:

    def __init__(self) -> None:
        pass
    

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






    