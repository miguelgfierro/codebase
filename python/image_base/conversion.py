import numpy as np
from PIL import Image
import cv2
import matplotlib.pylab as plt


def image_pil2scipy_array(img):
    """Convert a PIL image to a numpy image.
    Parameters:
        img (PIL image): A PIL image of uint8 between 0 and 255.
    Returns:
        img_new (numpy array): A numpy image of uint8 between 0 and 255.
    Examples:
        >>> from scipy import misc
        >>> img = Image.open('../../share/Lenna.png')
        >>> img_conv = image_pil2scipy_array(img)
        >>> img_conv.shape
        (512, 512, 3)
        >>> img_base = misc.imread('../../share/Lenna.png')
        >>> np.all(img_base==img_conv)
        True

    """
    return np.array(img)


def image_scipy_numpy2pil(img):
    """Convert a numpy image to a PIL image.
    Parameters:
        img (numpy array): A numpy image of uint8 between 0 and 255.
    Returns:
        img_new (PIL image): A PIL image.
    Examples:
        >>> from scipy import misc
        >>> from PIL import ImageChops
        >>> img = misc.imread('../../share/Lenna.png')
        >>> img_conv = image_scipy_numpy2pil(img)
        >>> img_conv.size
        (512, 512)
        >>> img_base = Image.open('../../share/Lenna.png')
        >>> ImageChops.difference(img_conv, img_base).getbbox()

    """
    img_new = Image.fromarray(img)
    return img_new


def image_cv2pil(img):
    """Convert a opencv image to a PIL image.
    Parameters:
        img (numpy array): A numpy image loaded with opencv of uint8 between 0 and 255 using BGR channels.
    Returns:
        img_new (PIL image): A PIL image.
    Examples:
        >>> from PIL import ImageChops
        >>> img = cv2.imread('../../share/Lenna.png')
        >>> img_conv = image_cv2pil(img)
        >>> img_conv.size
        (512, 512)
        >>> img_base = Image.open('../../share/Lenna.png')
        >>> ImageChops.difference(img_conv, img_base).getbbox()

    """
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_new = Image.fromarray(img)
    return img_new


def image_pil2cv(img):
    """Convert a PIL image to an opencv image.
    Parameters:
        img (PIL image): A PIL image of uint8 between 0 and 255.
    Returns:
        img_new (numpy array): A numpy image of uint8 between 0 and 255.
    Examples:
        >>> img = Image.open('../../share/Lenna.png')
        >>> img_conv = image_pil2cv(img)
        >>> img_conv.shape
        (512, 512, 3)
        >>> img_base = cv2.imread('../../share/Lenna.png')
        >>> np.all(img_base==img_conv)
        True

    """
    img_new = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    return img_new


def image_cv2plt(img):
    """Convert a opencv image to a matplotlib image.
    Parameters:
        img (numpy array): A numpy image loaded with opencv of uint8 between 0 and 255 using BGR channels.
    Returns:
        img_new (numpy array): A matplotlib image of float32 between 0 and 1 using RGB channels.
    Examples:
        >>> img = cv2.imread('../../share/Lenna.png')
        >>> img_conv = image_cv2plt(img)
        >>> img_conv.shape
        (512, 512, 3)
        >>> img_base = plt.imread('../../share/Lenna.png')
        >>> np.all(np.isclose(img_base, img_conv))
        True

    """
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_new = img.astype(np.float32)/255.0
    return img_new


def image_plt2cv(img):
    """Convert a matplotlib image to an opencv image.
    Parameters:
        img (numpy array): A matplotlib image of float32 between 0 and 1 using RGB channels.
    Returns:
        img_new (numpy array): A numpy image of uint8 between 0 and 255 using BGR channels.
    Examples:
        >>> img = plt.imread('../../share/Lenna.png')
        >>> img_conv = image_plt2cv(img)
        >>> img_conv.shape
        (512, 512, 3)
        >>> img_base = cv2.imread('../../share/Lenna.png')
        >>> np.all(img_base==img_conv)
        True

    """
    img = img*255
    img_new = cv2.cvtColor(np.array(img, dtype=np.uint8), cv2.COLOR_RGB2BGR)
    return img_new


def image_pil2plt(img):
    """Convert a PIL image to an matplotlib image.
    Parameters:
        img (PIL image): A PIL image of uint8 between 0 and 255.
    Returns:
        img_new (numpy array): A matplotlib image of float32 between 0 and 1 using RGB channels.
    Examples:
        >>> img = Image.open('../../share/Lenna.png')
        >>> img_conv = image_pil2plt(img)
        >>> img_conv.shape
        (512, 512, 3)
        >>> img_base = plt.imread('../../share/Lenna.png')
        >>> np.all(img_base==img_conv)
        True

    """
    img_new = np.array(img, dtype=np.float32)/255.0
    return img_new


def image_plt2pil(img):
    pass