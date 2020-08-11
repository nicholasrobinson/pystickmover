# Python AVIrem StickMover Driver

by Nicholas Robinson

## Overview

This driver allows a control the StickMover training device developed by AVIrem.de.

## Requirements

* python3
* StickMover device

## Installation

    $ pip install pystickmover
    
## Usage

### Simple Example

    $ python
    >>> # Import the library
    >>> import pystickmover
    >>> # Connect to the StickMover device via USB serial
    >>> stickmover = pystickmover.StickMover(serial_port='/dev/ttyUSB0')
    >>> # Set all axis exponential to +50%
    >>> stickmover.axis1_exp = 0.5
    >>> stickmover.axis2_exp = 0.5
    >>> stickmover.axis3_exp = 0.5
    >>> stickmover.axis4_exp = 0.5
    >>> # Set axis 1 to top position
    >>> stickmover.axis1 = 1.0
    >>> # Set all other axes to center position
    >>> stickmover.axis2 = 0.5
    >>> stickmover.axis3 = 0.5
    >>> stickmover.axis4 = 0.5
    >>> # Send the command to the StickMover device
    >>> stickmover.update()

### Sample Code Execution

    $ python pystickmover.py /dev/ttyUSB0
    
### Sample Code Output

    Writing: b'\x02\x03\xe8\x05\xdc\x05\xdc\x07\xd0\x00\x00\x00\x00\x86'
    Reading: b''
    Writing: b'\x02\x03\xf2\x05\xe6\x05\xe6\x07\xd0\x00\x00\x00\x00\xa4'
    Reading: b'\x0022d\xc8\x013'
    Writing: b'\x02\x03\xfc\x05\xf0\x05\xf0\x07\xd0\x00\x00\x00\x00\xc2'
    Reading: b'3d\xcb\x0244d\xce'
    Writing: b'\x02\x04\x06\x05\xfa\x05\xfa\x07\xc6\x00\x00\x00\x00\xd7'
    Reading: b''
    
    (ctrl-c pressed)
    
### Sample Code Output Explanation

The above output indicates the raw output of 4 stick position commands and the resulting responses from the StickMover device.

## References
    
* https://www.avirem.de/

## Notes

* This is a work in progress.

Please let me know if you find this useful or come up with any novel implementations.

Enjoy!

Nicholas Robinson

me@nicholassavilerobinson.com
