import random
import numpy as np


def get_n_first_elements(py_list, n_elements):
    """Get the first `n` elements of a list.
    Parameters:
        py_list (list): A list of elements.
        n_elements (int): The number of elements.
    Returns:
        sub_list (list): A list with the first `n` elements of `py_list`.
    Examples:
        >>> py_list = [1,2,3,4,5,6,7,8]
        >>> py_list_first = get_n_first_elements(py_list, 2)
        >>> py_list_first
        [1, 2]

    """
    return py_list[:n_elements]


def get_n_last_elements(py_list, n_elements):
    """Get the last `n` elements of a list.
    Parameters:
        py_list (list): A list of elements.
        n_elements (int): The number of elements.
    Returns:
        sub_list (list): A list with the last `n` elements of `py_list`.
    Examples:
        >>> py_list = [1,2,3,4,5,6,7,8]
        >>> py_list_first = get_n_last_elements(py_list, 2)
        >>> py_list_first
        [7, 8]

    """
    return py_list[-n_elements:]


def find_item_index(py_list, item):
    """Find the index of an item in a list.
    Parameters:
        py_list (list): A list of elements.
        item (int or str): The element in the list.
        n (int): The upper limit of the range to generate, from 0 to `n` - 1.
    Returns:
        index (int): the index of the element.
    Examples:
        >>> py_list = ["foo", "bar", "baz"]
        >>> item = "bar"
        >>> idx = find_item_index(py_list, item)
        >>> print("Index: %d" % idx)
        Index: 1

    """
    return py_list.index(item)


def generate_random_integers(number_values, min_val, max_val):
    """Generate a list with `n` random integers between a `minimum` and a `maximum`.
    Parameters:
        number_values (int): Number of values to generate.
        min_val (int): Minimum value.
        max_val (int): Maximum value.
    Returns:
        result_list (list): A list with random values.
    Examples:
        >>> result_list = generate_random_integers(number_values=5, min_val=0, max_val=10)
        >>> result_list
        [7, 9, 5, 1, 4]

    """
    l = random.sample(range(min_val, max_val), number_values)
    return l


def shuffle_list(py_list, inplace=False):
    """Shuffle a list
    If `inplace=True` the input list is modified (faster & less memory), if `inplace=False` a new list is
    generated (slower & more memory).
    Parameters:
        py_list (list): A list of elements.
        inplace (bool): If `True` the input list is modified, if `False` a new list is generated.
    Returns:
        result_list (list): A list with the values shuffled.
    Examples:
        >>> py_list = [1,2,3,4,5]
        >>> shuffle_list(py_list, True)
        >>> py_list
        [5, 1, 4, 2, 3]
        >>> shuffle_list(py_list, False)
        [5, 3, 2, 1, 4]

    """
    if inplace:
        random.shuffle(py_list)
    else:
        l = py_list[:] # fastest way to shallow copy a list https://stackoverflow.com/a/2612990
        random.shuffle(l)
        return l


def reverse_list(py_list, inplace=True):
    """Reverse a list.
    If `inplace=True` the input list is modified (faster & less memory), if `inplace=False` a new list is
    generated (slower & more memory).
    Parameters:
        py_list (list): A list of elements.
        inplace (bool): If `True` the input list is modified, if `False` a new list is generated.
    Returns:
        result_list (list): A list with the values reversed.
    Examples:
        >>> py_list = [1,2,3,4,5]
        >>> reverse_list(py_list, False)
        [5, 4, 3, 2, 1]
        >>> reverse_list(py_list, True)
        [5, 4, 3, 2, 1]

    """
    if inplace:
        py_list.reverse()
        # py_list[::-1] #don't use, much slower than reverse()
        return py_list
    else:
        result_list = list(reversed(py_list))
        return result_list


def create_consecutive_numbers(initial_num, final_num):
    """Create a list of consecutive numbers from `initial_num` to `final_num`.
    source: http://interactivepython.org/runestone/static/pythonds/AlgorithmAnalysis/Lists.html
    Parameters:
        initial_num (int): The first number of the series.
        final_num (int): The last number of the series.
    Returns:
        result_list (list): A list with values from `initial_num` to `final_num`.
    Examples:
        >>> create_consecutive_numbers(1,5)
        [1, 2, 3, 4, 5]

    """
    #Method 1: append
    #Do not use, slowest of all methods
    #l = []
    #for i in range(initial_num, final_num+1):
    #    l.append(i)

    #Method 2: list comprehension
    #Twice as fast as append
    #l = [i for i in range(initial_num, final_num+1)]

    #Method 3: list constructor
    #Twice as fast as list comprehension
    l = list(range(initial_num, final_num+1))
    return l


def flatten_list_of_lists(list_of_lists):
    """Convert a list os lists to a single list
    Parameters:
         list_of_lists (list of lists): A list of lists.
    Returns:
        result_list (list): A list
    Examples:
        >>> list_of_lists = [[1,2,3],[0,3,9]]
        >>> flatten_list_of_lists(list_of_lists)
        [1, 2, 3, 0, 3, 9]

    """
    result_list = [item for sublist in list_of_lists for item in sublist]
    return result_list


def split_list(py_list, perc_size=[0.8, 0.2], shuffle=False):
    """Split a list in weighted chunks
    Parameters:
        py_list (list): A list of elements.
        perc_size (list): The percentual size of each chunk size.
        shuffle (bool): Shuffle the list or not
    Returns:
        result_list (list of list): A list of lists with the chunks.
    Examples:
        >>> split_list(list(range(7)),[0.47,0.33,0.2])
        [[0, 1, 2], [3, 4, 5], [6]]
        >>> split_list(list(range(10)),[0.6,0.4], True)
        [[1, 2, 3, 6, 9, 5], [4, 8, 0, 7]]

    """
    assert sum(perc_size) == 1, "Percentage sizes do not sum to 1"
    l = py_list[:]
    if shuffle:
        random.shuffle(l)
    # Turn percentages into values between 0 and 1
    splits = np.cumsum(perc_size)

    # Split doesn't need last percent, it will just take what is left
    splits = splits[:-1]

    # Turn values into indices
    splits *= len(l)

    # Turn double indices into integers.
    splits = splits.round().astype(np.int)

    return [list(chunks) for chunks in np.split(l, splits)]


def intersection(list1, list2):
    """Intersection of two lists, returns the common elements in both lists.
    Parameters:
        list1 (list): A list of elements.
        list2 (list): A list of elements.
    Returns:
        result_list (list): A list with the common elements.
    Examples:
        >>> intersection([1,2,3], [2,3,4])
        [2, 3]

    """
    return list(set(list1) & set(list2))
