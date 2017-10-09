# source: https://github.com/keon/algorithms/blob/master/linkedlist/linkedlist.py
# Pros
# Linked Lists have constant-time insertions and deletions in any position,
# in comparison, arrays require O(n) time to do the same thing.
# Linked lists can continue to expand without having to specify
# their size ahead of time (remember our lectures on Array sizing
# form the Array Sequence section of the course!)

# Cons
# To access an element in a linked list, you need to take O(k) time
# to go from the head of the list to the kth element.
# In contrast, arrays have constant time operations to access
# elements in an array.


class DoublyLinkedListNode(object):
    def __init__(self, value=None):
        self.val = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.val)


class SinglyLinkedListNode(object):
    def __init__(self, value=None):
        self.val = value
        self.next = None

    def __str__(self):
        return str(self.val)


class LinkedList(object):
    """Linked list
    Examples:
        >>> a1 = SinglyLinkedListNode("A")
        >>> a2 = SinglyLinkedListNode("A")
        >>> b = SinglyLinkedListNode("B")
        >>> c1 = SinglyLinkedListNode("C")
        >>> d = SinglyLinkedListNode("D")
        >>> c2 = SinglyLinkedListNode("C")
        >>> a1.next = a2
        >>> a2.next = b
        >>> b.next = c1
        >>> c1.next = d
        >>> d.next = c2
        >>> ll = LinkedList(a1)
        >>> print(ll)
        A -> A -> B -> C -> D -> C
        >>> len(ll)
        6
        >>> ll.remove_duplicates()
        >>> ll.to_list()
        ['A', 'B', 'C', 'D']

    """
    def __init__(self, head=None):
        self.head = head

    def __len__(self):
        count = 0
        curr = self.head
        if curr is None: return count
        while curr.next:
            count += 1
            curr = curr.next
        count += 1
        return count

    def __str__(self):
        string = ""
        curr = self.head
        while curr.next:
            string += curr.val + " -> "
            curr = curr.next
        string += curr.val
        return string

    def to_list(self):
        lst = []
        curr = self.head
        while curr.next:
            lst.append(curr.val)
            curr = curr.next
        lst.append(curr.val)
        return lst

    def remove_duplicates(self):
        if self.head is None:
            return
        node = self.head
        seen_data = set()
        while node:
            if node.val not in seen_data:
                seen_data.add(node.val)
                prev = node
                node = node.next
            else:
                prev.next = node.next
                node = node.next



