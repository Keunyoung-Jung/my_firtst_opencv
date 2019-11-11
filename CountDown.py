import numpy as np
import cv2


def draw_countdown():
    count5 = 5
    
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('homework.mp4',fourcc,10.0,(512,512))
    count_frame = 1
    
    while True :
        count_frame += 1
            
        img = np.zeros((512,512,3), np.uint8)
    
        text = str(count5)
        org = (220,290)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.ellipse(img,(256,256),(200,200),0,0,36*count_frame,(100,100,100),-1)
        pts1 = cv2.ellipse2Poly((256,256),(100,100),0,0,36*count_frame,36)
        pts2 = cv2.ellipse2Poly((256,256),(200,200),0,0,36*count_frame,36)
        cv2.polylines(img,[pts1],False,(255,255,255))
        cv2.polylines(img,[pts2],False,(255,255,255))
        cv2.putText(img,text,org,font,4,(255,255,255),5)
        
        if count_frame == 10 :
            count5 -= 1
            count_frame = 1
        
        if count5 == -1 :
            break
        
        out.write(img)
        
        k = cv2.waitKey(100)
        if k == 27 :
            break
        
    out.release()
    cv2.destroyAllWindows()

draw_countdown()

file = 'homework.mp4'

cap = cv2.VideoCapture(file)

while(True) :
    ret, frame = cap.read()
    if not ret :
        break
    
    cv2.imshow('Video',frame)
    
    k = cv2.waitKey(100)
    if k == 27 :
        break
    
cap.release()
cv2.destroyAllWindows()