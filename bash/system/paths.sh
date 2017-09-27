#Remove recursively all files with a pattern
find . -type f -name '*.db' -delete


#Find a text inside files in a directory.
#-r or -R is recursive,
#-n is line number, and
#-w stands for match the whole word.
grep -rnw '/path/to/somewhere/' -e 'text'

#Remove files from a directory leaving a certain number, ex:100
ls -1tr | head -n -100 | xargs -d '\n' rm -f --
