def convert_bytes_in_int_lsb(arr, len,sizeInt = 32):
    ret = 0
    pos = sizeInt - 8
    for i in range(0,len):
        ret|=arr[i]<<pos
        pos+=8
    return ret

def convert_bytes_in_int_lsb2(arr, len, sizeInt = 32):
    ret = 0
    pos = sizeInt - 8
    for i in range(0,len):
        ret|=arr[i]<< 8 * i
    return ret
def convert_bytes_in_int_msb(arr, len, sizeInt = 32):
    ret = 0
    pos = sizeInt - 8
    for i in range(0,len):
        ret|=arr[i]<< pos * (len-i)
    return ret


def convert_int_in_hex_string(arr):
    ret = ""
    ret = ret + bytes(arr).hex()
    return ret

def convert_int_in_bytes(i):
    mask = (1<<8) - 1
    return [(i>>k) & mask for k in range(0,32,8)]

print(convert_bytes_in_int_lsb2([43, 242, 73, 97], 4))
