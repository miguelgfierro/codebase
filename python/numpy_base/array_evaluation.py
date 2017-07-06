import numpy as np


def has_same_sign_or_zero(data):
    """ Evaluate if the array has all elements with the same sign or zero.
    Parameters:
        data (numpy array): An array.
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

