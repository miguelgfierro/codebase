import pandas as pd


def replace_column_values(df, val_dict, col_name, new_col_name=None):
    """Replace all appearances of a value to another in a dictionary.
    Parameters:
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


def get_unique_values_in_column(df, col_name):
    """Get unique values in a column.
    Parameters:
        df (pd.DataFrame): Dataframe.
        col_name (str): Column name.
    Returns:
        vals (numpy array): Unique values.
    Examples:
        >>> df = pd.DataFrame({'letters':['a','a','c'], 'numbers':[1,2,3]})
        >>> vals = get_unique_values_in_column(df, 'letters')
        >>> print(vals)
        ['a' 'c']
    """
    return df[col_name].unique()


def get_random_fraction_of_rows(df, row_fraction=0.5, reindex=True):
    """Get a random fraction of the dataframe rows.
    Parameters:
        df (pd.DataFrame): Dataframe.
        row_fraction (float): Fraction (in percentage) of rows to retrieve.
        reindex (bool): Flag to reset the dataframe index or not.
    Returns:
        df_return (pd.DataFrame): Dataframe with a fraction of the original rows.
    Examples:
        >>> df = pd.DataFrame({'letters':['a','a','c'], 'numbers':[1,2,3]})
        >>> df_return = get_random_fraction_of_rows(df, 0.6)
        >>> df_return
          letters  numbers
        0       c        3
        1       a        1

    """
    return df.sample(frac=row_fraction).reset_index(drop=reindex)


def get_random_number_of_rows(df, num_rows, reindex=True):
    """Get a random number of the dataframe rows.
    Parameters:
        df (pd.DataFrame): Dataframe.
        num_rows (int): Number of rows to retrieve.
        reindex (bool): Flag to reset the dataframe index or not.
    Returns:
        df_return (pd.DataFrame): Dataframe with a random number of the original rows.
    Examples:
        >>> df = pd.DataFrame({'letters':['a','a','c'], 'numbers':[1,2,3]})
        >>> df_return = get_random_number_of_rows(df, 1)
        >>> df_return
          letters  numbers
        0       c        3

    """
    return df.sample(n=num_rows).reset_index(drop=reindex)


def select_values_by_range(df, row_ini, row_end, col_ini, col_end):
    """Select a range of values in the dataframe.
    Parameters:
        df (pd.DataFrame): Dataframe.
        row_ini (int): Initial row.
        row_end (int): Final row.
        col_ini (int): Initial column.
        col_end (int): Final column.
    Returns:
        df_return (pd.DataFrame): Dataframe with the specific range of rows and columns.
    Examples:
        >>> df = pd.DataFrame({'letters':['a','a','c'], 'numbers':[1,2,3]})
        >>> df_return = select_values_by_range(df, 0, 1, 'letters', 'numbers')
        >>> df_return
          letters  numbers
        0       a        1
        1       a        2

    """
    return df.loc[row_ini:row_end, col_ini:col_end]


def select_values_by_index(df, vector_row_pos, vector_col_pos):
    """Select values in the dataframe given specific indexes of rows and columns.
    Parameters:
        df (pd.DataFrame): Dataframe.
        vector_row_pos (array): Array of row positions.
        vector_col_pos (array): Array of column positions.
    Returns:
        df_return (pd.DataFrame): Dataframe with the specific values in the row and column indexes.
    Examples:
        >>> df = pd.DataFrame({'letters':['a','a','c'], 'numbers':[1,2,3]})
        >>> df_return = select_values_by_index(df, vector_row_pos=[0,2], vector_col_pos=[0,1])
        >>> df_return
          letters  numbers
        0       a        1
        2       c        3

    """
    return df.iloc[vector_row_pos, vector_col_pos]


def select_rows_where_value_equal(df, column, value):
    """Select rows in the dataframe whose column has a specific value.
    Parameters:
        df (pd.DataFrame): Dataframe.
        column (str): Column name.
        value (int, str, float): Value to compare with.
    Returns:
        df_return (pd.DataFrame): Dataframe with selected rows.
    Examples:
        >>> df = pd.DataFrame({'letters':['a','a','c'], 'numbers':[1,2,3]})
        >>> df_return = select_rows_where_value_equal(df, 'letters', 'a')
        >>> df_return
          letters  numbers
        0       a        1
        1       a        2

    """
    return df.loc[df[column] == value]


def select_rows_where_list_equal(df, column, items):
    """Select rows in the dataframe whose column has a list of values.
    Parameters:
        df (pd.DataFrame): Dataframe.
        column (str): Column name.
        items (list): List of items.
    Returns:
        df_return (pd.DataFrame): Dataframe with selected rows.
    Examples:
        >>> df = pd.DataFrame({'letters':['a','b','c'], 'numbers':[1,2,3]})
        >>> df_return = select_rows_where_list_equal(df, 'letters', ['a','b'])
        >>> df_return
          letters  numbers
        0       a        1
        1       b        2

    """
    return df.loc[df[column].isin(items)]

def select_all_columns_except_some(df, column_names):
    """Select all columns in the dataframe except those especifies in `column_list`.
    Parameters:
        df (pd.DataFrame): Dataframe.
        column_names (list): List of column names.
    Returns:
        df_return (pd.DataFrame): Dataframe with the columns removed.
    Examples:
        >>> df = pd.DataFrame({'letters':['a','b','c'], 'numbers':[1,2,3], 'numbers2':[4,5,6]})
        >>> df_return = select_all_columns_except_some(df, ['numbers','numbers2'])
        >>> df_return
          letters
        0       a
        1       b
        2       c

    """
    return df[df.columns.difference(column_names)]


def split_rows_by_condition(df, mask):
    """Split dataframe based on logical indexes (that could come from a condition).
    Parameters:
        df (pd.DataFrame): Dataframe.
        mask (pd.Series): Series with boolean indexes (could come from a condition).
    Returns:
        df_list (list): List of split dataframes.
    Examples:
        >>> df = pd.DataFrame({'letters':['a','b','c'], 'numbers':[1,2,3], 'numbers2':[4,5,6]})
        >>> mask = df['numbers'] > 1
        >>> df1, df2 = split_rows_by_condition(df, mask)
        >>> df1
          letters  numbers  numbers2
        1       b        2         5
        2       c        3         6
        >>> df2
          letters  numbers  numbers2
        0       a        1         4

    """
    df1 = df[mask]
    df2 = df[~mask]
    return df1, df2


def set_value_where_condition(df, value, col_val, value_cond1, col_cond1):
    """Set a value in a column where multiple conditions are fit
    Parameters:
        df (pd.DataFrame): Dataframe.
        value (int, float, str): Value to set.
        col_val (str): Column name for the set value
        value_cond1 (int, float, str): Value of the condition.
        col_cond1 (str): Column name for the condition.
    Returns:
        df_return (pd.DataFrame): Dataframe with the value modified.
    Examples:
        >>> df = pd.DataFrame({'letters':['a','b','c'], 'numbers':[1,2,3], 'numbers2':[4,5,6]})
        >>> df_return = set_value_where_condition(df, 10, 'numbers2', 'a', 'letters')
        >>> df_return
          letters  numbers  numbers2
        0       a        1        10
        1       b        2         5
        2       c        3         6

    """
    df.loc[df[col_cond1] == value_cond1, col_val] = value
    return df


def set_value_where_multiple_condition(df, value, col_val, value_cond1, col_cond1, value_cond2, col_cond2):
    """Set a value in a column where multiple conditions are fit
    Parameters:
        df (pd.DataFrame): Dataframe.
        value (int, float, str): Value to set.
        col_val (str): Column name for the set value
        value_cond1 (int, float, str): Value of the condition 1.
        col_cond1 (str): Column name for the condition 1.
        value_cond2 (int, float, str): Value of the condition 2.
        col_cond2 (str): Column name for the condition 2.
    Returns:
        df_return (pd.DataFrame): Dataframe with the value modified.
    Examples:
        >>> df = pd.DataFrame({'letters':['a','a','a'], 'numbers':[1,2,3], 'numbers2':[4,5,6]})
        >>> df_return = set_value_where_multiple_condition(df, 10, 'numbers2', 'a', 'letters', 1, 'numbers')
        >>> df_return
          letters  numbers  numbers2
        0       a        1        10
        1       a        2         5
        2       a        3         6

    """
    df.loc[(df[col_cond1] == value_cond1) & (df[col_cond2] == value_cond2), col_val] = value
    return df


