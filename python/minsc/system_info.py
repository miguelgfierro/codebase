import sys
import pkg_resources

No
def get_python_version():
    """Get the system's python version.
    Returns:
        version (str): Python version.
        
    """
    return sys.version


def get_library_version(library_name):
    """Get the version of a library.
    Parameters:
        library_name (str): Name of the library.
    Returns:
        version (str): Version of the library.
    Examples:
        >>> print(get_library_version("pandas")
       
    """
    return pkg_resources.get_distribution(library_name)
