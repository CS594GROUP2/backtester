import numpy as np
import pandas as pd
import numba as nb 


# helper function to loop through random values and fill output array
@nb.jit(nopython=True)
def generate_random(size, entp, extp):
    output_array = np.zeros(shape=size, dtype=np.int8)
    random_values = np.random.random(size)
    in_position = False

    # iterate through array, going in and out of position based on the random values
    for i in range(output_array.size):
        if in_position:
            if extp > random_values[i]:
                output_array[i] = -1
                in_position = False
        else:
            if entp > random_values[i]:
                output_array[i] = 1
                in_position = True
    
    return output_array

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
    def __init__(self, price_data=None, metadata=None):
        self.price_data : pd.DataFrame = price_data
        self.metadata : list = metadata
        self.trading_signals : np.ndarray = None

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
        target: a Pandas Series or Numpy Array containing the target data crossover values
        metadata: a List containing the metadata for the price data, included in get_results()
        
        Returns:
        a NumPy array of trading signals
        """

        # validate the column name is in the price data
        if column not in self.price_data.columns:
            raise ValueError("The column does not exist in the price data")
        
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