import dask.dataframe as dd
import pandas as pd


def save_csv(data, filename='file.*.csv', npartitions=1, **kwargs):
    """Save a dataframe into one of multiple `csv` files.
    Dask is designed to be used for big datasets.
    Args:
        data (pd.DataFrame): A dataframe
        filename (str): Name of the file with a globstring '*'. Dask will substitude
                        '*' with the number of partitions
        npartitions (int): Number of partitions of the data. It will generate a file per partition
        **kwargs (object): Same arguments as in pd.DataFrame.to_csv
    Examples:
        >>> import glob
        >>> df = pd.DataFrame({'col1':[1]*100, 'col2':[0.1]*100})
        >>> save_csv(df, filename='file.*.csv', npartitions=2, index=False, header=False)
        >>> len(glob.glob('file.*.csv'))
        2

    """
    d = dd.from_pandas(data, npartitions=npartitions)
    d.to_csv(filename, **kwargs)


def read_csv(filename, **kwargs):
    """Read a `csv` file.
    Args:
        filename (str): Name of the file. Optionally the filename can have a globstring '*',
                        then it will parse all files matching a pattern.
        **kwargs (object): Same arguments as in pd.DataFrame.read_csv
    Returns:
        data (pd.DataFrame): An dataframe.
    Examples:
        >>> df = read_csv('../../share/traj-*.csv', header=None, names=['time','q1','q2'])
        >>> df
               time   q1   q2
        0  0.041667  443  205
        1  0.083333  444  206
        2  0.125000  445  205
        3  0.166667  444  204
        >>> df = read_csv('../../share/traj.csv', header=None)
        >>> df
                  0    1    2
        0  0.041667  443  205
        1  0.083333  444  206

    """
    data = dd.read_csv(filename, **kwargs)
    d = data.compute().reset_index(drop=True)
    return d
