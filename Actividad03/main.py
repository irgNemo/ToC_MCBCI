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
   print(transition_function)

if __name__ == "__main__":
    main()


