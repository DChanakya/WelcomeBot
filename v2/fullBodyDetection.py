import numpy as np
import cv2
from matplotlib import pyplot as plt
cam = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('H:/Ubuntu/wb2/Demo/Final/haarcascade_frontalface_default.xml')
#low_cascade = cv2.CascadeClassifier('H:/Ubuntu/wb2/Demo/Final/haarcascades/haarcascade_lowerbody.xml')

cv2.waitKey(0) # If you don'tput this line,thenthe image windowis just a flash. If you put any number other than 0, the same happens.
cv2.destroyAllWindows()
while True:
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1 , 4)
    #low = low_cascade.detectMultiScale(gray, 1.1 , 3)
        
    for (x,y,w,h) in faces:
        #cv2.rectangle(im, (x,y), (x+w, y+h), (12,150,100),2)
        break;
    #for (x,y,w,h) in low:
    #     cv2.rectangle(img, (x,y), (x+w, y+h), (12,150,100),2)
        
    #cv2.imshow('image',im)
    if cv2.waitKey(1)==ord('q'):
        break;
cam.release()
cv2.destroyAllWindows()
import wbu
