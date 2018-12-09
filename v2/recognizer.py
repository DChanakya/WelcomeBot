import cv2
import numpy as np



cam = cv2.VideoCapture(0)
while True:
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, 1.2,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,255),2)
        Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
        if(Id==1):
            Id="Chanakya"
        elif(Id==2):
            Id="Chinmai"
        elif(Id==3):
            Id="Abhi"
        cv2.putText(im,str(Id), (x,y+h),font,2, 255)
    cv2.imshow('im',im) 
    if cv2.waitKey(1)==ord('q'):
        break;
cam.release()
cv2.destroyAllWindows()
