import RPi.GPIO as IO
import time,os
from pygame import mixer
IO.setwarnings(False)
IO.setmode(IO.BOARD)
IO.setup(16,IO.IN) #GPIO 2 -> Left IR out
IO.setup(18,IO.IN) #GPIO 3 -> Right IR out
IO.setup(32,IO.OUT) #GPIO 4 -> Motor 1 terminal A
IO.setup(36,IO.OUT) #GPIO 14 -> Motor 1 terminal B
IO.setup(38,IO.OUT) #GPIO 17 -> Motor Left terminal A
IO.setup(40,IO.OUT) #GPIO 18 -> Motor Left terminal B
location=""
stri="principal"
while(1):
    if( os.stat("buf.txt").st_size > 0 ):
        f=open("buf.txt","r")
        stri=f.read()
        f.close()
        f=open("buf.txt","w")
        f.write("")
        f.close()
        break


junctionCross=0

def selectRouting(stri):
    global junctionCross;
    if("principal" in stri):
        junctionCross=2;
    else:
        junctionCross=4;


def burst():
        IO.output(32,True) #1A+
        IO.output(36,False) #1B-
        IO.output(38,True) #2A+
        IO.output(40,False) #2B-
        time.sleep(0.8)
        
        IO.output(32,False) #1A+
        IO.output(36,False) #1B-
        IO.output(38,False) #2A+
        IO.output(40,False) #2B-

      

def linefollow(junctionCross):
    while 1:
        if(junctionCross==0):
            break;
        if(IO.input(16)==True and IO.input(18)==True): #both while move forward     
            print("Moving Forward")
            IO.output(32,True) #1A+
            IO.output(36,False) #1B-
            IO.output(38,True) #2A+
            IO.output(40,False) #2B-
            
        elif(IO.input(16)==False and IO.input(18)==True): #turn right  
            print("Moving Right")
            print("------------------------")
            IO.output(32,True) #1A+
            IO.output(36,True) #1B-
            IO.output(38,True) #2A+
            IO.output(40,False) #2B-
           
        elif(IO.input(16)==True and IO.input(18)==False): #turn left
            print("Moving Left")
            IO.output(32,True) #1A+
            IO.output(36,False) #1B-
            IO.output(38,True) #2A+
            IO.output(40,True) #2B-
        else:  #stay still
            print("Stopped at black line")
            IO.output(32,True) #1A+
            IO.output(36,True) #1B-
            IO.output(38,True) #2A+
            IO.output(40,True) #2B-
            junctionCross=junctionCross-1;
            
            burst();
            linefollow(junctionCross);
            

def startMoving():
    global stri
    global junctionCross;
    print("started");
    cross=junctionCross;
    selectRouting(stri);
    burst();
    linefollow(junctionCross);
    time.sleep(3);
    print('delay')
    linefollow(2)
        
startMoving();
