import numpy as np


def softmax(x):
    """Softmax of a vector. It is the normalized exponential function. Softmax is a generalization of the logistic
    function that squashes a vector z into another vector  of real values in the range (0, 1) that add up to 1.
    Parameters:
        x (list or numpy array): Input list or array.
    Returns:
        result (numpy array): The softmax of the array.
    Examples:
        >>> scores = [12, 5, 1]
        >>> softmax(scores)
        array([  9.99072278e-01,   9.11035992e-04,   1.66862063e-05])
        >>> sum(softmax(scores))
        1.0

    """
    return np.exp(x) / np.sum(np.exp(x), axis=0)


def RELU(x, inplace=False):
    """Rectified Linear Unit, removing the negative parts of the input: max(x,0)
    Benchmark: https://stackoverflow.com/a/40013151/5620182
    Parameters:
        x (list or numpy array): Input list or array.
        inplace (bool): Inplace flag.
    Returns:
        result (numpy array): The RELU of the array (if inplace is True).
    Examples:
        >>> x = np.array([[1,1,-3],[0.5,-1,1]])
        >>> RELU(x)
        array([[ 1. ,  1. , -0. ],
               [ 0.5, -0. ,  1. ]])
        >>> RELU(x, inplace=True)
        >>> x
        array([[ 1. ,  1. ,  0. ],
               [ 0.5,  0. ,  1. ]])

    """
    if inplace:
        np.maximum(x, 0, x)
    else:
        return x * (x > 0)


