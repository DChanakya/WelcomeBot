import cv2
import numpy as np
import time,os
# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap = cv2.VideoCapture('source.gif')

# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")

frame_counter=0;
# Read until video is completed
while(cap.isOpened()):
  if( os.stat("comd.txt").st_size > 0 ):
    f=open("comd.txt","w")
    f.write("");
    f.close()
    break
  # Capture frame-by-frame
  time.sleep(0.2)
  ret, frame = cap.read()
  if ret == True:
    frame_counter=frame_counter+1;
  
    # Display the resulting frame
    #cv2.resize(frame,(300,500))
    cv2.namedWindow("Frame",cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("Frame",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
    cv2.imshow('Frame',frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
    if frame_counter == 7:
      frame_counter = 0
      cap = cv2.VideoCapture("source.gif")
  # Break the loop
  else: 
    cap.set(1,1)
    break

# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()
