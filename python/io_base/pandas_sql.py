# From datacamp pandas cheat sheet:
# https://s3.amazonaws.com/assets.datacamp.com/blog_assets/PandasPythonForDataScience+(1).pdf

import pandas as pd
from sqlalchemy import create_engine


def save_to_database(data, connection_string):
    """Save a dataframe to a SQL database.
    Parameters:
        data (pd.DataFrame): A dataframe
        connection_string (str): Database connection string.
    Examples:
        >>> df = pd.DataFrame({'col1':[1,2,3], 'col2':[0.1,0.2,0.3]})
        >>> save_to_database(df, 'sqlite:///:memory:')

    """
    engine = create_engine(connection_string)
    pd.to_sql(data, engine)


def read_from_database(connection_string, query):
    """Make a query to a SQL database.
    Parameters:
        connection_string (str): Database connection string.
        query (str): Query.
    Returns:
        data (pd.DataFrame): An dataframe.
    Examples:
        >>> df = read_from_database('sqlite:///:memory:', 'SELECT * FROM my_table;')

    """
    engine = create_engine(connection_string)
    return pd.read_sql(query, engine)


