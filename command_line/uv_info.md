# Tools for uv (Python package manager)

uv is an extremely fast Python package manager written in Rust by Astral (creators of Ruff). It's 10-100x faster than pip/conda.

## Installation

```bash
# macOS / Linux / WSL
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## Create a virtual environment (centralized in ~/.venvs/)

```bash
# Create environment with default Python
uv venv ~/.venvs/myenv

# Create with specific Python version
uv venv ~/.venvs/py311 --python 3.11
uv venv ~/.venvs/py312 --python 3.12

# Examples for specific projects
uv venv ~/.venvs/recommenders --python 3.11

```

## Activate different environments

```bash
# Linux / macOS / WSL
source ~/.venvs/recommenders/bin/activate
source ~/.venvs/ml-project/bin/activate
source ~/.venvs/web-app/bin/activate

# Windows
~\.venvs\recommenders\Scripts\activate
~\.venvs\ml-project\Scripts\activate

# Deactivate current environment
deactivate
```

## List all environments

```bash
# List all environments in ~/.venvs/
ls ~/.venvs/

# Check which environment is active
which python
```

## Install packages

```bash
# Install a package
uv pip install package_name

# Install from requirements.txt
uv pip install -r requirements.txt

# Install with extras
uv pip install "package[extra1,extra2]"

# Install from GitHub
uv pip install "git+https://github.com/org/repo"

# Install from specific branch/tag/commit
uv pip install "git+https://github.com/org/repo@branch"
uv pip install "git+https://github.com/org/repo@v1.0.0"
uv pip install "git+https://github.com/org/repo@abc123"
```

## Install Recommenders repo

```bash
# Create and activate environment
uv venv ~/.venvs/recommenders --python 3.11
source ~/.venvs/recommenders/bin/activate

# Core package
uv pip install recommenders

# With examples support
uv pip install "recommenders[examples]"

# With GPU support (requires CUDA installed separately)
uv pip install "recommenders[examples,gpu]"

# From GitHub main branch
uv pip install "git+https://github.com/microsoft/recommenders"

# From specific branch
uv pip install "git+https://github.com/microsoft/recommenders@staging"
```

## List and manage packages

```bash
# List installed packages
uv pip list

# Show package info
uv pip show package_name

# Uninstall a package
uv pip uninstall package_name

# Freeze requirements
uv pip freeze > requirements.txt
```

## Compile and sync dependencies (lock file workflow)

```bash
# Compile requirements.in to requirements.txt (locked versions)
uv pip compile requirements.in -o requirements.txt

# Sync environment to match requirements exactly
uv pip sync requirements.txt
```

## Cache management

```bash
# Show cache directory
uv cache dir

# Clean cache
uv cache clean

# Clean cache for specific package
uv cache clean package_name
```

## Run Python with uv (without activating env)

```bash
# Run a script
uv run script.py

# Run a module
uv run -m pytest

# Run with specific Python version
uv run --python 3.11 script.py
```

## Project management (pyproject.toml workflow)

```bash
# Initialize a new project
uv init project_name

# Add a dependency
uv add package_name

# Add dev dependency
uv add --dev pytest

# Remove a dependency
uv remove package_name

# Lock dependencies
uv lock

# Sync project dependencies
uv sync
```

## uv vs conda comparison

| Feature | uv | conda |
|---------|-----|-------|
| Speed | 10-100x faster | Slower |
| Non-Python deps | No | Yes (CUDA, cuDNN, etc.) |
| Environment location | Flexible (project-local or centralized) | Centralized |
| Written in | Rust | Python |
| PyPI packages | Yes | Via conda-forge |

**Hybrid approach**: Use conda for CUDA/system deps, then uv inside for Python packages.
