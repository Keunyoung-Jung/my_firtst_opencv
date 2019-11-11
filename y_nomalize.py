import numpy as np
import cv2
import matplotlib.pyplot as plt

imagefile = 'data/lena.jpg'
src = cv2.imread(imagefile , cv2.IMREAD_GRAYSCALE)

minVal, maxVal , minLoc , maxLoc = cv2.minMaxLoc(src)

dst = cv2.normalize(src,None, 100,200,cv2.NORM_MINMAX)
minVal, maxVal , minLoc , maxLoc = cv2.minMaxLoc(dst)

print(minVal, maxVal , minLoc , maxLoc)

cv2.imshow('img',src)
cv2.imshow('dst',dst)


cv2.waitKey()
cv2.destroyAllWindows()