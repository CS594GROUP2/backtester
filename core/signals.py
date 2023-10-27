import numpy as np
import pandas as pd
import numba as nb 

# iterate through random array using numba
@nb.jit(nopython=True)
def random_loop(zero_array, rand_values, entp, extp):
    in_position = False

    # iterate through array, going in and out of position based on the random values
    for i in range(zero_array.size):
        if in_position:
            if extp > rand_values[i]:
                zero_array[i] = -1
                in_position = False
        else:
            if entp > rand_values[i]:
                zero_array[i] = 1
                in_position = True

# iterate through price data using numba
@nb.jit(nopython=True)
def generate_signals(price_data_np, target_np, signals): 
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
        self.metadata = dict()

    def random_signals(self, size, entry_probability, exit_probability):
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

        # Create output array with all zeros and specified size:
        output_array = np.zeros(shape=size, dtype=np.int8)

        # Create array of random values with same size:
        random_values = np.random.random(size)

        # Call helper function to efficiently loop through random array and fill the output array with signals
        random_loop(output_array, random_values, entry_probability, exit_probability)

        return output_array


    def above_below(self, hist_data: pd.DataFrame, target, metadata, column='Close') -> list:
    
        """
        Generates trading signals and stores them in a newly generated numpy array
        a positive trading signal(+1) is generated when the price crosses above the target
        a negative trading signal(-1) is generated when the price crosses below the target
        it is assumed to start not already in a position
        

        Args:
        price_data: A Pandas DataFrame containing the price data in OHLCV format note the close will be taken
        target: A Pandas DataFrame containing the target data crossover values
        metadata: A Pyhon dictionary containing the metadata for the price data and technical indicator
            - ticker: The ticker symbol of the price data
            - start_date: The start date of the price data
            - end_date: The end date of the price data
            - interval: The interval of the price data
            - indicator: The name of the technical indicator
            - parameters: The parameters of the technical indicator (nested dictionary)

        Returns:
        A list containing:
        a Numpy array of trading signals
        a Numpy array of the price data used
        a concatenation of the metadata from the price data and target data

        """

        self.metadata = metadata

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
        
        
        # check if the target is a pandas series and convert it to a numpy array dtype int8
        if isinstance(target, pd.Series):
            #convert all the NaN values to 0
            target = target.fillna(0)
            target = target.to_numpy(dtype=np.int8)
        # check if the target is already a numpy array
        elif isinstance(target, np.ndarray):
            pass
        # otherwise raise a value error
        else:
            raise ValueError("The target data is not a Pandas Series or Numpy Array")

        # convert the target data to a numpy array
        # check if the target is a dataframe
        if isinstance(hist_data, pd.DataFrame):
            # extract the closing column from the target data
            price_data = hist_data[column]
        # check if the target is already a numpy array
        elif isinstance(target, np.ndarray):
            pass
        # otherwise raise a value error
        else:
            raise ValueError("The target data is not a Pandas DataFrame or Numpy Array")
        
        # convert the price data to a numpy array
        price_data = price_data.to_numpy()


        # check that the shape of the price data and target data are the same
        if price_data.shape != target.shape:
            raise ValueError("The price data and target data are not the same shape")

        # create an array using zeros like the price data. make the array of type int8
        signals = np.zeros_like(price_data, dtype=np.int8)

        signal_generator = SignalGenerator()
        
        return [generate_signals(price_data, target, signals), price_data, metadata]
        


