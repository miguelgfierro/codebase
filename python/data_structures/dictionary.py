def invert_dictionary(dictionary):
    """Invert a dictionary.
    NOTE: if the values of the dictionary are not unique, the function returns the last mapping
    Args: 
        dictionary (dict): A dictionary
    Returns:
        dict: inverted dictionary
    Examples:
        >>> d = {1: 0, "a": 2, "b": "c"}
        >>> d_inv = invert_dictionary(d)
        >>> OrderedDict(sorted(d_inv.items()))
        OrderedDict([(0, 1), (2, 'a'), ('c', 'b')])
        >>> d = {1: 0, "a": 2, "b": "c", 5: 0}
        >>> d_inv = invert_dictionary(d)
        >>> OrderedDict(sorted(d_inv.items()))
        OrderedDict([(0, 5), (2, 'a'), ('c', 'b')])

    """
    return {v: k for k, v in dictionary.items()}
