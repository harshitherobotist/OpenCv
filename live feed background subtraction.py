import numpy as np
import cv2 as cv

Feed = cv.VideoCapture(0)
Check = Feed.isOpened()

if(Check):
    boolReturn,frame = Feed.read()
    while(boolReturn):
        boolReturn,frame = Feed.read()
        Background = frame
        
        cv.imshow('Video Feed',frame)
        key = cv.waitKey(1)
        if(key == 27):
            break
    cv.destroyWindow('Video Feed')
else:
    exit()
