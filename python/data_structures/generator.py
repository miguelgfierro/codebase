import numpy as np


def yield_data(data, batch_size, complete_batches=False):
    """Yield an array in batches.
    Args:
        data (numpy array or list): An array or list.
        batch_size (int): The size of the data batch yielded.
        complete_batches (bool): If `True` it will return complete batches, if `False` it will return the complete
                                 list so the last batch may have a different size.
    Returns:
        generator (iterable): An iterator that yield the data.
    Examples:
        >>> data = np.array([1,2,3,4,5,6,7,8,9,10,11,12]).reshape(3,2,2)
        >>> for l in yield_data(data, 2, False):
        ...     print(l)
        [[[1 2]
          [3 4]]
        <BLANKLINE>
         [[5 6]
          [7 8]]]
        [[[ 9 10]
          [11 12]]]
        >>> for l in yield_data(data, 2, True):
        ...     print(l)
        [[[1 2]
          [3 4]]
        <BLANKLINE>
         [[5 6]
          [7 8]]]
        >>> py_list = [0,0,1,1,2,2,3,3,4,4]
        >>> for l in yield_data(py_list, 4, False):
        ...     print(l)
        [0, 0, 1, 1]
        [2, 2, 3, 3]
        [4, 4]

    """
    if complete_batches:
        for i in range(len(data)//batch_size):
            yield data[i*batch_size:(i+1)*batch_size]
    else:
        for i in range(0, len(data), batch_size):
            yield data[i:i + batch_size]
