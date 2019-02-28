from skimage import io


def save_image(img, filename):
    """Save an image.
    
    Args:
        img (np.array): An image.
        filename (str): Name of the file.
    
    Examples:
        >>> img = io.imread('share/Lenna.png')
        >>> save_image(img, 'file.jpg')
    """
    io.imsave(filename, img)


def read_image(filename, is_color=True):
    """Read an image.
    
    Args:
        filename (str): Name of the file.
        is_color (bool): Read the image in color.
    
    Returns:
        img (np.array): An image.
    
    Examples:
        >>> img = read_image('share/Lenna.png')
        >>> img.shape
        (512, 512, 3)
        >>> img_gray = read_image('share/Lenna.png', False)
        >>> img_gray.shape
        (512, 512)
    """
    is_gray = not is_color
    return io.imread(filename, as_gray=is_gray)


def read_image_url(url):
    """Read an image from a URL.
    
    Args:
        url (str): URL of the file.
    
    Returns:
        np.array: An image.
    
    Examples:
        >>> img = read_image_url('https://raw.githubusercontent.com/miguelgfierro/codebase/master/share/Lenna.png')
        >>> img.shape
        (512, 512, 3)
    """
    return io.imread(url)
