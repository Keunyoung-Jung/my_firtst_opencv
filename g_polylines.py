import numpy as np
import cv2


img = np.zeros((512,512,3), np.uint8)
img = img[:]+255

pts1 = np.array([[100,100],[200,100],[200,200],[100,200]])
pts2 = np.array([[300,200],[400,100],[400,200]])
green = (0,255,0)
blue = (255,0,0)
red = (0,0,255)

cv2.polylines(img,[pts1,pts2],isClosed=True , color = blue)


cv2.imshow('img',img)

cv2.waitKey()
