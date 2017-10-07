

class BinaryTree:
    """A Binary Tree is a tree data structure in which each node has at most two children. It can be used to implement
    binary search trees and binary heaps, and are used for efficient searching and sorting.
    Examples:
        >>> r = BinaryTree('a')
        >>> r.get_root_val()
        'a'
        >>> r.get_left_child()

        >>> r.insert_left('b')
        >>> isinstance(r.get_left_child(), BinaryTree)
        True
        >>> r.get_left_child().get_root_val()
        'b'
        >>> r.insert_right('c')
        >>> isinstance(r.get_right_child(), BinaryTree)
        True
        >>> r.get_right_child().get_root_val()
        'c'
        >>> r.get_right_child().set_root_val('hello')
        >>> r.get_right_child().get_root_val()
        'hello'

    """
    def __init__(self, root_obj):
        self.key = root_obj
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if self.left_child is None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, new_node):
        if self.right_child is None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self,obj):
        self.key = obj

    def get_root_val(self):
        return self.key


