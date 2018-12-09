import RPi.GPIO as gpio
import time,os

def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(24,gpio.OUT)
    gpio.setup(22,gpio.OUT)
    gpio.setup(23,gpio.OUT)
    gpio.setup(16,gpio.OUT)
def forward(tf):
    init()
    gpio.output(24,False)
    gpio.output(22,True)
    time.sleep(3.5)
    gpio.output(24,True)
    gpio.output(22,False)
    time.sleep(2)
while(1):
    if( os.stat("buf1.txt").st_size > 0 ):
        f=open("buf1.txt","r")
        stri=f.read()
        f.close()
        f=open("buf1.txt","w")
        f.write("")
        f.close()
        break

print ("forward")
forward(4)
gpio.cleanup()
