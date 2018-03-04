from skimage import io


def plot_image(img):
    """Plot an image.
    Args:
        img (numpy array): An image.
    Examples:
        >>> img = io.imread('../../share/Lenna.png')
        >>> plot_image(img)

    """
    io.imshow(img)
    io.show()

