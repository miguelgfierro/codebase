import cv2
import numpy as np
import urllib.request as urllib


def save_image(img, filename):
    """Save an image.
    Args:
        img (numpy array): An image.
        filename (str): Name of the file.
    Examples:
        >>> img = cv2.imread('../../share/Lenna.png')
        >>> save_image(img, 'file.jpg')

    """
    cv2.imwrite(filename, img)


def read_image(filename, is_color=True):
    """Read an image.
    Args:
        filename (str): Name of the file.
        is_color (bool): Read the image in color.
    Returns:
        img (numpy array): An image.
    Examples:
        >>> img = read_image('../../share/Lenna.png')
        >>> shape = np.array(img.shape)
        >>> print(shape)
        [512 512   3]
        >>> img_gray = read_image('../../share/Lenna.png', False)
        >>> shape_gray = np.array(img_gray.shape)
        >>> print(shape_gray)
        [512 512]

    """
    return cv2.imread(filename, is_color)


def read_image_url(url):
    """Read an image from a URL.
    Args:
        url (str): URL of the file.
    Returns:
        img (numpy array): An image.
    Examples:
        >>> img = read_image_url('https://raw.githubusercontent.com/miguelgfierro/codebase/master/share/Lenna.png')
        >>> shape = np.array(img.shape)
        >>> print(shape)
        [512 512   3]

    """
    try:
        resp = urllib.urlopen(url)
    except urllib.HTTPError:
        raise('Error opening url {0}'.format(url))
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image
