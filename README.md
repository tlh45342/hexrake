# About

hexrake

Copyright 2003 Thaomas Hamilton tlh45342@gmail.com
hexrake is open source.  See the license file for more information

This module is created to perfomr the inverse task of HEXDUMP.
That is, to take a file created with hexdump and re-create the binary file it represents.

# Installation

To build and install the wheel

```bash
make install
```


# Example usage


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
