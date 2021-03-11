import numpy as np
import cv2 as cv

columns = int(input('Enter The Width of Color Window: '))
rows = int(input('Enter The Height of Color Window: '))
redValue = int(input('Enter The Brightness value of Red: '))
blueValue = int(input('Enter The Brightness value of Blue: '))
greenValue = int(input('Enter The Brightness value of Green: '))

redColorMatrix = np.ones([rows, columns])*redValue
blueColorMatrix = np.ones([rows, columns])*blueValue
greenColorMatrix = np.ones([rows, columns])*greenValue

redColorMatrix = np.uint8(redColorMatrix)
blueColorMatrix = np.uint8(blueColorMatrix)
greenColorMatrix = np.uint8(greenColorMatrix)

colorValue = cv.merge([blueColorMatrix,greenColorMatrix,redColorMatrix])

cv.imshow('Color',colorValue)


