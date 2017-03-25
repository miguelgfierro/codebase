import cv2


def normalize_image(img, min_val=0, max_val=1):
    """Normalize image between `min_val` and `max_val`.
    Parameters:
        img (numpy array): An image.
        min_val (int or float): Minimum value.
        max_val (int or float): Maximum value.
    Returns:
        img_new (numpy array): A normalized image.
    Examples:
        >>> img = cv2.imread('../../share/Lenna.png')
        >>> max(img.flatten())
        255
        >>> img_norm = normalize_image(img)
        >>> max(img_norm.flatten())
        1
        >>> min(img_norm.flatten())
        0

    """
    img_new = cv2.normalize(img, None, alpha=min_val, beta=max_val, norm_type=cv2.NORM_MINMAX)
    return img_new


def resize_image(img, new_width, new_height):
    """Resize image to a `new_width` and `new_height`.
    Parameters:
        img (numpy array): An image.
        new_width (int): New width.
        new_height (int): New height.
    Returns:
        img_new (numpy array): A resized image.
    Examples:
        >>> img = cv2.imread('../../share/Lenna.png')
        >>> height, width, channels = img.shape
        >>> img_resized = resize_image(img, width/2, height/2)
        >>> img_resized.shape
        (256L, 256L, 3L)

    """
    img_new = cv2.resize(img, (new_width, new_height))
    return img_new


def equalize_image(img):
    """Equalize the image histogram.
    Parameters:
        img (numpy array): An image.
    Returns:
        img_new (numpy array): A equalized image.
    Examples:
        >>> img = cv2.imread('../../share/Lenna.png')
        >>> img_eq = equalize_image(img)

    """
    return cv2.equalizeHist(img)


def crop_image(img, box):
    """Crop a rectangular region from an image.
    Parameters:
        img (numpy array): An image.
        box (tuple): Left, upper, right, and lower pixel coordinate. The origin of coordinates is
                    the upper left square.
    Returns:
        img_new (numpy array): A cropped image.
    Examples:
        >>> img = cv2.imread('../../share/Lenna.png')
        >>> box = (0, 100, 250, 400)
        >>> img_crop = crop_image(img, box)
        >>> img_crop.shape
        (300L, 250L, 3L)

    """
    return img[box[1]:box[3], box[0]:box[2]]
