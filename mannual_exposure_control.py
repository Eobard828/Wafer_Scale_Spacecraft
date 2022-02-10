# Mannual_Exposure_Control  - By: eobard - Wed Feb 9 2022

import sensor, image, time


GAIN_SCALE = 1.0

sensor.reset() # Reset and initialize the sensor.
sensor.set_pixformat(sensor.RGB565) # Set pixel format to RGB565 (or GRAYSCALE)
sensor.set_framesize(sensor.WQXGA2) # Set frame size to WQXGA2(2592x1944)

print("Initial gain == %f db" % sensor.get_gain_db())

sensor.skip_frames(time = 2000)

sensor.set_auto_exposure(False) # Stop the auto-exposure and auto-whiteballance
sensor.set_auto_whitebal(False)

sensor.skip_frames(time = 500)

current_gain_in_decibels = sensor.get_gain_db()
print("Current Gain == %f db" % current_gain_in_decibels)


sensor.set_auto_gain(False, \
    gain_db = current_gain_in_decibels * GAIN_SCALE)

print("New gain == %f db" % sensor.get_gain_db())


while(True):
    clock.tick()
    img = sensor.snapshot()
    print(clock.fps())
