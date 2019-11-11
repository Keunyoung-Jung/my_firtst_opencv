import numpy as np
import cv2
import matplotlib.pyplot as plt

src = cv2.imread('data/lena.jpg',cv2.IMREAD_GRAYSCALE)
dst = cv2.equalizeHist(src)

cv2.imshow('dst',dst)
cv2.waitKey()
cv2.destroyAllWindows()

plt.title('gray scale histogram of lena')

hist1 = cv2.calcHist(images = [src] , channels = [0] ,mask =None , histSize = [256], ranges = [0,256])
plt.plot(hist1, color = 'b', label = 'hist1 in src')

hist2 = cv2.calcHist(images = [dst] , channels = [0] ,mask =None , histSize = [256], ranges = [0,256])
plt.plot(hist2, color = 'r', alpha = 0.7 , label = 'hsit2 in dst')
plt.legend(loc = 'best')
plt.show()