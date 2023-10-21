"""This module containse the utilitary functions used in the deterministic finite automata
    
    Functions
    ---------
    parse_command_line()

"""

import argparse

ALPHABET_RE = "sigma\s=\s{.,?}"
FINAL_STATES_RE = ""
TRANSITION_FUNCTION_RE = ""
INITIAL_STATE_RE = ""
STATES_RE = ""

def load_config_file(filename):
    """This function load the config file where the deterministic finite
    automata is condigured

    Parameters
    ----------
        filename: filename or path to the config file

    Return
    ------
        automata_definition: a dictionary with the deterministic finite automata correctly validated
    """
    
    file_obj = open(filename)
    content_file = file_obj.read()



def parse_command_line():
    """Parse from command line the arguments passed by the user<F12>
       Return
       ------
           argparse.Namespace: Object argparse.Namespace with the command line parameters stored
    """
    parser = argparse.ArgumentParser(description="Deterministic finite automata")
    parser.add_argument('-i', "--input", help="input filename/path", required=True)

    return parser.parse_args()

