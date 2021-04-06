# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 21:48:34 2019

@author: Harshit
"""

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()
    
    laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    soblex = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize = 5)
    sobley = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize = 5)
    
    edges = cv2.Canny(frame, 200, 200)
    
    
    cv2.imshow('original', frame)
    cv2.imshow('laplacian', laplacian)
    cv2.imshow('soblex', soblex)
    cv2.imshow('sobley', sobley)
    cv2.imshow('edges', edges)
    
    
    k=cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
cap.release()