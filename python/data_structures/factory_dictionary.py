# Factories are not common in python. A nice way to make factories is through dictionaries.


def factory_example():
    """Example of factory with dictionaries.
    Examples:
        >>> shapes = factory_example()
        >>> shapes.get("circle", default_shape)(2)
        Number of circles: 2
        >>> shapes["square"](5)
        Number of squares: 5
        >>> shapes.get("no_exist", default_shape)(1)
        Number of shapes: 1

    """
    shapes = {
        "circle": lambda x: circle(x),
        "square": lambda x: square(x)
    }
    return shapes

def circle(num):
    print("Number of circles: {}".format(num))

def square(num):
    print("Number of squares: {}".format(num))

def default_shape(num):
    print("Number of shapes: {}".format(num))
