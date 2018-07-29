"""Alias examples
>>> function_with_a_long_name()
1
>>> foo()
1
>>> c1 = ClassWithALongName()
>>> c1.name
'long'
>>> c2 = C()
>>> c2.name
'long'


"""


def function_with_a_long_name():
    return 1


class ClassWithALongName:
    def __init__(self):
        self.name = 'long'

    def method_with_a_long_name(self):
        return 2


# alias of a function
foo = function_with_a_long_name

# alias of a class
C = ClassWithALongName
