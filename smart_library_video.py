import cv2
import numpy as np
template = cv2.imread(" ",0)   #Enter the templete image of the book
w,h = template.shape[::-1]
cap=cv2.VideoCapture(" ")      #Enter the video file or connect the webcam and replace with 0
if not cap.isOpened():
    raise IOError("Cannot open")
flag=0
while (True):
    ret,frame=cap.read()
    if ret==True:
        frame=cv2.resize(frame,(720,720),interpolation=cv2.INTER_AREA)
        frame=cv2.transpose(frame)
        frame=cv2.flip(frame,1)
        img_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        threshold=0.5
        loc=np.where(res>=threshold)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(frame,pt,(pt[0]+w,pt[1]+h),(0,200,200),2)
            flag=1
        cv2.imshow('output',frame)
    c=cv2.waitKey(1)
    if c==27:
        break
cap.release()
cv2.destroyAllWindows()
        
