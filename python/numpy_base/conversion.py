import pandas as pd


def convert_to_pandas_dataframe(data):
    """Convert a numpy array to a dataframe. Every column of the array is a column in the dataframe.
    Parameters:
        data (numpy array): An array.
    Returns:
        result (pd.DataFrame): An dataframe with the numpy array values.
    Examples:
        >>> import numpy as np
        >>> data = np.array([(1,10),(2,20),(3,30)], dtype='int')
        >>> df = convert_to_pandas_dataframe(data)
        >>> print(df)
           0   1
        0  1  10
        1  2  20
        2  3  30
        >>> df.shape
        (3, 2)


    """
    return pd.DataFrame(data)
