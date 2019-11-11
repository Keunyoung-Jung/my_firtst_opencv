import numpy as np
import cv2

src = cv2.imread('data/lena.jpg',cv2.IMREAD_GRAYSCALE)

kx , ky = cv2.getDerivKernels(1,0,ksize = 3)
sobelx = ky.dot(kx.T)

print('kx = ',kx)
print('ky = ',ky)
print('sobelx = ',sobelx)

gx = cv2.filter2D(src,cv2.CV_32F,sobelx)

kx, ky = cv2.getDerivKernels(0, 1, ksize=3)
sobelY = ky.dot(kx.T)  #실제로 
print('kx=', kx)
print('ky=', ky)
print('sobelY=', sobelY)
gy = cv2.filter2D(src, cv2.CV_32F, sobelY)
##gy = cv2.sepFilter2D(src, cv2.CV_32F, kx, ky)

#3
mag   = cv2.magnitude(gx, gy)
ret, edge = cv2.threshold(mag, 100, 255, cv2.THRESH_BINARY)

cv2.imshow('edge',  edge)
cv2.waitKey()    
cv2.destroyAllWindows()
