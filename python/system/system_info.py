import sys
import pkg_resources
import importlib
import os
import subprocess
import socket
import glob
from numba import cuda


def get_os():
    """Get OS name as:
    darwin: Mac.
    linux: Linux.
    Win32: Windows.
    Returns:
        version (str): OS name.
    Examples:
        >>> get_os() #doctest: +ELLIPSIS
        '...'

    """
    return sys.platform


def get_machine_name():
    """Get the machine's name
    Returns:
        name (str): Name of the machine
    Examples:
        >>> get_machine_name() #doctest: +ELLIPSIS
        '...'

    """
    return socket.gethostname()


def get_python_version():
    """Get the system's python version.
    Returns:
        version (str): Python version.
    Examples:
        >>> get_python_version() #doctest: +ELLIPSIS
        '...'

    """
    return sys.version


def get_library_version(library_name):
    """Get the version of a library.
    Args:
        library_name (str): Name of the library.
    Returns:
        version (str): Version of the library.
    Examples:
        >>> get_library_version("pandas") #doctest: +ELLIPSIS
        '0.23...'

    """
    try:
        version = pkg_resources.get_distribution(library_name).version
    except Exception:
        pass  # FIXME: better way?
    try:
        lib = importlib.import_module(library_name)
        version = lib.__version__
    except Exception as e:
        print(e)
    return version


def get_number_processors():
    """Get the number of processors in a CPU.
    Returns:
        num (int): Number of processors.
    Examples:
        >>> num = get_number_processors()
        >>> num >= 4
        True

    """
    try:
        num = os.cpu_count()
    except Exception:
        import multiprocessing  # force exception in case mutiprocessing is not installed

        num = multiprocessing.cpu_count()
    return num


def get_java_version():
    """Get java version, vendor, installation files and more information
    Examples:
        >>> get_java_version() # doctest: +SKIP
        java version "1.8.0_151"
        Java(TM) SE Runtime Environment (build 1.8.0_151-b12)
        Java HotSpot(TM) 64-Bit Server VM (build 25.151-b12, mixed mode)

    """
    os.system("java -version")


def get_gpu_name():
    """Get the GPUs in the system.
    Returns:
        result (list): List of strings with the GPU name.
    Examples (non executable):
        $ get_gpu_name()
        ['Tesla M60', 'Tesla M60', 'Tesla M60', 'Tesla M60']
        
    """
    try:
        out_str = subprocess.run(
            ["nvidia-smi", "--query-gpu=gpu_name", "--format=csv"],
            stdout=subprocess.PIPE,
        ).stdout
        out_list = out_str.decode("utf-8").split("\n")
        out_list = out_list[1:-1]
        return out_list
    except Exception as e:
        print(e)


def get_number_gpus():
    """Get the number of GPUs in the system.
    Returns:
        num (int): Number of GPUs.
    Examples (non executable):
        $ get_number_gpus()
        4

    """
    try:
        out_str = subprocess.run(["nvidia-smi", "-L"], stdout=subprocess.PIPE).stdout
        out_list = out_str.decode("utf-8").split("\n")
        return len(out_list) - 1
    except Exception as e:
        print(e)


def get_cuda_version():
    """Get CUDA version
    Returns:
        version (str): Version of the library.
    """
    if sys.platform == "win32":
        raise NotImplementedError("Implement this!")
    elif sys.platform == "linux" or sys.platform == "darwin":
        path = "/usr/local/cuda/version.txt"
        if os.path.isfile(path):
            with open(path, "r") as f:
                data = f.read().replace("\n", "")
            return data
        else:
            return "No CUDA in this machine"
    else:
        raise ValueError("Not in Windows, Linux or Mac")


def get_cudnn_version():
    """Get the CuDNN version
    Returns:
        version (str): Version of the library.
    """

    def find_cudnn_in_headers(candiates):
        for c in candidates:
            file = glob.glob(c)
            if file:
                break
        if file:
            with open(file[0], "r") as f:
                version = ""
                for line in f:
                    if "#define CUDNN_MAJOR" in line:
                        version = line.split()[-1]
                    if "#define CUDNN_MINOR" in line:
                        version += "." + line.split()[-1]
                    if "#define CUDNN_PATCHLEVEL" in line:
                        version += "." + line.split()[-1]
            if version:
                return version
            else:
                return "Cannot find CUDNN version"
        else:
            return "No CUDNN in this machine"

    if sys.platform == "win32":
        candidates = [r"C:\NVIDIA\cuda\include\cudnn.h"]
    elif sys.platform == "linux":
        candidates = [
            "/usr/include/x86_64-linux-gnu/cudnn_v[0-99].h",
            "/usr/local/cuda/include/cudnn.h",
            "/usr/include/cudnn.h",
        ]
    elif sys.platform == "darwin":
        candidates = ["/usr/local/cuda/include/cudnn.h", "/usr/include/cudnn.h"]
    else:
        raise ValueError("Not in Windows, Linux or Mac")
    return find_cudnn_in_headers(candidates)


def is_cuda_available():
    """Check if the system has cuda
    Returns:
        bool: True if cuda is installed, False otherwise.
    Examples:
        >>> is_cuda_available()
        False

    """
    return cuda.is_available()


def get_conda_environment():
    """Get the conda environment from which the script is being executed
    Returns:
        name (str): Environment name
    Examples:
        >>> get_conda_environment()
        'codebase'
        
    """
    return os.environ["CONDA_DEFAULT_ENV"]

