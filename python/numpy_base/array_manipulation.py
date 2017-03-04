import numpy as np


def split_array_in_subarrays(data, n_subarrays, axis=0):
    """Split an array in subarrays. Don't need to have the same size.
    Parameters:
        data (numpy array): An array.
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
    Parameters:
        array_list (list): A list of arrays.
        axis (int): Axis of the operation.
    Returns:
        result (numpy array): An array of concatenated values.
    Examples:
        >>> data1 = np.array([(1,2,3),(2,3,4)], dtype='int')
        >>> data2 = np.array([(4,5),(5,6)], dtype='int')
        >>> result = concatenate_arrays([data1, data2], 1)
        >>> result
        array([[1, 2, 3, 4, 5],
               [2, 3, 4, 5, 6]])

    """
    return np.concatenate(array_list, axis)