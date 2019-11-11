import numpy as np
import cv2
import matplotlib.pyplot as plt

imagefile = 'data/lena.jpg'
img = cv2.imread(imagefile, cv2.IMREAD_GRAYSCALE)
plt.axis('off')

#img = cv2.cvtColor(img, cv2.COLOR_BGRA2RGB)
#img = img[:,:,::-1]
img = np.array(img)

print(img.shape)

plt.imshow(img ,cmap='gray' , interpolation='bicubic')
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()
