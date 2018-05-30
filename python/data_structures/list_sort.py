# source: http://interactivepython.org/runestone/static/pythonds/index.html


def bubble_sort(alist, quick_impl=True):
    """Bubble sort. It compares adjacent items and exchanges them if they are
    out of order. Each pass through the list places the largest value in its
    proper place. In essence, each item “bubbles” up to the location where it
    belongs.
    Time complexity: O(n^2), space complexity: O(1)
    Args:
        alist (list): A list.
        quick_impl (bool): Since bubble sort iterates through the entire list,
                           sort can be modified to stop early if it finds that
                           the list is sorted
    Examples:
        >>> alist = [54,26,93,17,77,31]
        >>> bubble_sort(alist)
        >>> alist
        [17, 26, 31, 54, 77, 93]

    """
    # standard implementation
    if not quick_impl:
        for passnum in range(len(alist)-1, 0, -1):
            for i in range(passnum):
                if alist[i] > alist[i+1]:
                    temp = alist[i]
                    alist[i] = alist[i+1]
                    alist[i+1] = temp
    # quick implementation, stops earlier if list sorted
    else:
        exchanges = True
        passnum = len(alist)-1
        while passnum > 0 and exchanges:
            exchanges = False
            for i in range(passnum):
                if alist[i] > alist[i+1]:
                    exchanges = True
                    temp = alist[i]
                    alist[i] = alist[i+1]
                    alist[i+1] = temp
            passnum = passnum-1


def selection_sort(alist):
    """Selection sort. It looks for the largest value and, after completing
    the pass, places it in the proper location. As with a bubble sort, after
    the first pass, the largest item is in the correct place.
    Time complexity: O(n^2), space complexity: O(1)
    Args:
        alist (list): A list.
    Examples:
        >>> alist = [54,26,93,17,77,31]
        >>> selection_sort(alist)
        >>> alist
        [17, 26, 31, 54, 77, 93]

    """
    for fillslot in range(len(alist)-1, 0, -1):
        position_of_max = 0
        for location in range(1, fillslot+1):
            if alist[location] > alist[position_of_max]:
                position_of_max = location
        temp = alist[fillslot]
        alist[fillslot] = alist[position_of_max]
        alist[position_of_max] = temp


def insertion_sort(alist):
    """Insertion sort. It always maintains a sorted sublist in the lower
    positions of the list. Each new item is then “inserted” back into the
    previous sublist such that the sorted sublist is one item larger.
    Time complexity: O(n^2), space complexity: O(1)
    Args:
        alist (list): A list.
    Examples:
        >>> alist = [54,26,93,17,77,31]
        >>> insertion_sort(alist)
        >>> alist
        [17, 26, 31, 54, 77, 93]

    """
    for index in range(1, len(alist)):
        currentvalue = alist[index]
        position = index
        while position > 0 and alist[position-1] > currentvalue:
            alist[position] = alist[position-1]
            position = position - 1
        alist[position] = currentvalue


def merge_sort(alist):
    """Merge sort. Divide and conquer algo that was invented by John von 
    Neumann in 1945. It divides the list in halves recursively and then place
    the smaller items in the list comparing halves. Let's assume that the list
    is splitted in 2 halves, left and right, and that they are sorted. We
    compare the first element of left with the first element of right and
    place the smallest in the list. We can repeat this until both halves are
    finished. To achieve the assumption we have to note that a list of 1
    element is ordered by definition. Merge sort calls itself until the
    initial list is divided to single elements. Python sort algorithm is a
    modified version of merge sort: 
    http://python-textbok.readthedocs.io/en/1.0/Sorting_and_Searching_Algorithms.html#python-s-sorting-algorithm
    Explanation on video: https://www.youtube.com/watch?v=TzeBrDU-JaY
    Time complexity: O(n*log(n)), space complexity: O(n)
    Args:
        alist (list): A list.
    Examples:
        >>> alist = [54,26,93,17,77,31]
        >>> merge_sort(alist)
        >>> alist
        [17, 26, 31, 54, 77, 93]

    """
    if len(alist) > 1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        merge_sort(lefthalf)
        merge_sort(righthalf)
        i = 0  # left half iterator
        j = 0  # right half iterator
        k = 0  # list iterator
        # Find the smaller item of each half and place it in the list
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i+1
            else:
                alist[k] = righthalf[j]
                j = j+1
            k = k+1
        # When right half is finished, sort the left half
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i+1
            k = k+1
        # When left half is finished, sort the right half
        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j+1
            k = k+1


def quick_sort(alist):
    """Quick sort. Divide and conquer algo.
    It finds a pivot and place is in its correct place making all the left
    elements smaller then the pivot and all the right elements bigger than the
    pivot, then the function is called on the sublists.
    Time complexity: O(n*log(n)), space complexity: O(log(n))
    Args:
        alist (list): A list.
    Examples:
        >>> alist = [54,26,93,17,77,31]
        >>> quick_sort(alist)
        >>> alist
        [17, 26, 31, 54, 77, 93]

    """
    def _quick_sort_helper(alist, first, last):
        if first < last:
            splitpoint = _partition(alist, first, last)
            _quick_sort_helper(alist, first, splitpoint-1)
            _quick_sort_helper(alist, splitpoint+1, last)

    def _partition(alist, first, last):
        pivotvalue = alist[first]

        leftmark = first+1
        rightmark = last

        done = False
        while not done:

            while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
                leftmark = leftmark + 1

            while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
                rightmark = rightmark - 1

            if rightmark < leftmark:
                done = True
            else:
                temp = alist[leftmark]
                alist[leftmark] = alist[rightmark]
                alist[rightmark] = temp
        temp = alist[first]
        alist[first] = alist[rightmark]
        alist[rightmark] = temp
        return rightmark

    _quick_sort_helper(alist, 0, len(alist)-1)
