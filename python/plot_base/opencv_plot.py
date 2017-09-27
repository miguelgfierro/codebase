import cv2
import matplotlib.pyplot as plt


def plot_image(img, title='image'):
    """Plot an image.
    Parameters:
        img (numpy array): An image.
        title (str): Title of the image.
    Examples:
        >>> img = cv2.imread('../../share/Lenna.png')
        >>> import numpy as np
        >>> print(np.array(img.shape, dtype='int'))
        [512 512   3]
        >>> plot_image(img)

    """
    cv2.imshow(title,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def plot_image_matplotlib(img, figsize=(4,4)):
    """Plot an opencv image using matplotlib.
    Parameters:
        img (numpy array): An image.
        title (str): Title of the image.
    Examples:
        >>> img = cv2.imread('../../share/Lenna.png')
        >>> plot_image_matplotlib(img)

    """
    shape_len = len(img.shape)
    if shape_len == 3:#color image
        image = img.copy()
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        cmap = None
    elif shape_len == 2: #gray image
        image = img
        cmap = 'gray'
    else:
        raise Exception("Wrong image")
    plt.figure(figsize = figsize)
    plt.imshow(image, cmap=cmap)
    plt.axis('off')
    plt.show()
