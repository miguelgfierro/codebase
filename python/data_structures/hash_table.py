#source: http://interactivepython.org/runestone/static/pythonds/SortSearch/Hashing.html#implementing-the-map-abstract-data-type


class HashTable(object):
    """
    A hash table is a data structure that can map keys to values. The mapping between an item and the slot where
    that item belongs is called the hash function. In practice there can be hash collisions when the hash function
    generates the same index for more than one key. This has to be managed.
    In python hash tables are implemented as `dict`, to solve collisions they use __eq__
    Time complexity: search, insert, delete: O(1)
    Space complexity: O(n)
    Args:
        size (int): Size of the hash table.
    Examples:
        >>> H=HashTable(5)
        >>> H[54]="cat"
        >>> H[26]="dog"
        >>> H[93]="lion"
        >>> H.slots
        [None, 26, None, 93, 54]
        >>> H.data
        [None, 'dog', None, 'lion', 'cat']
        >>> H[26] = 'duck'
        >>> H.data
        [None, 'duck', None, 'lion', 'cat']

    """
    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self,key,data):
        """Add a key and value."""
        hashvalue = self.hashfunction(key,len(self.slots))
        if self.slots[hashvalue] is None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  #replace
            else:
                nextslot = self.rehash(hashvalue,len(self.slots))
                while self.slots[nextslot] is not None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot,len(self.slots))
                if self.slots[nextslot] is None:
                    self.slots[nextslot]=key
                    self.data[nextslot]=data
                else:
                    self.data[nextslot] = data #replace

    def hashfunction(self,key,size):
        """The hash function is a simple remainder method."""
        return key%size

    def rehash(self,oldhash,size):
        """The collision resolution technique is linear probing with a “plus 1” rehash function. Linear probing
        is looking sequentially for the next open slot"""
        return (oldhash+1)%size

    def get(self, key):
        """Return the value of a key."""
        startslot = self.hashfunction(key,len(self.slots))
        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position,len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

