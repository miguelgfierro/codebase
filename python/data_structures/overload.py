from functools import singledispatch


@singledispatch
def fun(arg, verbose=False):
    """Single Dispatch Generic Functions.
    A generic function is composed of multiple functions implementing the same operation for different types.
    When the implementation is chosen based on the type of a single argument, this is known as single dispatch.
    source: https://www.python.org/dev/peps/pep-0443/
    Examples:
        >>> fun("Hi!", verbose=True)
        Let me just say, Hi!
        >>> fun(5, verbose=True)
        Strength in numbers, eh? 5
        >>> fun([1,2,3], verbose=True)
        Enumerate this: [1, 2, 3]

    """
    if verbose:
        print("Let me just say,", end=" ")
    print(arg)


@fun.register(int)
def _(arg, verbose=False):
    if verbose:
        print("Strength in numbers, eh?", end=" ")
    print(arg)


@fun.register(list)
def _(arg, verbose=False):
    if verbose:
        print("Enumerate this:", end=" ")
    print(arg)



