import sys
if sys.version_info.major == 2:
    # Backward compatibility with python 2.
    from six.moves import urllib
    urlretrieve = urllib.request.urlretrieve
else:
    from urllib.request import urlretrieve


def download_file_urllib(url, filename=None):
    """Download a file using urllib.
    NOTE: It is recommended to use the package requests https://docs.python.org/2/library/urllib.html
    Parameters:
        url (str): URL of the file to download.
    Returns:
        fname (str): filename of the file downloaded
    Examples:
        >>> url = 'https://raw.githubusercontent.com/miguelgfierro/codebase/master/LICENSE'
        >>> filename = download_file_urllib(url, 'license.txt')
        >>> filename
        'license.txt'
        >>> line = open(filename).readline()
        >>> print(line)
        BSD License
        <BLANKLINE>

    """
    if filename is None: filename = url.rsplit('/', 1)[-1]
    fname, headers = urlretrieve(url, filename)
    return fname

