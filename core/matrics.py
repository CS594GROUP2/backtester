import numpy as np
import numba as nb

@nb.njit
def calculate_expectancy(win_loss_percents):
    """
    Calculate the expectancy of a list of win-loss percentages.

    This function takes a list of win-loss percentages as input, where values range
    from -1 to 1 (or more) representing percentage, with 0 representing no trade. 
    It calculates the expectancy by summing the non-zero percentages and dividing
    by the number of trades.

    Parameters:
    win_loss_percents (numpy.ndarray): win-loss percentages.

    Returns:
    float: The calculated expectancy, or None if the input list is empty.
    """

    if len(win_loss_percents) == 0:
        return None

    non_zero_percentages = win_loss_percents[win_loss_percents != 0]
    total_returns = np.sum(non_zero_percentages)
    number_of_trades = len(non_zero_percentages)

    if number_of_trades == 0:
        return None

    expectancy = total_returns / number_of_trades

    return np.float64(expectancy)

@nb.njit
def calculate_variance(expectancy, win_loss_percents):
    """
    Calculate the variance of a list of win-loss percentages.

    This function calculates the variance of a list of win-loss percentages, taking into account the expectancy (mean).
    The variance measures the degree of dispersion or spread of the values around the mean. A higher variance means 
    greater variability or dispersion in the dataset.

    Parameters:
    expectancy (float): The mean or expectancy of the win-loss percentages.
    win_loss_percents (numpy.ndarray): A list of win-loss percentages, including zero values.

    Returns:
    float: The calculated variance or None if the input list is empty or contains no non-zero values.
    """

    if not expectancy or len(win_loss_percents) == 0:
        return None

    non_zero_percentages = win_loss_percents[win_loss_percents != 0]
    number_of_trades = len(non_zero_percentages)

    if number_of_trades == 0:
        return None

    variance = np.sum((non_zero_percentages - expectancy) ** 2) / number_of_trades

    return np.float64(variance)

@nb.jit
def calculate_sharpe_ratio(expectancy, variance):
    """
    Calculate the Sharpe Ratio for a given investment or trading strategy.

    The Sharpe Ratio assesses the risk-adjusted returns of an investment or trading strategy.
    It is calculated as the difference between the expected return and the risk-free rate, divided by the standard deviation of returns.

    Parameters:
    expectancy (float): the mean or expectancy of the win-loss percentages.
    variance (float): The variance of returns or portfolio values.

    Returns:
    float: The calculated Sharpe Ratio, which measures risk-adjusted performance, or None if the input(s) is empty.
    """

    if not expectancy or not variance:
        return None

    sharpe_ratio = (expectancy - variance) / np.sqrt(variance)

    return np.float64(sharpe_ratio)