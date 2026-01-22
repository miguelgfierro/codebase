# Execute a python file on a conda environment

```bash
conda run -n env_name my_python_file.py
```

## Search a package

```bash
conda search -f cudatoolkit
conda search -f cudatoolkit -c conda-forge
conda search -f cudatoolkit -c numba
```

## Remove unused and cached packages

```bash
conda clean --all
```