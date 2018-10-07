import pandas as pd


def _get_nominal_integer_dict(nominal_vals):
    """Convert nominal values in integers, starting at 0.
    Args:
        nominal_vals (pd.Series): A series.
    Returns:
        d (dict): An dictionary with numeric values.

    """
    d = {}
    for val in nominal_vals:
        if val not in d:
            current_max = max(d.values()) if len(d) > 0 else -1
            d[val] = current_max + 1
    return d


def _convert_to_integer(srs, d):
    """Convert series to integer, given a dictionary.
    Args:
        srs (pd.Series): A series.
        d (dict): A dictionary mapping values to integers
    Returns:
        srs (pd.Series): An series with numeric values.

    """
    return srs.map(lambda x: d[x])


def _convert_to_string(srs):
    """Convert series to string.
    Args:
        srs (pd.Series): A series.
    Returns:
        srs (pd.Series): An series with string values.

    """
    return srs.map(lambda x: str(x))


def convert_cols_categorical_to_numeric(df, col_list=None):
    """Convert categorical columns to numeric and leave numeric columns
    as they are. You can force to convert a numerical column if it is
    included in col_list
    Args:
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
    if col_list is None:
        col_list = []
    ret = pd.DataFrame()
    for column_name in df.columns:
        column = df[column_name]
        if column.dtype == "object" or column_name in col_list:
            col_dict = _get_nominal_integer_dict(column)
            ret[column_name] = _convert_to_integer(column, col_dict)
        else:
            ret[column_name] = column
    return ret


def convert_related_cols_categorical_to_numeric(df, col_list):
    """Convert categorical columns, that are related between each other,
    to numeric and leave numeric columns
    as they are.
    Args:
        df (pd.DataFrame): Dataframe.
        col_list (list): List of columns.
    Returns:
        ret (pd.DataFrame): An dataframe with numeric values.
    Examples:
        >>> df = pd.DataFrame({'letters':['a','b','c'],'letters2':['c','d','a'],'numbers':[1,2,3]})
        >>> df_numeric = convert_related_cols_categorical_to_numeric(df, col_list=['letters','letters2'])
        >>> print(df_numeric)
           letters  letters2  numbers
        0        0         2        1
        1        1         3        2
        2        2         0        3

    """
    ret = pd.DataFrame()
    values = None
    for c in col_list:
        values = pd.concat([values, df[c]], axis=0)
        values = pd.Series(values.unique())
    col_dict = _get_nominal_integer_dict(values)
    for column_name in df.columns:
        column = df[column_name]
        if column_name in col_list:
            ret[column_name] = _convert_to_integer(column, col_dict)
        else:
            ret[column_name] = column
    return ret


def convert_cols_numeric_to_categorical(df, col_list=None):
    """Convert numerical columns to categorical and leave numeric columns
    as they are
    Args:
        df (pd.DataFrame): Dataframe.
        col_list (list): List of columns.
    Returns:
        ret (pd.DataFrame): An dataframe with categorical values.
    Examples:
        >>> import numpy as np
        >>> df = pd.DataFrame({'letters':['a','b','c'],'numbers1':[-1,0.5,10],'numbers2':[1,2,3]})
        >>> df_cat = convert_cols_numeric_to_categorical(df, col_list=['numbers1'])
        >>> print(df_cat)
          letters numbers1  numbers2
        0       a     -1.0         1
        1       b      0.5         2
        2       c     10.0         3
        >>> print(df_cat['numbers1'].dtype)
        object
        >>> print(df_cat['numbers2'].dtype)
        int64

    """
    if col_list is None:
        col_list = df.columns
    ret = pd.DataFrame()
    for column_name in df.columns:
        column = df[column_name]
        if column_name in col_list and column.dtype != "object":
            ret[column_name] = _convert_to_string(column)
        else:
            ret[column_name] = column
    return ret


def convert_to_numpy_array(df, columns=None):
    """Convert a dataframe to a numpy array. Every column of the dataframe is a column in the array.
    Args:
        df (pd.DataFrame): Dataframe.
        columns [list of string]: If None, return all columns, otherwise, returns specified columns.
    Returns:
        result (numpy array): An array with the dataframe values.
    Examples:
        >>> df = pd.DataFrame({'numbers1':[1,2,3], 'numbers2':[10,20,30]})
        >>> arr = convert_to_numpy_array(df)
        >>> arr
        array([[ 1, 10],
               [ 2, 20],
               [ 3, 30]])
        >>> arr.shape
        (3, 2)

    """
    return df.values(columns)


def replace_column_values(df, val_dict, col_name, new_col_name=None):
    """Replace all appearances of a value to another in a dictionary.
    Args:
        df (pd.DataFrame): Dataframe.
        val_dict (dict): Dictionary with the values to replace.
        col_name (str): Column name.
        new_col_name (str): New column name.
    Returns:
        df_return (pd.DataFrame): A dataframe with the values replaced.
    Examples:
        >>> df = pd.DataFrame({'letters':['a','a','c'], 'numbers':[1,2,3]})
        >>> df_return = replace_column_values(df, {'a':1}, 'letters')
        >>> df_return
          letters  numbers
        0       1        1
        1       1        2
        2       c        3
        >>> df_return = replace_column_values(df, {'a':1}, 'letters', 'new_column')
        >>> df_return
          letters  numbers new_column
        0       a        1          1
        1       a        2          1
        2       c        3          c

    """
    df_return = df.copy()
    if new_col_name is None:
        df_return[col_name].replace(val_dict, inplace=True)
    else:
        df_return[new_col_name] = df_return[col_name].replace(val_dict, inplace=False)
    return df_return


def split_text_in_column(df, component, col_name, new_col_list):
    """Split a text in a dataframe column by a component.
    Args:
        df (pd.DataFrame): Dataframe.
        component (str): Component for splitting the text.
        col_name (str): Column name.
        new_col_list (list): List of new column names.
    Returns:
        df_return (pd.DataFrame): A dataframe with the values replaced.
    Examples:
        >>> df = pd.DataFrame({'paths':['/user/local/bin/','/user/local/share/','/user/local/doc/'], 'numbers':[1,2,3]})
        >>> df_return = split_text_in_column(df, '/', 'paths', ['a','b','c'])
        >>> df_return
           numbers     a      b      c
        0        1  user  local    bin
        1        2  user  local  share
        2        3  user  local    doc

    """
    df_exp = df[col_name].str.split(component, expand=True)
    df_exp = df_exp.loc[:, (df_exp != "").any(axis=0)]  # remove columns with no text
    df_exp.columns = new_col_list
    df = pd.concat([df, df_exp], axis=1)
    df.drop(columns=col_name, inplace=True)
    return df
