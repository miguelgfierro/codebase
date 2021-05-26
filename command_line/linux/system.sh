#!/bin/bash

# System release (LSB=Linux Standard Base)
lsb_release -a

# Machine name, kernel name, version
uname -a

# Lists all PCI buses and devices connected to them
lspci

# Lists all USB buses and any connected USB devices
lsusb

# Lists detailed information of the hardware, like motherboard,
# CPU, BIOS, memory, buses and network
lshw

# Returns the current public IP
curl ifconfig.me

# Print all environment variables
printenv

# Check whether I'm using bash, sh or other
echo $SHELL
