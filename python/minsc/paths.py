import os
import glob


def get_current_folder_path():
    """ Get parent path of current file.
    Returns:
        path (str): parent path
    Examples:
        >>> print(get_current_folder_path())
        C:\\run3x\\codebase\\python\\minsc

    """
    return os.path.abspath(os.path.dirname(__file__))


def get_parent_folder_path():
    """ Get parent path of current file.
    Returns:
        path (str): parent path
    Examples:
        >>> print(get_parent_folder_path())
        C:\\run3x\\codebase\\python

    """
    return os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))


def get_file_count(folderpath):
    """ Return the number of files in a folder.
    Parameters:
        folderpath (str): folder path
    Returns:
        number (int): number of files in a folder
    Examples:
        >>> get_file_count('C:/run3x/codebase/python/minsc')
        3

    """
    return len(glob.glob(os.path.join(folderpath,'*')))