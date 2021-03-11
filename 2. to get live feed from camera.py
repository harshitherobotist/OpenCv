'''
A program to take live feed from vision source
'''
import numpy as np
import cv2 as cv

Feed = cv.VideoCapture(0)
'''capturing the live feed from camera and zero for
                            web cam ( we give cmera number in argument)'''
Check = Feed.isOpened()
''' To check presence of Video Feed or not
                          returns true or false'''

if(Check):
    boolReturn,frame = Feed.read()
    while(boolReturn):
        boolReturn,frame = Feed.read()
        cv.imshow('Video Feed',frame)
        key = cv.waitKey(1)
        if(key == 27):
            break
    cv.destroyWindow('Video Feed')
else:
    exit()
        
