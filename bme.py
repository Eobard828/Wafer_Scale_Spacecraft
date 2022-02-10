from csensor import sensor

class BME(Sensor):
    most_recent = {} # a dict of the most recent sensor values
    units = [] # a list of acceptable units for this sensor
    name = "BME280" # this sensors name
    addr = 0xEE
    chipid = 0x77
    sensors = [] # static list of all sensor-type objects
    # static
    registers = { # constant array of register vals for calibration data
        "T1":             0x88,
        "T2":             0x8A,
        "T3":             0x8C,
        "P1":             0x8E,
        "P2":             0x90,
        "P3":             0x92,
        "P4":             0x94,
        "P5":             0x96,
        "P6":             0x98,
        "P7":             0x9A,
        "P8":             0x9C,
        "P9":             0x9E,
        "H1":             0xA1,
        "H2":             0xE1,
        "H3":             0xE3,
        "H4":             0xE4,
        "H5":             0xE5,
        "H6":             0xE7,
        "VERSION":        0xD1,
        "SOFTRESET":      0xE0,
        "CAL26":          0xE1,
        "CONTROLHUMID":   0xF2,
        "CONTROL":        0xF4,
        "CONFIG":         0xF5,
        "PRESSUREDATA":   0xF7,
        "TEMPDATA":       0xFA,
        "HUMIDDATA":      0xFD,
    }
    # calibration read from dvc
    # nostatic
    calib_vals = {k: None for k in BME.registers.keys() if len(k) == 2}

    def __init__(self, i2c):
        self.super().__init__()
        self.i2c = i2c
        hs = ["H4", "H5", "H6"]
        for cv in BME.calib_vals.keys():
            size = 2
            if cv in hs:
                size = 1
            self.calib_vals[cv] = self.i2c.mem_read(1, self.addr, \
                    BME.registers[cv])
            # From deep in adafruit
        self.calib_vals["H4"] = ((self.calib_vals["H4"] & 0xF) << 4) | \
                                 ((self.calib_vals["H5"] >> 4) & 0x0F)
        self.calib_vals["H5"] = ((self.calib_vals["H6"] & 0xF) << 4) | \
                                 ((self.alib_vals["H5"] >> 4) & 0x0F)
        self.i2c.mem_write([0x03], self.addr, self.registers["CONTROLHUMID"])
        self.i2c.mem_write([0x3F], self.addr, self.registers["CONTROL"])

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
