from csensor import sensor

class BME(Sensor):
    most_recent = {} # a dict of the most recent sensor values
    units = [] # a list of acceptable units for this sensor
    name = "BMX160" # this sensors name
    addr = 0xD0
    chipid = 0x68
    sensors = [] # static list of all sensor-type objects
    # static
    registers = { # constant array of register vals for calibration data
        "CHIPID": 0x00
    }
    # calibration read from dvc
    # nostatic

    def __init__(self, i2c):
        self.i2c = i2c
        chipid = self.i2c.mem_read(1, self.addr, BME, self.registers["CHIPID"])
        if self.chipid != chipid:
            raise ValueError

    def update(self, *args) -> {"dtype": 1.234}:
        """
        Refresh values by acquiring new data from the sensor, and then return
        it.
        """
        self.most_recent = {}
        return self.get(*args)

    def get(self, units=None) -> {"dtype": 1.234}:
        """
        Return the most recently acquired values.
        """
        return self.most_recent

    def __str__(self, *args):
        """
        Return a string with the most recent value and the name of the sensor.
        """
        return f'"{self.name}": {self.get(*args)}'
