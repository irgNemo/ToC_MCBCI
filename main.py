#! /usr/bin/env python
"""Access point to the Sorting Algorithm Comparison System (SACS)

    The SACS performs a elapse time comparison between different Sorting algorithms from different strategies.

    Functions
    ------------
    main:
        Access point to the SACS system. It controls all the program flow.
"""

import sorting_algorithms as sa
import input_output as io


def main():
    unsorted_list = [89, 45, 68, 90, 29, 34, 17, 30]
    quick_sorted_list = sa.quick_sort(unsorted_list)
    #bubble_sorted_list = sa.bubble_sort(unsorted_list)
    results = [("Quick sort", quick_sorted_list)]
    io.formated_output(results)


if __name__ == "__main__":
    main()
