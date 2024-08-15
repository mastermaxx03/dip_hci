import cv2 as cv
import matplotlib.pyplot as plt
#Converting image to grayscale
image = cv.imread('Histogram-Equalization/image.jpg', cv.IMREAD_GRAYSCALE)
equalized_image = cv.equalizeHist(image)
cv.imwrite('Histogram-Equalization/equalized_image.jpg', equalized_image)
fig, axs = plt.subplots(2, 2, figsize=(10, 8))
axs[0, 0].imshow(image, cmap='gray')
axs[0, 0].set_title('Original Image')
axs[0, 0].axis('off')
axs[1, 0].hist(image.ravel(), bins=256, range=[0, 256],cumulative=True)
axs[1, 0].set_title('Histogram of Original Image')
axs[0, 1].imshow(equalized_image, cmap='gray')
axs[0, 1].set_title('Equalized Image')
axs[0, 1].axis('off')
axs[1, 1].hist(equalized_image.ravel(), bins=256, range=[0, 256],cumulative=True)
axs[1, 1].set_title('Histogram of Equalized Image')

plt.show()


