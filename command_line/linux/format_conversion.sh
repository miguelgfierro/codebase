#!/bin/bash

# Convert from SVG to PDF
inkscape --without-gui --file=foo.svg --export-pdf=foo.pdf

# Convert from PDF to SVG
inkscape --without-gui --file=foo.pdf  --export-plain-svg=foo.svg

# Convert from mp4 to mp3
ffmpeg -i 01.mp4 01.mp3
