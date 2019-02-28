# Dependency injection:
# Technique where one object (or static method) supplies the dependencies of another object.
# The objective is to decouple objects to the extent that no client code has to be changed
# simply because an object it depends on needs to be changed to a different one.
# Dependency injection is one form of the broader technique of inversion of control.
# Theoretically, the client is not allowed to call the injector code; it is the injecting code
# that constructs the services and calls the client to inject them. This means the client code
# does not need to know about the injecting code, just the interfaces. This separates the
# responsibilities of use and construction.
# In Python there are not many frameworks for dependency injection: https://stackoverflow.com/questions/2461702/why-is-ioc-di-not-common-in-python
#
# source code: http://python-3-patterns-idioms-test.readthedocs.io/en/latest/Factory.html


class Shape(object):
    """Factory class.
    
    Examples:
        >>> s = Shape.factory("Circle")
        >>> s.draw()
        Circle.draw
        >>> Shape.__subclasses__()
        [<class 'python.data_structures.factory_dependency_injection.Circle'>, <class 'python.data_structures.factory_dependency_injection.Square'>]
    """

    def factory(description):
        if description == "Circle":
            return Circle()
        if description == "Square":
            return Square()
        assert 0, "Bad shape creation: " + description

    factory = staticmethod(factory)


class Circle(Shape):
    def draw(self):
        print("Circle.draw")


class Square(Shape):
    def draw(self):
        print("Square.draw")


class ShapeDict(object):
    """Factory class based on dictionaries.
    
    Examples:
        >>> s = ShapeDict.factory("Square")
        >>> s.draw()
        Square.draw
        >>> Shape.__subclasses__()
        [<class 'python.data_structures.factory_dependency_injection.Circle'>, <class 'python.data_structures.factory_dependency_injection.Square'>]
    """

    def factory(description):
        classDict = {"Circle": Circle(), "Square": Square()}
        return classDict[description]

    factory = staticmethod(factory)

