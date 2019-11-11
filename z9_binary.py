import numpy as np
import cv2

src = cv2.imread('data/morphology.jpg',cv2.IMREAD_GRAYSCALE)
kernel = cv2.getStructuringElement(shape = cv2.MORPH_RECT,ksize = (3,3))
erode = cv2.erode(src,kernel , iterations = 5)
dilate = cv2.dilate(src,kernel, iterations = 5)
erode2 = cv2.erode(dilate,kernel,iterations = 7)

cv2.imshow('src' , src)
cv2.imshow('erode' , erode)
cv2.imshow('dilate' , dilate)
cv2.imshow('erode2' , erode2)

cv2.waitKey()
cv2.destroyAllWindows()
