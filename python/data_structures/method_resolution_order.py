# Method Resulution Order (MRO), also called C3 Superclass linearization, is an algorithm
# used to obtain the order in which methods should be inherited (the "linearization") in
# the presence of multiple inheritance.
# source: https://rhettinger.wordpress.com/2011/05/26/super-considered-super/
#

import logging
from collections import Counter, OrderedDict

logging.basicConfig(level="INFO")


class LoggingDict(dict):
    """This class has all the same capabilities as its parent, dict, but it
    extends the __setitem__ method to make log entries whenever a key is updated.
    
    Examples:
        >>> ld = LoggingDict([('red', 1), ('green', 2), ('blue', 3)])
        >>> ld.items() == {'blue': 3, 'green': 2, 'red': 1}.items()
        True
        >>> ld['red'] = 10 # logs: INFO:root:Setting 'red' to 10
        >>> LoggingDict.__mro__
        (<class 'python.data_structures.method_resolution_order.LoggingDict'>, <class 'dict'>, <class 'object'>)
    """

    def __setitem__(self, key, value):
        logging.info("Setting %r to %r" % (key, value))
        super().__setitem__(key, value)


class LoggingOD(LoggingDict, OrderedDict):
    """Build new functionality by reordering the MRO.
    The ancestor tree for our new class is: LoggingOD, LoggingDict, OrderedDict, dict, object. The result is
    that OrderedDict was inserted after LoggingDict and before dict! This means that the super() call
    in LoggingDict.__setitem__ now dispatches the key/value update to OrderedDict instead of dict.
    We did not alter the source code for LoggingDict. Instead we built a subclass whose only logic is to compose
    two existing classes and control their search order.
    
    Examples:
        >>> ld = LoggingOD([('red', 1), ('green', 2), ('blue', 3)])
        >>> ld
        LoggingOD([('red', 1), ('green', 2), ('blue', 3)])
        >>> ld['red'] = 10 # logs: INFO:root:Setting 'red' to 10
        >>> LoggingOD.__mro__
        (<class 'python.data_structures.method_resolution_order.LoggingOD'>, <class 'python.data_structures.method_resolution_order.LoggingDict'>, <class 'collections.OrderedDict'>, <class 'dict'>, <class 'object'>)
    """

    pass


class Root:
    """Root.draw can also employ defensive programming using an assertion to ensure it
    isn’t masking some other draw() method later in the chain.  This could happen if a
    subclass erroneously incorporates a class that has a draw() method but doesn’t inherit from Root.
    """

    def draw(self):
        # the delegation chain stops here
        assert not hasattr(super(), "draw")


class Shape(Root):
    """Getting the argument signatures to match"""

    def __init__(self, shapename, **kwds):
        self.shapename = shapename
        super().__init__(**kwds)

    def draw(self):
        print("Drawing.  Setting shape to:", self.shapename)
        super().draw()


class ColoredShape(Shape):
    """Getting the argument signatures to match
    
    Examples:
        >>> ColoredShape(color='blue', shapename='square').draw()
        Drawing.  Setting color to: blue
        Drawing.  Setting shape to: square

    """

    def __init__(self, color, **kwds):
        self.color = color
        super().__init__(**kwds)

    def draw(self):
        print("Drawing.  Setting color to:", self.color)
        super().draw()


class Moveable:
    """Occasionally, a subclass may want to use cooperative multiple
    inheritance techniques with a third-party class that wasn’t designed for
    it (perhaps its method of interest doesn’t use super() or perhaps the class
    doesn’t inherit from the root class). This situation is easily remedied
    by creating an adapter class that plays by the rules.
    """

    def __init__(self, x, y):
        """non-cooperative class that doesn't use super()"""
        self.x = x
        self.y = y

    def draw(self):
        print("Drawing at position:", self.x, self.y)


class MoveableAdapter(Root):
    """Show how to incorporate a non-cooperative class"""

    def __init__(self, *, x, y, **kwds):
        """make a cooperative adapter class for Moveable"""
        self.moveable = Moveable(x, y)
        super().__init__(**kwds)

    def draw(self):
        self.moveable.draw()
        super().draw()


class MovableColoredShape(ColoredShape, MoveableAdapter):
    """Mixing all together
    
    Examples:
        >>> MovableColoredShape(color='red', shapename='triangle', x=10, y=20).draw()
        Drawing.  Setting color to: red
        Drawing.  Setting shape to: triangle
        Drawing at position: 10 20
    """

    pass


class OrderedCounter(Counter, OrderedDict):
    """Counter that remembers the order elements are first encountered
    
    Examples:
        >>> OrderedCounter('abracadabra')
        OrderedCounter(OrderedDict([('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]))
    """

    def __repr__(self):
        return "%s(%r)" % (self.__class__.__name__, OrderedDict(self))

    def __reduce__(self):
        return self.__class__, (OrderedDict(self),)

