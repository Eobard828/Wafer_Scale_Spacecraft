import csensor, log, camera
import logging, time, pyb, os
from machine import I2C

from tmp import TMP
from ltr import LTR

RED, GREEN, BLUE = 1, 2, 3  # LED INDICES

files = os.listdir()
i = 0
while "run{}".format(i) in files:
    i += 1
dname = "run{}".format(i)
os.mkdir(dname)
fname = dname + "/out.log"
log_file = open(fname, 'a')
logging.basicConfig(stream=log_file)

camera.init()

sensor_addresses = {'BME280': 0x77, 'TMP100_0': 0x48, 'TMP100_1': 0x49, 'BMX160': 0x68, 'LTR_329ALS_01': 0x29}
i2c = I2C(2)  # create I2C peripheral at frequency of 400kHz

TMP(i2c=i2c, name='TMP100_1', addr=sensor_addresses['TMP100_1'])
LTR(i2c=i2c, name='LTR_329ALS_01')

flag = 0
def sched(t):
    global flag
    flag = 1

clock = time.clock()
tim = pyb.Timer(4)
tim.init(freq=2)
tim.callback(sched)

DATA_INTERVAL = const(60)
IMAGE_INTERVAL = const(3600)

def main():
    count = 0
    while True:
        global flag
        if not flag:
            continue

        flag = 0
        count += 1
        if count % 2 == 0:
            if count % (2 * DATA_INTERVAL) == 0:
                try:
                    log.log_data()
                    light = csensor.Sensor.sensors['LTR_329ALS_01'].get()
                    if light["ch0"] > 50 or light["ch1"] > 50 or count % 2 * IMAGE_INTERVAL == 0:
                        log.log_image(dname)
                except:
                    pyb.LED(RED).on()
                else:
                    pyb.LED(GREEN).on()
            else:
                pyb.LED(BLUE).on()
        else:
            for led in (RED, GREEN, BLUE):
                pyb.LED(led).off()


try:
    main()
finally:
    log_file.close()
