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
room="";
desti=100;
reached=False;

while(1):
    if( os.stat("buf.txt").st_size > 0 ):
        f=open("buf.txt","r")
        room=f.read()
        f.close()
        f=open("buf.txt","w")
        f.write("")
        f.close()
        break



def burst():
        IO.output(32,True) #1A+
        IO.output(36,False) #1B-
        IO.output(38,True) #2A+
        IO.output(40,False) #2B-
        time.sleep(0.8)
        print("Burst")
        IO.output(32,False) #1A+
        IO.output(36,False) #1B-
        IO.output(38,False) #2A+
        IO.output(40,False) #2B-

def mus():
        global desti;
        global reached;
        IO.output(32,True) #1A+
        IO.output(36,True) #1B-
        IO.output(38,True) #2A+
        IO.output(40,True) #2B-
        mixer.init()
        mixer.music.load("done.mp3")
        mixer.music.play()
        time.sleep(6)
        reached=False
        lineFollow(desti,-1)
    
def lineFollow(dest,rea):
    global desti;
    global reached;
    while 1:
        if(reached == True):
            mus()
        elif(desti==1):
            break;
        elif(IO.input(16)==True and IO.input(18)==True): #both while move forward     
            print("Condition 1")
            IO.output(32,True) #1A+
            IO.output(36,False) #1B-
            IO.output(38,True) #2A+
            IO.output(40,False) #2B-
        elif(IO.input(16)==True and IO.input(18)==False): #turn right  
            print("Condition 2")
            IO.output(32,True) #1A+
            IO.output(36,True) #1B-
            IO.output(38,True) #2A+
            IO.output(40,False) #2B-
        elif(IO.input(16)==False and IO.input(18)==True): #turn left
            print("Condition 3")
            IO.output(32,True) #1A+
            IO.output(36,False) #1B-
            IO.output(38,True) #2A+
            IO.output(40,True) #2B-
        else:  #stay still
            print("else condition")
            IO.output(32,True) #1A+
            IO.output(36,True) #1B-
            IO.output(38,True) #2A+
            IO.output(40,True) #2B-
            dest=dest-1;
            desti=dest
            burst();
            if(rea>0):
                rea=rea-1
            if(rea==0):
                reached=True
dest=7;
print("Going to room" + str(room))
lineFollow(dest,int(room))
