import RPi.GPIO as IO
import time
IO.setwarnings(False)
IO.setmode(IO.BOARD)
IO.setup( 16,IO.OUT) 
IO.setup(32,IO.IN,pull_up_down=IO.PUD_DOWN)
while 1:
    but=IO.input(32)
    if(but==IO.HIGH): #both while move forward     
        print("Success")
        IO.output(16,IO.HIGH)
        
    else:
        print("Success2")
        IO.output(16,False)

