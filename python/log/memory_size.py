import sys


def get_object_size(obj, units='Mb'):
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

if __name__ == "__main__":
    a = 7
    b = "A"
    print(get_object_size(a, 'bytes'))
    print(get_object_size(b, 'bytes'))
