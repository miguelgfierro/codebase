import numpy as np


def split_array_in_subarrays(data, n_subarrays, axis=0):
    """Split an array in subarrays. Don't need to have the same size.
    Args:
        data (np.array): An array.
        n_subarrays (int): The number of subarrays.
        axis (int): Axis of the operation.
    Returns:
        array_list (list): A list with subarrays.
    Examples:
        >>> data = np.array([(1,2,3,4,5),(2,3,4,5,6)], dtype='int')
        >>> array_list = split_array_in_subarrays(data, 2, 1)
        >>> array_list[0]
        array([[1, 2, 3],
               [2, 3, 4]])
        >>> array_list[1]
        array([[4, 5],
               [5, 6]])

    """
    return np.array_split(data, n_subarrays, axis)


def concatenate_arrays(array_list, axis=0):
    """Concatenate a list of arrays.
    Args:
        array_list (list): A list of arrays.
        axis (int): Axis of the operation.
    Returns:
        result (np.array): An array of concatenated values.
    Examples:
        >>> data1 = np.array([(1,2,3),(2,3,4)], dtype='int')
        >>> data2 = np.array([(4,5),(5,6)], dtype='int')
        >>> result = concatenate_arrays([data1, data2], 1)
        >>> result
        array([[1, 2, 3, 4, 5],
               [2, 3, 4, 5, 6]])

    """
    return np.concatenate(array_list, axis)


def one_hot_encoding_integer(y, num_classes=None):
    """Converts a class vector (integers) to binary class matrix.
    source: https://github.com/fchollet/keras/blob/d956d19fccf6de6344c282218f1b027453785fa9/keras/utils/np_utils.py
    Args:
        y (int): An integer class from 0 to num_classes.
        num_classes (int): Total number of classes.
    Returns:
        result (np.array): An array of one hot encoded classes.
    Examples:
        >>> one_hot_encoding_integer(2, 3)
        array([0, 0, 1])

    """
    y = np.array(y, dtype='int')
    input_shape = y.shape
    if input_shape and input_shape[-1] == 1 and len(input_shape) > 1:
        input_shape = tuple(input_shape[:-1])
    y = y.ravel()
    if not num_classes:
        num_classes = np.max(y) + 1
    n = y.shape[0]
    categorical = np.zeros((n, num_classes), dtype='int')
    categorical[np.arange(n), y] = 1
    output_shape = input_shape + (num_classes,)
    categorical = np.reshape(categorical, output_shape)
    return categorical


def binarize_array(data, threshold, lower, upper):
    """Binarize an array based on a threshold into lower and upper values.
    Args:
        data (np.array): An array.
        threshold (int or float): Threshold for binarization.
        lower (int or float): Lower value.
        upper (int or float): Upper value.
    Returns:
        result (np.array): A binarized array.
    Examples:
        >>> data = np.array([(1,3,5),(2,4,6)], dtype='int')
        >>> binarize_array(data, 3, 1, 6)
        array([[1, 1, 6],
               [1, 6, 6]])

    """
    return np.where(data > threshold, upper, lower)
