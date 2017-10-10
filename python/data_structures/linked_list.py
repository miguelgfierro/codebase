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
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)


class SinglyLinkedListNode(object):
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList(object):
    """Linked list
    Examples:
        >>> a1 = SinglyLinkedListNode("1")
        >>> a2 = SinglyLinkedListNode("1")
        >>> b = SinglyLinkedListNode("2")
        >>> c1 = SinglyLinkedListNode("3")
        >>> d = SinglyLinkedListNode("4")
        >>> c2 = SinglyLinkedListNode("3")
        >>> a1.next = a2
        >>> a2.next = b
        >>> b.next = c1
        >>> c1.next = d
        >>> d.next = c2
        >>> ll = LinkedList(a1)
        >>> print(ll)
        1 -> 1 -> 2 -> 3 -> 4 -> 3
        >>> len(ll)
        6
        >>> ll.remove_duplicates()
        >>> ll.to_list()
        ['1', '2', '3', '4']
        >>> reversed(ll)
        >>> print(ll)
        4 -> 3 -> 2 -> 1
        >>> ll.delete_value('2')
        >>> print(ll)
        4 -> 3 -> 1

    """
    def __init__(self, head=None):
        self.head = head

    def __len__(self):
        count = 1
        curr = self.head
        if curr is None: return count
        while curr.next:
            count += 1
            curr = curr.next
        return count

    def __str__(self):
        string = ""
        curr = self.head
        while curr.next:
            string += curr.value + " -> "
            curr = curr.next
        string += curr.value
        return string

    def __reversed__(self):
        current = self.head
        prev = None
        post = None
        while current:
            post = current.next
            current.next = prev
            prev = current
            current = post
        self.head = prev

    def to_list(self):
        lst = []
        curr = self.head
        while curr.next:
            lst.append(curr.value)
            curr = curr.next
        lst.append(curr.value)
        return lst

    def remove_duplicates(self):
        if self.head is None:
            return
        node = self.head
        seen_data = set()
        while node:
            if node.value not in seen_data:
                seen_data.add(node.value)
                prev = node
                node = node.next
            else:
                prev.next = node.next
                node = node.next

    def delete_value(self, value):
        if self.head.value == value:
            self.head = self.head.next
        curr = self.head.next
        prev = self.head
        while curr:
            if curr.value == value:
                prev.next = curr.next
                break
            prev = curr
            curr = curr.next

