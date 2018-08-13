import cv2


def apply_mask_to_image(img, mask):
    """Apply a binary mask to an image"""
    return cv2.bitwise_and(img, img, mask=mask)
