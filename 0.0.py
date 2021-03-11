import numpy as np
import cv2
version = cv2.__version__  #for showing version of any library double underscores used
print(version)

image1 = cv2.imread("puppy.jpg")
'''reading the image data and storing it in image1
                                     variable.The image to be stored in same folder as
                                     the python program is saved or we have to specify
                                     image directory'''
cv2.imshow('puppy',image1)  #showing image1 variable in window named puppy
print(image1.dtype) #data type of image 1 data
print(image1.ndim)  #dimension of image 1 data
print(image1.size)  # width*height*dimension = size, can be wrong in processed image
print(dtype(image1)) #type of image matrix e.g. np array ar np matrix
print(image1.shape) #tuple of 3 values (no of rows,no of coulmns, dimension)
cv2.waitKey(5000)
cv2.destroyWindow(image1)
print(image1)
