
class Stack(object):
    """A Stack is a linear structure of ordered items where  the addition
    of new items and the removal of existing items always takes place at the same end.
    This principle is called LIFO (Last In, First Out)
    Examples:
        >>> s = Stack()
        >>> s.is_empty()
        True
        >>> s.push(4)
        >>> s.push('dog')
        >>> print(s)
        ['dog', 4]
        >>> s.peek()
        'dog'
        >>> s.size()
        2
        >>> s.pop()
        'dog'
        >>> s.size()
        1

    """
    def __init__(self):
        self.items = []

    def __iter__(self):
        """Return the stack as LIFO"""
        return reversed(self.items)

    def __str__(self):
        """Return the string method of the stack as LIFO"""
        return str(list(iter(self)))

    def is_empty(self):
        """See whether the stack is empty"""
        return self.items == []

    def push(self, item):
        """Add a new item to the top of the stack"""
        self.items.append(item)

    def pop(self):
        """Remove the top item from the stack"""
        return self.items.pop()

    def peek(self):
        """Return the top item from the stack but does not remove it"""
        return self.items[-1]

    def size(self):
        """Return the number of items on the stack"""
        return len(self.items)
