import pandas as pd
from sqlalchemy import create_engine


def save_csv(data, filename, **kwargs):
    """Save a dataframe as `csv`.
    Parameters:
        data (pd.DataFrame): A dataframe
        filename (str): Name of the file.
    Examples:
        >>> df = pd.DataFrame({'col1':[1,2,3], 'col2':[0.1,0.2,0.3]})
        >>> save_csv(df, filename='file.csv', index=False, header=False)

    """
    data.to_csv(filename, **kwargs)


def read_csv(filename, **kwargs):
    """Read a `csv` file.
    Parameters:
        filename (str): Name of the file.
    Returns:
        data (pd.DataFrame): An dataframe.
    Examples:
        >>> df = read_csv(filename='../../share/traj.csv', header=None,
        ...                names=['time','q1','q2'], sep=',', usecols=[0,1,2])
        >>> df
               time   q1   q2
        0  0.041667  443  205
        1  0.083333  444  206

    """
    data = pd.read_csv(filename, **kwargs)
    return data


def save_to_sqlite(data, connection_string):
    """Save a dataframe to a SQL database.
    Parameters:
        data (pd.DataFrame): A dataframe
        connection_string (str): Database connection string.
    Examples:
        >>> df = pd.DataFrame({'col1':[1,2,3], 'col2':[0.1,0.2,0.3]})
        >>> save_to_sqlite(df, 'sqlite:///:memory:')

    """
    engine = create_engine(connection_string)
    pd.to_sql(data, engine)


def read_from_sqlite(connection_string, query):
    """Make a query to a SQL database.
    Parameters:
        connection_string (str): Database connection string.
        query (str): Query.
    Returns:
        data (pd.DataFrame): An dataframe.
    Examples:
        >>> df = read_from_sqlite('sqlite:///:memory:', 'SELECT * FROM my_table;')

    """
    engine = create_engine(connection_string)
    return pd.read_sql(query, engine)

