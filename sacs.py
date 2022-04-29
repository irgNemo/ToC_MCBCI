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

    args = io.parse_input()
    config_file_path = args.input
    output_file_path = args.output
    config_dict = io.load_config_file(config_file_path)
    results = []

    sorting_algorithms = config_dict["sorting_algorithms"].split(",")
    sorting_algorithms = [sorting_algorithm.strip() for sorting_algorithm in sorting_algorithms]
    unsorted_lists = config_dict["unsorted_lists"].split("|")
    unsorted_lists = [unsorted_list.strip("[] ").split(",") for unsorted_list in unsorted_lists]

    for sorting_algorithm in sorting_algorithms:
        for unsorted_list in unsorted_lists:
            sorted_list = sa.sort(sorting_algorithm, unsorted_list)
            results.append((sorting_algorithm, sorted_list))

    io.formatted_output(results)


if __name__ == "__main__":
    main()
