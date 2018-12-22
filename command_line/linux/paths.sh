#!/bin/bash

#Find a text inside files in a directory.
#-r or -R is recursive,
#-n is line number, and
#-w stands for match the whole word.
grep -rnw '/path/to/somewhere/' -e 'text'


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
