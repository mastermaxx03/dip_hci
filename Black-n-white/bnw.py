import cv2

# Load the color image
image = cv2.imread('Black-n-White/image.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply a binary threshold to get a black and white image
# Here, 127 is the threshold value, and 255 is the max value.
# You can adjust the threshold value to get different results.
_, black_and_white_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

# Display the original and black and white images
cv2.imshow('Original Image', image)
cv2.imshow('Black and White Image', black_and_white_image)
cv2.imwrite('Black-n-white/bnw.jpg',black_and_white_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the black and white image
cv2.imwrite('black_and_white_image.jpg', black_and_white_image)
