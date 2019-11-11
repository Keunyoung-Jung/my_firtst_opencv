import numpy as np
import matplotlib.pyplot as plt
import cv2

file = 'data/vtest.avi'

cap = cv2.VideoCapture(file)
frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
              int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

print('frame_size = ',frame_size)

while(True) :
    ret, frame = cap.read()
    if not ret :
        break
    
    cv2.imshow('Video',frame)
    
    k = cv2.waitKey(25)
    if k == 27 :
        break
cap.release()
cv2.destroyAllWindows()

