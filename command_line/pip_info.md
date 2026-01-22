# Tools for pip packages

# Create an environment named py36 inside folder env
python -m venv env\py36

# Create an environment named py36 inside folder env with a particular python version (Linux)
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.6 python3-virtualenv
virtualenv env/py36 -p /usr/bin/python3.6

# Activate environment py36 (Windows)
.\env\py36\Scripts\activate 

# Activate environment py36 (Linux)
source env/py36/bin/activate

# List all installed packages ordered by size
# Source: https://stackoverflow.com/a/51571259/5620182
pip list --format freeze|awk -F = {'print $1'}| xargs pip show | grep -E 'Location:|Name:' | cut -d ' ' -f 2 | paste -d ' ' - - | awk '{print $2 "/" tolower($1)}' | xargs du -sh 2> /dev/null|sort -h

# List the dependencies of a python library
pipdeptree -p library_name

# Print a dependency graph (requires the instalation of http://www.graphviz.org/
pip install graphviz
pipdeptree -p library_name --graph-output svg > dependencies.svg

# Uninstall libraries based on a pattern
pip uninstall -y $(pip list | grep pattern | awk '{print $1}')
