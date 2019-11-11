import numpy as np
import cv2


img = np.zeros((512,512,3), np.uint8)
img = img[:]+255

text = 'hi python opencv='
org = (50,100)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,text,org,font,1,(255,0,0),2)

size,baseLine = cv2.getTextSize(text,font,1,2)

cv2.rectangle(img,org,(org[0]+size[0],org[1] - size[1]),(0,0,255))
cv2.circle(img,org,3,(0,255,0),2)
cv2.imshow('img',img)

cv2.waitKey()