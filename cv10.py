# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 14:51:45 2019

@author: Harshit
"""

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()
    hsv = cv2.cvtColor(frame , cv2.COLOR_BGR2HSV)
    
    lower_red = np.array([50, 150, 50])
    upper_red = np.array([200, 250, 150])
    mask = cv2.inRange(hsv,lower_red,upper_red)
    res = cv2.bitwise_and(frame, frame, mask = mask)
    
    kernel = np.ones((15,15), np.float32)/255
    smooth = cv2.filter2D(res , -1, kernel)
    
    blur = cv2.GaussianBlur(res, (15,15), 0)
    
    cv2.imshow('blur', blur)
    cv2.imshow('frame', frame) 
    cv2.imshow('res', res)
    cv2.imshow(' smooth',  smooth)
    
    k=cv2.waitKey(5) & 0xFF
    if k==27:
        break
cv2.destroyAllWindows()
cap.release()
    
    