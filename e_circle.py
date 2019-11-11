import numpy as np
import cv2


img = np.zeros((512,512,3), np.uint8)
img = img[:]+255

pt1 = (100,100)
pt2 = (400,400)
green = (0,255,0)
blue = (255,0,0)
red = (0,0,255)

cx,cy = int(img.shape[1]/2) , int(img.shape[0]/2)

#center = (256,256)
center = (cx,cy)

cv2.circle(img,center,100,blue,2)
cv2.circle(img,center,200,blue,2)
cv2.circle(img,center,50,red,-1)

cv2.imshow('img',img)

cv2.waitKey()

cv2.destroyAllWindows()
