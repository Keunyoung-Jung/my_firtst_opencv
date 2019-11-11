import numpy as np
import cv2

'''
K-MEANS알고리즘은 데이터의 거리에 따라 군집화를 해주는 알고리즘 인데, 앞서 HSV로 색상을 변경하여 군집하하기 때문에
색상을 통해서 군집화가 되는 것을 확인할 수가 있다. 색상을 통해 군집화를 진행하므로 사진에서 나타나는 색상을 직접 확인해봤을때
과일들의 색상이 대략 4가지 정도로 나타나는 것을 경험적으로 알 수 있다. 그것을 극대화시키기 위해 침식, 팽창 연산을 이용하여
전처리 해준다면 K=4로만 주어도 비슷한 색상끼리 군집화가  되는 것을 알 수 있다. 그러나 침식, 팽창 연산을 하지 않은 원본
연상으로 할 때는 K의 값이 너무 작으면 색상 별 군집화가  모호해지고, K값이 너무 클 경우 같은 과일의 색일 지라도, 너무 세분화
되거나 노이즈의 생상이 따로 군집화 되어 낭비되는 군집이 생기므로 8~10정도의 K가 가장 좋다.
중심점의 경우 처음 어떻게 잡더라도 결국 반복 연산으로 군집의 평균을 찾아가므로  PP와 RANDOM 모두 비슷한 결과를 나타내고 있다.
'''

def draw_rect(src , colors , K):
    
    new = 255 - np.zeros(src.shape,dtype = src.dtype)
    new = new[0:int(src.shape[1]/K) , 0:int(src.shape[0])]
    
    start = (0,0)
    for i in range(len(colors)+1) :
        end = (i*int(src.shape[0]/K),int(src.shape[1]/K))
        cv2.rectangle(new,start,end,colors[i-1],-1)
        start = (end[0],0)
        
    return new

def preprocessing(src):
    
    kernel = cv2.getStructuringElement(shape = cv2.MORPH_RECT, ksize = (3,3))
    src = cv2.erode(src ,kernel,iterations = 4)
    src = cv2.dilate(src ,kernel,iterations = 4)
    src_hsv = cv2.cvtColor(src , cv2.COLOR_BGR2HSV)
    src_hsv = src_hsv.reshape((-1,3)).astype(np.float32)
    cv2.imshow('src',src)
    
    return src_hsv

def k_means(K,src_hsv):
    term_crit=(cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    ret, labels, centers = cv2.kmeans(src_hsv, K, None, term_crit, 5,
                                      cv2.KMEANS_RANDOM_CENTERS)
    
    labels2 = np.uint8(labels.reshape(src.shape[:2]))
    dst  = np.zeros(src.shape, dtype=src.dtype)
    
    colors = []
    
    for i in range(K): 
        r = np.random.randint(256)
        g = np.random.randint(256)
        b = np.random.randint(256)
        dst[labels2 == i] = [b, g, r]
        colors.append((b,g,r))
    return colors , dst
    
while True :
    origin = cv2.imread('data/fruits.jpg')
    src = origin.copy()
    src2 = origin.copy()
    src_hsv = preprocessing(src)
    src_hsv2 = cv2.cvtColor(src , cv2.COLOR_BGR2HSV)
    src_hsv2 = src_hsv2.reshape((-1,3)).astype(np.float32)
    
    K = 4
    K2 = 9
    #print(colors)
    colors , dst = k_means(K,src_hsv)
    colors2 , dst2 = k_means(K2, src_hsv2)
    new = draw_rect(src,colors,K)
    new2 = draw_rect(src2,colors2,K2)
    
    text = 'Press space bar'
    cv2.putText(dst,text,(105,35),cv2.FONT_HERSHEY_SIMPLEX,1 ,(255,255,255),3)
    
    cv2.imshow('new',new)
    cv2.imshow('new2',new2)
    cv2.imshow('orgin',origin)
    cv2.imshow('dst',dst)
    cv2.imshow('dst2',dst2)
    
    key = cv2.waitKey()
    if key == 27 :
        break

cv2.destroyAllWindows()
