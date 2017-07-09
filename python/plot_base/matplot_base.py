import matplotlib.pyplot as plt
import numpy as np


def plot_image(img):
    """Plot an image.
    Parameters:
        img (numpy array): An image.
    Examples:
        >>> import matplotlib.image as mpimg
        >>> img = mpimg.imread('../../share/Lenna.png')
        >>> img.shape
        (512, 512, 3)
        >>> plot_image(img)
        >>> img_gray = mpimg.imread('../../share/Lenna_gray.png')
        >>> img_gray.shape
        (512, 512)
        >>> plot_image(img_gray)

    """
    cmap = None
    if img.ndim == 2: cmap='gray'
    plt.imshow(img, cmap=cmap)
    plt.axis('off')
    plt.show()


def plot_histogram(hist, bins):
    """Plot an histogram.
    Parameters:
        hist (numpy array): Array with the histogram values.
        bins (numpy array): Array of the histogram bins.
    Examples:
        >>> x = 10 + 5*np.random.randn(1000)
        >>> hist, bins = np.histogram(x, bins=50)
        >>> plot_histogram(hist, bins)

    """
    width = np.diff(bins)
    center = (bins[:-1] + bins[1:]) / 2
    plt.bar(center, hist, align='center', width=width)
    plt.show()
