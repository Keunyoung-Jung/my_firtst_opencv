import numpy as np
import cv2


img = np.zeros((512,512,3), np.uint8)
img = img[:]+255

pt1 = (100,100)
pt2 = (400,400)
green = (0,255,0)
blue = (255,0,0)
red = (0,0,255)

cv2.rectangle(img,pt1,pt2,green,2)
cv2.line(img,(0,0),(500,0),blue,2)
cv2.line(img,(0,0),(0,500),red,2)

cv2.imshow('img',img)

cv2.waitKey()

cv2.destroyAllWindows()
