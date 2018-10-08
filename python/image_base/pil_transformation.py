from PIL import Image, ImageOps


def normalize_image(img):
    """Normalize image between 0 and 255.
    Args:
        img (PIL image): An image.
    Returns:
        img_new (PIL image): A normalized image.
    Examples:
        >>> img = Image.open('share/Lenna.png')
        >>> vals = img.getextrema() #gets min and max value in the three channels
        >>> vals
        ((54, 255), (3, 248), (8, 225))
        >>> img_norm = normalize_image(img)
        >>> vals = img_norm.getextrema()
        >>> vals
        ((0, 255), (0, 255), (0, 254))

    """
    return ImageOps.autocontrast(img)


def resize_image(img, new_width, new_height):
    """Resize image to a `new_width` and `new_height`.
    Args:
        img (PIL image): An image.
        new_width (int): New width.
        new_height (int): New height.
    Returns:
        img_new (PIL image): A resized image.
    Examples:
        >>> img = Image.open('share/Lenna.png')
        >>> img_resized = resize_image(img, 256, 256)
        >>> img_resized.size
        (256, 256)

    """
    img_new = img.resize((new_width, new_height))
    return img_new


def equalize_image(img):
    """Equalize the image histogram.
    Args:
        img (PIL image): An image.
    Returns:
        img_new (PIL image): A equalized image.
    Examples:
        >>> img = Image.open('share/Lenna.png')
        >>> img_eq = equalize_image(img)

    """
    return ImageOps.equalize(img)


def crop_image(img, box):
    """Crop a rectangular region from an image.
    Args:
        img (PIL image): An image.
        box (tuple): Left, upper, right, and lower pixel coordinate. The origin of coordinates is
                    the upper left square.
    Returns:
        img_new (PIL image): A cropped image.
    Examples:
        >>> img = Image.open('share/Lenna.png')
        >>> box = (0, 100, 250, 400)
        >>> img_crop = crop_image(img, box)
        >>> img_crop.size
        (250, 300)

    """
    return img.crop(box)


def convert_to_grayscale(img):
    """Convert a color image to grayscale.
    Args:
        img (PIL image): An image.
    Returns:
        img_new (PIL image): A grayscale image.
    Examples:
        >>> img = Image.open('share/Lenna.png')
        >>> img.mode
        'RGB'
        >>> img_gray = convert_to_grayscale(img)
        >>> img_gray.mode
        'L'

    """
    return img.convert("L")
