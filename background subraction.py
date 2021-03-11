'''Program for background subtraction(use still background) '''
import numpy as np
import cv2 as cv

#read background and image
imageBackground = cv.imread('Background black.png')
image = cv.imread('Test Image 1.png')

#convert background and image to gray scale
imageBackgroundGray = cv.cvtColor(imageBackground,cv.COLOR_BGR2GRAY)
imageGray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)

'''Take difference of background and image and take absolute value
of the difference'''
Difference = np.absolute(imageBackgroundGray - imageGray)

#Convert difference datatype to int 16 to remove noise
Difference = np.int16(Difference)

#Convert int16 to uint8 as all images are in uint8
Difference[Difference<0] = 0
Difference[Difference>255] = 255
Difference = np.uint8(Difference)

print('Difference',Difference)
#print('image',image)

cv.namedWindow('background',cv.WINDOW_FREERATIO)
cv.imshow('background', imageBackground)

cv.namedWindow('image',cv.WINDOW_FREERATIO)
cv.imshow('image',image)

cv.namedWindow('subtracted image',cv.WINDOW_FREERATIO)
cv.imshow('subtracted image', Difference)
