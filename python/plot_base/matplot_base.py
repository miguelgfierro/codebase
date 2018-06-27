import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d


def plot_image(img):
    """Plot an image.
    Args:
        img (np.array): An image.
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
    Args:
        hist (np.array): Array with the histogram values.
        bins (np.array): Array of the histogram bins.
    Examples:
        >>> x = 10 + 5*np.random.randn(1000)
        >>> hist, bins = np.histogram(x, bins=50)
        >>> plot_histogram(hist, bins)

    """
    width = np.diff(bins)
    center = (bins[:-1] + bins[1:]) / 2
    plt.bar(center, hist, align='center', width=width)
    plt.show()


def plot_traj(y, x=None, title=None, xlabel=None, ylabel=None, color='b'):
    """Plot a trajectory of points (x,y). If x is None it just take range(len(y)).
    Args:
        y (list or np.array): Y axis values.
        x (list or np.array): X axis values.
        title (str): Plot title.
        xlabel (str): X axis label.
        ylabel (str): Y axis label.
        color (str): Matplotlib color https://matplotlib.org/api/colors_api.html?highlight=color#module-matplotlib.colors.
    Examples:
        >>> plot_traj([0.5, 0.7, 1.3, 1.7])
        >>> plot_traj([0.5, 0.7, 1.3, 1.7], np.array([1,2,3,4]), title='Traj', xlabel='x', ylabel='y',color='r')

    """
    plt.figure()
    if x is None: x = range(len(y))
    plt.plot(x, y, color=color)
    if title is not None: plt.title(title)
    if xlabel is not None: plt.xlabel(xlabel)
    if ylabel is not None: plt.ylabel(ylabel)
    plt.show()


def plot_traj_interpolate(y, x=None, title=None, xlabel=None, ylabel=None, color='b'):
    """Plot a trajectory of points (x,y). If x is None it just take range(len(y)).
    Args:
        y (list or np.array): Y axis values.
        x (list or np.array): X axis values.
        title (str): Plot title.
        xlabel (str): X axis label.
        ylabel (str): Y axis label.
        color (str): Matplotlib color https://matplotlib.org/api/colors_api.html?highlight=color#module-matplotlib.colors.
    Examples:
        >>> plot_traj([0.5, 0.7, 1.3, 1.7])
        >>> plot_traj([0.5, 0.7, 1.3, 1.7], np.array([1,2,3,4]), title='Traj', xlabel='x', ylabel='y',color='r')

    """
    plt.figure()
    if x is None: x = range(len(y))
    dx = np.linspace(x[0], x[-1], num=len(y)*4, endpoint=True)
    fy = interp1d(x, y, kind='cubic')
    plt.plot(x, y, '.', color=color)
    plt.plot(dx, fy(dx), color=color)
    if title is not None: plt.title(title)
    if xlabel is not None: plt.xlabel(xlabel)
    if ylabel is not None: plt.ylabel(ylabel)
    plt.show()
