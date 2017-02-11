import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def plot_image(img):
    """Plot an image.
    Parameters:
        img (numpy array): An image.
    Examples:
        >>> img = mpimg.imread('../../share/Lenna.png')
        >>> import numpy as np
        >>> print(np.array(img.shape, dtype='int'))
        [512 512   3]
        >>> plot_image(img)
        >>> img_gray = mpimg.imread('../../share/Lenna_gray.png')
        >>> print(np.array(img_gray.shape, dtype='int'))
        [512 512]
        >>> plot_image(img_gray)

    """
    cmap = None
    if img.ndim == 2: cmap='gray'
    plt.imshow(img, cmap=cmap)
    plt.show()
