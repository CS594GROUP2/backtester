import pandas as pd
import numpy as np
import numba as nb

class SignalGenerator:
    def init(self):
        pass

    def random_signals(self, price_data: pd.DataFrame, entry_probablility, exit_probability):
        size = price_data.size

        signals = np.empty_like(price_data).astype(np.int8)

        random_values = np.random.random(size)

        signals = self.random_loop(signals, random_values, entry_probablility, exit_probability)
        return signals

    @nb.jit(nopython=True)
    def random_loop(empty_array, rand_values, entp, extp):
        in_position = False

        for i in range(empty_array.size):
            if in_position:
                if extp > rand_values[i]:
                    empty_array[i] = -1
                    in_position = False
                else:
                    empty_array[i] = 0
            else:
                if entp > rand_values[i]:
                    empty_array[i] = 1
                    in_position = True
                else:
                    empty_array[i] = 0

        return empty_array
