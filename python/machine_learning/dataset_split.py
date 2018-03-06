from sklearn.model_selection import train_test_split
from sklearn.utils import indexable


def split_train_test(X, y, test_size=0.2):
    """Split a dataset into train and test sets.
    Args:
        X (np.array or pd.DataFrame): Features.
        y (np.array or pd.DataFrame): Labels.
        test_size (float): Percentage in the test set.
    Returns:
        X_train, X_test, y_train, y_test (list): List with the dataset splitted.
    Example:
        >>> import numpy as np
        >>> X = np.random.randint(0,10, (100,5))
        >>> y = np.random.randint(0,1, 100)
        >>> X_train, X_test, y_train, y_test = split_train_test(X, y, test_size=0.2)
        >>> print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)
        (80, 5) (20, 5) (80,) (20,)

    """
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42, stratify=y)
    return X_train, X_test, y_train, y_test


def split_train_val_test(*arrays, val_size=0.2, test_size=0.2, random_seed=42):
    """Split a dataset into train, validation and test sets.
    Args:
        *arrays (list, np.array, pd.DataFrame): Dataset to split, it can be one or two objects with the same number of
                                                rows.
        val_size (float): Percentage in the validation set.
        test_size (float): Percentage in the test set.
        random_seed (float): Seed.
    Returns:
        *arrays_out (list): List with the dataset splitted. If the input is one element `X`, the output will be
                            `X_train, X_val, X_test`. If the input is two elements `X,y`, the output will be
                            `X_train, X_val, X_test, y_train, y_val, y_test`.
    Example:
        >>> import numpy as np
        >>> X = np.random.randint(0,10, (100,5))
        >>> y = np.random.randint(0,1, 100)
        >>> X_train, X_val, X_test, y_train, y_val, y_test = split_train_val_test(X, y, val_size=0.2, test_size=0.2)
        >>> print(X_train.shape, X_val.shape, X_test.shape)
        (60, 5) (20, 5) (20, 5)
        >>> print(y_train.shape, y_val.shape, y_test.shape)
        (60,) (20,) (20,)
        >>> import pandas as pd
        >>> df = pd.DataFrame(np.random.randn(100, 5), columns=list('ABCDE'))
        >>> df_train, df_val, df_test = split_train_val_test(df, val_size=0.2, test_size=0.2)
        >>> print(df_train.shape, df_val.shape, df_test.shape)
        (60, 5) (20, 5) (20, 5)

    """
    n_arrays = len(arrays)
    if n_arrays == 1:
        X_train, X_test = train_test_split(*arrays, test_size=test_size, random_state=random_seed)
        X_train, X_val = train_test_split(X_train, test_size=val_size/(1-test_size), random_state=random_seed)
        return X_train, X_val, X_test
    elif n_arrays == 2:
        X, y = indexable(*arrays)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_seed, stratify=y)
        X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=val_size/(1-test_size), random_state=random_seed, stratify=y_train)
        return X_train, X_val, X_test, y_train, y_val, y_test
    else:
        raise ValueError("Wrong number of inputs")

