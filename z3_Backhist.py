import numpy as np
import cv2

'''src = np.array([[0,0,0,0],
               [1,1,3,5],
               [6,1,1,3],
               [4,3,1,7]], dtype = np.uint8)

hist = cv2.calcHist(images = [src], channels = [0] , mask = None ,
                    histSize = [4] , ranges = [0,8])

print('hist = ',hist)

backP = cv2.calcBackProject([src], [0] , hist, [0,8] , scale = 1)

print('backP', backP)

'''
#spoid smiller color 
src = cv2.imread('data/fruits.jpg')
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

h,s,v = cv2.split(hsv)

roi = cv2.selectROI(src)
print('roi=',roi)

roi_h = h[roi[1]:roi[1] + roi[3],roi[0]:roi[0]+roi[2]]

hist = cv2.calcHist([roi_h],[0],None,[64],[0,256])
backP = cv2.calcBackProject([h.astype(np.float32)],[0],hist,[0,256],scale = 1.0)

hist = cv2.sort(hist , cv2.SORT_EVERY_COLUMN + cv2.SORT_DESCENDING)

k = 1 

T = hist[k][0] -1 
print('T = ',T)
ret , dst = cv2.threshold(backP,T,255,cv2.THRESH_BINARY)

cv2.imshow('dst',dst)
cv2.waitKey()
cv2.destroyAllWindows()
