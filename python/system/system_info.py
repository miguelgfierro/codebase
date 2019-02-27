import sys
import pkg_resources
import importlib
import os
import subprocess
import socket
import glob
import numpy as np
from psutil import virtual_memory
from numba import cuda
from numba.cuda.cudadrv.error import CudaSupportError


def get_os():
    """Get OS name as:
    darwin: Mac.
    linux: Linux.
    Win32: Windows.
    
    Returns:
        str: OS name.
    
    Examples:
        >>> get_os() #doctest: +ELLIPSIS
        '...'

    """
    return sys.platform


def get_machine_name():
    """Get the machine's name
    
    Returns:
        str: Name of the machine
    
    Examples:
        >>> get_machine_name() #doctest: +ELLIPSIS
        '...'
    
    """
    return socket.gethostname()


def get_python_version():
    """Get the system's python version.
    
    Returns:
        str: Python version.
    
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
        str: Version of the library.
    
    Examples:
        >>> get_library_version("pandas") #doctest: +ELLIPSIS
        '0.2...'
    
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
        int: Number of processors.
    
    Examples:
        >>> num = get_number_processors()
        >>> num >= 2
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
    """Get the GPU names in the system.
    
    Returns:
        list: List of strings with the GPU name.
    
    Examples:
        >>> get_gpu_name()
        []  
    
    """
    try:
        return [gpu.name.decode("utf-8") for gpu in cuda.gpus]
    except CudaSupportError:
        return []


def get_blas_version():
    """Shows BLAS version of MKL, OpenBLAS, ATLAS and LAPACK libraries.
    
    Returns:
        str: BLAS info.
    
    Examples:
        $ get_blas_version() 
        openblas_info:
            library_dirs = ['/home/travis/miniconda/envs/codebase/lib']
            language = c
            define_macros = [('HAVE_CBLAS', None)]
            libraries = ['openblas', 'openblas']
        openblas_lapack_info:
            library_dirs = ['/home/travis/miniconda/envs/codebase/lib']
            language = c
            define_macros = [('HAVE_CBLAS', None)]
            libraries = ['openblas', 'openblas']
        blis_info:
        NOT AVAILABLE
        lapack_mkl_info:
        NOT AVAILABLE
        lapack_opt_info:
            library_dirs = ['/home/travis/miniconda/envs/codebase/lib']
            language = c
            define_macros = [('HAVE_CBLAS', None)]
            libraries = ['openblas', 'openblas']
        blas_opt_info:
            library_dirs = ['/home/travis/miniconda/envs/codebase/lib']
            language = c
            define_macros = [('HAVE_CBLAS', None)]
            libraries = ['openblas', 'openblas']
        blas_mkl_info:
        NOT AVAILABLE
    
    """
    return np.__config__.show()


def get_number_gpus():
    """Get the number of GPUs in the system.
    
    Returns:
        int: Number of GPUs.
    
    Examples:
        >>> get_number_gpus()
        0
   
    """
    try:
        return len(cuda.gpus)
    except CudaSupportError:
        return 0


def get_gpu_compute_capability():
    """Get the GPUs compute capability.
    
    Returns:
        list: List of tuples (major, minor) indicating the supported compute capability.
    
    Examples:
        >>> get_gpu_compute_capability()
        []    
    
    """
    try:
        return [gpu.compute_capability for gpu in cuda.gpus]
    except CudaSupportError:
        return []


def get_cuda_version():
    """Get CUDA version
    
    Returns:
        str: Version of the library.
    
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
        str: Version of the library.
    
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
        str: Environment name
    
    Examples:
        >>> get_conda_environment()
        'codebase'    
    
    """
    return os.environ["CONDA_DEFAULT_ENV"]

