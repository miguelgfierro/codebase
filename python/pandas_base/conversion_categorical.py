import pandas as pd


def _get_nominal_integer_dict(nominal_vals):
    """Convert nominal values in integers, starting at 0.
    Parameters:
        nominal_vals (pd.Series): A series.
    Returns:
        d (dict): An dictionary with numeric values.

    """
    d = {}
    for val in nominal_vals:
        if val not in d:
            current_max = max(d.values()) if len(d) > 0 else -1
            d[val] = current_max+1
    return d


def _convert_to_integer(srs):
    """Convert series to integer.
    Parameters:
        srs (pd.Series): A series.
    Returns:
        srs (pd.Series): An series with numeric values.

    """
    d = _get_nominal_integer_dict(srs)
    return srs.map(lambda x: d[x])


def convert_cols_categorical_to_numeric(df, col_list=None):
    """Convert categorical columns to numeric and leave numeric columns
    as they are. You can force to convert a numerical column if it is
    included in col_list
    Parameters:
        df (pd.DataFrame): Dataframe.
        col_list (list): List of columns.
    Returns:
        ret (pd.DataFrame): An dataframe with numeric values.
    Examples:
        >>> df = pd.DataFrame({'letters':['a','b','c'],'numbers':[1,2,3]})
        >>> df_numeric = convert_cols_categorical_to_numeric(df)
        >>> print(df_numeric)
           letters  numbers
        0        0        1
        1        1        2
        2        2        3

    """
    if col_list is None: col_list = []
    ret = pd.DataFrame()
    for column_name in df.columns:
        column = df[column_name]
        if column.dtype == 'object' or column_name in col_list:
            ret[column_name] = _convert_to_integer(column)
        else:
            ret[column_name] = column
    return ret


def convert_cols_numeric_to_categorical(df):
    """
    Convert numerical columns to categorical and leave numeric columns
    as they are
    Parameters:
        df (pd.DataFrame): Dataframe.
    Returns:
        ret (pd.DataFrame): An dataframe with numeric values.

    """
    #TODO
    pass



