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
# source code: http://stackoverflow.com/a/3076636/5620182


class Shape(object):
    def __new__(cls, *args, **kwargs):
        # required because Line's __new__ method is the same as Shape's
        if cls is Shape:
            description, args = args[0], args[1:]
            if description == "It's flat":
                new_cls = Line
            else:
                raise ValueError(
                    "Invalid description: {}.".format(description))
        else:
            new_cls = cls
        return super(Shape, cls).__new__(new_cls, *args, **kwargs)

    def number_of_edges(self):
        return "A shape can have many edges..."


class Line(Shape):
    def number_of_edges(self):
        return 1


class SomeShape(Shape):
    pass


if __name__ == "__main__":

    l1 = Shape("It's flat")
    print(l1.number_of_edges()) # 1

    l2 = Line()
    print(l2.number_of_edges()) # 1

    u = SomeShape()
    print(u.number_of_edges()) # A shape can have many edges...

    s = Shape("Hexagon") # ValueError: Invalid description: Hexagon.
