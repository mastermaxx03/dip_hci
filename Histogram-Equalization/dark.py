import cv2
import numpy as np

# Load the color image
image = cv2.imread('Histogram-Equalization/image.jpg')

# Split the image into its three channels: B, G, and R
b, g, r = cv2.split(image)

# Apply histogram equalization to each channel
b_equalized = cv2.equalizeHist(b)
g_equalized = cv2.equalizeHist(g)
r_equalized = cv2.equalizeHist(r)

# Merge the equalized channels back together
equalized_image = cv2.merge((b_equalized, g_equalized, r_equalized))

# Scale down the pixel values to make the image darker
darkened_image = cv2.convertScaleAbs(equalized_image, alpha=0.5, beta=0)  # Adjust alpha to control darkness

# Display the original and darkened images
cv2.imshow('Original Image', image)
cv2.imshow('Equalized Image', equalized_image)
cv2.imshow('Darkened Image', darkened_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the darkened image
cv2.imwrite('Histogram-Equalization/darkened_image.jpg', darkened_image)
