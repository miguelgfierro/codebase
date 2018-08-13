import cv2
import numpy as np
import matplotlib.pyplot as plt
import warnings


def plot_image(img, title='image'):
    """Plot an image.
    Args:
        img (np.array): An image.
        title (str): Title of the image.
    Examples:
        >>> img = cv2.imread('../../share/Lenna.png')
        >>> import numpy as np
        >>> print(np.array(img.shape, dtype='int'))
        [512 512   3]
        >>> plot_image(img)

    """
    cv2.imshow(title, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def plot_image_matplotlib(img, figsize=None, title=None):
    """Plot an opencv image using matplotlib.
    Args:
        img (np.array): An image.
        figsize (tuple): Size of the figure in inches (w,h).
        title (str): Title of the image.
    Examples:
        >>> img = cv2.imread('../../share/Lenna.png')
        >>> plot_image_matplotlib(img)

    """
    shape_len = len(img.shape)
    if shape_len == 3:  # color image
        image = img.copy()
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        cmap = None
    elif shape_len == 2:  # gray image
        image = img
        cmap = 'gray'
    else:
        raise Exception("Wrong image")
    plt.figure(figsize=figsize)
    if title is not None:
        plt.title(title)
    plt.imshow(image, cmap=cmap)
    plt.axis('off')
    plt.show()


def draw_rectangle(img, rect, color=(0, 0, 255), thickness=2):
    """Draw a rectangle on an image.
    Args:
        img (np.array): An image.
        rect (tuple): A tuple of integers defining x, y, width and height.
        color (tuple): BGR color values.
        thickness (int): Thickness of the rectangle border
    Returns:
        img_result (np.array): An image with a rectangle
    Examples:
        >>> img = cv2.imread('../../share/Lenna.png')
        >>> img_box = draw_rectangle(img, (40, 20, 400, 491))
        >>> plot_image_matplotlib(img_box)

    """
    x, y, w, h = _ensure_rec_inside_image(img, rect)
    img_result = np.copy(img)
    cv2.rectangle(img_result, (x, y), (x+w, y+h), color, thickness)
    return img_result


def _ensure_rec_inside_image(img, rect):
    y_max, x_max = img.shape[0] - 1, img.shape[1] - 1
    x, y, w, h = rect
    if x > x_max or y > y_max:
        raise ValueError("Rectangle outside the image")
    if x + w > x_max:
        warnings.warn("Rectangle width {} too large".format(w))
        w = x_max - x
    if y + h > y_max:
        warnings.warn("Rectangle height {} too large".format(h))
        h = y_max - y
    return x, y, w, h
