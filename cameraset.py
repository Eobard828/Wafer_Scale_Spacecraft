# cameraset - By: eobard

import sensor, image, time, pyb

def init():
    sensor.reset() # Reset and initialize the sensor.
    sensor.set_pixformat(sensor.RGB565) # Set pixel format to RGB565 (or GRAYSCALE)
    sensor.set_framesize(sensor.WQXGA2) # Set frame size to WQXGA2(2592x1944)
    sensor.skip_frames(time = 2000)

def take_image():
    RED_LED_PIN = 1
    BLUE_LED_PIN = 3
    pyb.LED(BLUE_LED_PIN).on()
    sensor.snapshot().save("example.jpg")
    pyb.LED(BLUE_LED_PIN).off()
