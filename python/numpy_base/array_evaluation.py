import numpy as np


def has_same_sign(data):
    """ Evaluate if the array has all elements with the same sign.
    Args:
        data (np.array): An array.
    Returns:
        flag (bool): Boolean with the evaluation.
    Examples:
        >>> data = np.array([(1,2,3),(2,3,4)])
        >>> has_same_sign(data)
        True
        >>> data = np.array([0,0])
        >>> has_same_sign(data)
        WARNING: All zeros
        True
        >>> data = np.array([(0,0),(1,2)])
        >>> has_same_sign(data)
        False

    """
    try:
        idx = next((idx for idx, val in np.ndenumerate(data) if val != 0))
    except StopIteration:
        print('WARNING: All zeros')
        return True
    return np.all(data > 0) if data[idx] > 0 else np.all(data < 0)


def has_same_sign_or_zero(data):
    """ Evaluate if the array has all elements with the same sign or zero.
    Args:
        data (np.array): An array.
    Returns:
        flag (bool): Boolean with the evaluation.
    Examples:
        >>> data = np.array([(1,2,3),(2,3,4)])
        >>> has_same_sign_or_zero(data)
        True
        >>> data = np.array([0,0])
        >>> has_same_sign_or_zero(data)
        WARNING: All zeros
        True
        >>> data = np.array([(0,0),(-1,2)])
        >>> has_same_sign_or_zero(data)
        False

    """
    try:
        idx = next((idx for idx, val in np.ndenumerate(data) if val != 0))
    except StopIteration:
        print('WARNING: All zeros')
        return True
    return np.all(data >= 0) if data[idx] >= 0 else np.all(data <= 0)


def count_items(data, item):
    """Count the appearances of items in data
    Args:
        data (np.array): An array.
        item (int, float or str): The item to count.
    Returns:
        result (int): Count of appearances of item in data.
    Examples:
        >>> data = np.array([(1,0,0,0,1,1,0)])
        >>> count_items(data, 1)
        3

    """
    return np.count_nonzero(data == item)
