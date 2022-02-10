import camera, logging, pyb
import csensor


def log_data():
    try:
        sensors = csensor.Sensor.sensors.values()
        for sensor in sensors:
            sensor.update()

        logstring = "{}: {{".format(pyb.millis())
        logstring += "\n\t".join([str(sensor) for sensor in sensors])
        logstring += "\n}\n"

        logging.info(logstring)

    except BaseException as err:
        logging.error("Failed to save data with error type {}!".format(err))
        raise


def log_image(dir):
    try:
        file_name = camera.take_image(dir)
        logging.info("Successfully saved image to file {}.".format(file_name))
    except BaseException as err:
        logging.error("Failed to save image with error type {}!".format(err))
        raise
