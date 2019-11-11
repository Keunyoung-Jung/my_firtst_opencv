import numpy as np
import cv2
import matplotlib.pyplot as plt

counter = 1
def onChange(pos):
    global counter
    T1 = cv2.getTrackbarPos('T1','img')
    T2 = cv2.getTrackbarPos('T2','img2')
    
    _,gray_bin = cv2.threshold(gray,T1,255,cv2.THRESH_BINARY)
    _,gray2_bin = cv2.threshold(gray,T2,255,cv2.THRESH_BINARY)
    
    cv2.imshow('img',gray_bin)          #3번) 이진화한 영상을 표시 
    cv2.imshow('img2',gray2_bin)
    
    if counter > 1 :
        draw_hist(T1,T2)
    counter +=1


def draw_hist(T1,T2):                   #4번) 히스토그리기 함수 설정
    
    hist = cv2.calcHist(images = [gray] , channels = [0], mask = None,
                     histSize= [256] , ranges = [0,256])
    hist = hist.flatten()                #4번) histogram을 gray로 부터 생성
    binX = np.arange(256)                #4번) bin을 256개로 설정
    plt.cla()
    plt.title('histogram')
    plt.bar(binX,hist,width = 1 , color ='g')                   #4번) bar차트를 이용해서 시각화
    plt.vlines(T1, ymin = 0, ymax = 3000, colors = 'orange')    #4번) T1,T2,가 bar차트에 함께 표시되도록함
    plt.text(T1, 3000, 'T1')
    plt.vlines(T2, ymin = 0, ymax = 3000, colors = 'blue')
    plt.text(T2, 3000, 'T2')
    plt.show()

gray = cv2.imread('data/cell.png',cv2.IMREAD_GRAYSCALE)  #1번) 원본 영상을 gray로 읽어들여 gray로 치환                                  

cv2.imshow('img',gray)
cv2.imshow('img2',gray)

cv2.createTrackbar('T1','img',0,255,onChange)       #2번) 트랙바 두개를 생성
cv2.createTrackbar('T2','img2',0,255,onChange)

cv2.setTrackbarPos('T2','img2',230)                 #2번) 이진화를 적용할 임계값 230과 75를 각각 설정
cv2.setTrackbarPos('T1','img',75)

