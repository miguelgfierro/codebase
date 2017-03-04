import sys
import pkg_resources


def get_python_version():
    """Get the system's python version.
    Returns:
        version (str): Python version.
    Examples:
        >>> get_python_version()
        '2.7.12 |Anaconda 4.0.0 (64-bit)| (default, Jun 29 2016, 11:07:13) [MSC v.1500 64 bit (AMD64)]'
        
    """
    return sys.version


def get_library_version(library_name):
    """Get the version of a library.
    Parameters:
        library_name (str): Name of the library.
    Returns:
        version (str): Version of the library.
    Examples:
        >>> get_library_version("pandas")
        '0.19.2'
       
    """
    return pkg_resources.get_distribution(library_name).version
