import pandas as pd
from sqlalchemy import create_engine


def save_csv(data, filename, **kwargs):
    """Save a dataframe as `csv`.
    Args:
        data (pd.DataFrame): A dataframe
        filename (str): Name of the file.
    Examples:
        >>> df = pd.DataFrame({'col1':[1,2,3], 'col2':[0.1,0.2,0.3]})
        >>> save_csv(df, filename='file.csv', index=False, header=False)

    """
    data.to_csv(filename, **kwargs)


def read_csv(filename, **kwargs):
    """Read a `csv` file.
    Args:
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


def save_to_sqlite(data, database, table_name, **kargs):
    """Save a dataframe to a SQL database.
    Args:
        data (pd.DataFrame): A dataframe
        database (str): Database filename.
        connection_string (str): Database connection string.
        table_name (str): Table name
    Examples:
        >>> df = pd.DataFrame({'col1':[1,2,3], 'col2':[0.1,0.2,0.3]})
        >>> save_to_sqlite(df, 'test.db', 'table1', if_exists='replace')
        >>> import sqlite3
        >>> conn = sqlite3.connect('test.db')
        >>> cur = conn.cursor()
        >>> result = cur.execute("SELECT * FROM table1")
        >>> cur.fetchall()
        [(0, 1, 0.1), (1, 2, 0.2), (2, 3, 0.3)]
        >>> save_to_sqlite(df, 'test.db', 'table1', if_exists='append', index=False)
        >>> result = cur.execute("SELECT * FROM table1")
        >>> cur.fetchall()
        [(0, 1, 0.1), (1, 2, 0.2), (2, 3, 0.3), (None, 1, 0.1), (None, 2, 0.2), (None, 3, 0.3)]

    """
    connection_string = 'sqlite:///' + database
    engine = create_engine(connection_string)
    data.to_sql(table_name, engine, **kargs)


def read_from_sqlite(connection_string, query):
    """Make a query to a SQL database.
    Args:
        connection_string (str): Database connection string.
        query (str): Query.
    Returns:
        data (pd.DataFrame): An dataframe.
    Examples:
        >>> df = read_from_sqlite('sqlite:///:memory:', 'SELECT * FROM my_table;')

    """
    engine = create_engine(connection_string)
    return pd.read_sql(query, engine)

