#!/bin/bash

# Reduce pdf size
# Installation in Linux:
# $ sudo apt install ghostscript

gs -sDEVICE=pdfwrite -o output.pdf input1.pdf input2.pdf

