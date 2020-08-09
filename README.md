# Python AVIrem StickMover Driver

by Nicholas Robinson

## Overview

This driver allows a control the StickMover training device developed by AVIrem.de.

## Requirements

* python3
* StickMover device

## Installation

    $ git clone git://github.com/nicholasrobinson/pystickmover.git
    
## Usage

### Execution

    $ python pystickmover.py
    
### Sample Output

    Writing: b'\x02\x03\xe8\x05\xdc\x05\xdc\x07\xd0\x00\x00\x00\x00\x86'
    Reading: b''
    Writing: b'\x02\x03\xf2\x05\xe6\x05\xe6\x07\xd0\x00\x00\x00\x00\xa4'
    Reading: b'\x0022d\xc8\x013'
    Writing: b'\x02\x03\xfc\x05\xf0\x05\xf0\x07\xd0\x00\x00\x00\x00\xc2'
    Reading: b'3d\xcb\x0244d\xce'
    Writing: b'\x02\x04\x06\x05\xfa\x05\xfa\x07\xc6\x00\x00\x00\x00\xd7'
    Reading: b''
    
    (ctrl-c pressed)
    
### Sample Output Explanation

The above output indicates the raw output of 4 stick position commands and the resulting responses from the StickMover device.

## References
    
* https://www.avirem.de/

## Notes

* This is a work in progress.

Please let me know if you find this useful or come up with any novel implementations.

Enjoy!

Nicholas Robinson

me@nicholassavilerobinson.com
