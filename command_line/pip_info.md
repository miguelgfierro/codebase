# Tools for pip packages

## Create an environment named py311 inside folder env

```bash
python -m venv env\py11
```

## Create an environment named py311 inside folder env with a particular python version (Linux)

```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.11 python3-virtualenv
virtualenv env/py311 -p /usr/bin/python3.11
```

**Activate environment py311 (Windows)**

```bash
.\env\py311\Scripts\activate 
```

**Activate environment py311 (Linux)**

```bash
source env/py311/bin/activate
```

**List all installed packages ordered by size**

Source: https://stackoverflow.com/a/51571259/5620182

```bash
pip list --format freeze|awk -F = {'print $1'}| xargs pip show | grep -E 'Location:|Name:' | cut -d ' ' -f 2 | paste -d ' ' - - | awk '{print $2 "/" tolower($1)}' | xargs du -sh 2> /dev/null|sort -h
```

# List the dependencies of a python library

```bash
pipdeptree -p library_name
```

# Print a dependency graph (requires the instalation of http://www.graphviz.org/

```bash
pip install graphviz
pipdeptree -p library_name --graph-output svg > dependencies.svg
```

# Uninstall libraries based on a pattern

```bash
pip uninstall -y $(pip list | grep pattern | awk '{print $1}')
```
