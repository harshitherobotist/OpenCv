# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 11:42:46 2019

@author: Harshit
"""
import numpy as np
import cv2

img1= cv2.imread('puppy.jpg')
img2 = cv2.imread('ironman.jpg')

rows,cols,channels = img2.shape
roi = img1[0:rows,0:cols]

img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)

##add = img1 +img2
#add = cv2.add(img1,img2)

#weighted = cv2.addWeighted(img1, 0.4, img2, 0.6, 0)

mas_inv = cv2.bitwise_not(mask)
img1_bg = cv2.bitwise_and(roi , roi, mask=ask_inv)

#cv2.imshow('mask ', mask )
cv2.waitKey(0)
cv2.destroyAllWindows()