#!/bin/bash

# Check size
du -sh /home
du -sh /

# Clean unused libraries in conda
conda clean -a

# Review conda environments
conda env list
conda env remove -n ENV_NAME

# Clean tmp files
rm -rf tmp/*

# Clean unused Ubuntu files
sudo apt-get clean
sudo apt-get autoremove
sudo apt-get autoclean

