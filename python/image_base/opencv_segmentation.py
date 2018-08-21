import cv2


def apply_mask_to_image(img, mask):
    """Apply a binary mask to an image
    Args:
        img (np.array): An image.
        mask (np.array): Binary image.
    Returns:
        img_result (np.array): A masked image.
    """
    return cv2.bitwise_and(img, img, mask=mask)


def bounding_box(mask, max_contours=10):
    """Get the external bounding box of a mask.
    Args:
        mask (np.array): Binary image.
        max_contours (int): Maximun number of contours to consider
                            for computing the bounding box.
    Returns:
        rect (tuple): A tuple of integers defining x, y, width and height.
    Examples:
        >>> mask = cv2.imread('../../share/Lenna_mask.png', 0)
        >>> bounding_box(mask)
        (60, 32, 380, 480)
    """
    _, cnts, hierarchy = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x_min, x_max = mask.shape[1], 0
    y_min, y_max = mask.shape[0], 0
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[
        :max_contours]  # get largest contours by area
    for cont in cnts:
        x, y, w, h = cv2.boundingRect(cont)
        if x < x_min:
            x_min = x
        if x + w > x_max:
            x_max = x + w
        if y < y_min:
            y_min = y
        if y + h > y_max:
            y_max = y + h
    return x_min, y_min, x_max-x_min, y_max-y_min
