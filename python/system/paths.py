import os
import glob
import errno


def get_current_folder_path():
    """ Get parent path of current file.
    Returns:
        path (str): parent path
    Examples:
        >>> get_current_folder_path() #doctest: +ELLIPSIS
        '.../codebase/python/system'

    """
    return os.path.abspath(os.path.dirname(__file__))


def get_parent_folder_path():
    """ Get parent path of current file.
    Returns:
        path (str): parent path
    Examples:
        >>> get_parent_folder_path() #doctest: +ELLIPSIS
        '.../codebase/python'

    """
    return os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))


def count_files_in_folder(folderpath, pattern="*"):
    """ Return the number of files in a folder.
    Args:
        folderpath (str): folder path.
        pattern (str): Pattern to filter.
    Returns:
        number (int): number of files in a folder
    Examples:
        >>> count_files_in_folder("cpp")
        5
        >>> count_files_in_folder("cpp", pattern="*.txt")
        1

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
        >>> l = get_filenames_in_folder("cpp")   
        >>> Counter(l) == Counter(['io', 'log', 'numeric', 'CMakeLists.txt', 'playground.cpp'])
        True
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
        >>> l = get_files_in_folder_recursively("cpp")
        >>> Counter(l) == Counter(['CMakeLists.txt', 'playground.cpp', 'io/read_file.cpp', 'io/read_file.hpp', 'log/timer.hpp', 'numeric/math_constants.hpp', 'numeric/math_utils.hpp'])
        True
        
    """
    if folderpath[-1] != os.path.sep:  # Add final '/' if it doesn't exist
        folderpath += os.path.sep
    names = [
        x.replace(folderpath, "")
        for x in glob.iglob(folderpath + "/**", recursive=True)
        if os.path.isfile(x)
    ]
    return sorted(names)


def remove_file(filename):
    """Remove file if it exists.
    Original code: https://stackoverflow.com/a/10840586/5620182
    Examples:
        >>> shutil.copyfile(os.path.join("share", "traj.csv"), "copy.csv")
        >>> os.path.isfile("copy.csv")
        True
        >>> remove_file("copy.csv")
        >>> os.path.isfile("copy.csv")
        False

    """
    try:
        os.remove(filename)
    except OSError as e:  # this would be "except OSError, e:" before Python 2.6
        if e.errno != errno.ENOENT:  # errno.ENOENT = no such file or directory
            raise  # re-raise exception if a different error occurred
