import os
import RPi.GPIO as IO
import time
from pygame import mixer

IO.setwarnings(False)
IO.setmode(IO.BOARD)
IO.setup(16,IO.IN) #GPIO 2 -> Left IR out
IO.setup(18,IO.IN) #GPIO 3 -> Right IR out
IO.setup(32,IO.OUT) #GPIO 4 -> Motor 1 terminal A
IO.setup(36,IO.OUT) #GPIO 14 -> Motor 1 terminal B
IO.setup(38,IO.OUT) #GPIO 17 -> Motor Left terminal A
IO.setup(40,IO.OUT) #GPIO 18 -> Motor Left 

def front():
        IO.output(32,True) #1A+
        IO.output(36,False) #1B-
        IO.output(38,True) #2A+
        IO.output(40,False) #2B-
        time.sleep(0.2)
        IO.output(32,False) #1A+
        IO.output(36,False) #1B-
        IO.output(38,False) #2A+
        IO.output(40,False) #2B-

def back():
        IO.output(32,False) #1A+
        IO.output(36,True) #1B-
        IO.output(38,False) #2A+
        IO.output(40,True) #2B-
        time.sleep(0.2)
        IO.output(32,False) #1A+
        IO.output(36,False) #1B-
        IO.output(38,False) #2A+
        IO.output(40,False) #2B-



def left():
        IO.output(32,True) #1A+
        IO.output(36,False) #1B-
        IO.output(38,True) #2A+
        IO.output(40,True) #2B-
        time.sleep(0.2)
        IO.output(32,False) #1A+
        IO.output(36,False) #1B-
        IO.output(38,False) #2A+
        IO.output(40,False) #2B-
def right():
        IO.output(32,True) #1A+
        IO.output(36,True) #1B-
        IO.output(38,True) #2A+
        IO.output(40,False) #2B-
        time.sleep(0.2)
        IO.output(32,False) #1A+
        IO.output(36,False) #1B-
        IO.output(38,False) #2A+
        IO.output(40,False) #2B-
def stop():
        IO.output(32,False) #1A+
        IO.output(36,False) #1B-
        IO.output(38,False) #2A+
        IO.output(40,False) #2B-
        time.sleep(0.2)

while(1):
    if( os.stat("buf.txt").st_size > 0 ):
        f=open("buf.txt","r")
        stri=f.read()
        f.close()
        if("front" in stri):
            front();
        
        if("left" in stri):
            left();
        
        if("right" in stri):
            right();
        if("back" in stri):
            back();
        
        if("stop" in stri):
            f=open("buf.txt","w")
            f.write("");
            f.close();
            
