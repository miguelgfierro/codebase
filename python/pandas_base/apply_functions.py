import pandas as pd


def apply_function_on_axis_dataframe(df, func, axis=0):
    """Apply a function on a row/column basis of a DataFrame.
    Args:
        df (pd.DataFrame): Dataframe.
        func (function): The function to apply.
        axis (int): The axis of application (0=columns, 1=rows).
    Returns:
        df_return (pd.DataFrame): Dataframe with the applied function.
    Examples:
        >>> df = pd.DataFrame(np.array(range(12)).reshape(4, 3), columns=list('abc'))
        >>> f = lambda x: x.max() - x.min()
        >>> apply_function_on_axis_dataframe(df, f, 1)
        0    2
        1    2
        2    2
        3    2
        dtype: int64
        >>> apply_function_on_axis_dataframe(df, f, 0)
        a    9
        b    9
        c    9
        dtype: int64

    """
    return df.apply(func, axis)


def apply_function_elementwise_dataframe(df, func):
    """Apply a function on a row/column basis of a DataFrame.
    Args:
        df (pd.DataFrame): Dataframe.
        func (function): The function to apply.
    Returns:
        df_return (pd.DataFrame): Dataframe with the applied function.
    Examples:
        >>> df = pd.DataFrame(np.array(range(12)).reshape(4, 3), columns=list('abc'))
        >>> f = lambda x: '%.1f' % x
        >>> apply_function_elementwise_dataframe(df, f)
             a     b     c
        0  0.0   1.0   2.0
        1  3.0   4.0   5.0
        2  6.0   7.0   8.0
        3  9.0  10.0  11.0

    """
    return df.applymap(func)


def apply_function_elementwise_series(ser, func):
    """Apply a function on a row/column basis of a DataFrame.
    Args:
        ser (pd.Series): Series.
        func (function): The function to apply.
    Returns:
        ser_return (pd.Series): Series with the applied function.
    Examples:
        >>> df = pd.DataFrame(np.array(range(12)).reshape(4, 3), columns=list('abc'))
        >>> ser = df['b']
        >>> f = lambda x: '%.1f' % x
        >>> apply_function_elementwise_series(ser, f)
        0     1.0
        1     4.0
        2     7.0
        3    10.0
        Name: b, dtype: object

    """
    return ser.map(func)
