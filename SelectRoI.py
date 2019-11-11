import numpy as np
import cv2
import matplotlib.pyplot as plt

imagefile = 'data/lena.jpg'
src = cv2.imread(imagefile)
result = src.copy()
#roi = cv2.selectROI('roi',src,showCrosshair=True)

roi = cv2.selectROIs('src',src , False,False)
print('rect=',roi)
counter = 0
print(src.shape)

for i in roi :
    counter += 1 
    x,y,w,h = i[0],i[1],i[2],i[3]
    if counter == 1 :
        img = src[y:y+h,x:x+w]
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        cv2.rectangle(src,(x,y),(x+w,y+h),(0,0,255),2)
        ret , img = cv2.threshold(img,150,255,cv2.THRESH_BINARY)
        img = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
        result[y:y+h,x:x+w] = img
    elif counter == 2 :
        img2 = src[y:y+h,x:x+w,:]
        cv2.rectangle(src,(x,y),(x+w,y+h),(0,255,0),2)
        img2 = 255 - src[y:y+h,x:x+w,:]
        
        result[y:y+h,x:x+w] = img2
        

cv2.imshow('src',src)
cv2.imshow('result',result)

cv2.waitKey()
cv2.destroyAllWindows()