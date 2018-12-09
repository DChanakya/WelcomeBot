import RPi.GPIO as IO
import time
IO.setwarnings(False)
IO.setmode(IO.BOARD)
IO.setup(16,IO.IN) #GPIO 2 -> Left IR out
IO.setup(18,IO.IN) #GPIO 3 -> Right IR out
IO.setup(32,IO.OUT) #GPIO 4 -> Motor 1 terminal A
IO.setup(36,IO.OUT) #GPIO 14 -> Motor 1 terminal B
IO.setup(38,IO.OUT) #GPIO 17 -> Motor Left terminal A
IO.setup(40,IO.OUT) #GPIO 18 -> Motor Left terminal B
row=0
while 1:
 
    if(IO.input(16)==False and IO.input(18)==False): #both while move forward     
        print("Condition 1")
        IO.output(32,True) #1A+
        IO.output(36,False) #1B-
        IO.output(38,True) #2A+
        IO.output(40,False) #2B-
    elif(IO.input(16)==False and IO.input(18)==True): #turn right
        if(Third==True):
            row=row+1;
            if(row==tab):
                print("Righting")
                IO.output(32,True) #1A+
                IO.output(36,True) #1B-
                IO.output(38,True) #2A+
                IO.output(40,False) #2B-
        elif(Third==False):
            print("Righting")
            IO.output(32,True) #1A+
            IO.output(36,True) #1B-
            IO.output(38,True) #2A+
            IO.output(40,False) #2B-
                
        
    elif(IO.input(16)==True and IO.input(18)==False): #turn left
        if(Third==True):
            row=row+1;
            if(row==tab):
                print("Lefting")
                IO.output(32,True) #1A+
                IO.output(36,False) #1B-
                IO.output(38,True) #2A+
                IO.output(40,True) #2B-
        elif(Third==False):
            print("Lefting")
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
