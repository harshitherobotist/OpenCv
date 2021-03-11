'''Program for color subtraction Red, Green ,Blue
'''
import numpy as np
import cv2 as cv

image1 = cv.imread('Test Image 3.png')

BlueMatrix = image1[:,:,0]
GreenMatrix = image1[:,:,1]
RedMatrix = image1[:,:,2]

print('BlueMatrix\n',BlueMatrix)
print('GreenMatrix\n',GreenMatrix)
print('RedMatrix\n',RedMatrix)

RedOnly = RedMatrix - BlueMatrix - GreenMatrix
BlueOnly = BlueMatrix - RedMatrix - GreenMatrix
GreenOnly = GreenMatrix - RedMatrix - BlueMatrix

RedOnly[RedOnly<0] = 0
GreenOnly[GreenOnly<0] = 0
BlueOnly[BlueOnly<0] = 0

RedOnly[RedOnly>255] = 255
GreenOnly[GreenOnly>255] = 255
BlueOnly[BlueOnly>255] = 255

RedOnly = np.uint8(RedOnly)
BlueOnly = np.uint8(BlueOnly)
GreenOnly = np.uint8(GreenOnly)

cv.namedWindow('test image',cv.WINDOW_FREERATIO)
cv.imshow('test image',image1)

cv.namedWindow('Red Object',cv.WINDOW_FREERATIO)
cv.imshow('Red Object',RedOnly)

cv.namedWindow('Green Object',cv.WINDOW_FREERATIO)
cv.imshow('Green Object',GreenOnly)

cv.namedWindow('Blue Object',cv.WINDOW_FREERATIO)
cv.imshow('Blue Object',BlueOnly)

#cv.namedWindow('red split',cv.WINDOW_FREERATIO)
#cv.imshow('red split',RedMatrix)
