import numpy as np
import pandas as pd
import numba as nb

class SignalGenerator:

    # constructor method no data members
    def __init__(self):
        pass


    def above_below( price_data: pd.DataFrame, target: pd.DataFrame, metadata: pd.DataFrame) -> list:

    
    """
    Generates trading signals
    a positive trading signal(+1) is generated when the price crosses above the target
    a negative trading signal(-1) is generated when the price crosses below the target
    it is assumed to start not already in a position
    

    Args:
    price_data: A Pandas DataFrame containing the price data and metadata
    target: A Pandas DataFrame containing the target data crossover values

    Returns:
    A list containing a Numpy array of trading signals
    and a concatenation of the metadata from the price data and target data

    """

    # extract the closing column from the price data
    price_data = price_data['Close']

    # convert the price data to a numpy array
    price_data = price_data.to_numpy()

    # convert the target data to a numpy array
    target = target.to_numpy()

    # check that the shape of the price data and target data are the same
    if price_data.shape != target.shape:
        raise ValueError("The price data and target data are not the same shape")

    # create an array using zeros like the price data. make the array of type int8
    signals = np.zeros_like(price_data, dtype=np.int8)
    
    # iterate through price data using numba
    @nb.jit(nopython=True)
    def generate_signals(price_data, target): -> numpy.ndarray
        pass

    



    