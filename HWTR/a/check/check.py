#to make thick

import numpy as np
import cv2

# read

img = cv2.imread('abc.png', cv2.IMREAD_GRAYSCALE)
new_img = cv2.threshold(img, 250, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
cv2.imwrite('abc.png', new_img)
img = cv2.imread('abc.png', cv2.IMREAD_GRAYSCALE)

# increase contrast
pxmin = np.min(img)
pxmax = np.max(img)
imgContrast = (img - pxmin) / (pxmax - pxmin) * 255

# increase line width
kernel = np.ones((3, 3), np.uint8)
imgMorph = cv2.erode(imgContrast, kernel, iterations = 5)

# write
cv2.imwrite('abc_check.png', imgMorph)

#new_img = cv2.cvtColor(imgMorph, cv2.COLOR_BGR2GRAY)
