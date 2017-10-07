
class BinaryHeap(object):
    """A Binary Heap is a data structure in form of a binary tree that holds the shape and head property. The
    shape property implies that it is a complete binary tree (all levels are complete except the last ones) and the
    heap property is that for every node x with parent p, the key in p is smaller than or equal to the key in x.
    A Binary Heap is a common method to implement priority queues.
    Timpe complexity:
    search: O(n); insert&delete: O(log(n)); pop: O(1)
    Examples:
        >>> bh = BinaryHeap()
        >>> bh.build([9,5,6,2,3])
        >>> bh.pop()
        2
        >>> bh.pop()
        3
        >>> bh.pop()
        5
        >>> bh.pop()
        6
        >>> bh.pop()
        9

    """
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def swap_up(self,i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                tmp = self.heap_list[i // 2]
                self.heap_list[i // 2] = self.heap_list[i]
                self.heap_list[i] = tmp
            i = i // 2

    def insert(self,k):
        self.heap_list.append(k)
        self.current_size = self.current_size + 1
        self.swap_up(self.current_size)

    def swap_down(self,i):
        while (i * 2) <= self.current_size:
            mc = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                tmp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[mc]
                self.heap_list[mc] = tmp
            i = mc

    def min_child(self,i):
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i*2] < self.heap_list[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def pop(self):
        retval = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size = self.current_size - 1
        self.heap_list.pop()
        self.swap_down(1)
        return retval

    def build(self, alist):
        i = len(alist) // 2
        self.current_size = len(alist)
        self.heap_list = [0] + alist[:]
        while i > 0:
            self.swap_down(i)
            i = i - 1