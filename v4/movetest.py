import RPi.GPIO as IO
import time,os
from pygame import mixer
IO.setwarnings(False)
IO.setmode(IO.BOARD)
##
##IO.setup(16,IO.OUT)

##IO.setup(29,IO.IN) #GPIO 2 -> Left IR out
##IO.setup(31,IO.IN) #GPIO 3 -> Right IR out 
##IO.setup(33,IO.IN) #GPIO 2 -> Left IR out
##IO.setup(35,IO.IN) #GPIO 2 -> Left IR out
##IO.setup(37,IO.IN) #GPIO 2 -> Left IR out
IO.setup(15,IO.IN) #GPIO 2 -> Left IR out
##IO.setup(13,IO.IN) #GPIO 3 -> Right IR out 
##IO.setup(11,IO.IN) #GPIO 2 -> Left IR out


##IO.output(16,1)
##print("IR pin activated")
####
##IO.output(16,1)
##print("IR pin activated")
##IO.output(16,0)
##print("IR pin activated")
time.sleep(2)
while 1:
####    if(IO.input(29)==True and IO.input(31)==True and IO.input(33)==True and IO.input(35)==True and IO.input(37)==True and IO.input(15)==True and IO.input(13)==True and IO.input(11)==True):
##       print("out of bound")
##    if(IO.input(29)==True and IO.input(31)==True and IO.input(33)==True and IO.input(15)==True and IO.input(13)==True and IO.input(11)==True):
##       print("move forward")
##       time.sleep(1)
##    elif(IO.input(29)==False and IO.input(31)==False and IO.input(33)==False and IO.input(15)==True and IO.input(13)==True and IO.input(11)==True):
##       print("move left")
##       time.sleep(1)
##    elif(IO.input(29)==True and IO.input(31)==True and IO.input(33)==True and IO.input(15)==False and IO.input(13)==False and IO.input(11)==False):
##       print("move right")
##       time.sleep(1)
##    elif(IO.input(29)==False and IO.input(31)==False and IO.input(33)==False and IO.input(15)==False and IO.input(13)==False and IO.input(11)==False):
##       print("move back")
    print(IO.input(15))
    time.sleep(1)
##    print(IO.input(31))
##    print("------2--------")
##    print(IO.input(33))
##    print("-------3-------")
##    print(IO.input(35))
##    print("------4--------")
##    print(IO.input(37))
##    print("------5-------")
