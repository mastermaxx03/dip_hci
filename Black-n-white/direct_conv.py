import cv2
import numpy as np

# Load the color image
image = cv2.imread('Black-n-white/image.jpg')

# Define the threshold for each channel
threshold = 127

# Create a mask where any pixel above the threshold in any channel is set to white
_, b_thresh = cv2.threshold(image[:, :, 0], threshold, 255, cv2.THRESH_BINARY)
_, g_thresh = cv2.threshold(image[:, :, 1], threshold, 255, cv2.THRESH_BINARY)
_, r_thresh = cv2.threshold(image[:, :, 2], threshold, 255, cv2.THRESH_BINARY)

# Combine the thresholds
black_and_white_image = cv2.bitwise_and(b_thresh, g_thresh)
black_and_white_image = cv2.bitwise_and(black_and_white_image, r_thresh)

# Display the original and black and white images
cv2.imshow('Original Image', image)
cv2.imshow('Black and White Image', black_and_white_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the black and white image
cv2.imwrite('Black-n-white/black_and_white_image.jpg', black_and_white_image)
