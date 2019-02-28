from abc import ABC, abstractmethod


class AbstractClassExample(ABC):
    """Abstract class example.
    
    Examples:
        >>> c1 = DontDoAnything(1)
        Traceback (most recent call last):
            ...
        TypeError: Can't instantiate abstract class DontDoAnything with abstract methods do_something
        >>> c2 = DoAdd42(2)
        >>> c2.do_something()
        44
        >>> c3 = DoMul42InInit(1)
        >>> c3.value
        42
        >>> c3.do_something()
        42
    """

    def __init__(self, value):
        self.value = value
        super().__init__()

    @abstractmethod
    def do_something(self):
        pass


class DontDoAnything(AbstractClassExample):
    pass


class DoAdd42(AbstractClassExample):
    def do_something(self):
        return self.value + 42


class DoMul42InInit(AbstractClassExample):
    def __init__(self, value):
        super().__init__(value)
        self.value *= 42

    def do_something(self):
        return self.value
