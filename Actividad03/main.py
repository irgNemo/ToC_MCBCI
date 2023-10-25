#! /usr/bin/env python
"""This program built an deterministic finite automata based on a definition 
and validate a set of strings. The DFA is described in a text file as well 
as the test set and the corresponding expected response

Functions
---------
main: access point to the program
"""

import deterministic_finite_automata as dfa

def main():
   parser_namespace = dfa.parse_command_line()
   config_filename = parser_namespace.input
   automata_definition = dfa.load_config_file(config_filename)
   dfa.validate_automata_definition(automata_definition)
   transition_function = dfa.build_transition_matrix(automata_definition["f"])
   validation_result = dfa.evaluate_string(transition_function, automata_definition["test"], automata_definition["q0"], automata_definition["F"])
   dfa.print_result_table(validation_result, automata_definition["expected"])

if __name__ == "__main__":
    main()


