def function_with_a_long_name():
    """Alias examples with  functions.

    Examples:
        >>> function_with_a_long_name()
        1
        >>> foo()
        1
        >>> FOO()
        1
    """
    return 1


class ClassWithALongName:
    """Alias examples with class name, class method and functions.
    
    Examples:
        >>> c1 = ClassWithALongName()
        >>> c1.x
        17
        >>> c2 = C()
        >>> c2.x, c2.xValue
        (17, 17)
        >>> c2.x = 0
        >>> c2.x, c2.xValue
        (0, 0)
        >>> c1.xValue = 50
        >>> c1.x, c1.xValue
        (50, 50)
        >>> c2.x, c2.xValue  # c1 and c2 are two different instances of the same class
        (0, 0)
    """

    def __init__(self):
        self._x = 17

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, inp):
        self._x = inp

    # Alias of a method
    xValue = x


# Alias of a function
foo = FOO = function_with_a_long_name

# Alias of a class
C = ClassWithALongName
