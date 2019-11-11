import numpy as np
import cv2
import matplotlib.pyplot as plt

imagefile = 'data/lena.jpg'
src = cv2.imread(imagefile, cv2.IMREAD_GRAYSCALE)
shape = src.shape[0] , src.shape[1] ,3
dst = np.zeros(shape,dtype = np.uint8)

dst[:,:,0] = src

dst[100:400 , 200:300] = [255,255,255]

cv2.imshow('img',src)
cv2.imshow('dst',dst)


cv2.waitKey()
cv2.destroyAllWindows()
