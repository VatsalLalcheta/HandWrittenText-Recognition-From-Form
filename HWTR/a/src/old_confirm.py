from seco_old_conf import *

#to make thick

import numpy as np
import cv2

def RowOCR(img_addr):									#img_addr = "../advvs/svvs.png"
	img = cv2.imread(img_addr, cv2.IMREAD_GRAYSCALE)
	new_img = cv2.threshold(img, 250, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
	cv2.imwrite('../check/mid0.png', new_img)
	'''

	# read
	img = cv2.imread('../check/github.png', cv2.IMREAD_GRAYSCALE)

	# increase contrast
	pxmin = np.min(img)
	pxmax = np.max(img)
	imgContrast = (img - pxmin) / (pxmax - pxmin) * 255

	# increase line width
	kernel = np.ones((3, 3), np.uint8)
	imgMorph = cv2.erode(imgContrast, kernel, iterations = 5)

	# write
	cv2.imwrite('../check/mid0.png', imgMorph)
	#img = cv2.imread('../check/mid0.png', cv2.IMREAD_GRAYSCALE)
	#new_img = cv2.threshold(img, 250, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
	#cv2.imwrite('../check/mid0.png', new_img)
	'''
	##############################################################################

	#for split
	new_a = []
	tracker = 0
	while(1):
		img = cv2.imread('../check/mid'+str(tracker)+'.png') # Read in the image and convert to grayscale
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
		p = img[:, :j+1]
		q = img[:, j+1:]
		new_a.append(p)
		
		if(q.all()!=None):
			try:
				
				cv2.imwrite('../check/znew2.png', q)
			except:
				print(tracker)
				break
		cv2.imwrite('../check/mid'+str(tracker)+'.png',q)	
		
	###############################################################################
	template = {"name" : [], "contact" : [], "Email" : [], "Date" : [], "Rating" : []}
	ans_str = ""
	dict_key = ["name", "contact", "Email", "Date", "Rating"]
	xyz = []
	for i in range(len(new_a)):											# send csv index from prev file

		try:
			img = new_a[i] # Read in the image and convert to grayscale
			gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
			gray = 255*(gray < 128).astype(np.uint8) # To invert the text to white
			coords = cv2.findNonZero(gray) # Find all non-zero points (text)


			x, y, w, h = cv2.boundingRect(coords) # Find minimum spanning bounding box
			rect = img[y:y+h, x:x+w] # Crop the image - note we do this on the original image
			cv2.destroyAllWindows()

			cv2.imwrite("../check/new"+str(i)+".png", rect) # Save the image
			new_a[i] = rect
		except:
			pass
	newnewa = main(new_a)
	print(newnewa)	
#	return(newnewa)

RowOCR("../check/abc2.png")
