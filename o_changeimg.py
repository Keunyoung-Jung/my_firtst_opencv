
import numpy as np
import cv2

img = cv2.imread('./data/lena.jpg') # cv2.IMREAD_COLOR
#img = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)

cv2.imshow('img',img)
print(img.shape)

img = img.flatten()

print(img.shape)

img = img.reshape(-1,512,512)

print(img.shape)

cv2.imshow('img4',img[0])

cv2.waitKey()