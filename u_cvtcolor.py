import numpy as np
import cv2
import matplotlib.pyplot as plt

imagefile = 'data/lena.jpg'
src = cv2.imread(imagefile)

src2 = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
src3 = cv2.cvtColor(src,cv2.COLOR_BGR2YCrCb)
src4 = cv2.cvtColor(src,cv2.COLOR_BGR2HSV)

cv2.imshow('img',src)
cv2.imshow('img2',src2)
cv2.imshow('img3',src3)
cv2.imshow('img4',src4)



cv2.waitKey()
cv2.destroyAllWindows()