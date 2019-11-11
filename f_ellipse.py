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

#center = (256,256)
ptCenter = (cx,cy)

cv2.ellipse(img,ptCenter,size,0,0,360,blue)
cv2.ellipse(img,ptCenter,size,45,0,360,red)
cv2.ellipse(img,ptCenter,(int(size[0]/2),int(size[1]/2)),0,0,360,blue,5)
cv2.ellipse(img,ptCenter,(int(size[0]/2),int(size[1]/2)),45,0,360,red,5)

cv2.imshow('img',img)

cv2.waitKey()

cv2.destroyAllWindows()
