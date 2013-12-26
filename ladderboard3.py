

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

# su[ress warnings
GPIO.setwarnings(False)

# cleanup
GPIO.cleanup()

GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)


GPIO.output(7, True) # blue 1
GPIO.output(11, True) # red 2
GPIO.output(12, True) # red 1
GPIO.output(13, True) # yellow 2
GPIO.output(15, True) # yellow 1
GPIO.output(16, True) # green 2
GPIO.output(18, True) # green 1
GPIO.output(22, True) # blue 2  

#turn off sequentially

time.sleep(.25)

GPIO.output(11, False) # red 2

time.sleep(.25)

GPIO.output(12, False) # red 1

time.sleep(.25)

GPIO.output(13, False) # yellow 2

time.sleep(.25)

GPIO.output(15, False) # yellow 1

time.sleep(.25)

GPIO.output(16, False) # green 2

time.sleep(.25)

GPIO.output(18, False)# Green 1

time.sleep(.25)

GPIO.output(22, False) # Blue 2

time.sleep(.25)

GPIO.output(7, False) #blue 1

time.sleep(.5)

for x in range (5):
    blue1 = 7
    GPIO.output(blue1, True)
    time.sleep(.25)
    GPIO.output(blue1, False)
    

