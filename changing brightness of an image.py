import numpy as np
import cv2 as cv

image1 = cv.imread('rat.jpg')
brightness = int(input('Enter Brightness Value : \n'))
darkness = int(input('Enter Contrast Value : \n'))
#print(image1)

shape = image1.shape
#print('shape=',shape)


ad = np.ones(shape) + brightness
sub = np.ones(shape) - darkness

brightImage = image1 + ad

brightImage[brightImage>255]=255
brightImage[brightImage<0]=0
brightImage = np.uint8(brightImage)

#darkImage = np.int16(image1) + np.int16(sub)
darkImage = (image1) + (sub)

print(darkImage.dtype)
darkImage[darkImage>255]=255
darkImage[darkImage<0]=0
darkImage = np.uint8(darkImage)
cv.imwrite('C:/Users/Harshit/Desktop/image1.2.png',darkImage)

cv.namedWindow('image',cv.WINDOW_KEEPRATIO)
cv.imshow('image',image1)

cv.namedWindow('Bright image',cv.WINDOW_KEEPRATIO)
cv.imshow('Bright image',brightImage)

cv.namedWindow('Dark image',cv.WINDOW_KEEPRATIO)
cv.imshow('Dark image',darkImage)
