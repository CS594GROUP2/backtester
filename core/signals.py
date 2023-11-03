import numpy as np
import pandas as pd
import numba as nb 


# helper function to loop through random values and fill output array
@nb.jit(nopython=True)
def generate_random(size, entp, extp):
    random_signals = np.zeros(shape=size, dtype=np.int8)
    random_values = np.random.random(size)
    in_position = False

    # iterate through array, going in and out of position based on the random values
    for i in range(random_signals.size):
        if in_position:
            if extp > random_values[i]:
                random_signals[i] = -1
                in_position = False
        else:
            if entp > random_values[i]:
                random_signals[i] = 1
                in_position = True
    
    return random_signals

@nb.jit(nopython=True)
def generate_signals(price_data_np, target_np):
    signals = np.zeros_like(price_data_np, dtype=np.int8)
    in_position = False

    # iterate through grabbing items from prifce_data_np and target_np
    for i in range(1, price_data_np.size):
        if target_np[i] == 0:
            pass
        if price_data_np[i] > target_np[i] and not in_position:
            signals[i] = 1
            in_position = True
        elif price_data_np[i] < target_np[i] and in_position:
            signals[i] = -1
            in_position = False
        else:
            pass
    
    return signals

class SignalGenerator:

    # constructor method no data members
    def __init__(self):
        pass

    def generate_random(self, size, entry_probability, exit_probability) -> np.ndarray:
        """
            Returns random trading strategy for a given size, entry and exit probability.

            Args:
            size: The size of the dataset.
            entry_probability: Float from 0 to 1 that indicates the chance that the random strategy will enter a position.
            exit_probability: Float from 0 to 1 that indicates the chance that the random strategy will leave a position.
            Returns:
            An array of trading signals that reflect a random trading strategy.
        """

        # Exceptions:
        if size <= 0:
            raise ValueError("Size must be greater than 0")
        if entry_probability < 0 or entry_probability > 1:
            raise ValueError("entry_probability must be between 0 and 1")
        if exit_probability < 0 or exit_probability > 1:
            raise ValueError("exit_probability must be between 0 and 1")
        
        self.metadata['random_signals'] = True

        random_signals = generate_random(size, entry_probability, exit_probability)
        self.trading_signals = random_signals

        return self.trading_signals

    def generate_above_below(self, target, column='Close') -> np.ndarray:
        """
        Generates trading signals and stores them in a newly generated numpy array
        a positive trading signal(+1) is generated when the price crosses above the target
        a negative trading signal(-1) is generated when the price crosses below the target
        it is assumed to start not already in a position
        

        Args:
        price_data: A Pandas DataFrame containing the price data in OHLCV format note the close will be taken
        target: A Pandas DataFrame containing the target data crossover values
        metadata: A Pandas DataFrame containing the metadata for the price data will append the target metadata and return

        Returns:
        a NumPy array of trading signals
        """
        # check if the price data is a dataframe
        if isinstance(hist_data, pd.DataFrame):
            # extract the closing column from the price data
            price_data = hist_data[column].to_numpy()
        # check if the price data is a pandas series
        elif isinstance(hist_data, pd.Series):
            price_data = hist_data.to_numpy()
        # check if the price data is already a numpy array
        elif isinstance(hist_data, np.ndarray):
            pass
        # otherwise raise a value error
        else:
            raise ValueError("The price data is not a Pandas DataFrame or Numpy Array")
        
        
        # validate the target data (must be a Pandas Series or Numpy Array)
        if isinstance(target, pd.Series):
            # convert all the NaN values to 0
            target = target.fillna(0)
            target = target.to_numpy(dtype=np.int8)
        elif isinstance(target, np.ndarray):
            pass
        else:
            raise ValueError("The target data is not a Pandas Series or Numpy Array")

        if not isinstance(target, np.ndarray):
            raise ValueError("The target data is not a Numpy Array")
        
        # extract the closing column from the price data
        price_data_close = self.price_data[column].to_numpy()

        # check shape of price data and target data
        if price_data_close.shape != target.shape:
            raise ValueError("The price data and target data are not the same shape")
        
        above_below_signals = generate_signals(price_data_close, target)
        self.trading_signals = above_below_signals

        return self.trading_signals

    def get_results(self):
        """
        Returns:
        A list containing:
        a Numpy array of trading signals
        a Numpy array of the price data
        a List of metadata
        """
        return [self.trading_signals, self.price_data, self.metadata]