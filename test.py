import Sensors
def convert_bytes_in_int_lsb(arr, len):
    ret = 0
    pos = 0
    for i in range(0,len):
        ret|=arr[i]<<pos
        pos+=8
    return ret

def convert_bytes_in_int_msb(arr, len):
    ret = 0
    pos = 24
    for i in range(0,len):
        ret|=arr[i]<<pos
        pos-=8
    return ret

def convert_int_in_hex_string(arr):
    ret = ""
    ret = ret + bytes(arr).hex()
    return ret

int_values = [170, 170, 187, 187, 13, 0, 103, 1, 234, 0]

new_row = [0, 0, 0, 0, 0]
new_row[0] = convert_int_in_hex_string(int_values[0:4])
new_row[1] = convert_bytes_in_int_lsb(int_values[4:], 2)
new_row[2] = Sensors.SENSOR_TYPES(int_values[6]) #Type
new_row[3] = int_values[7] #Channel
new_row[4] = convert_bytes_in_int_lsb(int_values[8:],Sensors.get_value_size(new_row[2])) 

#print(new_row[2],Sensors.get_value_size(new_row[2]))
print(new_row)