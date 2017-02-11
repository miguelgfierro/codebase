#from http://stackoverflow.com/a/3076636/5620182

class Shape(object):
    def __new__(cls, *args, **kwargs):
        if cls is Shape:                            # <-- required because Line's
            description, args = args[0], args[1:]   #  __new__ method is the
            if description == "It's flat":          #     same as Shape's
                new_cls = Line
            else:
                raise ValueError("Invalid description: {}.".format(description))
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
    print(l1.number_of_edges())

    l2 = Line()
    print(l2.number_of_edges())

    u = SomeShape()
    print(u.number_of_edges())

    s = Shape("Hexagon")
