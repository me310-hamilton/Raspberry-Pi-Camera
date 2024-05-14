from picamera2 import Picamera2, Preview
import time
import cv2
import RPi.GPIO as gp
import os
gp.setwarnings(False)
gp.setmode(gp.BOARD)
gp.setup(7,gp.OUT)
gp.setup(11,gp.OUT)
gp.setup(12,gp.OUT)
gp.setup(13,gp.OUT)

i2c = "i2cset -y 10 0x24 0x24 0x12"

# Set to single channel 0
#i2cset -y 10 0x24 0x24 0x02
# Set to single channel 1
#i2cset -y 10 0x24 0x24 0x12
# Set to single channel 2
#i2cset -y 10 0x24 0x24 0x22
# Set to single channel 3
#i2cset -y 10 0x24 0x24 0x32

os.system(i2c)
gp.output(7, True)
gp.output(11, True)
gp.output(12, False)

picam2 = Picamera2()
camera_config = picam2.create_preview_configuration()
picam2.configure(camera_config)
picam2.start_preview(Preview.QTGL)
picam2.start()
time.sleep(2)
picam2.capture_file("test.jpg")
