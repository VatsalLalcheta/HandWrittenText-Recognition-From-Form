import cv2
import numpy as np

def crop(filename):
    #Read the image
    img = cv2.imread(filename)
    #Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #Separate the background from the foreground
    bit = cv2.bitwise_not(gray)
    #Apply adaptive mean thresholding
    amtImage = cv2.adaptiveThreshold(bit, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 35, 15)
    #Apply erosion to fill the gaps
    kernel = np.ones((15,15),np.uint8)
    erosion = cv2.erode(amtImage,kernel,iterations = 2)
    #Take the height and width of the image
    (height, width) = img.shape[0:2]
    #Ignore the limits/extremities of the document (sometimes are black, so they distract the algorithm)
    image = erosion[50:height - 50, 50: width - 50]
    (nheight, nwidth) = image.shape[0:2]
    #Create a list to save the indexes of lines containing more than 20% of black.
    index = []
    for x in range (0, nheight):
        line = []

        for y in range(0, nwidth):
            line2 = []
            if (image[x, y] < 150):
                line.append(image[x, y])
        if (len(line) / nwidth > 0.2):  
            index.append(x)
    #Create a list to save the indexes of columns containing more than 15% of black.
    index2 = []
    for a in range(0, nwidth):
        line2 = []
        for b in range(0, nheight):
            if image[b, a] < 150:
                line2.append(image[b, a])
        if (len(line2) / nheight > 0.15):
            index2.append(a)

    #Crop the original image according to the max and min of black lines and columns.
    img = img[min(index):max(index) + min(250, (height - max(index))* 10 // 11) , max(0, min(index2)): max(index2) + min(250, (width - max(index2)) * 10 // 11)]
    #Save the image
    cv2.imwrite('res_' + filename, img)

crop("out6.png")
