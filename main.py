#! /usr/bin/env python
"""Access point to the Sorting Algorithm Comparison System (SACS)

    The SACS performs a elapse time comparison between different Sorting algorithms from different strategies.

    Functions
    ------------
    main:
        Access point to the SACS system. It controls all the program flow.
"""

import sort_algorithms as sa


def main():
    a = [89, 45, 68, 90, 29, 34, 17]
    print(a)
    sa.quick_sort(a)
    print(a)

if __name__ == "__main__":
    main()
