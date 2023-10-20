#! /usr/bin/env python
"""This program built an deterministic finite automata based on a definition 
and validate a set of strings. The DFA is described in a text file as well 
as the test set and the corresponding expected response

Functions
---------
main: access point to the program
"""

import input_output as io

def main():
   parser_namespace = io.parse_command_line()
   config_filename = parser_namespace.input
   automata_definition = io.load_config_file(config_filename)

if __name__ == "__main__":
    main()


