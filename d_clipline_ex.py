import numpy as np
import cv2


img = np.zeros((512,512,3), np.uint8)
img = img[:]+255

x1,y1 = 100,100
x2,y2 = 400,400
pt1 = (120,50)
pt2 = (300,500)
green = (0,255,0)
blue = (255,0,0)
red = (0,0,255)

cv2.rectangle(img,(x1,y1),(x2,y2),red,2)
cv2.line(img,pt1,pt2,blue,2)

imgRect = (x1,y1,x2-x1,y2-y1)
ret , p1 , p2 = cv2.clipLine(imgRect,pt1,pt2)

if ret is True :
    cv2.circle(img,p1,10,green,2)
    cv2.circle(img,p2,10,green,2)
    

cv2.imshow('img',img)

cv2.waitKey()

cv2.destroyAllWindows()
