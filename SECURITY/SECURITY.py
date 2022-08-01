#!/usr/bin/env python
import os
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN)
x = 0
try:
    while True:
        sleep(2)
        if GPIO.input(24):
                while(x < 1):
                        sleep(1)
                        os.system('/home/pi/scripts/fswebcam_bash_call.sh')
                        os.system('/home/pi/python/SECURITY_email.py')
                        os.system('/home/pi/python/SECURITY_text.py')
                        x = x + 1
                        sleep(1)
                while(x < 10):
                        os.system('/home/pi/scripts/copy_webcam.sh')
                        x = x + 1
                x = 1

except KeyboardInterrupt:
    GPIO.cleanup()
