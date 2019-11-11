import numpy as np
import cv2
import matplotlib.pyplot as plt

imagefile = 'data/lena.jpg'
src = cv2.imread(imagefile, cv2.IMREAD_GRAYSCALE)

#roi = cv2.selectROI('roi',src,showCrosshair=True)
roi = cv2.selectROIs('src',src)
print('rect=',roi)


#x,y,w,h = roi[0],roi[1],roi[2],roi[3]

#img = src[y:y+h,x:x+w]


for i in roi :
    x,y,w,h = i[0],i[1],i[2],i[3]
    cv2.rectangle(src,(x,y),(x+w,y+h),255)

cv2.imshow('src',src)

cv2.waitKey()
cv2.destroyAllWindows()