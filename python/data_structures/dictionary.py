def invert_dictionary(dictionary):
    """Invert a dictionary.
    NOTE: if the values of the dictionary are not unique, the function returns the last mapping
    Args: 
        dictionary (dict): A dictionary
    Returns:
        dict: inverted dictionary
    Examples:
        >>> d = {1: 0, "a": 2, "b": "c"}
        >>> invert_dictionary(d)
        {0: 1, 2: 'a', 'c': 'b'}
        >>> d = {1: 0, "a": 2, "b": "c", 5: 0}
        >>> invert_dictionary(d)
        {0: 5, 2: 'a', 'c': 'b'}

    """
    return {v: k for k, v in dictionary.items()}
