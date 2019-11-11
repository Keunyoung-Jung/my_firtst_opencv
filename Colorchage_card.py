import numpy as np
import cv2

def reverse(img):
    img = 255 - img
    return img

def preprocessing(img) :
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    kernel = cv2.getStructuringElement(shape = cv2.MORPH_RECT, ksize = (3,3))
    ret,dst = cv2.threshold(gray , 128, 255 ,cv2.THRESH_BINARY)
    opening = cv2.morphologyEx(dst , cv2.MORPH_OPEN,kernel,iterations = 1)
    rev = reverse(opening)
    return rev

t = 50
sw = 1
while True:
    
    src = cv2.imread('data/Heart10.jpg')
    pre = preprocessing(src)
    
    ret , labels = cv2.connectedComponents(pre)
    
    dst = np.zeros(src.shape,dtype = src.dtype)
    
    for i in range(1, ret) :
        b = np.random.randint(256)
        g = np.random.randint(256)
        r = np.random.randint(256)
        dst[labels == i] = [b,g,r]
        
    dst = reverse(dst)
    text = 'Press space bar'
    cv2.putText(dst,text,(55,35),cv2.FONT_HERSHEY_SIMPLEX,1,(b,g,r),3)
    cv2.imshow('dst',dst)
    k = cv2.waitKey(t)
    if k == 27 :
        break
    elif k == ord(' ') :
        if sw == 1 :
            t =  0
            sw = 0
        else :
            t = 50
            sw = 1
    
cv2.destroyAllWindows()