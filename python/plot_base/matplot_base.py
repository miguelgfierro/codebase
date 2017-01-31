import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def plot_image(img):
    """Plot an image
    Parameters:
        img (numpy array): An image.
    Examples:
        >>> img = mpimg.imread('../../share/Lenna.png')
        >>> plot_image(img)

    """
    plt.imshow(img)
    plt.show()
