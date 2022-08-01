#!/bin/bash

DATE=$(date +"%m-%d-%Y_%H:%M.%S")

fswebcam -r 640x480 --no-banner -d v4l2:/dev/video0 -i 0 -D 1  /home/pi/SECURITY/$DATE.jpeg
