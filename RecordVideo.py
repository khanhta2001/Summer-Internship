"""
This file is for rasberry Pi to record a video and store it in storage. You can change storage location
to any place you prefer.
"""

from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.start_preview()

camera.start_recording('/media/pi/18UF-1823/video.h264')

""" this /media/pi/18UF-1823/video.h264 is a usb location of a specific usb. Change the location to another place
or else it will not work. 
"""

sleep(60)

"""Sleep() is a function that delays (waits) execution of a part of the file. In this case, it will wait 60 secs 
before it stops recording. Can change to any time you like. 
"""

camera.stop_recording()
camera.stop_preview()