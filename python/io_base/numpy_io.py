# Benchmark on IO performance: http://stackoverflow.com/a/41425878/5620182

import numpy as np


def save_file(data, filename):
    """Save a np.array. The file is saved as `filename.npy`.
    Args:
        data (np.array): An array.
        filename (str): Name of the file.
    Examples:
        >>> a = np.ones(5)
        >>> save_file(a, 'file')

    """
    np.save(filename, data)


def read_file(filename):
    """Read a np.array.
    Args:
        filename (str): Name of the file.
    Returns:
        data (np.array): An array.
    Examples:
        >>> b = read_file('share/data.npy')
        >>> b.shape
        (5,)

    """
    data = np.load(filename)
    return data

