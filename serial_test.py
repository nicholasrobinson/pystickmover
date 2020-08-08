import serial
import time
# Constants
ENDIAN = 'big'
CENTER_STICKS = '02 05 dc 05 dc 05 dc 05 dc 00 00 00 00 86'

# Convert data
def generate_payload(axis1=1500, axis2=1500, axis3=1500, axis4=1500):
    mode        = b'\x02'
    axis1       += 100
    axis1_bytes = axis1.to_bytes(2, byteorder=ENDIAN)
    axis2_bytes = axis2.to_bytes(2, byteorder=ENDIAN)
    axis3_bytes = axis3.to_bytes(2, byteorder=ENDIAN)
    axis4_bytes = axis4.to_bytes(2, byteorder=ENDIAN)
    fill        = b'\x00\x00\x00\x00'
    partial_payload = mode + axis1_bytes + axis2_bytes + axis3_bytes + axis4_bytes + fill
    check   = (sum(partial_payload) & 0xff).to_bytes(1, byteorder=ENDIAN)
    return partial_payload + check

raw_data_strings = [
      CENTER_STICKS,
      generate_payload().hex(), # Experiment
      CENTER_STICKS,
]
data_strings = [raw_data_string.replace(' ','') for raw_data_string in raw_data_strings]
datas = [bytes.fromhex(data_string) for data_string in data_strings]
# Write data
ser = serial.Serial('/dev/cu.usbserial-DN2VI335', baudrate=57600, timeout=1)
# ser = serial.Serial('/tmp/serial')
for data in datas:
    print('writing', data)
    # byte_array = bytearray(data)
    # checksum = hex(sum(byte_array[:-1]) & 0xff)
    # print('checksum', checksum)
    ser.write(data)
    print('reading', ser.read(1000))
ser.close()