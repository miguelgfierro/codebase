import pandas as pd


def get_nominal_integer_dict(nominal_vals):
    d = {}
    for val in nominal_vals:
        if val not in d:
            current_max = max(d.values()) if len(d) > 0 else -1
            d[val] = current_max+1
    return d


def convert_to_integer(srs):
    d = get_nominal_integer_dict(srs)
    return srs.map(lambda x: d[x])


def convert_cols_categorical_to_numeric(df, col_list=None):
    """
    Convert categorical columns to numeric and leave numeric columns
    as they are. You can force to convert a numerical column if it is
    included in col_list
    :param df: dataframe
    :param col_list: optional list of columns
    :return: dataframe with only numerical values
    """
    ret = pd.DataFrame()
    for column_name in df.columns:
        column = df[column_name]
        if column.dtype == 'object' or column_name in col_list:
            ret[column_name] = convert_to_integer(column)
        else:
            ret[column_name] = column
    return ret


def convert_cols_numeric_to_categorical(df):
    """
    Convert numerical columns to categorical and leave numeric columns
    as they are
    :param df: dataframe
    :return: dataframe with only numerical values
    """
    #TODO
    pass


if __name__ == "__main__":

    df = pd.DataFrame({'letters':['a','b','c'],
                       'numbers':[1,2,3]})
    print("Example of conversion from categorical to numeric")
    df_numeric = convert_cols_categorical_to_numeric(df)
    print(df_numeric)


