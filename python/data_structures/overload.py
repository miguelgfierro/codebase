# Overloading is a software engineering process whereby multiple
# functions of different types or arguments are defined with the same name.
# Due to dynamic typing overloading is not common in python.
# In programming languages that defer data type identification until run-time
# the selection among alternative functions must occur at run-time, based on
# the dynamically determined types of function arguments. Functions whose
# alternative implementations are selected in this manner are referred
# to most generally as multimethods (also multiple dispatch).
# Generally there are three ways of doing overloading in python:
# optional arguments, multiple dispatch and single dispatch.
#

from functools import singledispatch


def fun_optional_arguments(arg1=None, arg2=None, arg3=None, verbose=True):
    """Example of function overload with optional arguments.
    Examples:
        >>> fun_optional_arguments(arg1="Hi!", verbose=True)
        Let me just say, Hi!
        >>> fun_optional_arguments(arg2=5, verbose=True)
        Strength in numbers, eh? 5
        >>> fun_optional_arguments(arg3=[1,2,3], verbose=True)
        Enumerate this: [1, 2, 3]

    """
    if arg1 is not None:
        if verbose:
            print("Let me just say,", end=" ")
        print(arg1)
    if arg2 is not None:
        if verbose:
            print("Strength in numbers, eh?", end=" ")
        print(arg2)
    if arg3 is not None:
        if verbose:
            print("Enumerate this:", end=" ")
        print(arg3)


def fun_multiple_dispatch(arg, verbose=False):
    """Example of function overloading using multiple dispatch (also called
    multimethods), it requires the use of helper functions.
    More info: http://matthewrocklin.com/blog/work/2014/02/25/Multiple-Dispatch
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
    """Overload of fun_multiple_dispatch for argument string"""
    if verbose:
        print("Let me just say,", end=" ")
    print(arg)


def _fun_int(arg, verbose=False):
    """Overload of fun_multiple_dispatch for argument int"""
    if verbose:
        print("Strength in numbers, eh?", end=" ")
    print(arg)


def _fun_list(arg, verbose=False):
    """Overload of fun_multiple_dispatch for argument list"""
    if verbose:
        print("Enumerate this:", end=" ")
    print(arg)


@singledispatch
def fun_single_dispatch(arg, verbose=False):
    """Overloading using single dispatch generic functions.
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
        >>> keys = fun_single_dispatch.registry.keys()  # To access all registered implementations
        >>> print(list(keys)) # doctest: +SKIP
        [<class 'list'>, <class 'object'>, <class 'int'>, <class 'NoneType'>]

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

