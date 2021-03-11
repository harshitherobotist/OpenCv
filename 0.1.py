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
print(dtype(Check))

