import cv2 as cv
import numpy as np
img=cv.imread("img.jpg")  
cv.imshow("a",img)

print(img)
m = img.astype(np.float32)
grm=(m[:, :, 0] + m[:, :, 1] + m[:, :, 2]) / 3  #using formula
grm = grm.astype(np.uint8)
cv.imshow("g",grm)
cv.imwrite('result_image.jpg',grm)
k = cv.waitKey(0)