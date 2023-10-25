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
TEST_RE = "(test)\s*=\s*(\[.+(,.+)*\])"
EXPECTED_RE = "(expected)\s*=\s*(\[.+(,.+)*\])"
DFA_REGEXPS = [ALPHABET_RE,STATES_RE,INITIAL_STATE_RE,FINAL_STATES_RE,TRANSITION_FUNCTION_RE, TEST_RE, EXPECTED_RE]


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
            sub_string = tuple_value[1:-1]
            sub_string = sub_string.split(",")
            tuple_value = set(sub_string)
        elif is_list(tuple_value):
            sub_string = tuple_value[1:-1]
            tuple_value = sub_string.split(",")

        automata_definition[tuple_name] = tuple_value
    
    return automata_definition

def evaluate_string(transition_matrix, test_list, init_state, final_state_set):
    validation_results = []
    for string in test_list:
        current_state = init_state
        for character in string:
            next_state = transition_matrix[current_state][character]
            current_state = next_state
        validation_results += ["accepted"] if current_state in final_state_set else ["rejected"]
    
    return validation_results
            

def is_set(value):
    """Evaluate if value correspond to a set definition
        
        Parameters
        ----------
            value: the string to be evaluated

        Return
        ------
            True if value corresponds to a set definition
    """
    return True if re.match("{.*}", value) else False

def is_list(value):
    """Evaluate if value correspond to a list definition

    Parameters
    ----------
        value: a string to be evaluated

    Return
    ------
        True if value corresponds to a list definition
    """

    return True if re.match("\[.*\]", value) else False


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
    assert len(automata_definition["test"]) == len(automata_definition["expected"]), "The lists test and expected are from differente length"

    transition_function_set = automata_definition["f"]
    for item in transition_function_set:
        match = re.match("\((.*) (.*)\)->(.*)", item)
        antecedent_state = match.groups()[0]
        antecedent_alphabet = match.groups()[1]
        consequent = match.groups()[2]
        assert antecedent_state in automata_definition["Q"], "{} is not in {}".format(antecedent_state, automata_definition["Q"])
        assert antecedent_alphabet in automata_definition["sigma"], "{} is not in {}".format(antecedent_alphabet, automata_definition["sigma"])
        assert consequent in automata_definition["Q"], "{} is not in {}".format(consequent, automata_definition["Q"])
    
    for string_test in automata_definition["test"]:
        for character in string_test:
            assert character in automata_definition["sigma"], "The character '{}' of the string test '{}' contains element(s) not in sigma set {}".format(character, string_test, automata_definition["sigma"])
    
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
                Accession example:
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

def print_result_table(automata_results, expected_results):
    results_tuple = zip(automata_results, expected_results)
    header = "|{0:^15}|{1:^15}|{2:^15}|"
    
    print(header.format("Evaluated","Expected","Match?"))
    for evaluated, expected in results_tuple:
        print("|{0:^15}|{1:^15}|{2:^15}|".format(evaluated, expected, evaluated == expected))