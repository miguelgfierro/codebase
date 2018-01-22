from ast import literal_eval


def decode_string(s):
    """Convert a string literal to a number or a bool.
    Parameters:
        s (str): String
    Returns:
        val (str,float,int or bool): Value decoded
    Examples:
        >>> decode_string('a')
        'a'
        >>> val = decode_string('1.0')
        >>> type(val)
        <class 'int'>
        >>> val
        1
        >>> val = decode_string('1')
        >>> type(val)
        <class 'int'>
        >>> val
        1
        >>> val = decode_string('1.5')
        >>> type(val)
        <class 'float'>
        >>> val
        1.5
        >>> val = decode_string('True')
        >>> type(val)
        <class 'bool'>
        >>> val
        True

    """
    if isinstance(s, str):
        # Does it represent a literal?
        try:
            val = literal_eval(s)
        except:
            # if it doesn't represent a literal, no conversion is done
            val = s
    else:
        # It's already something other than a string
        val = s
    # Is the float actually an int? (i.e. is the float 1.0 ?)
    if isinstance(val, float):
        if val.is_integer():
            return int(val)
        return val
    return val
