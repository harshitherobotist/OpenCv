# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 11:08:51 2019

@author: Harshit
"""

import numpy as np
import cv2

img = cv2.imread('ironman.jpg', cv2.IMREAD_COLOR)

img[55,55] = [255,255,255]
px = img[55,55]
print(px)
roi = img[100:150, 100:150] = [255,255,255]
face = img[10:100, 50:140]
img[0:90, 0:90] = face
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows