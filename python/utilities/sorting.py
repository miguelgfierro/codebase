#source: http://interactivepython.org/runestone/static/pythonds/index.html


def bubble_sort(alist, quick_impl=True):
    """Bubble sort. It compares adjacent items and exchanges them if they are out of order. Each pass through
    the list places the largest value in its proper place. In essence, each item “bubbles” up to the location where it belongs.
    Time complexity: O(n^2), space complexity: O(1)
    Parameters:
        alist (list): A list.
        quick_impl (bool): Since bubble sort iterates through the entire list, sort can be modified to stop early
                           if it finds that the list is sorted
    Examples:
        >>> alist = [54,26,93,17,77,31]
        >>> bubble_sort(alist)
        >>> alist
        [17, 26, 31, 54, 77, 93]

    """
    #standard implementation
    if not quick_impl:
        for passnum in range(len(alist)-1,0,-1):
            for i in range(passnum):
                if alist[i] > alist[i+1]:
                    temp = alist[i]
                    alist[i] = alist[i+1]
                    alist[i+1] = temp
    #quick implementation, stops earlier if list sorted
    else:
        exchanges = True
        passnum = len(alist)-1
        while passnum > 0 and exchanges:
           exchanges = False
           for i in range(passnum):
               if alist[i]>alist[i+1]:
                   exchanges = True
                   temp = alist[i]
                   alist[i] = alist[i+1]
                   alist[i+1] = temp
           passnum = passnum-1


def selection_sort(alist):
    """Selection sort. It looks for the largest value and, after completing the pass, places it in the proper location.
    As with a bubble sort, after the first pass, the largest item is in the correct place.
    Time complexity: O(n^2), space complexity: O(1)
    Parameters:
        alist (list): A list.
    Examples:
        >>> alist = [54,26,93,17,77,31]
        >>> selection_sort(alist)
        >>> alist
        [17, 26, 31, 54, 77, 93]

    """
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax=0
        for location in range(1,fillslot+1):
            if alist[location]>alist[positionOfMax]:
                positionOfMax = location
        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp


def insertion_sort(alist):
    """Insertion sort. It always maintains a sorted sublist in the lower positions of the list. Each new item is
    then “inserted” back into the previous sublist such that the sorted sublist is one item larger.
    Time complexity: O(n^2), space complexity: O(1)
    Parameters:
        alist (list): A list.
    Examples:
        >>> alist = [54,26,93,17,77,31]
        >>> insertion_sort(alist)
        >>> alist
        [17, 26, 31, 54, 77, 93]

    """
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index
        while position > 0 and alist[position-1] > currentvalue:
            alist[position] = alist[position-1]
            position = position-1
        alist[position] = currentvalue