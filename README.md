# About

hexrake

Copyright 2023 Thomas Hamilton tlh45342@gmail.com
hexrake is open source.  See the license file for more information

This module is created to perform the inverse task of HEXDUMP.
That is, to take a file created with hexdump and re-create the binary file it represents.

## Getting

```bash
git clone https://github.com/tlh45342/hexrake.git
```

# Installation

To build and install the wheel

```bash
make install
```

# Notice:

For Raspberry-pi I might suggest making sure the shim "python-is-python3" is installed.

```bash
apt install python-is-python3
```

# As a command line tool

  Excuting the following

```bash
  python -m hexdump binaryfile > output.txt
  python -m hexrake -f output.txt -o binaryfile2
  md5sum binaryfile
  md5sum binaryfile2
```
 
  The hash values for the two files should be identical
  
# CREDITS

# NOTES

Tom please finish.  Not to self... might include a test harness/directory.
