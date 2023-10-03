import pandas as pd
import numpy as np
import numba as nb

class SignalGenerator:
    def __init__(self):
        pass

    def random_signals(self, size, entry_probablility, exit_probability):
        signals = np.zeros(shape=size, dtype=np.int8)
        random_values = np.random.random(size)

        self.random_loop(signals, random_values, entry_probablility, exit_probability)
        return signals

    @nb.jit(nopython=True)
    def random_loop(zero_array, rand_values, entp, extp):
        in_position = False

        for i in range(zero_array.size):
            if in_position:
                if extp > rand_values[i]:
                    zero_array[i] = -1
                    in_position = False
            else:
                if entp > rand_values[i]:
                    zero_array[i] = 1
                    in_position = True
