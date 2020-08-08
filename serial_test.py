import serial
import time

# Constants
ENDIAN = 'big'
RX_BYTE_LENGTH = 100
AXIS_MIN = 1000
AXIS_MAX = 2000

def sanitize_input(axis):
    axis_output = axis * (AXIS_MAX - AXIS_MIN) + AXIS_MIN
    if axis_output > AXIS_MAX:
        return AXIS_MAX
    elif axis_output < AXIS_MIN:
        return AXIS_MIN
    else:
        return int(axis_output)

# Convert data
def generate_payload(axis1=0.5, axis2=0.5, axis3=0.5, axis4=0.5):
    axis1_output    = sanitize_input(axis1)
    axis2_output    = sanitize_input(axis2)
    axis3_output    = sanitize_input(axis3)
    axis4_output    = sanitize_input(axis4)
    mode            = b'\x02'
    axis1_bytes     = axis1_output.to_bytes(2, byteorder=ENDIAN)
    axis2_bytes     = axis2_output.to_bytes(2, byteorder=ENDIAN)
    axis3_bytes     = axis3_output.to_bytes(2, byteorder=ENDIAN)
    axis4_bytes     = axis4_output.to_bytes(2, byteorder=ENDIAN)
    fill_bytes      = b'\x00\x00\x00\x00'
    partial_payload = mode + axis1_bytes + axis2_bytes + axis3_bytes + axis4_bytes + fill_bytes
    check_bytes     = (sum(partial_payload) & 0xff).to_bytes(1, byteorder=ENDIAN)
    return partial_payload + check_bytes

# Write data
ser = serial.Serial('/dev/cu.usbserial-DN2VI335', baudrate=57600, timeout=0.1)
axis1 = 0.0
axis2 = 0.0
axis3 = 0.0
axis4 = 0.0
for i in range(100):
    data = generate_payload(axis1, axis2, axis3, axis4)
    print('writing', axis1, data)
    ser.write(data)
    print('reading', ser.read(RX_BYTE_LENGTH))
    axis1 += 0.01
    axis2 += 0.01
    axis3 += 0.01
    axis4 += 0.01

ser.close()