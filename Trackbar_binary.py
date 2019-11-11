import numpy as np
import cv2
import matplotlib.pyplot as plt
def onChange(x):
    pass
src=cv2.imread('./data/baboon.jpg',cv2.IMREAD_GRAYSCALE)
cv2.namedWindow('trackBar',cv2.WINDOW_NORMAL)
T1=0
T2=0
cv2.createTrackbar('T1','trackBar',T1,255,onChange)
cv2.createTrackbar('T2','trackBar',T2,255,onChange)
bins=255
width=int(256/bins)
barX=np.arange(0,bins)*width
hist=cv2.calcHist(images=[src],channels=[0],mask=None,histSize=[bins],ranges=[0,255])
plt.hist(barX,bins=bins,weights=hist)
plt.savefig('fig1.png')
while True:
    _,img1=cv2.threshold(src,T1,255,cv2.THRESH_BINARY)
    _,img2=cv2.threshold(src,T2,255,cv2.THRESH_BINARY)
    img3=cv2.imread('fig1.png')
    img3=cv2.resize(img3,(360,255))
    cv2.line(img3,(T1+58,30),(T1+58,230),(0,0,255),1)
    cv2.line(img3,(T2+58,30),(T2+58,230),(0,255,0),1)
    T1=cv2.getTrackbarPos('T1','trackBar')
    T2=cv2.getTrackbarPos('T2','trackBar')
    cv2.imshow('trackBar',cv2.hconcat([img1,img2]))
    cv2.imshow('figure',img3)
    k=cv2.waitKey(1)
    if k==27:
        break

cv2.destroyAllWindows()