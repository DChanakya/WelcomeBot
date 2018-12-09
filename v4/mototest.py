import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
##GPIO.setup(5,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)


GPIO.output(11,False)
GPIO.output(13,True)
time.sleep(2)
GPIO.output(11,True)
GPIO.output(13,False)
time.sleep(2)
