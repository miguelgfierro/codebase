#!/bin/bash

#Find a text inside files in a directory.
#-r or -R is recursive,
#-n is line number, and
#-w stands for match the whole word.
grep -rnw '/path/to/somewhere/' -e 'text'


# Extract the version of a python init file
# E.g.: a __init__.py with __version__ = "0.1.5"
# The output of the following command is 0.1.5
awk '/__version__ = / {print $3}' __init__.py | sed 's/"//g'


#Find files modified between dates
find . -newermt 'Oct 3 00:00' ! -newermt 'Oct 4 00:00' -ls


#Count files in a folder recursively
find DIR_NAME -type f | wc -l


#Remove files from a directory leaving a certain number, ex:100
ls -1tr | head -n -100 | xargs -d '\n' rm -f --


#Remove recursively all files with a name
find . -type f -name '.DS_Store' -delete


#Remove recursively all files with a pattern
find . -type f -name '*.db' -delete


#Remove files modified between dates
find . -newermt 'Oct 3 00:00' ! -newermt 'Oct 4 00:00' -delete


# Remove all files and folders except those with a pattern "*.yaml"
find my_folder ! -name "*.yaml" 
find my_folder ! -name "*.yaml" -delete 2>/dev/null  # Ignore warning outputs


