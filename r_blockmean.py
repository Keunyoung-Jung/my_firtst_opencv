import numpy as np
import cv2
import matplotlib.pyplot as plt

imagefile = 'data/lena.jpg'
src = cv2.imread(imagefile, cv2.IMREAD_GRAYSCALE)
dst = np.zeros_like(src)

N = 128

height , width = src.shape
h, w = height//N , width//N

for i in range(N) :
    for j in range(N) :
        y = i * h
        x = j * w 
        roi = src[y:y + h, x:x + w]
        dst[y:y+h,x:x+w] = cv2.mean(roi)[0]

#mean_value = src[:int(height/N), :int(width/N)].mean()
#dst[:int(height/N), :int(width/N)] = mean_value


cv2.imshow('img',src)
cv2.imshow('dst',dst)


cv2.waitKey()
cv2.destroyAllWindows()
