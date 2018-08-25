import cv2
import numpy as np


def apply_mask_to_image(img, mask):
    """Apply a binary mask to an image
    Args:
        img (np.array): An image.
        mask (np.array): Binary image.
    Returns:
        img_result (np.array): A masked image.
    Examples:
        >>> from codebase.python.plot_base.opencv_plot import plot_image_matplotlib as pp
        >>> img = cv2.imread('../../share/Lenna.png')
        >>> mask = cv2.imread('../../share/Lenna_mask.png', 0)
        >>> masked = apply_mask_to_image(img, mask)
        >>> pp(masked)
    """
    return cv2.bitwise_and(img, img, mask=mask)


def bounding_box(mask, max_contours=10):
    """Get the external bounding box of a mask.
    Args:
        mask (np.array): Binary image.
        max_contours (int): Maximum number of contours to consider
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


def grabcut_rect(img, rect, iterations=3):
    """Grabcut segmentation using a rectangle as initial region of
    confidence.
    Args:
        img (np.array): An image.
        rect (tuple): A tuple of integers defining x, y, width and height.
        iterations (int): Iterations.
    Returns:
        img_result (np.array): A segmented image.
        mask (np.array): Binary image.
    Examples:
        >>> from codebase.python.plot_base.opencv_plot import plot_image_matplotlib as pp
        >>> img = cv2.imread('../../share/Lenna.png')
        >>> rect = (60, 32, 380, 480)
        >>> img_result, mask = grabcut_rect(img, rect, iterations=1)
        >>> pp(img_result)

    """
    img_result, mask = _grabcut(img, rect=rect, iterations=iterations)
    return img_result, mask


def grabcut_mask(img, mask, iterations=3):
    """Grabcut segmentation using a mask as initial region of
    confidence.
    Args:
        img (np.array): An image.
        mask (np.array): Binary image.
        iterations (int): Iterations.
    Returns:
        img_result (np.array): A segmented image.
        mask (np.array): Binary image.
    Examples:
        >>> from codebase.python.plot_base.opencv_plot import plot_image_matplotlib as pp
        >>> img = cv2.imread('../../share/Lenna.png')
        >>> mask = cv2.imread('../../share/Lenna_mask.png', 0)
        >>> img_result, mask = grabcut_mask(img, mask, iterations=1)
        >>> pp(img_result)

    """
    img_result, mask = _grabcut(img, mask=mask, iterations=iterations)
    return img_result, mask


def _grabcut(img, mask=None, rect=None, iterations=3):
    bgd_model = np.zeros((1, 65), np.float64)
    fgd_model = np.zeros((1, 65), np.float64)
    if mask is not None and rect is None:
        method = cv2.GC_INIT_WITH_MASK
        mask[mask == 255] = cv2.GC_FGD
    elif rect is not None and mask is None:
        method = cv2.GC_INIT_WITH_RECT
    else:
        raise ValueError("Error with the inputs mask or rect")
    mask, _, _ = cv2.grabCut(img, mask, rect, bgd_model, fgd_model, iterations, method)
    mask = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
    img_result = img * mask[:, :, np.newaxis]
    return img_result, mask


