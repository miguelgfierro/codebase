import numpy as np


def softmax(vect):
    """Softmax of a vector. It is the normalized exponential function. Softmax is a generalization of the logistic
    function that squashes a vector z into another vector  of real values in the range (0, 1) that add up to 1.
    Parameters:
        vect (list or numpy array): Input list or array.
    Returns:
        softmax (numpy array): The softmax of the array.
    Examples:
        >>> scores = [12, 5, 1]
        >>> softmax(scores)
        array([  9.99072278e-01,   9.11035992e-04,   1.66862063e-05])
        >>> sum(softmax(scores))
        1.0

    """
    return np.exp(vect) / np.sum(np.exp(vect), axis=0)

