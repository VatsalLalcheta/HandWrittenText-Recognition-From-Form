#to make thick

import numpy as np
import cv2

# read
img = cv2.imread('1new.png', cv2.IMREAD_GRAYSCALE)

# increase contrast
pxmin = np.min(img)
pxmax = np.max(img)
imgContrast = (img - pxmin) / (pxmax - pxmin) * 255

# increase line width
kernel = np.ones((3, 3), np.uint8)
imgMorph = cv2.erode(imgContrast, kernel, iterations = 5)

# write
cv2.imwrite('mid0.png', imgMorph)

##############################################################################

#for split
new_a = []
tracker = 0
while(1):
#	img = imgMorph # Read in the image and convert to grayscale
	
	#print(img.shape)
	#print(gray.shape)
	img = cv2.imread('mid'+str(tracker)+'.png') # Read in the image and convert to grayscale
	tracker += 1

	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	gray = 255*(gray < 128).astype(np.uint8) # To invert the text to white


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
#	print(type(a))
	p = img[:, :j+1]
	q = img[:, j+1:]
	new_a.append(p)
	
	if(q.all()!=None):
		try:
			
			cv2.imwrite('znew2.png', q)
		except:
			print(tracker)
			break
	cv2.imwrite('mid'+str(tracker)+'.png',q)	
	#	print(np.shape(gray))
#	cv2.imwrite('znew1.png', p)

#	cv2.imwrite('znew2.png', q)

#cv2.imshow("Cropped", new_a[1]) # Show it
#cv2.waitKey(0)

	
###############################################################################

for i in range(len(new_a)):
	try:
		img = new_a[i] # Read in the image and convert to grayscale
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		gray = 255*(gray < 128).astype(np.uint8) # To invert the text to white
		coords = cv2.findNonZero(gray) # Find all non-zero points (text)


		x, y, w, h = cv2.boundingRect(coords) # Find minimum spanning bounding box
		rect = img[y:y+h, x:x+w] # Crop the image - note we do this on the original image
		#cv2.imshow("Cropped", rect) # Show it
		#cv2.waitKey(0)
		cv2.destroyAllWindows()
		cv2.imwrite("new"+str(i)+".png", rect) # Save the image
	except:
		break
