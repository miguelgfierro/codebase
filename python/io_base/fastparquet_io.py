from fastparquet import ParquetFile
from fastparquet import write


def save_file(data, filename):
    """Save a dataframe in parquet format.
    Args:
        data (pd.DataFrame): A dataframe
        filename (str): Name of the file.
    Examples:
        >>> import pandas as pd
        >>> df = pd.DataFrame({'col1':[1,2,3], 'col2':[0.1,0.2,0.3]})
        >>> save_file(df, 'file.parq')

    """
    write(filename, data)


def read_file(filename):
    """Read a parquet file.
    Args:
        filename (str): Name of the file.
    Returns:
        data (pd.DataFrame): An dataframe.
    Examples:
        >>> import pandas as pd
        >>> df = pd.DataFrame({'col1':[1,2,3], 'col2':[0.1,0.2,0.3]})
        >>> write('file.parq', df)
        >>> df = read_file('file.parq')
        >>> df
           col1  col2
        0     1   0.1
        1     2   0.2
        2     3   0.3

    """
    pf = ParquetFile(filename)
    data = pf.to_pandas()
    return data


