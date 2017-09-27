#Remove recursively all files with a pattern
find . -type f -name '*.db' -delete


#Find a text inside files in a directory.
#-r or -R is recursive,
#-n is line number, and
#-w stands for match the whole word.
grep -rnw '/path/to/somewhere/' -e 'text'
