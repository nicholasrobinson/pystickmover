import serial

class StickMover:
    AXIS_MIN_OUTPUT     = 1000
    AXIS_MAX_OUTPUT     = 2000
    AXIS_BYTES          = 2
    AXIS_MIN_INPUT      = 0.0
    AXIS_MAX_INPUT      = 1.0
    AXIS_CENTER_INPUT   = 0.5
    CHECKSUM_BYTES      = 1
    RX_BYTES            = 100
    ENDIANNESS          = 'big'
    BAUD_RATE           = 57600
    ACK_TIMEOUT         = 0.01

    @staticmethod
    def sanitize_axis(axis_input):
        axis_output = axis_input * (StickMover.AXIS_MAX_OUTPUT - StickMover.AXIS_MIN_OUTPUT) + StickMover.AXIS_MIN_OUTPUT
        if axis_output > StickMover.AXIS_MAX_OUTPUT:
            return StickMover.AXIS_MAX_OUTPUT
        elif axis_output < StickMover.AXIS_MIN_OUTPUT:
            return StickMover.AXIS_MIN_OUTPUT
        else:
            return int(axis_output)

    @staticmethod
    def generate_payload(axis1_input=0.5, axis2_input=0.5, axis3_input=0.5, axis4_input=0.5):
        mode_bytes      = b'\x02'
        axis1_bytes     = StickMover.sanitize_axis(axis1_input).to_bytes(StickMover.AXIS_BYTES, byteorder=StickMover.ENDIANNESS)
        axis2_bytes     = StickMover.sanitize_axis(axis2_input).to_bytes(StickMover.AXIS_BYTES, byteorder=StickMover.ENDIANNESS)
        axis3_bytes     = StickMover.sanitize_axis(axis3_input).to_bytes(StickMover.AXIS_BYTES, byteorder=StickMover.ENDIANNESS)
        axis4_bytes     = StickMover.sanitize_axis(axis4_input).to_bytes(StickMover.AXIS_BYTES, byteorder=StickMover.ENDIANNESS)
        fill_bytes      = b'\x00\x00\x00\x00'
        partial_payload = mode_bytes + axis1_bytes + axis2_bytes + axis3_bytes + axis4_bytes + fill_bytes
        check_bytes     = (sum(partial_payload) & 0xff).to_bytes(StickMover.CHECKSUM_BYTES, byteorder=StickMover.ENDIANNESS)
        return partial_payload + check_bytes

    def __init__(self, serial_port, debug=False):
        self.serial_connection = serial.Serial(serial_port, baudrate=StickMover.BAUD_RATE, timeout=StickMover.ACK_TIMEOUT)
        self.axis1 = StickMover.AXIS_CENTER_INPUT
        self.axis2 = StickMover.AXIS_CENTER_INPUT
        self.axis3 = StickMover.AXIS_CENTER_INPUT
        self.axis4 = StickMover.AXIS_CENTER_INPUT
        self.debug = debug

    def __del__(self):
        self.serial_connection.close()

    def update(self):
        payload = StickMover.generate_payload(self.axis1, self.axis2, self.axis3, self.axis4)
        if self.debug:
            print('Writing:', payload)
        self.serial_connection.write(payload)
        repsonse = self.serial_connection.read(StickMover.RX_BYTES)
        if self.debug:
            print('Reading:', repsonse)

if __name__ == "__main__":
    try:
        stickmover = StickMover('/dev/cu.usbserial-DN2VI335', True)
        stickmover.axis1 = 0.0
        stickmover.axis2 = 0.5
        stickmover.axis3 = 0.5
        stickmover.axis4 = 1.0
        axis1_step = 0.01
        axis2_step = 0.01
        axis3_step = 0.01
        axis4_step = 0.01
        while True:
            stickmover.update()
            if stickmover.axis1 > StickMover.AXIS_MAX_INPUT or stickmover.axis1 < StickMover.AXIS_MIN_INPUT:
                axis1_step *= -1.0
            if stickmover.axis2 > StickMover.AXIS_MAX_INPUT or stickmover.axis2 < StickMover.AXIS_MIN_INPUT:
                axis2_step *= -1.0
            if stickmover.axis3 > StickMover.AXIS_MAX_INPUT or stickmover.axis3 < StickMover.AXIS_MIN_INPUT:
                axis3_step *= -1.0
            if stickmover.axis4 > StickMover.AXIS_MAX_INPUT or stickmover.axis4 < StickMover.AXIS_MIN_INPUT:
                axis4_step *= -1.0
            stickmover.axis1 += axis1_step
            stickmover.axis2 += axis2_step
            stickmover.axis3 += axis3_step
            stickmover.axis4 += axis4_step
    except KeyboardInterrupt:
        pass
    