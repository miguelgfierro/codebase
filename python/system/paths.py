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


def count_files_in_folder(folderpath):
    """ Return the number of files in a folder.
    Parameters:
        folderpath (str): folder path
    Returns:
        number (int): number of files in a folder
    Examples:
        >>> count_files_in_folder('C:/run3x/codebase/python/minsc')
        3

    """
    return len(glob.glob(os.path.join(folderpath,'*')))


def get_filenames_in_folder(folderpath):
    """ Return the files names in a folder.
    Parameters:
        folderpath (str): folder path
    Returns:
        number (list): list of files
    Examples:
        >>> get_filenames_in_folder('C:/run3x/codebase/python/minsc')
        ['paths.py', 'system_info.py', '__init__.py']

    """
    names = [os.path.basename(x) for x in glob.glob(os.path.join(folderpath, '*'))]
    return sorted(names)


def make_directory(folderpath):
    """ Make a directory.
    Parameters:
        folderpath (str): folder path
    Examples:
        >>> make_directory('C:/run3x/codebase/python/minsc/dir1/dir2')

    """
    if not os.path.exists(folderpath):
        os.makedirs(folderpath)
