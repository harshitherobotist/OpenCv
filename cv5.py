import numpy as np
import cv2

img =cv2.imread('ironman.jpg', cv2.IMREAD_COLOR)
cv2.line(img, (0,0), (115,115), (255,255,255), 15)

cv2.rectangle(img, (50,50) , (200,250), (0,255,0), 5)
cv2.imshow('image' ,img)

cv2.waitKey(0)
cv2.destroyAllWindows()