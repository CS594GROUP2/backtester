import numpy as np
import pandas as pd
import numba as nb 

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
        pass

    def above_below(self, hist_data: pd.DataFrame, target, metadata, column='Close') -> list:

    
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
        A list containing:
        a Numpy array of trading signals
        a Numpy array of the price data used
        a concatenation of the metadata from the price data and target data

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
        


