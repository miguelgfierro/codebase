import cv2


def plot_image(img, title='image'):
    """Plot an image.
    Parameters:
        img (numpy array): An image.
        title (str): Title of the image.
    Examples:
        >>> img = cv2.imread('../../share/Lenna.png')
        >>> plot_image(img)

    """
    cv2.imshow(title,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
