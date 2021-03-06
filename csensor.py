class Sensor(object):
    most_recent = {} # a dict of the most recent sensor values
    units = [] # a list of acceptable units for this sensor
    name = "" # this sensors name
    sensors = {}  # static dict of all sensor-type objects

    def __init__(self, name):
        self.name = name
        Sensor.sensors[name] = self

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
        Return a string with the most recent values and the name of the sensor.
        """
        return "{}: {}".format(self.name, self.get(*args))
