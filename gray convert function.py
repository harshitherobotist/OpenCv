import numpy as np
import cv2 as cv

image = cv.imread('Test Image 2.png')

grayImage = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

print(grayImage)

cv.namedWindow('gray image',cv.WINDOW_FREERATIO)
cv.imshow('gray image',grayImage)
