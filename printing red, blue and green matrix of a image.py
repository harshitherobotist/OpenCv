import numpy as np
import cv2 as cv
image1 = cv.imread('Test Image 2.png')
BlueMatrixOnly = image1[: ,: ,0]
GreenMatrixOnly = image1[: ,: ,1]
RedMatrixOnly = image1[: ,: ,2]

print("BlueMatrix = \n",BlueMatrixOnly)
print("GreenMatrix = \n",GreenMatrixOnly)
print("RedMatrix = \n",RedMatrixOnly)

splitImage = cv.split(image1)
# print(splitImage)
cv.namedWindow('Test Image',cv.WINDOW_KEEPRATIO)
cv.imshow('Test Image',image1)
