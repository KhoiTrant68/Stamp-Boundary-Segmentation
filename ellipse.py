import os
import cv2
import numpy as np


def draw_ellipses_custom(ori_image):
    # Get only red color on image
    image_hsv = cv2.cvtColor(ori_image, cv2.COLOR_BGR2HSV)
    # lower boundary RED color range values; Hue (0 - 10)
    lower1 = np.array([0, 100, 20])
    upper1 = np.array([10, 255, 255])

    # upper boundary RED color range values; Hue (160 - 180)
    lower2 = np.array([160, 100, 20])
    upper2 = np.array([179, 255, 255])

    # Get mask for red color
    lower_mask = cv2.inRange(image_hsv, lower1, upper1)
    upper_mask = cv2.inRange(image_hsv, lower2, upper2)
    full_mask = lower_mask + upper_mask

    # Crop red color image
    only_red_image = ori_image.copy()
    only_red_image = cv2.bitwise_and(only_red_image, only_red_image, mask=full_mask)

    # Convert the image to grayscale
    gray = cv2.cvtColor(only_red_image, cv2.COLOR_BGR2GRAY)

    # Apply GaussianBlur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Use Canny edge detection
    edges = cv2.Canny(blurred, 100, 200)

    # Find contours in the edge-detected image
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Fit ellipses to contours and draw them on the original image
    max_ellipse = None
    max_area_ellipse = 0

    for contour in contours:
        if len(contour) >= 5:
            ellipse = cv2.fitEllipse(contour)
            (_, _), (MA, ma), _ = ellipse
            area = np.pi / 4 * MA * ma

            if area > max_area_ellipse:
                max_area_ellipse = area
                max_ellipse = ellipse
    result = max_ellipse

    return result
