import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)


gpio.output(11,False)
gpio.output(13,True)
time.sleep(2)
gpio.output(11,True)
gpio.output(13,False)
time.sleep(2)


pwm=GPIO.PWM(5,50)
pwm.start(5)
time.sleep(1)
pwm.ChangeDutyCycle(12)
time.sleep(1)
pwm.ChangeDutyCycle(7)
time.sleep(1)
GPIO.cleanup()
