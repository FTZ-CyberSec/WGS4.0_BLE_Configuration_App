from util import *

type_digitalIn = 0
type_digitalOut = 1
type_analog_in = 2
type_analog_out = 3
type_generic = 100
type_illuminance = 101
type_presence = 102
type_temperature = 103
type_humidity = 104
type_accelerometer = 113
type_barometer = 115
type_voltage = 116
type_current = 117
type_frequency = 118
type_percentage = 120
type_altitude = 121
type_concentration = 125
type_power = 128
type_distance = 130
type_energy = 131
type_direction = 132
type_time = 133
type_gyrometer = 134
type_colour = 135
type_gps = 136
type_switch = 142


class WGS_LPP(object):
    def __init__(self, type, name,size,  divisor, channel=0,value=0):
        super().__init__()
        self.name = name
        self.size = size
        self.type = type
        self.value = value
        self.divisor = divisor
        self.channel = channel
        self.value_f = self.value/divisor


all_sensor_types = [WGS_LPP(type_digitalIn, "DigitalIn (Waterlevel)",1, 1.0), WGS_LPP(
    type_temperature, "Temperature",2, 10.0), WGS_LPP(type_generic, "Generic (Message Counter)", 4,1.0), WGS_LPP(type_time, "Time",4, 1.0) ]


def parse_byte_array(arr):
    retWGS_LPP_List = []
    i = 1
    while(i<len(arr)):
        size = 0
        for sensor in all_sensor_types:
            if arr[i] == sensor.type and sensor.size + 1<=len(arr) and arr[i-1]!=0: #Richtiger Typ, nicht zu kurz und Channel ist nicht 0
                size = sensor.size
                retWGS_LPP_List.append(WGS_LPP(sensor.type, sensor.name, sensor.size , sensor.divisor,channel=arr[i-1], value = convert_bytes_in_int_lsb2(arr[i+1:],sensor.size, sizeInt=  sensor.size*8  )))
                break;
        i+= size + 1
    return retWGS_LPP_List



test = parse_byte_array([0x76, 0x64, 0x17, 0x2, 0x0, 0x0, 0x76, 0x85, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0])
for t in test:
    print(t.name, t.value)