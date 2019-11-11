import numpy as np
import cv2
import matplotlib.pyplot as plt

imagefile = 'data/lena.jpg'
img2 = 'data/banana.jpg'
src = cv2.imread(imagefile)
src2 = cv2.imread(img2)

rows, cols, channels = src.shape

view = cv2.add(src,src2)

#M1 = cv2.getRotationMatrix2D((rows /2 ,cols / 2),45,0.5)


cv2.imshow('view',view)

cv2.waitKey()
cv2.destroyAllWindows()