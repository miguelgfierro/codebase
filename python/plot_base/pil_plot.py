import matplotlib.pyplot as plt
from PIL import Image


def plot_image_matplot(img):
    """Plot an image.
    Args:
        img (PIL image): A PIL image.
    Examples:
        >>> img = Image.open('share/Lenna.png')
        >>> plot_image_matplot(img)
        >>> img_gray = Image.open('share/Lenna_gray.png')
        >>> plot_image_matplot(img_gray)

    """
    cmap = None
    if img.mode == "L":
        cmap = "gray"
    plt.imshow(img, cmap=cmap)
    plt.axis("off")
    plt.show()


def plot_image(img):
    """Plot an image.
    Args:
        img (PIL image): A PIL image.
    Examples:
        >>> img = Image.open('share/Lenna.png')
        >>> plot_image(img)
        >>> img_gray = Image.open('share/Lenna_gray.png')
        >>> plot_image(img_gray)

    """
    img.show()
