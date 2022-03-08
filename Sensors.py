from enum import Enum


class SENSOR_TYPES(Enum):
    DIGITAL_INPUT = 0
    TEMPERATURE = 103
    ANALOG_INPUT = 2


class Sensor(object):
    def __init__(self, type, valueSize):
        self.type = type
        self.valueSize = valueSize
        self.name = "?"
        self.channel = 0


Sensors = [Sensor(SENSOR_TYPES.DIGITAL_INPUT, 1), Sensor(SENSOR_TYPES.TEMPERATURE, 4), Sensor(SENSOR_TYPES.ANALOG_INPUT, 4)]


def get_value_size(type):
    for s in Sensors:
        if s.type == type:
            return s.valueSize
    return 0


testts = SENSOR_TYPES(103)
testts = SENSOR_TYPES.DIGITAL_INPUT
print(testts)
