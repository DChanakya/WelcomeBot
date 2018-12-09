import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)
pwm=GPIO.PWM(3,50)

pwm.start(8)
time.sleep(1)
time.sleep(2)
pwm.ChangeDutyCycle(1)
time.sleep(3)
pwm.stop()
GPIO.cleanup()
