import RPi.GPIO as IO
import time
IO.setwarnings(False)
IO.setmode(IO.BOARD)
##IO.setup(16,IO.IN) #GPIO 2 -> Left IR out
##IO.setup(18,IO.IN) #GPIO 3 -> Right IR out
IO.setup(32,IO.OUT) #GPIO 4 -> Motor 1 terminal A
IO.setup(36,IO.OUT) #GPIO 14 -> Motor 1 terminal B
IO.setup(38,IO.OUT) #GPIO 17 -> Motor Left terminal A
IO.setup(40,IO.OUT) #GPIO 18 -> Motor Left terminal B

IO.output(32,True) #1A+
IO.output(36,False) #1B-
IO.output(38,True) #2A+
IO.output(40,False) #2B-
time.sleep(5)

IO.output(32,False) #1A+
IO.output(36,False) #1B-
IO.output(38,False) #2A+
IO.output(40,False) #2B-

