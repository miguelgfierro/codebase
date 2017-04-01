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
