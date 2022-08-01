#!/usr/bin/env python
# for use with fswebcam and Logitech Z270 webcam
import os
DATE=$(date +"%Y-%m-%d_%H%M_%S")
os.system("fswebcam -D 1 --resolution 1280x720 --loop 1 --no-banner /home/pi/Pictures/$DATE.jpg ")
exit()

