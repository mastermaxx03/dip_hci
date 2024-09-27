import pywt
import cv2
import matplotlib.pyplot as plt
import os  # Import the os module for file system operations

# Load the image
image_path = 'Joker.jpg'  # Replace with your image file name
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Get the directory of the original image
image_dir = os.path.dirname(image_path)

# Choose a wavelet family (e.g., 'db1', 'haar', 'sym4')
wavelet = 'db1'  # You can experiment with different wavelets

# Perform the DWT
coeffs = pywt.dwt2(image, wavelet)

# Extract the approximation and detail coefficients
cA, (cH, cV, cD) = coeffs

# Display the original image
plt.subplot(2, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')

# Display the approximation coefficients
plt.subplot(2, 2, 2)
plt.imshow(cA, cmap='gray')
plt.title('Approximation Coefficients')

# Display the horizontal detail coefficients
plt.subplot(2, 2, 3)
plt.imshow(cH, cmap='gray')
plt.title('Horizontal Detail Coefficients')

# Display the vertical detail coefficients
plt.subplot(2, 2, 4)
plt.imshow(cV, cmap='gray')
plt.title('Vertical Detail Coefficients')

plt.tight_layout()
plt.show()

# Save the output images in the same folder as the input image
cv2.imwrite(os.path.join(image_dir, 'Joker_cA.jpg'), cA)
cv2.imwrite(os.path.join(image_dir, 'Joker_cH.jpg'), cH)
cv2.imwrite(os.path.join(image_dir, 'Joker_cV.jpg'), cV)
cv2.imwrite(os.path.join(image_dir, 'Joker_cD.jpg'), cD)

print("DWT images saved to the same directory as the original image.")