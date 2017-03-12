import cv2


def normalize_image(img, min_val=0, max_val=1):
    """Normalize image between `min_val` and `max_val`.
    Parameters:
        img (numpy array): An image.
        min_val (int or float): Minimum value.
        max_val (int or float): Maximum value.
    Returns:
        img_norm (numpy array): A normalized image.
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
    img_norm = cv2.normalize(img, None, alpha=min_val, beta=max_val, norm_type=cv2.NORM_MINMAX)
    return img_norm

