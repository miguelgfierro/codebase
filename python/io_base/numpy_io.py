# Benchmark on IO performance: http://stackoverflow.com/a/41425878/5620182

import numpy as np


def save_file(data, filename):
    """Save a numpy array. The file is saved as `filename.npy`.
    Parameters:
        data (numpy array): An array.
        filename (str): Name of the file.
    Examples:
        >>> a = np.ones(1000)
        >>> save_file(a, 'file')

    """
    np.save(filename, data)


def read_file(filename):
    """Read a numpy array.
    Parameters:
        filename (str): Name of the file.
    Returns:
        data (numpy array): An array.
    Examples:
        >>> b = read_file('file.npy')
        >>> b.shape
        (1000,)

    """
    data = np.load(filename)
    return data


