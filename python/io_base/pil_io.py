# Info: http://effbot.org/imagingbook/image.htm
from PIL import Image


def save_image(img, filename):
    """Save an image.
    Parameters:
        img (numpy array): An image.
        filename (str): Name of the file.
    Examples:
        >>> img = Image.open('../../share/Lenna.png')
        >>> save_image(img, 'file.jpg')

    """
    img.save(filename)


def read_image(filename):
    """Read an image.
    Parameters:
        filename (str): Name of the file.
    Returns:
        img (PIL image): An image in PIL format.
    Examples:
        >>> img = read_image('../../share/Lenna.png')
        >>> print(img.size)
        (512, 512)
        >>> print(img.mode)
        RGB
        >>> img_gray = read_image('../../share/Lenna_gray.png')
        >>> print(img_gray.size)
        (512, 512)
        >>> print(img_gray.mode)
        L

    """
    return Image.open(filename)
