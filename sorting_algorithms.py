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

    This method identify the list's values types and sort them.

    Parameters
    ----------
    A : list
        A is list with the elements to be sorted

    Returns
    ---------
    list
        a list of sorted values or objects
        
    """

    sorted_list = unsorted_list.copy()
    sorted_list_length = len(sorted_list)
    for i in range(sorted_list_length - 1):
        minimum = i
        for j in range(i + 1, sorted_list_length):
            if sorted_list[j] < sorted_list[minimum]:
                minimum = j
        swap_values(i, minimum, sorted_list)
        #temp = sorted_list[i]
        #sorted_list[i] = sorted_list[minimum]
        #sorted_list[minimum] = temp
    return sorted_list


def bubble_sort(unsorted_list: list)->list:
    """ Sort a list of numbers, letters, and objects using the brute 
    force strategy called Bubble sort.

    This method identify the list's values type and sort them.

    Parameters
    ---------------
    unsorted_list : list
        unsorted_list is a list with the elements to be sorted

    Returns
    ---------------
    list
        a list of sorted values or objects

    """
    
    sorted_list = unsorted_list.copy()
    list_length = (unsorted_list)
    for i in range(list_length - 2):
        for j in range(list_length - 2 - i):
            if sorted_list[j + 1] < sorted_list[j]:
                swap_values(j, j + 1, sorted_list)


def swap_values(i:int, j:int, list_to_swap:list):
    """ Swap the values of the index i and j in the list_to_swap list

        Parameters
        ------------
        i: int
            index of the first value to swap
        j: int
            index of the second value to swap
        list_to_swap: list
            list where the swap will be performed
    """

    temp = list_to_swap[i]
    list_to_swap[i] = list_to_swap[j]
    list_to_swap[j] = temp

