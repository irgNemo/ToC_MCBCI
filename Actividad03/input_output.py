"""This module containse the utilitary functions used in the deterministic finite automata
    
    Functions
    ---------
    parse_command_line()

"""

import argparse

def load_config_file(filename):
    print(filename)



def parse_command_line():
    """Parse from command line the arguments passed by the user<F12>
       Return
       ------
           argparse.Namespace: Object argparse.Namespace with the command line parameters stored
    """
    parser = argparse.ArgumentParser(description="Deterministic finite automata")
    parser.add_argument('-i', "--input", help="input filename/path", required=True)

    return parser.parse_args()

