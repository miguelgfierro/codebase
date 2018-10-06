import os
import glob


def get_current_folder_path():
    """ Get parent path of current file.
    Returns:
        path (str): parent path
    Examples:
        >>> print(get_current_folder_path()) #doctest: +ELLIPSIS
        .../codebase/python/system

    """
    return os.path.abspath(os.path.dirname(__file__))


def get_parent_folder_path():
    """ Get parent path of current file.
    Returns:
        path (str): parent path
    Examples:
        >>> print(get_parent_folder_path()) #doctest: +ELLIPSIS
        .../codebase/python

    """
    return os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))


def count_files_in_folder(folderpath):
    """ Return the number of files in a folder.
    Args:
        folderpath (str): folder path
    Returns:
        number (int): number of files in a folder
    Examples:
        >>> count_files_in_folder("python/system")
        5

    """
    return len(glob.glob(os.path.join(folderpath, "*")))


def count_files_in_folder_recursively(folderpath):
    """ Return the number of files in a folder recursively.
    Args:
        folderpath (str): folder path
    Returns:
        number (int): number of files in a folder
    Examples:
        >>> count_files_in_folder_recursively("cpp")
        7

    """
    if folderpath[-1] != os.path.sep:  # Add final '/' if it doesn't exist
        folderpath += os.path.sep
    return len(
        [x for x in glob.iglob(folderpath + "/**", recursive=True) if os.path.isfile(x)]
    )


def get_filenames_in_folder(folderpath):
    """ Return the files or folder names inside a folder.
    Args:
        folderpath (str): folder path
    Returns:
        filelist (list): list of files
    Examples:
        >>> get_filenames_in_folder("python/system")
        ['memory_size.py', 'notebook_memory_management.py', 'paths.py', 'system_info.py', '__init__.py']

    """
    names = [os.path.basename(x) for x in glob.glob(os.path.join(folderpath, "*"))]
    return sorted(names)


def get_files_in_folder_recursively(folderpath):
    """ Return the files inside a folder recursively.
    Args:
        folderpath (str): folder path
    Returns:
        filelist (list): list of files
    Examples:
        >>> get_files_in_folder_recursively("cpp")
        ['CMakeLists.txt', 'playground.cpp', 'io/read_file.cpp', 'io/read_file.hpp', 'log/timer.hpp', 'numeric/math_constants.hpp', 'numeric/math_utils.hpp']

    """
    if folderpath[-1] != os.path.sep:  # Add final '/' if it doesn't exist
        folderpath += os.path.sep
    names = [
        x.replace(folderpath, "")
        for x in glob.iglob(folderpath + "/**", recursive=True)
        if os.path.isfile(x)
    ]
    return sorted(names)

