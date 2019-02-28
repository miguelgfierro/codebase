import cv2
import numpy as np


def resize_image(img, new_width, new_height):
    """Resize image to a `new_width` and `new_height`.
    
    Args:
        img (np.array): An image.
        new_width (int): New width.
        new_height (int): New height.
    
    Returns:
        np.array: A resized image.
    
    Examples:
        >>> img = cv2.imread('share/Lenna.png')
        >>> height, width, channels = img.shape
        >>> img_resized = resize_image(img, width/2, height/2)
        >>> img_resized.shape
        (256, 256, 3)
    """
    img_new = cv2.resize(img, (int(new_width), int(new_height)))
    return img_new


def resize_image_aspect_ratio(img, new_width=None, new_height=None):
    """Resize image, if only one of new_width or new_height is given, the resize is done maintaining the ratio.
    If both parameters are given, the image may be deformed
    
    Args:
        img (np.array): An image.
        new_width (int): New width.
        new_height (int): New height.
    
    Returns:
        np.array: A resized image.
    
    Examples:
        >>> img = cv2.imread('share/Lenna_face.png')
        >>> height, width, channels = img.shape
        >>> img_resized = resize_image_aspect_ratio(img, new_width=300)
        >>> img_resized.shape
        (525, 300, 3)
        >>> img_resized = resize_image_aspect_ratio(img, new_height=150)
        >>> img_resized.shape
        (150, 85, 3)
    """
    height, width = img.shape[:2]
    if new_width is not None and new_height is None:
        r = new_width / width
        new_height = int(height * r)
    elif new_width is None and new_height is not None:
        r = new_height / height
        new_width = int(width * r)
    img_new = cv2.resize(img, (new_width, new_height))
    return img_new


def crop_image(img, box):
    """Crop a rectangular region from an image.
    
    Args:
        img (np.array): An image.
        box (tuple): Left, upper, right, and lower pixel coordinate. The origin of coordinates is
                    the upper left square.
    
    Returns:
        np.array: A cropped image.
    
    Examples:
        >>> img = cv2.imread('share/Lenna.png')
        >>> box = (0, 100, 250, 400)
        >>> img_crop = crop_image(img, box)
        >>> img_crop.shape
        (300, 250, 3)
    """
    return img[box[1] : box[3], box[0] : box[2]]


def equalize_image(img):
    """Equalize the image histogram.
    
    Args:
        img (np.array): An image.
    
    Returns:
        np.array: A equalized image.
    
    Examples:
        >>> img = cv2.imread('share/Lenna_gray.png', 0)
        >>> img_eq = equalize_image(img)
    """
    return cv2.equalizeHist(img)


def normalize_image(img, min_val=0, max_val=1):
    """Normalize image between `min_val` and `max_val`.
    
    Args:
        img (np.array): An image.
        min_val (int or float): Minimum value.
        max_val (int or float): Maximum value.
    
    Returns:
        np.array: A normalized image.
    
    Examples:
        >>> img = cv2.imread('share/Lenna.png')
        >>> max(img.flatten())
        255
        >>> img_norm = normalize_image(img)
        >>> max(img_norm.flatten())
        1
        >>> min(img_norm.flatten())
        0
    """
    img_new = cv2.normalize(
        img, None, alpha=min_val, beta=max_val, norm_type=cv2.NORM_MINMAX
    )
    return img_new


def convert_to_binary(
    img, threshold=127, max_value=255, adaptative=False, return_thresh=False
):
    """Converts an image to black and white.
    It determines the binary threshold automatically from the image using
    Otsu's method.
    
    Args:
        img (np.array): An image.
        threshold (int or float): Threshold.
        max_value (int or float): Max value.
        adaptative (bool): Flag to select whether to use adaptative method or not
        return_thresh (bool): Flag to return Otsu's threshold.
    
    Returns:
        np.array: A black and white image.
        float: Otsu's threshold.
    
    Examples:
        >>> img = cv2.imread('share/Lenna.png')
        >>> img_bw, t = convert_to_binary(img, adaptative=True, return_thresh=True)
        >>> np.min(img_bw), np.max(img_bw)
        (0, 255)
        >>> t
        117.0
        >>> img_bw = convert_to_binary(img, threshold=100, max_value=1)
        >>> np.min(img_bw), np.max(img_bw)
        (0, 1)
    """
    if len(img.shape) != 2:
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        img_gray = img
    if adaptative:
        method = cv2.THRESH_BINARY | cv2.THRESH_OTSU
    else:
        method = cv2.THRESH_BINARY
    thresh, img_new = cv2.threshold(img_gray, threshold, max_value, method)
    if return_thresh:
        return img_new, thresh
    else:
        return img_new


def convert_to_grayscale(img):
    """Convert a color image to grayscale.
    
    Args:
        img (np.array): An image.
    
    Returns:
        np.array: A grayscale image.
    
    Examples:
        >>> img = cv2.imread('share/Lenna.png')
        >>> img.shape
        (512, 512, 3)
        >>> img_gray = convert_to_grayscale(img)
        >>> img_gray.shape
        (512, 512)
    """
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def convert_to_colorspace(img, color_space="hsv"):
    """Convert an opencv image in BGR to another color space.
    More info: https://docs.opencv.org/3.3.1/de/d25/imgproc_color_conversions.html
    HSV range: hue [0,179], saturation [0,255] and value [0,255].
    HLS range: hue [0,179], lightness [0,255] and saturation [0,255].
    YCrCb range: all [0-255].
    Luv ranges: all [0-255].
    Lab ranges: all [0-255].
    XYZ ranges: all [0-255].
    
    Args:
        img (np.array): An image.
        color_space (str): Color space.
    
    Returns:
        np.array: An image in the color space.
    
    Examples:
        >>> img = cv2.imread('share/Lenna.png')
        >>> img_new = convert_to_colorspace(img, 'hsv')
        >>> h, s, v = cv2.split(img_new)
        >>> print(np.max(h), np.max(s), np.max(v))
        179 246 255
        >>> img_new = convert_to_colorspace(img, 'luv')
        >>> l, a, b = cv2.split(img_new)
        >>> print(np.max(l), np.max(a), np.max(b))
        247 181 219
    """
    spaces = {
        "hsv": cv2.COLOR_BGR2HSV,
        "hls": cv2.COLOR_BGR2HLS,
        "ycrcb": cv2.COLOR_BGR2YCrCb,
        "luv": cv2.COLOR_BGR2Luv,
        "lab": cv2.COLOR_BGR2Lab,
        "xyz": cv2.COLOR_BGR2XYZ,
    }
    return cv2.cvtColor(img, spaces[color_space])
