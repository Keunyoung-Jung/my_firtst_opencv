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
size = (200,100)
ptCenter = (cx,cy)



cv2.imshow('img',img)

cv2.waitKey()