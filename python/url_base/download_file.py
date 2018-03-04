import sys
import os
import wget
if sys.version_info.major == 2:
    # Backward compatibility with python 2.
    from six.moves import urllib
    urlretrieve = urllib.request.urlretrieve
else:
    from urllib.request import urlretrieve


def maybe_download(filename, url, expected_bytes=None, verbose=False):
    """Download a file if it is not already downloaded.
    Args:
        filename (str): File name.
        url (str): URL of the file to download.
        expected_bytes (int): Expected file size in bytes.
        verbose (bool): Verbose flag
    Returns:
        filename (str): File name of the file downloaded
    Examples:
        >>> url = 'https://raw.githubusercontent.com/miguelgfierro/codebase/master/LICENSE'
        >>> if os.path.exists('license.txt'): os.remove('license.txt')
        >>> filename = maybe_download('license.txt', url, expected_bytes=1531, verbose=True)
        File license.txt verified with 1531 bytes
        >>> filename = maybe_download('license.txt', url, expected_bytes=1531, verbose=True)
        File license.txt already downloaded
        File license.txt verified with 1531 bytes
        >>> filename = maybe_download('license.txt', url)
        >>> filename
        'license.txt'

    """
    if not os.path.exists(filename):
        if verbose:
            filename = wget.download(url, out=filename)
        else:
            filename, _ = urlretrieve(url, filename)
    else:
        if verbose: print("File {} already downloaded".format(filename))
    if expected_bytes is not None:
        statinfo = os.stat(filename)
        if statinfo.st_size == expected_bytes:
            if verbose: print('File {} verified with {} bytes'.format(filename, expected_bytes))
        else:
            raise Exception('Failed to verify {}'.format(filename))
    return filename


