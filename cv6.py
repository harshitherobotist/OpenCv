# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 11:00:11 2019

@author: Harshit
"""

import numpy as np
import cv2

img =cv2.imread('ironman.jpg', cv2.IMREAD_COLOR)
cv2.line(img, (0,0), (115,115), (255,255,255), 5)


cv2.rectangle(img, (50,50) , (200,250), (0,255,0), 5)
cv2.circle(img, (150,150), 55,(0,0,255), 4 )

pts = np.array([[0,0],[20,30],[50,70],[50,20]], np.int32) 

cv2.polylines(img, [pts], True, (0,255,255), 3 )

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'hello world', (0,200), font, 1, (255,255,0), 2, cv2.LINE_AA)

cv2.imshow('image' ,img)

cv2.waitKey(0)
cv2.destroyAllWindows()