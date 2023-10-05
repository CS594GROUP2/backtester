import numpy as np
import numba as nb


class SignalGenerator:
    def __init__(self):
        pass

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

        # Create output array with all zeros and specified size:
        output_array = np.zeros(shape=size, dtype=np.int8)

        # Create array of random values with same size:
        random_values = np.random.random(size)

        # Call helper function to efficiently loop through random array and fill the output array with signals
        random_loop(output_array, random_values, entry_probability, exit_probability)

        return output_array

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
