import cv2


def largest_contour(mask):
    """Get the largest contour from a binary image
    
    Args:
        mask (np.array): Binary image.
    
    Returns:
        np.array: Array of points.
    
    Examples:
        >>> mask = cv2.imread('share/Lenna_mask.png', 0)
        >>> cnts = largest_contour(mask)
        >>> len(cnts)
        544
    """
    _, contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    largest_contour = contours[0]
    return largest_contour

