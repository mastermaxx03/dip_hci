import cv2
import numpy as np

# Read the image
img = cv2.imread('Histogram-Equalization/image.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply histogram equalization
equ = cv2.equalizeHist(gray)

# Convert the image back to BGR
equ_bgr = cv2.cvtColor(equ, cv2.COLOR_GRAY2BGR)

# Display the original and equalized images
cv2.imshow('Original Image', img)
cv2.imshow('Equalized Image', equ_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()