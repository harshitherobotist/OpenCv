import numpy as np
import cv2 as cv

image = cv.imread('Test Image 2.png')

blueMatrixOnly = image[:,:,0]
greenMatrixOnly = image[:,:,1]
redMatrixOnly = image[:,:,2]

blueValue = 0.114*np.float16(blueMatrixOnly)
greenValue = 0.587*np.float16(greenMatrixOnly)
redValue = 0.299*np.float16(redMatrixOnly)

grayImage = blueValue+greenValue+redValue
grayImage = np.round(grayImage, 0)
grayImage = np.uint8(grayImage)
print(grayImage)
#print(image)

cv.namedWindow('colored Image',cv.WINDOW_FREERATIO)
cv.imshow('colored Image',image)

cv.namedWindow('gray Image',cv.WINDOW_FREERATIO)
cv.imshow('gray Image',grayImage)

