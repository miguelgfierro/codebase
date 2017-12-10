from __future__ import division
import sys
import psutil


def get_object_size(obj, units='Mb'):
    """Calculate the size of an object.
    Parameters:
        obj (obj or str or array): Object.
        units (str): Units [bytes, Kb, Mb, Gb]
    Returns:
        size (float): Size of the object.
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


def get_ram_memory(units='Mb'):
    """Get the RAM memory of the current machine.
    Parameters:
        units (str): Units [bytes, Kb, Mb, Gb]
    Returns:
        size (float): Memory size.
    Examples:
        >>> get_ram_memory('Gb')
        4.0

    """
    s_bytes = psutil.virtual_memory()[0]
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
