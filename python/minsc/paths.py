import os


def get_current_folder_path():
    """ Get parent path of current file.
    Returns:
        path (string): parent path
    Examples:
        >>> print(get_current_folder_path())
        C:\\run3x\\codebase\\python\\minsc

    """
    return os.path.abspath(os.path.dirname(__file__))


def get_parent_folder_path():
    """ Get parent path of current file.
    Returns:
        path (string): parent path
    Examples:
        >>> print(get_parent_folder_path())
        C:\\run3x\\codebase\\python

    """
    return os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))


