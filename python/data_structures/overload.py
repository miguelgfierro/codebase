# Overloading is a software engineering process whereby multiple
# functions of different types or arguments are defined with the same name.
# Due to dynamic typing overloading is not common in python.
# Generally there are three ways of doing overloading in python:
# optional arguments, multiple dispatch and single dispatch.
#

from functools import singledispatch


def fun_multiple_dispatch(arg, verbose=True):
    """Generic way of overloading a function.
    The standard way to do overloading is using multiple dispatch
    with helper functions.
    Examples:
        >>> fun_multiple_dispatch("Hi!", verbose=True)
        Let me just say, Hi!
        >>> fun_multiple_dispatch(5, verbose=True)
        Strength in numbers, eh? 5
        >>> fun_multiple_dispatch([1,2,3], verbose=True)
        Enumerate this: [1, 2, 3]
        >>> fun_multiple_dispatch(None)
        Traceback (most recent call last):
        ...
        NotImplementedError: Type not implemented
    """
    if isinstance(arg, str):
        return _fun_str(arg, verbose)
    elif isinstance(arg, int):
        return _fun_int(arg, verbose)
    elif isinstance(arg, list):
        return _fun_list(arg, verbose)
    else:
        raise NotImplementedError("Type not implemented")


def _fun_str(arg, verbose=False):
    """Overload of fun_base for argument string"""
    if verbose:
        print("Let me just say,", end=" ")
    print(arg)


def _fun_int(arg, verbose=False):
    """Overload of fun_base for argument int"""
    if verbose:
        print("Strength in numbers, eh?", end=" ")
    print(arg)


def _fun_list(arg, verbose=False):
    """Overload of fun_base for argument list"""
    if verbose:
        print("Enumerate this:", end=" ")
    print(arg)


@singledispatch
def fun_single_dispatch(arg, verbose=False):
    """Single Dispatch Generic Functions.
    A generic function is composed of multiple functions implementing the same operation for different types.
    When the implementation is chosen based on the type of a single argument, this is known as single dispatch.
    source: https://www.python.org/dev/peps/pep-0443/
    Examples:
        >>> fun_single_dispatch("Hi!", verbose=True)
        Let me just say, Hi!
        >>> fun_single_dispatch(5, verbose=True)
        Strength in numbers, eh? 5
        >>> fun_single_dispatch([1,2,3], verbose=True)
        Enumerate this: [1, 2, 3]
        >>> fun_single_dispatch(None)
        Nothing.
        >>> fun_single_dispatch.registry.keys() #To access all registered implementations
        dict_keys([<class 'list'>, <class 'NoneType'>, <class 'int'>, <class 'object'>])

    """
    if verbose:
        print("Let me just say,", end=" ")
    print(arg)


@fun_single_dispatch.register(int)
def _(arg, verbose=False):
    if verbose:
        print("Strength in numbers, eh?", end=" ")
    print(arg)


@fun_single_dispatch.register(list)
def _(arg, verbose=False):
    if verbose:
        print("Enumerate this:", end=" ")
    print(arg)


def nothing(arg, verbose=False):
    print("Nothing.")


# To enable registering lambdas and pre-existing functions, the register() attribute can be used in a functional form:
fun_single_dispatch.register(type(None), nothing)



