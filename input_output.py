"""The input_output module contains several functions to load files and to format the SACS outputs

    Functions
    ---------------
    load_config_file(file_path:str)->dict
    comparison_output(results:dict)->

"""

import argparse
import re

PATTERN_SORTING_ALGORITHMS = "(sorting_algorithms)\s*=\s*(\w+(,\s?\w*)*)"
PATTERN_UNSORTED_LIST = "(unsorted_lists)\s*=\s*((\[(\w,?)+\])(\|\[(\w,?)+\])*)"
PATTERNS_CONFIG_FILE = [PATTERN_SORTING_ALGORITHMS, PATTERN_UNSORTED_LIST]


def load_config_file(file_path: str) -> dict:
    """Load config file

    Read the config file and create a dictionary with the configuration
     information for used in SACS

    Parameters
    -------------
    file_path: File path and name of the configuration file


    return:
    -------------
    dict: Dictionary with the information stored in the config file
    """
    config_dict = {}

    f = open(file_path, 'r')
    text = f.read()
    f.close()

    for pattern in PATTERNS_CONFIG_FILE:
        re_obj = re.compile(pattern)
        result = re_obj.search(text)
        config_dict[result.group(1)] = result.group(2)

    return config_dict


def formatted_output(results: dict):
    """Write a formated table with the results of the comparison
        
        The table contains a header with the information. Every row represents the evaluation of one sorting algorithm on a list of elements

        Parameters
        -----------
        results:
            The results obtained from the differents comparisons. The results argument is list of Tuples, every Tuple contains: (algorith_name, sorted_list)
    """

    header = "{0:^10}|{1:^20}|{2:^30}|"
    row = "{algorithm:^10}|{address:^20X}|{lista!s:^30}|"
    print(header.format("Algorithm", "Physical address", "List"))
    for value in results:
        algorithm = value[0]
        sorted_list = value[1]
        print(row.format(algorithm=algorithm, address=id(sorted_list), lista=sorted_list))


def parse_input() -> argparse.Namespace:
    """Read the arguments of sacs

    Parameters
    -------------


    Returns
    ------------
    argparse.Namespace
        The object argparse.Namespace where the command line arguments are stored
    """
    parser = argparse.ArgumentParser(description='Time comparison of several sorting algorithms')
    parser.add_argument('-i', '--input', help='Config file path', required=True)
    parser.add_argument('-o', '--output', help='Path and file name were the results are written. '
                                               'If not indicated, the results are written in the '
                                               'standar output')

    return parser.parse_args()

