import numpy as np
import cv2
import matplotlib.pyplot as plt

imagefile = 'data/lena.jpg'
src1 = cv2.imread(imagefile , cv2.IMREAD_GRAYSCALE)
src2 = np.zeros_like(src1 , dtype = np.uint8) +255
#rows, cols , channels = src2.shape

dst1 = 255 - src1
dst2 = cv2.subtract(src2,src1)
dst3 = cv2.compare(dst1,dst2,cv2.CMP_NE)
n = cv2.countNonZero(dst3)

print('n = ',n)


cv2.imshow('img',src1)
cv2.imshow('dst1',dst1)
cv2.imshow('dst2',dst2)


cv2.waitKey()
cv2.destroyAllWindows()
