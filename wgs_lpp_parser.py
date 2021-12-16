from util import *

sensor_types = {
    0: {'size': 1, 'name': 'digitalIn', 'signed': False, 'divisor': 1, 'key': 'channel'},
    1: {'size': 1, 'name': 'digitalOut', 'signed': False, 'divisor': 1, 'key': 'channel'},
    2: {'size': 2, 'name': 'analog_in', 'signed': True, 'divisor': 100, 'key': 'channel'},
    3: {'size': 2, 'name': 'analog_out', 'signed': True, 'divisor': 100, 'key': 'channel'},
    100: {'size': 4, 'name': 'generic', 'signed': False, 'divisor': 1, 'key': 'channel'},
    101: {'size': 2, 'name': 'illuminance', 'signed': False, 'divisor': 1, 'key': 'channel'},
    102: {'size': 1, 'name': 'presence', 'signed': False, 'divisor': 1, 'key': 'channel'},
    103: {'size': 2, 'name': 'temperature', 'signed': True, 'divisor': 10, 'key': 'channel'},
    104: {'size': 1, 'name': 'humidity', 'signed': False, 'divisor': 2, 'key': 'channel'},
    113: {'size': 6, 'name': 'accelerometer', 'signed': True, 'divisor': 1000, 'key': 'channel'},
    115: {'size': 2, 'name': 'barometer', 'signed': False, 'divisor': 10, 'key': 'channel'},
    116: {'size': 2, 'name': 'voltage', 'signed': False, 'divisor': 100, 'key': 'channel'},
    117: {'size': 2, 'name': 'current', 'signed': False, 'divisor': 1000, 'key': 'channel'},
    118: {'size': 4, 'name': 'frequency', 'signed': False, 'divisor': 1, 'key': 'channel'},
    120: {'size': 1, 'name': 'percentage', 'signed': False, 'divisor': 1, 'key': 'channel'},
    121: {'size': 2, 'name': 'altitude', 'signed': True, 'divisor': 1, 'key': 'channel'},
    125: {'size': 2, 'name': 'concentration', 'signed': False, 'divisor': 1, 'key': 'channel'},
    128: {'size': 2, 'name': 'power', 'signed': False, 'divisor': 1, 'key': 'channel'},
    130: {'size': 4, 'name': 'distance', 'signed': False, 'divisor': 1000, 'key': 'channel'},
    131: {'size': 4, 'name': 'energy', 'signed': False, 'divisor': 1000, 'key': 'channel'},
    132: {'size': 2, 'name': 'direction', 'signed': False, 'divisor': 1, 'key': 'channel'},
    133: {'size': 4, 'name': 'timestamp', 'signed': False, 'divisor': 1, 'key': 'value'},
    134: {'size': 6, 'name': 'gyrometer', 'signed': True, 'divisor': 100, 'key': 'channel'},
    135: {'size': 3, 'name': 'colour', 'signed': False, 'divisor': 1, 'key': 'channel'},
    136: {'size': 9, 'name': 'gps', 'signed': True, 'divisor': [10000, 10000, 100], 'key': 'channel'},
    142: {'size': 1, 'name': 'switch', 'signed': False, 'divisor': 1, 'key': 'channel'},
    155: {'size': 2, 'name': 'capacity', 'signed': False, 'divisor': 10, 'key': 'channel'},
}


def parse_byte_array(arr):
    ret_wgs_lpp_list = []
    i = 1
    while i < len(arr):
        size = 0
        for sensor in sensor_types:
            if arr[i] == sensor.type and sensor.size + 1 <= len(arr) and arr[i - 1] != 0:
                size = sensor.size
                ret_wgs_lpp_list.append(
                    {
                        "channel": int(arr[0]),
                        "name": "",
                        "type": int(arr[1]),
                        "value": float()
                    })
                break
        i += size + 1
    return ret_wgs_lpp_list


test = parse_byte_array([0x76, 0x64, 0x17, 0x2, 0x0, 0x0, 0x76, 0x85, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0])
