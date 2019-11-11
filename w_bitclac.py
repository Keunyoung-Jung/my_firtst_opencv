import numpy as np
import cv2
import matplotlib.pyplot as plt

imagefile = 'data/lena.jpg'
imagefile2 = 'data/opencv_logo.png'
src1 = cv2.imread(imagefile)
src2 = cv2.imread(imagefile2)
rows, cols , channels = src2.shape

roi = src1[0:rows , 0:cols]

gray = cv2.cvtColor(src2, cv2.COLOR_BGRA2GRAY)

ret , mask = cv2.threshold(gray,160,255,cv2.THRESH_BINARY)
#ret , mask_inv = cv2.threshold(gray,160,255,cv2.THRESH_BINARY_INV)
mask_inv = cv2.bitwise_not(mask)

src1_bg = cv2.bitwise_and(roi , roi ,mask = mask)

src2_fg = cv2.bitwise_and(src2, src2, mask = mask_inv)

dst = cv2.add(src1_bg , src2_fg)

src1[0:rows , 0:cols] = dst
cv2.imshow('dst',dst)

cv2.imshow('src1_bg', src1_bg)
cv2.imshow('src2_fg', src2_fg)


cv2.imshow('img',src1)
cv2.imshow('mask',mask)
cv2.imshow('mask_inv',mask_inv)



cv2.waitKey()
cv2.destroyAllWindows()
