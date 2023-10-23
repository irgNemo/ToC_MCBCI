"""This module containse the utilitary functions used in the deterministic finite automata
    
    Functions
    ---------
    parse_command_line()

"""

import argparse
import re

ALPHABET_RE = "(sigma)\s*=\s*({[a-z0-9](,[a-z-0-9])*})"
FINAL_STATES_RE = "(F)\s*=\s*({[a-z][0-9]+(,[a-z][0-9]+)*})"
TRANSITION_FUNCTION_RE = "(f)\s*=\s*({\([a-z][0-9]+ [a-z0-9]\)->[a-z][0-9]+(,\([a-z][0-9]+ [a-z0-9]\)->[a-z][0-9]+)*})"
INITIAL_STATE_RE = "(q0)\s*=\s*([a-z][0-9])"
STATES_RE = "(Q)\s*=\s*({[a-z][0-9](,[a-z][0-9])*})"
DFA_REGEXPS = [ALPHABET_RE,STATES_RE,INITIAL_STATE_RE,FINAL_STATES_RE,TRANSITION_FUNCTION_RE]
        

def parse_command_line():
    """Parse from command line the arguments passed by the user
       
       Return
       ------
           argparse.Namespace: Object argparse.Namespace with the command line parameters stored
    """
    parser = argparse.ArgumentParser(description="Deterministic finite automata")
    parser.add_argument('-i', "--input", help="input filename/path", required=True)

    return parser.parse_args()

def load_config_file(filename):
    """This function load the config file where the deterministic finite
    automata is configured

    Parameters
    ----------
        filename: filename or path to the config file

    Return
    ------
        automata_definition: a dictionary with the deterministic finite automata correctly validated
    """
    
    automata_definition = {}
    file_obj = open(filename)
    content_file = file_obj.read()

    for reg_exp in DFA_REGEXPS:
        matcher = re.compile(reg_exp)
        match = matcher.search(content_file)
        assert match, "The regular expresion " + reg_exp + " does not match. Correct the config file ... bye"
        tuple_name = match.groups()[0]
        tuple_value = match.groups()[1]
        
        if is_set(tuple_value):
            tuple_value = set(tuple_value[1:-1].split(","))
        
        automata_definition[tuple_name] = tuple_value
    
    return automata_definition


def is_set(value):
    """Evaluate if the string correspond to a set definition
        
        Parameters
        ----------
            value: the string to be evaluated

        Return
        ------
            True if value corresponds to a set definition
    """
    return True if re.match("{.*}", value) else False


def validate_automata_definition(automata_definition):
    """This function validate that the information on each element of the automata tuple are correct. This is, 
        q0 is an element of Q
        F is a subset of Q
        f is formed by elements of Q and sigma, accordingly.

        Parameters:
        ----------
            automata_definition: contains a dictionary with each tuple and its corresponding value.

        Returns:
        --------
            True if everything is correct

        rises:
        ------
            exception when the conditions does not fit
    """
    assert automata_definition["q0"] in automata_definition["Q"], "q0 is not in Q!!!"
    assert automata_definition["F"].issubset(automata_definition["Q"]), "F is not in Q!!!"

    transition_function_set = automata_definition["f"]
    for item in transition_function_set:
        match = re.match("\((.*) (.*)\)->(.*)", item)
        antecedent_state = match.groups()[0]
        antecedent_alphabet = match.groups()[1]
        consequent = match.groups()[2]
        assert antecedent_state in automata_definition["Q"], "{} is not in {}".format(antecedent_state, automata_definition["Q"])
        assert antecedent_alphabet in automata_definition["sigma"], "{} is not in {}".format(antecedent_alphabet, automata_definition["sigma"])
        assert consequent in automata_definition["Q"], "{} is not in {}".format(consequent, automata_definition["Q"])
    
    return True

def build_transition_matrix(transition_sets):
    """This function build a dictionary with the transition of the automata.
        The key of the dictionary are both the state and the character of the test string.

        Parameteres:
        ------------
            transition_set: a set with the transitions rules obtained from config file

        Return:
        -------
            transition_matrix: a dictionary corresponding to the transition matrix. 
                Accesion example:
                    transition_matrix[actual_state][actual_character] -> new state 
    """
    transition_matrix = {}
    for item in transition_sets:
        match = re.match("\((.*) (.*)\)->(.*)", item)
        f_tuple = match.groups()
        antecedent_state = f_tuple[0]
        antecedent_alphabet = f_tuple[1]
        consequent = f_tuple[2]
        if antecedent_state not in transition_matrix:
            transition_matrix[antecedent_state] = {}
        transition_matrix[antecedent_state][antecedent_alphabet] = consequent
    
    return transition_matrix
