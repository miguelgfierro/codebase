import pandas as pd


def remove_nan(df):
    """Remove NaN and reindex.
    Parameters:
        df (pd.DataFrame): Dataframe.
    Returns:
        df_return (pd.DataFrame): Dataframe without NaN.
    Examples:
        >>> df = pd.DataFrame({'letters':['a','a','c'], 'numbers':[1,None,3]})
        >>> df_return = remove_nan(df)
        >>> df_return
          letters  numbers
        0       a      1.0
        1       c      3.0

    """
    return df.dropna().reset_index(drop=True)


def replace_nan(df, value):
    """Replace NaN for a value.
    Parameters:
        df (pd.DataFrame): Dataframe.
        value (int or str): Value
    Returns:
        df_return (pd.DataFrame): Dataframe with the replaced value.
    Examples:
        >>> df = pd.DataFrame({'letters':['a','a','c'], 'numbers':[1,2,None]})
        >>> df_return = replace_nan(df, 7)
        >>> df_return
          letters  numbers
        0       a      1.0
        1       a      2.0
        2       c      7.0

    """
    return df.fillna(value)


def drop_columns(df, cols):
    """Drop columns.
    Parameters:
        df (pd.DataFrame): Dataframe.
        cols (int, str or list): Column name, column index or list of column names.
    Returns:
        df_return (pd.DataFrame): Dataframe with the replaced value.
    Examples:
        >>> df = pd.DataFrame({'letters':['a','b','c'], 'numbers':[1,2,3]})
        >>> drop_columns(df, 'numbers')
          letters
        0       a
        1       b
        2       c

    """
    return df.drop(cols, axis=1)


def drop_rows(df, rows):
    """Drop rows.
    Parameters:
        df (pd.DataFrame): Dataframe.
        rows (int, str or list): Row name, row index or list of row names.
    Returns:
        df_return (pd.DataFrame): Dataframe with the replaced value.
    Examples:
        >>> df = pd.DataFrame({'letters':['a','b','c'], 'numbers':[1,2,3]})
        >>> drop_rows(df, 0)
          letters  numbers
        1       b        2
        2       c        3

    """
    return df.drop(rows, axis=0)


def drop_duplicates(df):
    """Drop duplicate rows and reindex.
    Parameters:
        df (pd.DataFrame): Dataframe.
    Returns:
        df_return (pd.DataFrame): Dataframe with the replaced value.
    Examples:
        >>> df = pd.DataFrame({'letters':['b','b','c'], 'numbers':[2,2,3]})
        >>> drop_duplicates(df)
          letters  numbers
        0       b        2
        1       c        3

    """
    return df.drop_duplicates().reset_index(drop=True)


