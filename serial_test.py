import serial
import time
# Convert data
raw_data_strings = [
    # '02 05 dc 05 dc 05 dc 05 dc 00 00 00 00 86', # Experiment
    '02 05 dc 05 dc 05 dc 05 dc 00 00 00 00 86', # Left/Right sticks:   Center
    '02 03 e8 05 dc 05 dc 05 dc 00 00 00 00 90', # Left stick:          Right
    '02 05 dc 05 dc 05 dc 05 dc 00 00 00 00 86', # Left/Right sticks:   Center
    '02 05 dc 07 d0 05 dc 05 dc 00 00 00 00 7c', # Left stick:          Top
    '02 05 dc 05 dc 05 dc 05 dc 00 00 00 00 86', # Left/Right sticks:   Center
    '02 05 dc 05 dc 03 e8 05 dc 00 00 00 00 90', # Right stick:         Top
    '02 05 dc 05 dc 05 dc 05 dc 00 00 00 00 86', # Left/Right sticks:   Center
    '02 05 dc 05 dc 05 dc 03 e8 00 00 00 00 90', # Right stick:         Right
    '02 05 dc 05 dc 05 dc 05 dc 00 00 00 00 86', # Left/Right sticks:   Center
]
data_strings = [raw_data_string.replace(' ','') for raw_data_string in raw_data_strings]
datas = [bytes.fromhex(data_string) for data_string in data_strings]
# Write data
ser = serial.Serial('/dev/cu.usbserial-DN2VI335', baudrate=57600, timeout=1)
# ser = serial.Serial('/tmp/serial')
for data in datas:
    print('writing', data)
    ser.write(data)
    print('reading', ser.read(1000))
ser.close()