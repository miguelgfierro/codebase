import pandas as pd


def save_file(data, filename):
    """Save a dataframe as `csv`.
    Parameters:
        data (pd.DataFrame): A dataframe
        filename (str): Name of the file.
    Examples:
        >>> df = pd.DataFrame({'col1':[1,2,3], 'col2':[0.1,0.2,0.3]})
        >>> save_file(df, 'file.csv')

    """
    data.to_csv(filename, index=False, header=False)


def read_file(filename):
    """Read a `csv` file.
    Parameters:
        filename (str): Name of the file.
    Returns:
        data (pd.DataFrame): An dataframe.
    Examples:
        >>> df = read_file('../../share/traj.csv')
        >>> df
               time   q1   q2
        0  0.041667  443  205
        1  0.083333  444  206

    """
    data = pd.read_csv(filename, header=None, names=['time','q1','q2'], sep=',', usecols=[0,1,2])
    return data



