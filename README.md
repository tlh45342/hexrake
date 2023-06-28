# About

hexrake

Copyright 2003 Thomas Hamilton tlh45342@gmail.com
hexrake is open source.  See the license file for more information

This module is created to perfomr the inverse task of HEXDUMP.
That is, to take a file created with hexdump and re-create the binary file it represents.

## Getting

If wanting to create as a docker image the following command can be used.

```bash
git clone https://github.com/tlh45342/hexrake.git
```

# Installation

To build and install the wheel

```bash
make install
```

# Command line tool

  Excuting the following

```bash
  python -m hexdump binaryfile > output.txt
  python -m hexrake output.txt > binaryfile2
  md5sum binaryfile
  mdfsum binaryfile2
```
 
  The hash values for the two files should be identical
  
# CREDITS
