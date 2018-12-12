import RPi.GPIO as IO
import time,os
from pygame import mixer
IO.setwarnings(False)
IO.setmode(IO.BOARD)
IO.setup(16,IO.IN) #GPIO 2 -> Left IR out
IO.setup(18,IO.IN) #GPIO 3 -> Right IR out
IO.setup(36,IO.OUT) #GPIO 4 -> Motor 1 terminal A
IO.setup(32,IO.OUT) #GPIO 14 -> Motor 1 terminal B
IO.setup(38,IO.OUT) #GPIO 17 -> Motor Left terminal A
IO.setup(40,IO.OUT) #GPIO 18 -> Motor Left terminal B
IO.setup(5,IO.OUT) #Left Motor Enabler
IO.setup(7,IO.OUT) #Right Motor Enabler

IO.output(5,IO.HIGH)
IO.output(7,IO.HIGH)

while 1:
   
    if(IO.input(16)==True and IO.input(18)==True): #both while move forward     
        
        print("Moving Forward")
        IO.output(32,True) #1A+
        IO.output(36,False) #1B-
        IO.output(38,True) #2A+
        IO.output(40,False) #2B-
    elif(IO.input(16)==True and IO.input(18)==False): #turn right      
        
       # pwml.changeDutyCycle(15)
        print("Moving Right")
        print("------------------------")
        IO.output(32,True) #1A+
        IO.output(36,True) #1B-
        IO.output(38,True) #2A+
        IO.output(40,False) #2B-
    elif(IO.input(16)==False and IO.input(18)==True): #turn left    
        
       # pwmr.changeDutyCycle(15)
        print("Moving Left")
        IO.output(32,True) #1A+
        IO.output(36,False) #1B-
        IO.output(38,True) #2A+
        IO.output(40,True) #2B-
    else:  #stay still
        print("No black line")
        
        IO.output(32,True) #1A+
        IO.output(36,True) #1B-
        IO.output(38,True) #2A+
        IO.output(40,True) #2B-

