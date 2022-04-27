""" Sort algorithms module

This module contains all the sort algorithms seen during the ToC course

Functions:
    Quick sort: Sort an array of number, letters, and objects using the 
    quick sort strategy.
    Bubble sort: Sort an array of number, letters, and objects using the
    buble sort strategy

"""


def quick_sort(unsorted_list : list) -> list:
    """Sort a list of numbers, letters, and objects using the brute force
    strategy called Quick sort

    This method identify the list's values types and sorted

    Parameters
    ----------
    A : list
        A is list with the elements to be sorted

    Returns
    ---------
    list
        a list of sorted values or objects
        
    """
    list_length = len(unsorted_list)
    for i in range(list_length - 1):
        minimum = i
        for j in range(i + 1, list_length):
            if unsorted_list[j] < unsorted_list[minimum]:
                minimum = j
        temp = unsorted_list[i]
        unsorted_list[i] = unsorted_list[minimum]
        unsorted_list[minimum] = temp



def bubble_sort():
    """
    """
    pass

