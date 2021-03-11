import numpy as np
import cv2 as cv

VisionSource = cv.VideoCapture(0)

if VisionSource.isOpened():
    boolReturn,frame = VisionSource.read()
    while(boolReturn):
        boolReturn,frame = VisionSource.read()
        cv.imshow('Live Feed',frame)
        
        blueMatrix = frame[:,:,0]
        greenMatrix = frame[:,:,1]
        redMatrix = frame[:,:,2]
        
        blueImage = blueMatrix-greenMatrix-redMatrix
        greenImage = greenMatrix-blueMatrix-redMatrix
        redImage = redMatrix-blueMatrix-greenMatrix

        blueImage[blueImage<0] = 0
        blueImage[blueImage>255] = 255
        greenImage[greenImage<0] = 0
        greenImage[greenImage>255] = 255
        redImage[redImage<0] = 0
        redImage[redImage>255] = 255

        redImage = np.uint8(redImage)
        blueImage = np.uint8(blueImage)
        greenImage = np.uint8(greenImage)
        
        cv.imshow('Live Red',redImage)
        cv.imshow('Live green',greenImage)
        cv.imshow('Live blue',blueImage)
        
        Key = cv.waitKey(5)
        if(Key==27):
            cv.destroyAllWindows()
            break
else:
    exit()
