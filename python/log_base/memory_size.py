import sys


def get_object_size(obj, units='Mb'):
    """Calculate the size of an object.
    Parameters:
        obj (obj or str or array): Object.
        units (str): Units [bytes, Kb, Mb, Gb]
    Returns:
        size (int): Size of the object.
    Examples:
        >>> get_object_size(7, 'bytes')
        24
        >>> get_object_size("ABC", 'bytes')
        36

    """
    s_bytes = sys.getsizeof(obj)
    if units == 'bytes':
        return s_bytes
    elif units == 'Kb':
        return s_bytes/1024
    elif units == 'Mb':
        return s_bytes/1024/1024
    elif units == 'Gb':
        return s_bytes/1024/1024/1024
    else:
        raise AttributeError("Units not correct")

