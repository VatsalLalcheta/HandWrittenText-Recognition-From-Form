#for split

import numpy as np
import cv2

img = cv2.imread('abc_check.png') # Read in the image and convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = 255*(gray < 128).astype(np.uint8) # To invert the text to white

print(img.shape)
print(gray.shape)


a = 0
b = 0
count = 0
flag = True
for j in range(len(gray[0])):
	a = 0
	for i in range(len(gray)):
		a += gray[i][j]
	if(a==0 and b!=0 and count > 100):
		break
	if(a==0 and b!=0):
		count += 1
	elif(a!=0):
		b = 1

p = img[:, :j+1]
q = img[:, j+1:]

cv2.imwrite('znew1.png', p)
print(p,q)
if(q.all()!=None):
	cv2.imwrite('znew2.png', q)
