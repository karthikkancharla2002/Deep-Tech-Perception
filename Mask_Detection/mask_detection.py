#Just using eyes and mouth smartly, no mask involved
import cv2
import numpy as np

mouth_cascade = cv2.CascadeClassifier('haarcascade_mcs_mouth.xml')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

font = cv2.FONT_HERSHEY_SIMPLEX
  
# org
org = (50, 50)
org2=(0,180) 
# fontScale
fontScale = 1
   
# Blue color in BGR
color = (255, 0, 0)
  
# Line thickness of 2 px
thickness = 2

while True:
    _, img = cap.read() #like each frame

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # faces = face_cascade.detectMultiScale(gray,1.1,4)
    eyes = eye_cascade.detectMultiScale(gray,1.1,4)
    mouth = mouth_cascade.detectMultiScale(gray, 1.7, 11)
    if len(mouth)==0 & len(eyes):
        cv2.putText(img,'Please Smile for Mask detection',org, font, fontScale, color, thickness, cv2.LINE_AA)
    
    for (x,y,w,h) in mouth:
        # y = int(y - 0.15*h)
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
    if len(mouth):
        cv2.putText(img,'No Mask detected',org2, font, fontScale, color, thickness, cv2.LINE_AA)
    elif len(mouth)==0 & len(eyes):
        cv2.putText(img,'Mask detected!',org2, font, fontScale, color, thickness, cv2.LINE_AA)



        

    for(x,y,w,h) in eyes:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

        cv2.imshow('img',img)

        k = cv2.waitKey(30) & 0xff
        if k==27:
            break

cap.release()
