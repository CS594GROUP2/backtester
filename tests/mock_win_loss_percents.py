import numpy as np
import datetime as dt
import pandas as pd


def mock_win_loss_percents(array_length=100):
    """
    Mock the win loss percents numpy array.

    Args:
        array_length (int): The length of the numpy array to mock.

    Returns:
        np.array: A numpy array of win loss percents.
    """

    mock = np.random.random(array_length)
    for i in range(len(mock)):
        if mock[i] > 0.1:
            mock[i] = 0
        elif mock[i] < -0.1:
            mock[i] = 0


    return mock


print(mock_win_loss_percents())

def mock_timestamps(array_length=100):
    """
    Mock the timestamps numpy array.

    Args:
        array_length (int): The length of the numpy array to mock.

    Returns:
        np.array: A numpy array of timestamps.
    """
    time_now = dt.datetime.now()
    time_delta = dt.timedelta(days=1)
    mock = np.empty(array_length, dtype=object)

    for i in range(array_length):
        mock[i] = time_now + time_delta * i

    # turn mock into a pd.Series
    mock = pd.Series(mock)

    return mock

