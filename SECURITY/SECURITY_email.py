#!/usr/bin/env python
# this script is meant to be used with a webcam and motion sensor. It takes a picture when motion is sensed.
import os
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN) # infrared motion sensor attached to GPIO 24
try:
    while True:
        if GPIO.input(24):  # if the infrared sensor is triggered...
            os.system('/home/pi/scripts/webcam.sh')
        sleep(.3)

except KeyboardInterrupt:
    GPIO.cleanup()
