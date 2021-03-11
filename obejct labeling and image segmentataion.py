'''Program for background subtraction(use still background) '''
import numpy as np
import cv2 as cv

#read background and image
imageBackground = cv.imread('white background.png')
image = cv.imread('white foreground.png')

#convert background and image to gray scale
imageBackgroundGray = cv.cvtColor(imageBackground,cv.COLOR_BGR2GRAY)
imageGray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)

'''Take difference of background and image and take absolute value
of the difference'''
Difference = np.absolute(imageBackgroundGray - imageGray)

#Convert difference datatype to int 16 to remove noise
Difference = np.int16(Difference)

#Convert int16 to uint8 as all images are in uint8
Difference[Difference<0] = 0
Difference[Difference>255] = 255
Difference = np.uint8(Difference)

cv.namedWindow('subtracted image',cv.WINDOW_FREERATIO)
cv.imshow('subtracted image', Difference)

#Threholding grayscale image to get black and white background
Difference[Difference<29] = 0 #Choose threshold value according to the image
Difference[Difference>=29] = 255
Difference = np.uint8(Difference)
BlackNwhite = Difference
#object labeling using predefined function
labels , labelMatrix = cv.connectedComponents(BlackNwhite,8)#second argument is 4 way or 8 way labelling
print("labels = ",labels)
print("label Matrix = ",labelMatrix)
print("No of Objects in Image = ",labels-1)# as background is also object

for i in range(1,labels+1):
    objecti = labelMatrix == i
    objecti = np.uint8(objecti)
    objecti[objecti >0]= 255

#print('Difference',Difference)
#print('image',image)

cv.namedWindow('Black and White',cv.WINDOW_FREERATIO)
cv.imshow('Black and White',BlackNwhite)

cv.namedWindow('background',cv.WINDOW_FREERATIO)
cv.imshow('background', imageBackground)

cv.namedWindow('image',cv.WINDOW_FREERATIO)
cv.imshow('image',image)


