import sys
import pkg_resources


def get_python_version():
    return sys.version


def get_library_version(library_name):
    return pkg_resources.get_distribution(library_name).version


if __name__ == "__main__":

    print(get_python_version())

    print(get_library_version("pandas"))

