import cv2


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
