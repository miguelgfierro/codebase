import random


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


def create_consecutive_numbers(final_num):
    """Create a list of consecutive numbers from 0 to `final_num`.
    source: http://interactivepython.org/runestone/static/pythonds/AlgorithmAnalysis/Lists.html
    Parameters:
        final_num (int): The last number of the series.
    Returns:
        result_list (list): A list with values from 0 to `final_num`.
    Examples:
        >>> create_consecutive_numbers(5)
        [0, 1, 2, 3, 4]

    """
    #Method 1: append
    #Do not use, slowest of all methods
    #l = []
    #for i in range(final_num):
    #    l.append(i)

    #Method 2: list comprehension
    #Twice as fast as append
    #l = [i for i in range(final_num)]

    #Method 3: list constructor
    #Twice as fast as list comprehension
    l = list(range(final_num))
    return l


def from_list_of_lists_to_list(list_of_lists):
    """Convert a list os lists to a single list
    Parameters:
         list_of_lists (list of lists): A list of lists.
    Returns:
        result_list (list): A list
    Examples:
        >>> list_of_lists = [[1,2,3],[0,3,9]]
        >>> from_list_of_lists_to_list(list_of_lists)
        [1, 2, 3, 0, 3, 9]

    """
    result_list = [item for sublist in list_of_lists for item in sublist]
    return result_list

