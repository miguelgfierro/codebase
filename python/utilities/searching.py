

def sequential_search(alist, item):
    """Sequential search
    Complexity:
    item is present: best case=1, worst case=n, avg=n/2
    item not present: best case=n, worst case=n, avg=n
    Parameters:
        alist (list): A list.
        item (int): The item to search.
    Returns:
        found (bool): Boolean with the answer of the search.
    Examples:
        >>> alist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
        >>> sequential_search(alist, 3)
        False
        >>> sequential_search(alist, 13)
        True

    """
    pos = 0
    found = False
    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos += 1
    return found


def ordered_sequential_search(ordered_list, item):
    """Ordered Sequential search
    Complexity:
    item is present: best case=1, worst case=n, avg=n/2
    item not present: best case=1, worst case=n, avg=n/2
    Parameters:
        ordered_list (list): An ordered list.
        item (int): The item to search.
    Returns:
        found (bool): Boolean with the answer of the search.
    Examples:
        >>> alist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
        >>> sequential_search(alist, 3)
        False
        >>> sequential_search(alist, 13)
        True

    """
    pos = 0
    found = False
    stop = False
    while pos < len(ordered_list) and not found and not stop:
        if ordered_list[pos] == item:
            found = True
        else:
            if ordered_list[pos] > item:
                stop = True
            else:
                pos += 1
    return found





