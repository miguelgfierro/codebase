
class Deque(object):
    """A deque (double-ended queue) is a linear structure of
    ordered items where the addition and removal of items can
    take place on any end.
    Thus deques can work as FIFO (First In, First Out) or 
    LIFO (Last In, First Out)
    Examples:
        >>> d = Deque()
        >>> d.is_empty()
        True
        >>> d.add_front(4)
        >>> d.add_front('dog')
        >>> print(d)
        [4, 'dog']
        >>> d.size()
        2
        >>> d.remove_front()
        'dog'
        >>> d.add_rear(True)
        >>> print(d)
        [True, 4]
        >>> d.remove_rear()
        True

    """
    def __init__(self):
        self.items = []

    def __str__(self):
        """Return the string method of the deque"""
        return str(list(self.items))

    def is_empty(self):
        """See whether the deque is empty"""
        return self.items == []

    def add_front(self, item):
        """Add an item in the front"""
        self.items.append(item)

    def add_rear(self, item):
        """Add an item in the rear"""
        self.items.insert(0, item)

    def remove_front(self):
        """Remove an item in the front"""
        return self.items.pop()

    def remove_rear(self):
        """Remove an item in the rear"""
        return self.items.pop(0)

    def size(self):
        """Return the number of items on the deque"""
        return len(self.items)
