import cv2
import numpy as np
from matplotlib import pyplot as plt

def get_pixel(img, center, x, y):
    """
    Gets the pixel value at the specified coordinates, handling boundary conditions.

    Args:
        img: The input image.
        center: The value of the center pixel.
        x: The x-coordinate of the pixel.
        y: The y-coordinate of the pixel.

    Returns:
        1 if the pixel value is greater than or equal to the center pixel value, 0 otherwise.
    """
    try:
        # Check if the pixel is within the image boundaries
        if 0 <= x < img.shape[0] and 0 <= y < img.shape[1]:
            if img[x][y] >= center:
                return 1
        return 0
    except:
        # Handle boundary conditions by returning 0
        return 0

def lbp_calculated_pixel(img, x, y):
    """
    Calculates the LBP value for the pixel at the specified coordinates.

    Args:
        img: The input image.
        x: The x-coordinate of the pixel.
        y: The y-coordinate of the pixel.

    Returns:
        The LBP value for the pixel.
    """
    center = img[x][y]

    # Handle the case when the center pixel value is 0
    if center == 0:
        return 0

    val_ar = []

    # Calculate the LBP value based on the neighborhood pixels
    val_ar.append(get_pixel(img, center, x - 1, y - 1))
    val_ar.append(get_pixel(img, center, x - 1, y))
    val_ar.append(get_pixel(img, center, x - 1, y + 1))
    val_ar.append(get_pixel(img, center, x, y + 1))
    val_ar.append(get_pixel(img, center, x + 1, y + 1))
    val_ar.append(get_pixel(img, center, x + 1, y))
    val_ar.append(get_pixel(img, center, x + 1, y - 1))
    val_ar.append(get_pixel(img, center, x, y - 1))

    # Convert the binary values to decimal
    power_val = [1, 2, 4, 8, 16, 32, 64, 128]
    val = 0
    for i in range(len(val_ar)):
        val += val_ar[i] * power_val[i]

    return val

# Provide the correct path to the image file
path = '/Users/animesh/dip_hci/LocalBinaryPattern/Batman.jpg'
img_bgr = cv2.imread(path, 1)

# Handle the case when the image cannot be loaded
if img_bgr is None:
    print("Error: Could not load image.")
    exit()

height, width, _ = img_bgr.shape

img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
img_lbp = np.zeros((height, width), np.uint8)

for i in range(0, height):
    for j in range(0, width):
        img_lbp[i, j] = lbp_calculated_pixel(img_gray, i, j)

plt.imshow(img_bgr)
plt.show()

plt.imshow(img_lbp, cmap="gray")
plt.show()

# Save the LBP image in the same directory as the script
cv2.imwrite("LocalBinaryPattern/Batman_lbp.jpg", img_lbp)

print("LBP Program is finished")