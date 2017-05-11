from skimage import io
import numpy as np


def save_image(img, filename):
    """Save an image.
    Parameters:
        img (numpy array): An image.
        filename (str): Name of the file.
    Examples:
        >>> img = io.imread('../../share/Lenna.png')
        >>> save_image(img, 'file.jpg')

    """
    io.imsave(filename, img)


def read_image(filename, is_color=True):
    """Read an image.
    Parameters:
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
    is_gray = not is_color
    return io.imread(filename, as_grey=is_gray)


def read_image_url(url):
    """Read an image from a URL.
    Parameters:
        url (str): URL of the file.
    Returns:
        img (numpy array): An image.
    Examples:
        >>> img = read_image_url('https://raw.githubusercontent.com/miguelgfierro/codebase/master/share/Lenna.png')
        >>> shape = np.array(img.shape)
        >>> print(shape)
        [512 512   3]

    """
    return io.imread(url)
