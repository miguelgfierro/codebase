# Benchmark on IO performance: http://stackoverflow.com/a/41425878/5620182

try:
    import cPickle as pickle
except ImportError:
    import pickle


def save_file(data, filename):
    """Save data as pickle. The standard pickle file name is `*.pk`.
    Args:
        data (numpy array or dict): Data to save.
        filename (str): Name of the file.
    Examples:
        >>> import numpy as np
        >>> data = np.ones(5)
        >>> save_file(data, 'file.pk')

    """
    pickle.dump(data, open(filename, "wb"))


def read_file(filename):
    """Read a pickle file.
    Args:
        filename (str): Name of the file.
    Returns:
        data (np.array or dict): Data to read.
    Examples:
        >>> read_file('share/data.pk')
        array([1., 1., 1., 1., 1.])

    """
    data = pickle.load(open(filename, "rb"))
    return data

