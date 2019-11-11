import numpy as np
import cv2
from matplotlib import pyplot as plt
src1  = cv2.imread('./data/baboon.jpg', cv2.IMREAD_GRAYSCALE)
src2  = cv2.imread('./data/baboon.jpg', cv2.IMREAD_GRAYSCALE)
hist3 = cv2.calcHist(images=[src1], channels=[0], mask=None,
                    histSize=[256], ranges=[0, 256])
hist3 = hist3.flatten()
binX = np.arange(256)
plt.bar(binX, hist3, width=1, color='b')


def onChange(pos): # 트랙바 핸들러
    global img
    t1w = cv2.getTrackbarPos('T1','img1')
    t2w = cv2.getTrackbarPos('T2','img2')
    ret1, dst1 = cv2.threshold(src1, t1w, 255, cv2.THRESH_BINARY)                   
    ret2, dst2 = cv2.threshold(src2, t2w, 255, cv2.THRESH_BINARY)
    cv2.imshow('img1', dst1)
    cv2.imshow('img2', dst2)
    plt.axvline(t1w, color='r', linestyle='-', linewidth=1)
    plt.axvline(t2w, color='b', linestyle='-', linewidth=1)
    plt.show()

cv2.imshow('img1', src1)
cv2.imshow('img2', src2)

cv2.createTrackbar('T1', 'img1', 0, 255, onChange)
cv2.createTrackbar('T2', 'img2', 0, 255, onChange)

plt.show()

cv2.waitKey()
cv2.destroyAllWindows()
