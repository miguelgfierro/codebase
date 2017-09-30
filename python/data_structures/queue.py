
class Queue(object):
    """A queue is a linear structure of ordered items where the addition
    of new items and the removal of existing items always takes place at the same end.
    This principle is called FIFO (First In, First Out)
    Examples:
        >>> q = Queue()
        >>> q.is_empty()
        True
        >>> q.enqueue(4)
        >>> q.enqueue('dog')
        >>> print(q)
        ['dog', 4]
        >>> q.size()
        2
        >>> q.dequeue()
        4
        >>> q.size()
        1

    """
    def __init__(self):
        self.items = []

    def __str__(self):
        """Return the string method of the queue as FIFO"""
        return str(list(self.items))

    def is_empty(self):
        """See whether the queue is empty"""
        return self.items == []

    def enqueue(self, item):
        """Add a new item to the queue"""
        self.items.insert(0, item)

    def dequeue(self):
        """Remove the first item in the queue"""
        return self.items.pop()

    def size(self):
        """Return the number of items on the queue"""
        return len(self.items)
