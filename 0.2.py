import numpy as np
import cv2 as cv

Feed = cv.VideoCapture(0)
FeedCheck = Feed.isOpened()
if(FeedCheck):
    Check,frame = Feed.read()
    while(Check):
        Check,frame = Feed.read()
        cv.imshow('Video Capture',frame)
        key = cv.waitKey(1)
        if( key == 67 or key == 99):
            imageName = input('Enter the Image Name with file extension!! :  ')
            cv.imwrite(imageName,frame)
            print('The Image is saved in working directory')
            break
        
    cv.destroyWindow('Video Capture')
else:
    exit()
